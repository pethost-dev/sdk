"""A local fake of the API: an HTTP server on 127.0.0.1 that speaks the Connect protocol as the
API does. It keeps each call as the wire carried it, and answers what the check told it to, in
raw bytes, so that it can also say what this version of the package does not know."""

from __future__ import annotations

import base64
import gzip
import json
import threading
import time
from dataclasses import dataclass, field
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Any

# The HTTP status the Connect protocol gives each of its codes.
STATUS = {
    "canceled": 499, "unknown": 500, "invalid_argument": 400, "deadline_exceeded": 504,
    "not_found": 404, "already_exists": 409, "permission_denied": 403, "resource_exhausted": 429,
    "failed_precondition": 400, "aborted": 409, "out_of_range": 400, "unimplemented": 501,
    "internal": 500, "unavailable": 503, "data_loss": 500, "unauthenticated": 401,
}


@dataclass
class Call:
    """One call as it arrived."""

    verb: str
    path: str
    headers: dict[str, str]
    body: bytes


@dataclass
class Answer:
    status: int = 200
    content_type: str = "application/proto"
    body: bytes = b""
    delay: float = 0.0


@dataclass
class Fake:
    """The server. `calls` are the calls so far; the next one gets what `answer` or `fail` set."""

    calls: list[Call] = field(default_factory=list[Call])
    next: Answer = field(default_factory=Answer)

    def __post_init__(self) -> None:
        self._server = HTTPServer(("127.0.0.1", 0), self._handler())
        self.url = f"http://127.0.0.1:{self._server.server_port}"
        threading.Thread(target=self._server.serve_forever, daemon=True).start()

    def answer(self, body: bytes, delay: float = 0.0) -> None:
        """The next call succeeds with this message, as bytes."""
        self.next = Answer(body=body, delay=delay)

    def fail(self, code: str, message: str, details: list[tuple[str, bytes]] | None = None) -> None:
        """The next call fails with a code, and with details: each a type's full name and its bytes."""
        error: dict[str, Any] = {"code": code, "message": message}
        if details:
            error["details"] = [
                {"type": name, "value": base64.b64encode(value).decode().rstrip("=")} for name, value in details
            ]
        self.next = Answer(STATUS.get(code, 500), "application/json", json.dumps(error).encode())

    def close(self) -> None:
        self._server.shutdown()
        self._server.server_close()

    def _handler(self) -> type[BaseHTTPRequestHandler]:
        fake = self

        class Handler(BaseHTTPRequestHandler):
            def do_POST(self) -> None:
                body = self.rfile.read(int(self.headers.get("content-length", "0")))
                if self.headers.get("content-encoding") == "gzip":
                    body = gzip.decompress(body)
                headers = {name.lower(): value for name, value in self.headers.items()}
                fake.calls.append(Call("POST", self.path, headers, body))

                answer = fake.next
                time.sleep(answer.delay)
                self.send_response(answer.status)
                self.send_header("content-type", answer.content_type)
                self.send_header("content-length", str(len(answer.body)))
                self.end_headers()
                self.wfile.write(answer.body)

            def do_GET(self) -> None:  # The API is called by POST: a GET is a call the SDK must not make.
                fake.calls.append(Call("GET", self.path, {}, b""))
                self.send_error(405)

            def log_message(self, format: str, *args: object) -> None:
                return

        return Handler
