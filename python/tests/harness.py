"""What every check stands on: each surface of the package, its fakes, a client of each kind that
calls them, and the two ways a sample goes through the package. A check is written once, for any
surface, and its module's load_tests (by_surface) runs it on every one."""

from __future__ import annotations

import asyncio
import contextlib
import inspect
import re
import unittest
from collections.abc import Callable, Generator
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any, cast

from protobuf import DescMessage, DescMethod, Message
from protobuf.wkt.google.protobuf.timestamp_pb import Timestamp

from .api import SURFACES
from .facts import Facts, Runtime
from .fake import Fake
from .samples import Plan, pair, public_class, reaches, wire_class

TOKEN = "pth_check"  # The API token every client is made with.
SERVER_TOKEN = "sbc.test"  # The token of every connection the API's fake answers with.


@dataclass(frozen=True)
class Surface:
    """A surface as the checks call it: its facts, and its RPCs and messages in the wire layer."""

    facts: Facts
    rpcs: dict[str, DescMethod]  # By the method that calls it.
    messages: dict[str, DescMessage]
    streams: frozenset[str]
    requests: dict[str, DescMessage]
    responses: dict[str, DescMessage]
    most_members: int  # The most members a oneof has: so many samples set each member of every oneof once.

    @property
    def label(self) -> str:
        return self.facts.name or "pethost"

    @property
    def runtime(self) -> Runtime | None:
        return self.facts.runtime

    def client(self, asynchronous: bool = False) -> type[Any]:
        """The surface's client, or its asyncio one."""
        found: type[Any] = getattr(self.facts.public, ("Async" if asynchronous else "") + self.facts.client)
        return found

    @property
    def error(self) -> Any:
        """The surface's error, which each code's class is a subclass of."""
        return getattr(self.facts.public, self.facts.client + "Error")

    def error_of(self, code: str) -> Any:
        """The class of one of the protocol's codes, as its JSON writes it: not_found is NotFoundError."""
        return getattr(self.facts.public, "".join(word.capitalize() for word in code.split("_")) + "Error")

    def connected(self, method: str) -> bool:
        """Whether a method is called at a Connection, not at the API's address."""
        return self.runtime is not None and self.rpcs[method].parent.type_name == self.runtime.service

    def path(self, method: str) -> str:
        rpc = self.rpcs[method]
        return f"/{rpc.parent.type_name}/{rpc.name}"

    def first_reaching(self, roots: dict[str, DescMessage]) -> list[tuple[str, DescMessage]]:
        """Every message the roots hold, each with the first root that holds it."""
        found: dict[str, str] = {}
        for root, desc in roots.items():
            for name in sorted(reaches(desc)):
                found.setdefault(name, root)
        return [(root, self.messages[name]) for name, root in found.items()]


def surface_of(facts: Facts) -> Surface:
    services = facts.wire.desc().services
    rpcs = {method: next(rpc for service in services for rpc in service.methods if rpc.name == name) for method, name in facts.methods.items()}
    messages = {desc.name: desc for desc in facts.wire.desc().messages}
    return Surface(
        facts=facts,
        rpcs=rpcs,
        messages=messages,
        streams=frozenset(method for method, rpc in rpcs.items() if rpc.method_kind == "server_streaming"),
        requests={method: rpc.input for method, rpc in rpcs.items()},
        responses={method: rpc.output for method, rpc in rpcs.items()},
        most_members=max([len(oneof.fields) for desc in messages.values() for oneof in desc.oneofs] + [1]),
    )


CHECKED = tuple(surface_of(facts) for facts in SURFACES)

LoadTests = Callable[[unittest.TestLoader, unittest.TestSuite, "str | None"], unittest.TestSuite]


def by_surface(*cases: type[unittest.TestCase], connected: bool = False) -> LoadTests:
    """A test module's load_tests: each of its checks once for each surface (only those with a
    service answered at a Connection, where connected), as a class of its own."""

    def load_tests(loader: unittest.TestLoader, standard: unittest.TestSuite, pattern: str | None) -> unittest.TestSuite:
        suite = unittest.TestSuite()
        for surface in CHECKED:
            if connected and surface.runtime is None:
                continue
            for case in cases:
                named = type(f"{case.__name__}_{surface.label}", (case,), {"surface": surface, "__module__": case.__module__})
                suite.addTests(loader.loadTestsFromTestCase(cast("type[unittest.TestCase]", named)))
        return suite

    return load_tests


def connection(facts: Runtime, server: Fake, token: str = SERVER_TOKEN, lasting: timedelta = timedelta(hours=1)) -> Message[Any]:
    """A Connection to a fake server, as the wire carries it, that expires after lasting."""
    expire = Timestamp.from_datetime(datetime.now(timezone.utc) + lasting)
    surface = next(surface for surface in CHECKED if surface.runtime is facts)
    desc = surface.responses[facts.connect]
    return cast("Message[Any]", wire_class(desc)(**{facts.url: server.url, facts.token: token, facts.expire: expire}))


class Checked(unittest.TestCase):
    """A check of one surface."""

    surface: Surface
    maxDiff = None


class Case(Checked):
    """A check with the fakes and a client of them: the API's, and for a surface with a service
    answered at a Connection, a server's, which the API's ConnectSandbox answers send it to."""

    asynchronous = False
    fake: Fake  # The API.
    server: Fake  # A Connection's server; for a surface without one, the API's fake too.
    client: Any

    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Fake()
        cls.server = cls.fake
        runtime = cls.surface.runtime
        if runtime is not None:
            cls.server = Fake()
            cls.fake.route(cls.surface.path(runtime.connect), connection(runtime, cls.server).to_binary())
        cls.client = cls.make()

    @classmethod
    def make(cls, token: str | None = TOKEN, **options: Any) -> Any:
        """A client of this check's kind, of the fake API unless options say otherwise."""
        return cls.surface.client(cls.asynchronous)(token, **{"base_url": cls.fake.url, **options})

    def fresh(self, **options: Any) -> Any:
        """A client of its own for one check, closed after it: it holds no connection yet."""
        client = self.make(**options)
        self.addCleanup(self.shut, client)
        return client

    def shut(self, client: Any) -> None:
        client.close()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.close()
        cls.fake.close()
        if cls.server is not cls.fake:
            cls.server.close()

    @classmethod
    def close(cls) -> None:
        cls.client.close()

    def fake_of(self, method: str) -> Fake:
        """Where a method's call arrives."""
        return self.server if self.surface.connected(method) else self.fake

    def bearer_of(self, method: str) -> str:
        """The authorization a method's call carries."""
        return f"Bearer {SERVER_TOKEN if self.surface.connected(method) else TOKEN}"

    def call(self, method: str, **arguments: Any) -> Any:
        """Calls a method: its response. To the checks of every method a stream is a call too,
        the one that returns the stream's only response; None = it yielded none."""
        answer = getattr(self.client, method)(**arguments)
        if method not in self.surface.streams:
            return self.result(answer)
        responses, error = self.read(answer)
        if error is not None:
            raise error
        (response,) = responses or [None]
        return response

    def result(self, answer: Any) -> Any:
        """What a method that is no stream returned."""
        return answer

    def read(self, stream: Any) -> tuple[list[Any], Exception | None]:
        """Reads a stream to its end: its responses, and the error that ended it, if one did."""
        responses: list[Any] = []
        try:
            for response in stream:
                responses.append(response)
        except Exception as error:
            return responses, error
        return responses, None

    def required(self, method: str) -> dict[str, str]:
        """The arguments a method cannot be called without, each empty: the call's subject."""
        parameters = inspect.signature(getattr(self.client, method)).parameters.values()
        return {parameter.name: "" for parameter in parameters if parameter.default is inspect.Parameter.empty}

    @contextlib.contextmanager
    def answering(self, method: str, *responses: bytes) -> Generator[Fake, None, None]:
        """Where a method's call arrives, told to answer it with these. The connections the
        client asks for itself have an answer of their own there (setUpClass), which a check of
        the method that asks for one sets aside while it calls it."""
        fake = self.fake_of(method)
        fake.answer(*responses)
        path = self.surface.path(method)
        standing = fake.routes.pop(path, None)
        try:
            yield fake
        finally:
            if standing is not None:
                fake.routes[path] = standing

    def sends(self, method: str, plan: Plan) -> None:
        """Calls a method with a sample of its request: the fake must receive the wire's side of
        it, by POST, at the RPC's path; a request_id left empty, one the client made."""
        rpc = self.surface.rpcs[method]
        expected, arguments = pair(rpc.input, plan)
        with self.answering(method, b"") as fake:
            self.call(method, **arguments)

        call = fake.calls[-1]
        self.assertEqual((call.verb, call.path), ("POST", self.surface.path(method)))
        sent = wire_class(rpc.input).from_binary(call.body)
        self.made_request_id(method, arguments, sent, expected)
        self.assertEqual(sent, expected)
        self.assertEqual(call.body, expected.to_binary())

    def made_request_id(self, method: str, arguments: dict[str, Any], sent: Any, expected: Any) -> None:
        """Where a method's request_id was left empty, the client sends one it made: so many
        random bytes in lowercase hex. The sample expects it from then on."""
        field = self.surface.facts.request_ids.get(method)
        if field is None or arguments.get(field):
            return
        runtime = self.surface.runtime
        assert runtime is not None, "a request_id is filled by a surface with a Runtime"
        self.assertRegex(getattr(sent, field), re.compile(f"^[0-9a-f]{{{2 * runtime.request_id_bytes}}}$"))
        setattr(expected, field, getattr(sent, field))

    def receives(self, method: str, plan: Plan) -> None:
        """Answers a method with a sample of its response: the call must return the public side.
        A stream's response with nothing set is the API's pulse, and the stream yields none."""
        sent, given = pair(self.surface.responses[method], plan)
        pulse = method in self.surface.streams and not sent.to_binary()
        expected = None if pulse else public_class(self.surface.responses[method])(**given)
        with self.answering(method, sent.to_binary()):
            self.assertEqual(self.call(method, **self.required(method)), expected)

    def assertCode(self, error: object, code: str) -> None:
        """An error is the class of one of the protocol's codes, as its JSON writes it."""
        self.assertIs(type(error), self.surface.error_of(code))

    def fails(self) -> Any:
        """Calls the API's first method, which the fake was told to fail: the error it raises."""
        method = next(iter(self.surface.facts.methods))
        with self.assertRaises(self.surface.error) as raised:
            self.call(method, **self.required(method))
        return raised.exception


class AsyncCase(Case):
    """A check of the asyncio client: the checks of the synchronous one, on a loop of its own."""

    asynchronous = True
    loop: asyncio.AbstractEventLoop

    @classmethod
    def setUpClass(cls) -> None:
        cls.loop = asyncio.new_event_loop()
        super().setUpClass()

    @classmethod
    def close(cls) -> None:
        cls.loop.run_until_complete(cls.client.aclose())
        cls.loop.close()

    def shut(self, client: Any) -> None:
        self.loop.run_until_complete(client.aclose())

    def result(self, answer: Any) -> Any:
        return self.loop.run_until_complete(answer)

    def read(self, stream: Any) -> tuple[list[Any], Exception | None]:
        async def read() -> tuple[list[Any], Exception | None]:
            responses: list[Any] = []
            try:
                async for response in stream:
                    responses.append(response)
            except Exception as error:
                return responses, error
            return responses, None

        return self.loop.run_until_complete(read())
