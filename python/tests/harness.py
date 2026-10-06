"""What every check stands on: the fake, a client that calls it, and the two ways a sample goes
through the package."""

from __future__ import annotations

import inspect
import unittest
from typing import Any

from protobuf import DescMessage, DescMethod

import pethost

from .api import METHODS, wire
from .fake import Fake
from .samples import Plan, pair, public_class, reaches, wire_class

SERVICE = wire.desc().services[0]
RPCS: dict[str, DescMethod] = {
    method: next(rpc for rpc in SERVICE.methods if rpc.name == name) for method, name in METHODS.items()
}
MESSAGES: dict[str, DescMessage] = {desc.name: desc for desc in wire.desc().messages}
REQUESTS = {method: rpc.input for method, rpc in RPCS.items()}
RESPONSES = {method: rpc.output for method, rpc in RPCS.items()}

# The most members a oneof has: so many samples set each member of every oneof once.
MOST_MEMBERS = max([len(oneof.fields) for desc in MESSAGES.values() for oneof in desc.oneofs] + [1])


def first_reaching(roots: dict[str, DescMessage]) -> list[tuple[str, DescMessage]]:
    """Every message the roots hold, each with the first root that holds it."""
    found: dict[str, str] = {}
    for root, desc in roots.items():
        for name in sorted(reaches(desc.name)):
            found.setdefault(name, root)
    return [(root, MESSAGES[name]) for name, root in found.items()]


class Case(unittest.TestCase):
    """A check with the fake and a client of it."""

    client_class: Any = pethost.Pethost
    fake: Fake
    client: Any
    maxDiff = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Fake()
        cls.client = cls.client_class("pth_check", base_url=cls.fake.url)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.close()
        cls.fake.close()

    @classmethod
    def close(cls) -> None:
        cls.client.close()

    def call(self, method: str, **arguments: Any) -> Any:
        return getattr(self.client, method)(**arguments)

    def required(self, method: str) -> dict[str, str]:
        """The arguments a method cannot be called without, each empty: the call's subject."""
        parameters = inspect.signature(getattr(self.client, method)).parameters.values()
        return {parameter.name: "" for parameter in parameters if parameter.default is inspect.Parameter.empty}

    def sends(self, method: str, plan: Plan) -> None:
        """Calls a method with a sample of its request: the fake must receive the wire's side of
        it, by POST, at the RPC's path."""
        rpc = RPCS[method]
        expected, arguments = pair(rpc.input, plan)
        self.fake.answer(b"")
        self.call(method, **arguments)

        call = self.fake.calls[-1]
        self.assertEqual((call.verb, call.path), ("POST", f"/{SERVICE.type_name}/{rpc.name}"))
        self.assertEqual(wire_class(rpc.input).from_binary(call.body), expected)
        self.assertEqual(call.body, expected.to_binary())

    def receives(self, method: str, plan: Plan) -> None:
        """Answers a method with a sample of its response: the call must return the public side."""
        sent, given = pair(RESPONSES[method], plan)
        self.fake.answer(sent.to_binary())
        self.assertEqual(self.call(method, **self.required(method)), public_class(RESPONSES[method])(**given))

    def fails(self) -> pethost.PethostError:
        """Calls the API's first method, which the fake was told to fail: the error it raises."""
        method = next(iter(METHODS))
        with self.assertRaises(pethost.PethostError) as raised:
            self.call(method, **self.required(method))
        return raised.exception
