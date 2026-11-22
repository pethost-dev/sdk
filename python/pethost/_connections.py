"""The connections a client keeps, by what each is for: where a service answered at a Connection
is called for one key, the bearer of those calls, and until when (internal/sdk's Runtime, rules
3 and 4). The generated clients call, connect and repeat; this keeps. Written by hand: nothing
here names a message or a method."""

from __future__ import annotations

import datetime
import threading
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Kept:
    """A connection as a client keeps it. Its token is a credential: it is never printed."""

    url: str  # https://host: the server, where its calls go.
    token: str = field(repr=False)
    expire: datetime.datetime | None  # None = not said: it is good for the call it was made for alone.

    @property
    def headers(self) -> dict[str, str]:
        """What a call made with it sends beside the package's own headers: its bearer."""
        return {"authorization": f"Bearer {self.token}"}

    def good(self, margin: datetime.timedelta, now: datetime.datetime) -> bool:
        """Whether a call may still be made with it: its expiry more than the margin away."""
        return self.expire is not None and self.expire - margin > now


class Connections:
    """A client's connections, one for each key. One is kept while it is good, and those that
    are not are dropped whenever one is kept. Two calls that race for one key may both connect;
    the last connection kept is the key's. A lock keeps the map whole for a client used from
    several threads; nothing waits on a call under it."""

    def __init__(self, margin_seconds: int) -> None:
        self._margin = datetime.timedelta(seconds=margin_seconds)
        self._kept: dict[str, Kept] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> Kept | None:
        """The key's connection while it is good; None = connect."""
        with self._lock:
            kept = self._kept.get(key)
        if kept is None or not kept.good(self._margin, _now()):
            return None
        return kept

    def keep(self, key: str, connection: Kept) -> None:
        """Keeps a key's connection, in place of the one it had, if it is good at all."""
        now = _now()
        with self._lock:
            for stale in [k for k, kept in self._kept.items() if not kept.good(self._margin, now)]:
                del self._kept[stale]
            if connection.good(self._margin, now):
                self._kept[key] = connection

    def drop(self, key: str, refused: Kept) -> None:
        """Drops a key's connection that a server refused, unless another took its place since."""
        with self._lock:
            if self._kept.get(key) == refused:
                del self._kept[key]


def _now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)
