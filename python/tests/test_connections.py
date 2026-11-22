"""The methods of a service answered at a Connection (internal/sdk's Runtime): each called at the
server the API's fake sends it to, with that connection's token and never the API's, one
connection a key while it is good, those the answers hold kept, a call made once more on a new
connection after a code that answers a call that did nothing, and a request_id made once a call."""

from __future__ import annotations

import re
from datetime import timedelta
from typing import Any

from protobuf import DescField, DescMessage, Message

from .facts import Runtime, Seed
from .fake import Answer, failure
from .harness import TOKEN, AsyncCase, Case, by_surface, connection
from .samples import Plan, kind_of, pair, public_class, repeated, wire_class


def seeded(desc: DescMessage, runtime: Runtime, seed: Seed, key: str, held: Message[Any]) -> Message[Any]:
    """A sample of a response that holds a connection where its seed says: a key's, held."""
    if not seed.path:
        sample, _ = pair(desc, Plan())
        field = next(f for f in desc.fields if holds(f, held.desc()))
        setattr(sample, runtime.key, key)
        setattr(sample, field.local_name, held)
        return sample

    step = next(f for f in desc.fields if f.name == seed.path[0])
    inner = kind_of(step)
    assert isinstance(inner, DescMessage)
    value = seeded(inner, runtime, Seed(seed.method, seed.path[1:]), key, held)
    outer: Message[Any] = wire_class(desc)()
    setattr(outer, step.local_name, [value] if repeated(step) else value)
    return outer


def holds(field: DescField, desc: DescMessage) -> bool:
    """Whether a field holds a message of that type."""
    kind = kind_of(field)
    return isinstance(kind, DescMessage) and kind.type_name == desc.type_name


class Connections(Case):
    def setUp(self) -> None:
        self.client = self.fresh(workspace="the client's")
        runtime = self.surface.runtime
        assert runtime is not None
        self.runtime = runtime
        self.connected = [method for method in self.surface.facts.methods if self.surface.connected(method)]
        self.unary = [method for method in self.connected if method not in self.surface.streams]
        # A method whose request_id the client makes, if one is: its repeat must send the same.
        self.repeated = next((m for m in self.unary if m in self.surface.facts.request_ids), self.unary[0])
        self.since = len(self.fake.calls)
        self.addCleanup(self.server.script)
        self.addCleanup(self.server.answer, b"")

    def connects(self) -> list[Any]:
        """The requests of the connections the API's fake answered during this check."""
        path = self.surface.path(self.runtime.connect)
        desc = self.surface.requests[self.runtime.connect]
        return [wire_class(desc).from_binary(call.body) for call in self.fake.calls[self.since :] if call.path == path]

    def at(self, method: str, key: str) -> Any:
        """Calls a method at a key: its response, or a stream's whole reading."""
        answer = self.call(method, **{self.runtime.key: key})
        return self.read(answer) if method in self.surface.streams else answer

    def test_each_method_at_its_server(self) -> None:
        """Each method reaches the server with the connection's token and the package's name,
        never with the API token; the connection was asked for once, with the client's workspace
        where its request names one."""
        workspace = self.surface.facts.workspace
        for method in self.connected:
            with self.subTest(method=method):
                self.server.answer(b"")
                self.at(method, "one")
                call = self.server.calls[-1]
                self.assertEqual(call.path, self.surface.path(method))
                self.assertEqual(call.headers["authorization"], "Bearer sbc.test")
                self.assertTrue(call.headers["user-agent"].startswith("pethost-python/"))
                self.assertFalse([value for value in call.headers.values() if TOKEN in value])

        (asked,) = self.connects()
        self.assertEqual(getattr(asked, self.runtime.key), "one")
        if self.runtime.connect in self.surface.facts.workspaced:
            self.assertEqual(getattr(asked, workspace), "the client's")

    def test_one_connection_a_key(self) -> None:
        """Two calls at one key connect once; a call at another connects again."""
        self.server.answer(b"")
        self.at(self.unary[0], "one")
        self.at(self.unary[-1], "one")
        self.assertEqual(len(self.connects()), 1)
        self.at(self.unary[0], "two")
        self.assertEqual([getattr(asked, self.runtime.key) for asked in self.connects()], ["one", "two"])

    def test_a_connection_an_answer_holds(self) -> None:
        """A connection an answer holds is the key's: a call at it connects to nothing, and
        carries its token."""
        for seed in self.runtime.seeds:
            with self.subTest(method=seed.method):
                key = f"seeded-{seed.method}"
                held = connection(self.runtime, self.server, token="sbc.seed")
                self.fake.answer(seeded(self.surface.responses[seed.method], self.runtime, seed, key, held).to_binary())
                self.call(seed.method, **self.required(seed.method))

                self.server.answer(b"")
                self.at(self.unary[0], key)
                self.assertEqual(self.server.calls[-1].headers["authorization"], "Bearer sbc.seed")
                self.assertEqual([getattr(asked, self.runtime.key) for asked in self.connects()], [])

    def test_a_connection_near_its_end(self) -> None:
        """A connection that ends within the margin is used for its own call alone: each call
        connects again."""
        path = self.surface.path(self.runtime.connect)
        standing = self.fake.routes[path]
        self.addCleanup(self.fake.routes.__setitem__, path, standing)
        lasting = timedelta(seconds=self.runtime.margin_seconds / 2)
        self.fake.route(path, connection(self.runtime, self.server, lasting=lasting).to_binary())

        self.server.answer(b"")
        self.at(self.unary[0], "one")
        self.at(self.unary[0], "one")
        self.assertEqual(len(self.connects()), 2)

    def test_once_more_on_a_new_connection(self) -> None:
        """A call made with a kept connection and refused with a code that answers a call that
        did nothing is made once more, the same request, on a new connection; a second refusal
        is the call's."""
        for code in self.runtime.retry:
            with self.subTest(code=code):
                self.server.answer(b"")
                self.at(self.unary[0], code)  # The connection is kept from here on.
                calls, connects = len(self.server.calls), len(self.connects())

                self.server.script(failure(code, "refused"), Answer())
                self.at(self.repeated, code)
                first, again = self.server.calls[calls:]
                self.assertEqual(first.body, again.body)
                self.assertEqual(len(self.connects()), connects + 1)

                self.server.script(failure(code, "refused"), failure(code, "refused again"))
                with self.assertRaises(self.surface.error_of(code)) as raised:
                    self.at(self.repeated, code)
                self.assertEqual(raised.exception.message, "refused again")
                self.assertEqual((len(self.server.calls), len(self.connects())), (calls + 4, connects + 2))

    def test_never_more_than_once(self) -> None:
        """A new connection refused is not asked for again, and nothing else is made again: an
        unavailable server may have done the call."""
        for code in [*self.runtime.retry, "unavailable"]:
            with self.subTest(code=code):
                calls, connects = len(self.server.calls), len(self.connects())
                self.server.fail(code, "refused")
                with self.assertRaises(self.surface.error_of(code)):
                    self.at(self.repeated, code)  # On a connection made for this call.
                self.assertEqual((len(self.server.calls), len(self.connects())), (calls + 1, connects + 1))
                if code == "unavailable":
                    with self.assertRaises(self.surface.error_of(code)):
                        self.at(self.repeated, code)  # On the connection kept.
                    self.assertEqual((len(self.server.calls), len(self.connects())), (calls + 2, connects + 1))

    def test_request_ids(self) -> None:
        """A request_id left empty is a new one, so many random bytes in lowercase hex, another
        each call; one given is sent as it is."""
        hexadecimal = re.compile(f"^[0-9a-f]{{{2 * self.runtime.request_id_bytes}}}$")
        for method, field in self.surface.facts.request_ids.items():
            with self.subTest(method=method):
                fake = self.fake_of(method)
                request = wire_class(self.surface.requests[method])
                sent: list[str] = []
                for given in ("", "", "mine"):
                    fake.answer(b"")
                    self.call(method, **{**self.required(method), field: given})
                    sent.append(getattr(request.from_binary(fake.calls[-1].body), field))
                self.assertRegex(sent[0], hexadecimal)
                self.assertRegex(sent[1], hexadecimal)
                self.assertNotEqual(sent[0], sent[1])
                self.assertEqual(sent[2], "mine")

    def test_a_stream_once_more_before_its_first_response(self) -> None:
        """A stream refused before its first response on a kept connection is called once more
        on a new one; once a response came, its failure is the stream's."""
        for method in sorted(set(self.connected) & self.surface.streams):
            with self.subTest(method=method):
                self.server.answer(b"")
                self.at(self.unary[0], method)  # The connection is kept from here on.
                connects = len(self.connects())
                sample, given = pair(self.surface.responses[method], Plan())
                expected = public_class(self.surface.responses[method])(**given)

                self.server.script(failure("unauthenticated", "expired"), Answer([sample.to_binary()]))
                self.assertEqual(self.at(method, method), ([expected], None))
                self.assertEqual(len(self.connects()), connects + 1)

                self.server.script(failure("unauthenticated", "expired", after=(sample.to_binary(),)))
                responses, error = self.at(method, method)
                self.assertEqual(responses, [expected])
                self.assertCode(error, "unauthenticated")
                self.assertEqual(len(self.connects()), connects + 1)

    def call(self, method: str, **arguments: Any) -> Any:
        """A call; a stream's method returns its stream, for the check to read."""
        if method in self.surface.streams:
            return getattr(self.client, method)(**arguments)
        return super().call(method, **arguments)


class AsyncConnections(AsyncCase, Connections):
    """The asyncio client's connections, through the checks of the synchronous one's."""


load_tests = by_surface(Connections, AsyncConnections, connected=True)
