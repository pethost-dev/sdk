"""What a failed call raises."""

from __future__ import annotations

import unittest.mock

from connectrpc.code import Code

import pethost

from .api import DETAILS
from .harness import MESSAGES, SERVICE, Case, first_reaching
from .samples import Plan, alone, pair, public_class

PACKAGE = SERVICE.type_name.rsplit(".", 1)[0]


def error_class(code: Code) -> type[pethost.PethostError]:
    """The class of one of the protocol's codes: NOT_FOUND is NotFoundError."""
    found: type[pethost.PethostError] = getattr(pethost, "".join(word.capitalize() for word in code.name.split("_")) + "Error")
    return found


class Errors(Case):
    def test_each_code(self) -> None:
        """Each code of the protocol is its own class, with the API's message and no cause."""
        for code in Code:
            with self.subTest(code=code.name):
                self.fake.fail(code.value, f"said with {code.value}")
                error = self.fails()
                self.assertIs(type(error), error_class(code))
                self.assertEqual((error.message, str(error), error.detail), (f"said with {code.value}",) * 2 + (None,))
                self.assertIsNone(error.__cause__)

    def test_each_detail(self) -> None:
        """Each detail arrives as its class, on any code: every field of it, then each alone."""
        details = {name: MESSAGES[name] for name in DETAILS}
        for name, desc in first_reaching(details):
            for plan in [Plan(), *alone(desc)]:
                with self.subTest(detail=name, plan=plan):
                    sent, given = pair(details[name], plan)
                    self.fake.fail("failed_precondition", "refused", [(f"{PACKAGE}.{name}", sent.to_binary())])
                    self.assertEqual(self.fails().detail, public_class(details[name])(**given))

    def test_a_detail_the_package_cannot_read(self) -> None:
        """A detail a later API added, and one whose bytes are not its message, are passed over:
        the error is its code's all the same, and the first detail the package reads is its detail."""
        sent, given = pair(MESSAGES[DETAILS[0]], Plan())
        known = (f"{PACKAGE}.{DETAILS[0]}", sent.to_binary())
        unread = {
            "added later": (f"{PACKAGE}.AddedLater", sent.to_binary()),
            "not its message": (f"{PACKAGE}.{DETAILS[0]}", b"\xff"),
        }

        for why, detail in unread.items():
            with self.subTest(detail=why):
                self.fake.fail("unavailable", "something else", [detail])
                error = self.fails()
                self.assertIs(type(error), pethost.UnavailableError)
                self.assertEqual((error.message, error.detail), ("something else", None))

                self.fake.fail("unavailable", "something else, and something known", [detail, known])
                self.assertEqual(self.fails().detail, public_class(MESSAGES[DETAILS[0]])(**given))

    def test_never_reached(self) -> None:
        """A call that never reached the API, or got no answer in time, fails with a code too."""
        nowhere = pethost.Pethost("pth_check", base_url="http://127.0.0.1:1", timeout=2)
        with nowhere, unittest.mock.patch.object(self, "client", nowhere):
            self.assertIs(type(self.fails()), pethost.UnavailableError)

        hurried = pethost.Pethost("pth_check", base_url=self.fake.url, timeout=0.05)
        with hurried, unittest.mock.patch.object(self, "client", hurried):
            self.fake.answer(b"", delay=0.5)
            self.assertIs(type(self.fails()), pethost.DeadlineExceededError)
