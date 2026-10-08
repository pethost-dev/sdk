"""Every class as the API's JSON, both ways: what the package writes is the wire layer's own JSON
of the same message under the proto's field names, and what it reads is what the API takes."""

from __future__ import annotations

import base64
import json
import unittest
from collections.abc import Iterator
from datetime import datetime
from typing import Any

import pethost

from protobuf import DescEnum, DescMessage, Message, ScalarType

from .harness import MESSAGES, MOST_MEMBERS
from .samples import Plan, alone, attribute, is_time, kind_of, pair, public_class, repeated

CLASSES = [desc for desc in MESSAGES.values() if hasattr(pethost, desc.name)]

# The integers JSON has as strings: its numbers do not hold 64 bits.
WIDE = {ScalarType.INT64, ScalarType.UINT64, ScalarType.SINT64, ScalarType.FIXED64, ScalarType.SFIXED64}

# What from_dict takes, each as the wire layer's options that write it: the API's own form, keys
# in lowerCamelCase, enums by their numbers.
TAKEN: tuple[dict[str, Any], ...] = ({"use_proto_field_name": True}, {}, {"print_enums_as_ints": True})


def samples(desc: DescMessage, *, sending: bool) -> Iterator[tuple[Plan, Message[Any], Any]]:
    """Samples of a class, each as the wire layer's message and as the class's value: every field
    at once with each member of each oneof in turn, then each field alone, at a sample, at its
    zero and at a number its enum does not have, and the message with no field."""
    for plan in [*(Plan(member=member, sending=sending) for member in range(MOST_MEMBERS)), *alone(desc, sending=sending)]:
        sent, given = pair(desc, plan)
        yield plan, sent, public_class(desc)(**given)


class Json(unittest.TestCase):
    maxDiff = None

    def test_to_dict(self) -> None:
        """A class writes what the wire layer writes of the message it sends, under the proto's
        field names: `json.dumps` takes it, it has the API's form, and from_dict reads it back."""
        for desc in CLASSES:
            for plan, sent, value in samples(desc, sending=True):
                with self.subTest(message=desc.name, plan=plan):
                    written = value.to_dict()
                    self.assertEqual(json.loads(json.dumps(written)), json.loads(sent.to_json(use_proto_field_name=True)))
                    self.in_the_form(desc, written)
                    self.assertEqual(public_class(desc).from_dict(written), value)

    def test_from_dict(self) -> None:
        """A class reads what the API writes, a field at its zero too, which to_dict leaves out,
        and what the API takes beside its own form: keys in lowerCamelCase, an enum by its number."""
        for desc in CLASSES:
            for plan, sent, value in samples(desc, sending=False):
                for form in TAKEN:
                    with self.subTest(message=desc.name, plan=plan, form=form):
                        self.assertEqual(public_class(desc).from_dict(json.loads(sent.to_json(**form))), value)

    def test_what_no_version_of_the_api_has(self) -> None:
        """A key that is no field of the message is refused, as the API refuses it, and so is a
        value that is not of its field's kind; a 64-bit integer is read as a number too, and
        one that 64 bits do not hold is an OverflowError."""
        for desc in CLASSES:
            cls = public_class(desc)
            with self.subTest(message=desc.name):
                with self.assertRaises(ValueError):
                    cls.from_dict({"no_such_field": 1})
                for field in desc.fields:
                    with self.assertRaises((TypeError, ValueError)):
                        cls.from_dict({field.name: {} if repeated(field) else []})
                    if kind_of(field) in WIDE and not repeated(field):
                        self.assertEqual(cls.from_dict({field.name: 7}), cls.from_dict({field.name: "7"}))
                        with self.assertRaises(OverflowError):
                            cls.from_dict({field.name: 2**64})

    def test_a_value_its_enum_does_not_have(self) -> None:
        """A number a later API gave an enum is read as a member and written as the number; a
        name this version does not know is refused."""
        for desc in CLASSES:
            cls = public_class(desc)
            for field in desc.fields:
                kind = kind_of(field)
                if not isinstance(kind, DescEnum) or repeated(field):
                    continue
                with self.subTest(field=f"{desc.name}.{field.name}"):
                    later = max(value.number for value in kind.values) + 1000
                    read = cls.from_dict({field.name: later})
                    self.assertIs(getattr(read, attribute(field.name)), public_class(kind)(later))
                    self.assertEqual(read.to_dict(), {field.name: later})
                    with self.assertRaises(ValueError):
                        cls.from_dict({field.name: "ADDED_LATER"})

    def in_the_form(self, desc: DescMessage, written: dict[str, Any]) -> None:
        """Holds a message's JSON to the API's form by the proto's descriptor, without a codec, at
        every depth: a key is a field's name in the proto, a oneof's member under its own; an
        enum is its value's name in the proto, or the number of a value the proto has not; a
        64-bit integer is a string, a time RFC 3339 in UTC, bytes base64."""
        fields = {field.name: field for field in desc.fields}
        for key, value in written.items():
            self.assertIn(key, fields)
            kind = kind_of(fields[key])
            for one in value if repeated(fields[key]) else [value]:
                if is_time(kind):
                    self.assertEqual(one[-1], "Z")
                    datetime.fromisoformat(one[:-1])
                elif isinstance(kind, DescMessage):
                    self.in_the_form(kind, one)
                elif isinstance(kind, DescEnum):
                    self.assertIn(one, {v.name for v in kind.values} if isinstance(one, str) else {one} - {v.number for v in kind.values})
                elif kind in WIDE:
                    self.assertEqual(one, str(int(one)))
                elif kind is ScalarType.BYTES:
                    self.assertEqual(base64.b64encode(base64.b64decode(one)).decode(), one)
