"""The two clients: who they say calls, and that the asyncio one does what the other does."""

from __future__ import annotations

import os
import unittest.mock
from typing import Any

from pethost._version import VERSION

from .fake import CALL
from .harness import TOKEN, AsyncCase, Case, by_surface
from .samples import Plan, wire_class


class Clients(Case):
    def first(self) -> str:
        """The surface's first method, which is called at the API's address."""
        return next(iter(self.surface.facts.methods))

    def test_who_calls(self) -> None:
        """Every call carries the token and the package's name and version, and is a call of
        the Connect protocol whose message is binary protobuf."""
        self.fake.answer(b"")
        method = self.first()
        self.call(method, **self.required(method))

        headers = self.fake.calls[-1].headers
        self.assertEqual(headers["authorization"], f"Bearer {TOKEN}")
        self.assertEqual(headers["user-agent"], f"pethost-python/{VERSION}")
        self.assertEqual((headers["content-type"], headers["connect-protocol-version"]), (CALL, "1"))

    def test_token(self) -> None:
        """Without a token given, the environment's; without that, no client."""
        method = self.first()
        with unittest.mock.patch.dict(os.environ, {"PETHOST_TOKEN": "pth_environment"}):
            with self.surface.client()(base_url=self.fake.url) as client:
                self.fake.answer(b"")
                getattr(client, method)(**self.required(method))
        self.assertEqual(self.fake.calls[-1].headers["authorization"], "Bearer pth_environment")

        with unittest.mock.patch.dict(os.environ, clear=True):
            with self.assertRaises(ValueError):
                self.surface.client()()

    def test_a_token_as_a_file_holds_it(self) -> None:
        """A token comes without the line end around it; one that no header could carry is
        refused when the client is made, in words that do not repeat it."""
        method = self.first()
        with self.surface.client()("pth_from_a_file\n", base_url=self.fake.url) as client:
            self.fake.answer(b"")
            getattr(client, method)(**self.required(method))
        self.assertEqual(self.fake.calls[-1].headers["authorization"], "Bearer pth_from_a_file")

        with self.assertRaises(ValueError) as refused:
            self.surface.client()("pth_two\nlines")
        self.assertNotIn("pth_two", str(refused.exception))

    def test_workspace(self) -> None:
        """A client made with a workspace sends it in each request that names none, and a
        request's own where it names one. A request of a service answered at a Connection,
        whose server reads no workspace, gets none from the client."""
        facts = self.surface.facts
        named = [method for method, desc in self.surface.requests.items() if any(f.name == facts.workspace for f in desc.fields)]
        self.assertTrue(named or not facts.workspace, "no request names a workspace")
        self.assertLessEqual(facts.workspaced, set(named))

        options: dict[str, Any] = {facts.workspace: "the client's"}
        with self.surface.client()(TOKEN, base_url=self.fake.url, **options) as client:
            for method in named:
                filled = "the client's" if method in facts.workspaced else ""
                for given, sent in (("", filled), ("its own", "its own")):
                    with self.subTest(method=method, given=given):
                        fake = self.fake_of(method)
                        fake.answer(b"")
                        answer = getattr(client, method)(**{**self.required(method), facts.workspace: given})
                        if method in self.surface.streams:
                            list(answer)
                        body = wire_class(self.surface.requests[method]).from_binary(fake.calls[-1].body)
                        self.assertEqual(getattr(body, facts.workspace), sent)

    def test_timeout(self) -> None:
        """A timeout that is no time is refused when the client is made, not by every call."""
        for timeout in (0, -1, 0.0001):
            with self.subTest(timeout=timeout), self.assertRaises(ValueError):
                self.surface.client()(TOKEN, timeout=timeout)


class AsyncClients(AsyncCase):
    """The asyncio client, through the checks of the synchronous one: every field of every
    message, both ways. The converters are the same; its methods are its own."""

    def test_every_field_set(self) -> None:
        for method in self.surface.facts.methods:
            for member in range(self.surface.most_members):
                with self.subTest(method=method, member=member):
                    self.sends(method, Plan(member=member, sending=True))
                    self.receives(method, Plan(member=member))

    def test_a_failed_call(self) -> None:
        self.fake.fail("not_found", "no such thing")
        error = self.fails()
        self.assertCode(error, "not_found")
        self.assertIsNone(error.__cause__)


load_tests = by_surface(Clients, AsyncClients)
