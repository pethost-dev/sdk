"""What the generated modules lean on, the same for any version of the API: the open enum, the
oneof and encoding checks, times, the token, who calls. Written by hand: nothing here names a
message or a method."""

from __future__ import annotations

import datetime
import enum
import os
from typing import TYPE_CHECKING, Any, NoReturn, TypeVar

from protobuf import Message
from protobuf.wkt.google.protobuf.timestamp_pb import Timestamp

from ._version import VERSION

if TYPE_CHECKING:
    from collections.abc import Sequence

    from connectrpc.request import RequestContext

TOKEN_VARIABLE = "PETHOST_TOKEN"
USER_AGENT = f"pethost-python/{VERSION}"

_EPOCH = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
_Wire = TypeVar("_Wire", bound="Message[Any]")

# A value the API added after this version was generated, kept so that it is one object however
# often it arrives: `is` and `==` work on it as on a declared member.
_unrecognized: dict[tuple[type[OpenEnum], int], OpenEnum] = {}


class OpenEnum(enum.Enum):
    """An enum of the API.

    Its zero member, UNSPECIFIED, is how the API says "absent". A value the API added after this
    version of the package is a member too, named UNRECOGNIZED_<number>: comparing, printing and
    `match` work on it, so end a `match` with `case _` and never with `assert_never`.
    """

    @classmethod
    def _missing_(cls, value: object) -> OpenEnum | None:
        if not isinstance(value, int) or isinstance(value, bool):
            return None

        member = object.__new__(cls)
        member._name_ = f"UNRECOGNIZED_{value}"
        member._value_ = value
        return _unrecognized.setdefault((cls, value), member)


def never(value: NoReturn) -> NoReturn:
    """Type-checks only where every case before it was handled: a converter ends a oneof with it."""
    raise AssertionError(f"unhandled: {value!r}")


def one_of(owner: str, **members: object) -> None:
    """Refuses two members of one oneof: the API can hold only one."""
    given = [name for name, value in members.items() if value is not None]
    if len(given) > 1:
        raise TypeError(f"{owner} takes at most one of {', '.join(members)}: got {' and '.join(given)}")


def strings(name: str, values: Sequence[str]) -> list[str]:
    """A list of strings for the wire; one string, which Python also takes for a sequence, is refused."""
    if isinstance(values, str):
        raise TypeError(f"{name} takes a list of strings, not one string: [{values!r}]")
    return list(values)


def checked(wire: _Wire) -> _Wire:
    """Makes the wire layer refuse here what it cannot encode, as Python's own error: an integer
    out of its kind's range (OverflowError), a string that is not text (UnicodeEncodeError).
    Inside the call the same refusal would come back as UNAVAILABLE, "retry later"."""
    # ponytail: this encodes a request twice; check each integer's range in the converters
    # instead when a request grows large enough for that to show.
    wire.to_binary()
    return wire


def time_from_wire(wire: Timestamp) -> datetime.datetime:
    """An aware UTC datetime. A datetime holds microseconds: the nanoseconds below are cut."""
    return _EPOCH + datetime.timedelta(seconds=wire.seconds, microseconds=wire.nanos // 1000)


def time_to_wire(value: datetime.datetime) -> Timestamp:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError("a datetime without a time zone: write datetime.now(timezone.utc)")
    return Timestamp.from_datetime(value)


def token_or_environment(token: str | None) -> str:
    """The token given, or the environment's, without the line end a file or a secret store left
    on it. One that could not be a header's value is refused here, in words that do not repeat
    it: the HTTP client's own refusal would quote the token into a traceback."""
    token = (token or os.environ.get(TOKEN_VARIABLE) or "").strip()
    if not token:
        raise ValueError(f"no API token: pass one, or set {TOKEN_VARIABLE}")
    if not token.isascii() or not token.isprintable():
        raise ValueError("the API token has a character no token has: copy it again from the panel")
    return token


def timeout_ms(timeout: float | None) -> int | None:
    if timeout is None:
        return None
    if timeout < 0.001:
        raise ValueError("timeout is in seconds, 0.001 at least: None = no limit")
    return int(timeout * 1000)


class Caller:
    """Says who calls, on every call: the token, and this package with its version. It is
    connectrpc's metadata interceptor, for the synchronous client and the asyncio one."""

    def __init__(self, token: str) -> None:
        self._authorization = f"Bearer {token}"

    def _sign(self, ctx: RequestContext[Any, Any]) -> None:
        ctx.request_headers["authorization"] = self._authorization
        ctx.request_headers["user-agent"] = USER_AGENT

    def on_start_sync(self, ctx: RequestContext[Any, Any], /) -> None:
        self._sign(ctx)

    def on_end_sync(self, token: None, ctx: RequestContext[Any, Any], error: Exception | None, /) -> None:
        return

    async def on_start(self, ctx: RequestContext[Any, Any]) -> None:
        self._sign(ctx)

    async def on_end(self, token: None, ctx: RequestContext[Any, Any], error: Exception | None, /) -> None:
        return
