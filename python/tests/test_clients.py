"""The two clients: who they say calls, and that the asyncio one does what the other does."""

from __future__ import annotations

import asyncio
import os
import unittest.mock
from typing import Any

import pethost
from pethost._version import VERSION

from .api import METHODS
from .harness import MOST_MEMBERS, Case
from .samples import Plan


class Clients(Case):
    def test_who_calls(self) -> None:
        """Every call carries the token and the package's name and version."""
        self.fake.answer(b"")
        method = next(iter(METHODS))
        self.call(method, **self.required(method))

        headers = self.fake.calls[-1].headers
        self.assertEqual(headers["authorization"], "Bearer pth_check")
        self.assertEqual(headers["user-agent"], f"pethost-python/{VERSION}")
        self.assertEqual(headers["content-type"], "application/proto")

    def test_token(self) -> None:
        """Without a token given, the environment's; without that, no client."""
        method = next(iter(METHODS))
        with unittest.mock.patch.dict(os.environ, {"PETHOST_TOKEN": "pth_environment"}):
            with pethost.Pethost(base_url=self.fake.url) as client:
                self.fake.answer(b"")
                getattr(client, method)(**self.required(method))
        self.assertEqual(self.fake.calls[-1].headers["authorization"], "Bearer pth_environment")

        with unittest.mock.patch.dict(os.environ, clear=True):
            with self.assertRaises(ValueError):
                pethost.Pethost()

    def test_a_token_as_a_file_holds_it(self) -> None:
        """A token comes without the line end around it; one that no header could carry is
        refused when the client is made, in words that do not repeat it."""
        method = next(iter(METHODS))
        with pethost.Pethost("pth_from_a_file\n", base_url=self.fake.url) as client:
            self.fake.answer(b"")
            getattr(client, method)(**self.required(method))
        self.assertEqual(self.fake.calls[-1].headers["authorization"], "Bearer pth_from_a_file")

        with self.assertRaises(ValueError) as refused:
            pethost.Pethost("pth_two\nlines")
        self.assertNotIn("pth_two", str(refused.exception))

    def test_timeout(self) -> None:
        """A timeout that is no time is refused when the client is made, not by every call."""
        for timeout in (0, -1, 0.0001):
            with self.subTest(timeout=timeout), self.assertRaises(ValueError):
                pethost.Pethost("pth_check", timeout=timeout)


class AsyncClients(Case):
    """The asyncio client, through the checks of the synchronous one: every field of every
    message, both ways. The converters are the same; its methods are its own."""

    client_class = pethost.AsyncPethost
    loop: asyncio.AbstractEventLoop

    @classmethod
    def setUpClass(cls) -> None:
        cls.loop = asyncio.new_event_loop()
        super().setUpClass()

    @classmethod
    def close(cls) -> None:
        cls.loop.run_until_complete(cls.client.aclose())
        cls.loop.close()

    def call(self, method: str, **arguments: Any) -> Any:
        return self.loop.run_until_complete(getattr(self.client, method)(**arguments))

    def test_every_field_set(self) -> None:
        for method in METHODS:
            for member in range(MOST_MEMBERS):
                with self.subTest(method=method, member=member):
                    self.sends(method, Plan(member=member, sending=True))
                    self.receives(method, Plan(member=member))

    def test_a_failed_call(self) -> None:
        self.fake.fail("not_found", "no such thing")
        error = self.fails()
        self.assertIs(type(error), pethost.NotFoundError)
        self.assertIsNone(error.__cause__)
