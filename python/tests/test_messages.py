"""Every message of the API through the package, both ways."""

from __future__ import annotations

import pethost

from .api import METHODS
from .harness import MESSAGES, MOST_MEMBERS, REQUESTS, RESPONSES, Case, first_reaching
from .samples import REFUSED, Plan, alone, attribute, empty, pair, public_class, refusal_of


class Messages(Case):
    def test_every_field_set(self) -> None:
        """Every field of every message at once, with each member of each oneof in turn."""
        for method in METHODS:
            for member in range(MOST_MEMBERS):
                with self.subTest(method=method, member=member):
                    self.sends(method, Plan(member=member, sending=True))
                    self.receives(method, Plan(member=member))

    def test_one_field_at_a_time(self) -> None:
        """Each field alone in its message, at a sample, at its zero and at a number its enum does
        not have, and the message with no field at all. Here shows a field a converter leaves out
        or takes from another, a zero sent that must not be or dropped that must be, each member
        of a oneof and its zero, and what every absent field reads as."""
        for method, desc in first_reaching(REQUESTS):
            for plan in alone(desc, sending=True):
                with self.subTest(sent=plan):
                    self.sends(method, plan)
        for method, desc in first_reaching(RESPONSES):
            for plan in alone(desc):
                with self.subTest(received=plan):
                    self.receives(method, plan)

    def test_what_this_version_does_not_know(self) -> None:
        """A field a later API added is passed over, at every depth; a oneof whose member is one
        a later API added reads as a oneof with no member."""
        for method in METHODS:
            with self.subTest(method=method):
                self.receives(method, Plan(unknown=True))
        for method, desc in first_reaching(RESPONSES):
            if desc.oneofs:
                with self.subTest(oneof=desc.name):
                    self.receives(method, empty(desc, Plan(unknown=True)))

    def test_refused_before_sending(self) -> None:
        """One string for a list of strings, a time without a zone and an integer out of range
        are Python's own errors, and nothing is sent."""
        for method, desc in first_reaching(REQUESTS):
            for field in desc.fields:
                error = refusal_of(field)
                if error is None:
                    continue
                with self.subTest(field=f"{desc.name}.{field.name}"):
                    _, arguments = pair(REQUESTS[method], Plan(only=(desc.name, field.name), value=REFUSED, sending=True))
                    calls = len(self.fake.calls)
                    with self.assertRaises(error):
                        self.call(method, **arguments)
                    self.assertEqual(len(self.fake.calls), calls)

    def test_two_members_of_a_oneof(self) -> None:
        """Two members of one oneof are a TypeError, for a class and for a method alike."""
        for desc in MESSAGES.values():
            for oneof in desc.oneofs:
                if len(oneof.fields) < 2:
                    continue
                first, second = (attribute(field.name) for field in oneof.fields[:2])
                _, one = pair(desc, Plan(only=(desc.name, oneof.fields[0].name)))
                _, two = pair(desc, Plan(only=(desc.name, oneof.fields[1].name)))
                both = {**one, second: two[second]}
                self.assertIsNotNone(both[first])

                with self.subTest(oneof=f"{desc.name}.{oneof.name}"):
                    for method, request in REQUESTS.items():
                        if request.name == desc.name:
                            with self.assertRaises(TypeError):
                                self.call(method, **both)
                    if hasattr(pethost, desc.name):
                        with self.assertRaises(TypeError):
                            public_class(desc)(**both)
