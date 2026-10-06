"""What the package declares, held to the wire layer's descriptors and the proto's facts."""

from __future__ import annotations

import dataclasses
import inspect
import unittest

import pethost

from protobuf import DescField, DescMessage, ScalarType

from .api import DETAILS, METHODS, OPTIONAL, wire
from .harness import MESSAGES, REQUESTS, RESPONSES, first_reaching
from .samples import Plan, absent, attribute, empty, kind_of, marked, pair, public_class, repeated


def subject_of(request: DescMessage) -> str | None:
    """The parameter a call must give, and alone may give by position: the request's field
    number 1, when it is a plain string (outside a oneof, not repeated, not marked (optional))."""
    for member in request.members:
        if not isinstance(member, DescField) or member.number != 1:
            continue
        if kind_of(member) is ScalarType.STRING and not repeated(member) and not marked(member):
            return attribute(member.name)
    return None


class Declarations(unittest.TestCase):
    def test_classes(self) -> None:
        """A class has its message's fields and no other, each absent by default, and is frozen."""
        for desc in MESSAGES.values():
            if not hasattr(pethost, desc.name):
                continue
            with self.subTest(message=desc.name):
                _, nothing = pair(desc, empty(desc, Plan()))
                cls = public_class(desc)
                self.assertEqual({field.name for field in dataclasses.fields(cls)}, set(nothing))
                self.assertEqual(cls(), cls(**nothing))
                for name in nothing:
                    with self.assertRaises(dataclasses.FrozenInstanceError):
                        setattr(cls(), name, None)

    def test_methods(self) -> None:
        """A method takes its request's fields and no other: each a keyword absent by default,
        but the subject, which has no default and alone may be given by position."""
        for method, desc in REQUESTS.items():
            with self.subTest(method=method):
                _, nothing = pair(desc, empty(desc, Plan()))
                parameters = dict(inspect.signature(getattr(pethost.Pethost, method)).parameters)
                del parameters["self"]
                self.assertEqual(set(parameters), set(nothing))
                for name, parameter in parameters.items():
                    if name == subject_of(desc):
                        self.assertIs(parameter.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD, name)
                        self.assertIs(parameter.default, inspect.Parameter.empty, name)
                    else:
                        self.assertIs(parameter.kind, inspect.Parameter.KEYWORD_ONLY, name)
                        self.assertEqual(parameter.default, nothing[name], name)
                self.assertEqual(inspect.signature(getattr(pethost.AsyncPethost, method)).parameters.keys(), {"self", *parameters})

    def test_optional_fields(self) -> None:
        """The fields marked (optional) are fields of messages the checks reach, and may be None."""
        details = {name: MESSAGES[name] for name in DETAILS}
        reached = {desc.name for roots in (REQUESTS, RESPONSES, details) for _, desc in first_reaching(roots)}
        fields = {f"{desc.name}.{field.name}": field for desc in MESSAGES.values() for field in desc.fields}
        for name in OPTIONAL:
            with self.subTest(field=name):
                self.assertIn(name.split(".")[0], reached)
                self.assertIsNone(absent(fields[name]))

    def test_enums(self) -> None:
        """An enum has its values under the wire layer's names, with the proto's numbers. A number
        it does not have is a member too: one object, named for its number, outside the list."""
        for desc in wire.desc().enums:
            if not hasattr(pethost, desc.name):
                continue
            with self.subTest(enum=desc.name):
                cls = public_class(desc)
                self.assertEqual({member.name: member.value for member in cls}, {value.local_name: value.number for value in desc.values})
                later = cls(max(member.value for member in cls) + 1000)
                self.assertIs(later, cls(later.value))
                self.assertEqual(later.name, f"UNRECOGNIZED_{later.value}")
                self.assertNotIn(later, list(cls))

    def test_names(self) -> None:
        """The package exports its clients, its errors, and a class for each method's response
        and each detail; it has a method for each RPC of the facts and no other."""
        public = {name for name in vars(pethost.Pethost) if not name.startswith("_")}
        self.assertEqual(public, {*METHODS, "close"})
        for name in [*DETAILS, *(desc.name for desc in RESPONSES.values()), "Pethost", "AsyncPethost", "PethostError", "ErrorDetail"]:
            self.assertIn(name, pethost.__all__)
        self.assertEqual({name for name in pethost.__all__ if not hasattr(pethost, name)}, set())
