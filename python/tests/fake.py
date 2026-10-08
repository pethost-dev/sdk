"""A local fake of the API: an HTTP server on 127.0.0.1 that speaks the Connect protocol as the
API does, to a call and to a stream of responses. It keeps each call as the wire carried it, and
answers what the check told it to, in raw bytes, so that it can also say what this version of
the package does not know."""

from __future__ import annotations

import base64
import gzip
import json
import struct
import threading
import time
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any

# The HTTP status the Connect protocol gives each of its codes, where a call that is no stream fails.
STATUS = {
    "canceled": 499, "unknown": 500, "invalid_argument": 400, "deadline_exceeded": 504,
    "not_found": 404, "already_exists": 409, "permission_denied": 403, "resource_exhausted": 429,
    "failed_precondition": 400, "aborted": 409, "out_of_range": 400, "unimplemented": 501,
    "internal": 500, "unavailable": 503, "data_loss": 500, "unauthenticated": 401,
}

# What a call says its body is, as its answer does: one message, or a stream's envelopes.
CALL = "application/proto"
STREAM = "application/connect+proto"

# An envelope's flags: its message is compressed; it is the stream's last, and says how it ended.
COMPRESSED = 1
END = 2

# How long a check waits for the fake to see that a stream's caller left.
PATIENCE = 10.0


@dataclass
class Call:
    """One call as it arrived."""

    verb: str
    path: str
    headers: dict[str, str]
    body: bytes  # Its one message, uncompressed: a stream's out of its envelope.


@dataclass
class Answer:
    """What the next call gets: its one response, or a stream each of its responses in turn."""

    responses: list[bytes] = field(default_factory=lambda: [b""])
    error: dict[str, Any] | None = None  # What it fails with, as the protocol's JSON says an error.
    delay: float = 0.0
    left: threading.Event | None = None  # A stream then has no end: the fake sets this when its caller is gone.


@dataclass
class Fake:
    """The server. `calls` are the calls so far; the next one gets what `answer`, `fail` or `hold` set."""

    calls: list[Call] = field(default_factory=list[Call])
    next: Answer = field(default_factory=Answer)

    def __post_init__(self) -> None:
        # A thread a connection: a stream the fake holds open keeps no other call waiting.
        self._server = ThreadingHTTPServer(("127.0.0.1", 0), self._handler())
        self.url = f"http://127.0.0.1:{self._server.server_port}"
        threading.Thread(target=self._server.serve_forever, daemon=True).start()

    def answer(self, *responses: bytes, delay: float = 0.0) -> None:
        """The next call succeeds with this message, as bytes; a stream with each in turn, and ends."""
        self.next = Answer(list(responses), delay=delay)

    def fail(self, code: str, message: str, details: list[tuple[str, bytes]] | None = None, after: tuple[bytes, ...] = ()) -> None:
        """The next call fails with a code, and with details: each a type's full name and its
        bytes. A stream fails after these responses."""
        error: dict[str, Any] = {"code": code, "message": message}
        if details:
            error["details"] = [
                {"type": name, "value": base64.b64encode(value).decode().rstrip("=")} for name, value in details
            ]
        self.next = Answer(list(after), error)

    def hold(self, *responses: bytes) -> threading.Event:
        """The next call, a stream, gets these responses and no end: the fake waits for its
        caller to leave, and then sets what this returns. To HTTP/1.1, which the fake speaks,
        leaving a call is closing its connection."""
        left = threading.Event()
        self.next = Answer(list(responses), left=left)
        return left

    def close(self) -> None:
        self._server.shutdown()
        self._server.server_close()

    def _handler(self) -> type[BaseHTTPRequestHandler]:
        fake = self

        class Handler(BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"  # A stream's answer has no length to say first: it goes in chunks.
            # A response goes out as it is written: the checks wait for each, not for a full packet.
            disable_nagle_algorithm = True

            def handle(self) -> None:
                try:
                    super().handle()
                except OSError:
                    return  # The caller closed the connection under an answer.

            def do_POST(self) -> None:
                headers = {name.lower(): value for name, value in self.headers.items()}
                stream = headers.get("content-type") == STREAM
                fake.calls.append(Call("POST", self.path, headers, message_of(self.sent(), headers, stream)))

                answer = fake.next
                time.sleep(answer.delay)
                if stream:
                    self.answer_stream(answer)
                elif answer.error is not None:
                    self.answer_call(STATUS[answer.error["code"]], "application/json", json.dumps(answer.error).encode())
                else:
                    self.answer_call(200, CALL, answer.responses[0])

            def do_GET(self) -> None:  # The API is called by POST: a GET is a call the SDK must not make.
                fake.calls.append(Call("GET", self.path, {}, b""))
                self.send_error(405)

            def sent(self) -> bytes:
                """The call's body: of the length it says, or, as a stream's request comes, in chunks."""
                if self.headers.get("transfer-encoding") != "chunked":
                    return self.rfile.read(int(self.headers.get("content-length", "0")))

                body = b""
                while size := int(self.rfile.readline(), 16):
                    body += self.rfile.read(size)
                    self.rfile.readline()
                self.rfile.readline()
                return body

            def answer_call(self, status: int, content_type: str, body: bytes) -> None:
                self.send_response(status)
                self.send_header("content-type", content_type)
                self.send_header("content-length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def answer_stream(self, answer: Answer) -> None:
                """Each response in an envelope as it is written, then the envelope that ends
                the stream and says how: the status is 200 also where the stream fails. For a
                caller that takes gzip every envelope is compressed, as the API's are, the one
                of a response with nothing set too: on the wire that one is not empty."""
                squeezed = "gzip" in self.headers.get("connect-accept-encoding", "")
                self.send_response(200)
                self.send_header("content-type", STREAM)
                if squeezed:
                    self.send_header("connect-content-encoding", "gzip")
                self.send_header("transfer-encoding", "chunked")
                self.end_headers()
                for response in answer.responses:
                    self.wfile.write(chunk(envelope(0, response, squeezed)))

                if answer.left is None:
                    end = {} if answer.error is None else {"error": answer.error}
                    self.wfile.write(chunk(envelope(END, json.dumps(end).encode(), squeezed)) + chunk(b""))
                    return

                self.close_connection = True
                try:
                    self.rfile.read(1)  # It ends when the caller closes the connection, and not before.
                finally:
                    answer.left.set()

            def log_message(self, format: str, *args: object) -> None:
                return

        return Handler


def envelope(flags: int, message: bytes, squeezed: bool) -> bytes:
    """A message as a stream of the protocol carries it: its flags, its length, its bytes,
    compressed for a caller that takes gzip."""
    if squeezed:
        flags, message = flags | COMPRESSED, gzip.compress(message)
    return struct.pack(">BI", flags, len(message)) + message


def chunk(data: bytes) -> bytes:
    """A piece of a body that has no length said first, as HTTP/1.1 writes it; an empty one ends the body."""
    return f"{len(data):x}\r\n".encode() + data + b"\r\n"


def message_of(body: bytes, headers: dict[str, str], stream: bool) -> bytes:
    """The one message a call carries, uncompressed: a stream's is in an envelope."""
    if not stream:
        return gzip.decompress(body) if headers.get("content-encoding") == "gzip" else body

    flags, length = struct.unpack(">BI", body[:5])
    assert len(body) == 5 + length, "a stream's request is one message"
    if flags & COMPRESSED:
        assert headers.get("connect-content-encoding") == "gzip", "a message compressed, and not as the call says"
        return gzip.decompress(body[5:])
    return body[5:]
