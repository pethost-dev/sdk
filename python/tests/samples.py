"""Samples of the API's messages, for any version of it: one walk over a message's descriptor in
the wire layer builds the wire message and, beside it, what the package must make of it (the
arguments of the public class, or of the method). A check sends one side through the package
and expects the other.

The walk knows the package's rules and none of its code. A public class is named as its message
and takes its fields by their names; an absent field is None where the proto says absence means
something (a message, a oneof's member, a field marked (optional)) and the zero value anywhere
else; an enum is the public enum of the same name; a time is an aware datetime; a list is a
tuple. Every value is made from its field's name, so two fields swapped do not look alike."""

from __future__ import annotations

import functools
import keyword
import zlib
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Any

from protobuf import DescEnum, DescField, DescMessage, DescOneof, Message, Oneof, ScalarType
from protobuf.wkt.google.protobuf.timestamp_pb import Timestamp

import pethost

from .api import OPTIONAL, wire

# A field no version of the API has, as the wire carries it: number 2**29 - 1, the largest.
UNKNOWN_FIELD = b"\xf8\xff\xff\xff\x0f\x01"

# What a field is set to. REFUSED is a value the package must refuse before it sends anything.
SAMPLE, ZERO, UNKNOWN, REFUSED = "a sample", "its zero", "a number its enum does not have", "a value to refuse"

INTEGERS = set(ScalarType) - {ScalarType.STRING, ScalarType.BYTES, ScalarType.BOOL, ScalarType.DOUBLE, ScalarType.FLOAT}


@dataclass(frozen=True)
class Plan:
    """Which fields a sample sets, and to what."""

    member: int | None = 0  # Of each oneof, the member of this index (modulo their number); None = none.
    only: tuple[str, str] | None = None  # (message, field): that message has this field alone.
    value: str = SAMPLE  # What `only`'s field is set to.
    sending: bool = False  # The wire side is what the package must send, not what it is given.
    unknown: bool = False  # Every wire message carries a field the package does not know.


def empty(desc: DescMessage, plan: Plan) -> Plan:
    """The plan of a message with nothing set: no field has the empty name."""
    return Plan(only=(desc.name, ""), sending=plan.sending, unknown=plan.unknown)


def alone(desc: DescMessage, **how: Any) -> list[Plan]:
    """The plans that set one field of a message alone, to each value a check gives it, and
    first the plan that sets none."""
    plans = [empty(desc, Plan(**how))]
    for field in desc.fields:
        plans += [Plan(only=(desc.name, field.name), value=value, **how) for value in values_of(field)]
    return plans


def values_of(field: DescField) -> list[str]:
    """What a check sets a field to when it alone is set."""
    kind = kind_of(field)
    if repeated(field) or is_time(kind):
        return [SAMPLE]
    if isinstance(kind, DescEnum):
        return [SAMPLE, ZERO, UNKNOWN]
    return [SAMPLE, ZERO]


def refusal_of(field: DescField) -> type[Exception] | None:
    """What the package raises for a field's REFUSED value: one string where a list of strings
    goes, a time without a zone, an integer no kind holds. None = its kind has no such value."""
    kind = kind_of(field)
    if repeated(field):
        return TypeError if kind is ScalarType.STRING else None
    if is_time(kind):
        return ValueError
    return OverflowError if kind in INTEGERS else None


def kind_of(field: DescField) -> DescMessage | DescEnum | ScalarType:
    """What one value of a field is."""
    value: Any = field.value
    kind: DescMessage | DescEnum | ScalarType
    if repeated(field):
        kind = value.element
    else:
        kind = getattr(value, "message", None) or getattr(value, "enum", None) or value.scalar
    return kind


def repeated(field: DescField) -> bool:
    return hasattr(field.value, "element")


def is_time(kind: object) -> bool:
    return isinstance(kind, DescMessage) and kind.type_name == Timestamp.desc().type_name


def marked(field: DescField) -> bool:
    return f"{field.parent.name}.{field.name}" in OPTIONAL


def attribute(name: str) -> str:
    """A field's name in Python."""
    return name + "_" if keyword.iskeyword(name) else name


def public_class(desc: DescMessage | DescEnum) -> Any:
    return getattr(pethost, desc.name)


def wire_class(desc: DescMessage | DescEnum) -> Any:
    return getattr(wire, desc.name)


@functools.cache
def reaches(name: str) -> frozenset[str]:
    """The names of the messages a message holds at any depth, its own among them."""
    found = {name}
    for field in getattr(wire, name).desc().fields:
        kind = kind_of(field)
        if isinstance(kind, DescMessage) and not is_time(kind):
            found |= reaches(kind.name)
    return frozenset(found)


def number(name: str) -> int:
    """A small number of the name's own: it fits every integer kind and is the same in every run."""
    return zlib.crc32(name.encode()) % 1000 + 1


def one(field: DescField, plan: Plan, how: str) -> tuple[Any, Any]:
    """One value of a field: the wire's, and the public one."""
    kind = kind_of(field)
    if is_time(kind):
        when = datetime(2026, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=number(field.name), microseconds=number(field.name))
        return Timestamp.from_datetime(when), when.replace(tzinfo=None) if how == REFUSED else when
    if isinstance(kind, DescMessage):
        sent, given = pair(kind, plan if how == SAMPLE else empty(kind, plan))
        return sent, public_class(kind)(**given)
    if isinstance(kind, DescEnum):
        numbers = [value.number for value in kind.values]
        chosen = {ZERO: 0, UNKNOWN: max(numbers) + 1000}.get(how, numbers[1 + number(field.name) % (len(numbers) - 1)])
        return wire_class(kind)(chosen), public_class(kind)(chosen)

    value: Any
    if kind is ScalarType.STRING:
        value = "" if how == ZERO else field.name
    elif kind is ScalarType.BYTES:
        value = b"" if how == ZERO else field.name.encode()
    elif kind is ScalarType.BOOL:
        value = how != ZERO
    elif kind in INTEGERS:
        value = {ZERO: 0, REFUSED: 2**70}.get(how, number(field.name))
    else:
        value = 0.0 if how == ZERO else number(field.name) + 0.5
    return value, value


def absent(field: DescField) -> Any:
    """What the public side holds for a field outside a oneof that the wire does not carry."""
    if repeated(field):
        return ()
    if isinstance(kind_of(field), DescMessage) or marked(field):
        return None
    return one(field, Plan(), ZERO)[1]


def chosen_member(oneof: DescOneof, plan: Plan, here: bool) -> DescField | None:
    """The member a sample sets: the one `only` names; else one that leads to `only`'s message,
    so that the message is in the sample; else the plan's."""
    if plan.only is not None and here:
        return next((field for field in oneof.fields if field.name == plan.only[1]), None)
    if plan.only is not None:
        for field in oneof.fields:
            kind = kind_of(field)
            if isinstance(kind, DescMessage) and not is_time(kind) and plan.only[0] in reaches(kind.name):
                return field
    if plan.member is None:
        return None
    return oneof.fields[plan.member % len(oneof.fields)]


def pair(desc: DescMessage, plan: Plan) -> tuple[Message[Any], dict[str, Any]]:
    """A wire message and the arguments of the public class (or method) for the same thing: every
    field by its keyword, the absent ones too, so that nothing rests on a default."""
    sent: Message[Any] = wire_class(desc)()
    given: dict[str, Any] = {}
    here = plan.only is not None and plan.only[0] == desc.name
    how = plan.value if here else SAMPLE

    for member in desc.members:
        if isinstance(member, DescOneof):
            given.update({attribute(field.name): None for field in member.fields})
            chosen = chosen_member(member, plan, here)
            if chosen is not None:
                value, given[attribute(chosen.name)] = one(chosen, plan, how)
                setattr(sent, member.local_name, Oneof(chosen.name, value))
            continue

        given[attribute(member.name)] = absent(member)
        if plan.only is not None and here and member.name != plan.only[1]:
            continue

        value, public = one(member, plan, how)
        if repeated(member):
            value, public = [value], public if how == REFUSED else (public,)
        given[attribute(member.name)] = public
        # Sent at its zero only where absence means something else: a plain field is left out.
        if not (plan.sending and how == ZERO and absent(member) is not None):
            setattr(sent, member.local_name, value)

    if plan.unknown:
        sent = wire_class(desc).from_binary(sent.to_binary() + UNKNOWN_FIELD)
    return sent, given
