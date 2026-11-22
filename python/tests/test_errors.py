"""What a failed call raises."""

from __future__ import annotations

import unittest.mock

from connectrpc.code import Code

from .harness import TOKEN, Case, by_surface
from .samples import Plan, alone, pair, public_class


class Errors(Case):
    def package(self) -> str:
        """The proto package, which an error detail's type name starts with."""
        return next(iter(self.surface.rpcs.values())).parent.type_name.rsplit(".", 1)[0]

    def test_each_code(self) -> None:
        """Each code of the protocol is its own class, with the API's message and no cause."""
        for code in Code:
            with self.subTest(code=code.name):
                self.fake.fail(code.value, f"said with {code.value}")
                error = self.fails()
                self.assertCode(error, code.value)
                self.assertEqual((error.message, str(error), error.detail), (f"said with {code.value}",) * 2 + (None,))
                self.assertIsNone(error.__cause__)

    def test_each_detail(self) -> None:
        """Each detail arrives as its class, on any code: every field of it, then each alone."""
        details = {name: self.surface.messages[name] for name in self.surface.facts.details}
        for name, desc in self.surface.first_reaching(details):
            for plan in [Plan(), *alone(desc)]:
                with self.subTest(detail=name, plan=plan):
                    sent, given = pair(details[name], plan)
                    self.fake.fail("failed_precondition", "refused", [(f"{self.package()}.{name}", sent.to_binary())])
                    self.assertEqual(self.fails().detail, public_class(details[name])(**given))

    def test_a_detail_the_package_cannot_read(self) -> None:
        """A detail a later API added, and one whose bytes are not its message, are passed over:
        the error is its code's all the same, and the first detail the package reads is its detail."""
        first = self.surface.facts.details[0]
        sent, given = pair(self.surface.messages[first], Plan())
        known = (f"{self.package()}.{first}", sent.to_binary())
        unread = {
            "added later": (f"{self.package()}.AddedLater", sent.to_binary()),
            "not its message": (f"{self.package()}.{first}", b"\xff"),
        }

        for why, detail in unread.items():
            with self.subTest(detail=why):
                self.fake.fail("unavailable", "something else", [detail])
                error = self.fails()
                self.assertCode(error, "unavailable")
                self.assertEqual((error.message, error.detail), ("something else", None))

                self.fake.fail("unavailable", "something else, and something known", [detail, known])
                self.assertEqual(self.fails().detail, public_class(self.surface.messages[first])(**given))

    def test_never_reached(self) -> None:
        """A call that never reached the API, or got no answer in time, fails with a code too."""
        nowhere = self.surface.client()(TOKEN, base_url="http://127.0.0.1:1", timeout=2)
        with nowhere, unittest.mock.patch.object(self, "client", nowhere):
            self.assertCode(self.fails(), "unavailable")

        hurried = self.surface.client()(TOKEN, base_url=self.fake.url, timeout=0.05)
        with hurried, unittest.mock.patch.object(self, "client", hurried):
            self.fake.answer(b"", delay=0.5)
            self.assertCode(self.fails(), "deadline_exceeded")


load_tests = by_surface(Errors)
