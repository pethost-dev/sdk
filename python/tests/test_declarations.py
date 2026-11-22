"""What the package declares, held to the wire layer's descriptors and the proto's facts."""

from __future__ import annotations

import dataclasses
import inspect

from protobuf import DescField, DescMessage, ScalarType

from .harness import Checked, by_surface
from .samples import Plan, absent, attribute, empty, kind_of, marked, pair, public_class, repeated


def subject_of(request: DescMessage) -> tuple[str, bool] | None:
    """The parameter a call alone may give by position, and whether it must: the request's field
    number 1, when it is a plain string (outside a oneof, not repeated, not marked (optional)),
    which a call must give when it names a thing by its id (*_id)."""
    for member in request.members:
        if not isinstance(member, DescField) or member.number != 1:
            continue
        if kind_of(member) is ScalarType.STRING and not repeated(member) and not marked(member):
            return attribute(member.name), member.name.endswith("_id")
    return None


class Declarations(Checked):
    def test_classes(self) -> None:
        """A class has its message's fields and no other, each absent by default, and is frozen."""
        for desc in self.surface.messages.values():
            if not hasattr(self.surface.facts.public, desc.name):
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
        but the subject, which alone may be given by position, and has no default where it is an
        id."""
        for method, desc in self.surface.requests.items():
            with self.subTest(method=method):
                _, nothing = pair(desc, empty(desc, Plan()))
                parameters = dict(inspect.signature(getattr(self.surface.client(), method)).parameters)
                del parameters["self"]
                self.assertEqual(set(parameters), set(nothing))
                subject = subject_of(desc)
                for name, parameter in parameters.items():
                    if subject is not None and name == subject[0]:
                        self.assertIs(parameter.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD, name)
                        self.assertEqual(parameter.default, inspect.Parameter.empty if subject[1] else nothing[name], name)
                    else:
                        self.assertIs(parameter.kind, inspect.Parameter.KEYWORD_ONLY, name)
                        self.assertEqual(parameter.default, nothing[name], name)
                self.assertEqual(inspect.signature(getattr(self.surface.client(True), method)).parameters.keys(), {"self", *parameters})

    def test_optional_fields(self) -> None:
        """The fields marked (optional) are fields of messages the checks reach, and may be None."""
        details = {name: self.surface.messages[name] for name in self.surface.facts.details}
        roots = (self.surface.requests, self.surface.responses, details)
        reached = {desc.name for messages in roots for _, desc in self.surface.first_reaching(messages)}
        fields = {f"{desc.name}.{field.name}": field for desc in self.surface.messages.values() for field in desc.fields}
        for name in self.surface.facts.optional:
            with self.subTest(field=name):
                self.assertIn(name.split(".")[0], reached)
                self.assertIsNone(absent(fields[name]))

    def test_enums(self) -> None:
        """An enum has its values under the wire layer's names, with the proto's numbers. A number
        it does not have is a member too: one object, named for its number, outside the list."""
        for desc in self.surface.facts.wire.desc().enums:
            if not hasattr(self.surface.facts.public, desc.name):
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
        and each detail; its client has a method for each RPC of the facts and no other."""
        facts = self.surface.facts
        public = {name for name in vars(self.surface.client()) if not name.startswith("_")}
        self.assertEqual(public, {*facts.methods, "close"})
        clients = [facts.client, f"Async{facts.client}", f"{facts.client}Error", "ErrorDetail"]
        for name in [*facts.details, *(desc.name for desc in self.surface.responses.values()), *clients]:
            self.assertIn(name, facts.public.__all__)
        self.assertEqual({name for name in facts.public.__all__ if not hasattr(facts.public, name)}, set())


load_tests = by_surface(Declarations)
