"""The hand-written runtime, where the samples do not reach: they hold a time to the microsecond."""

from __future__ import annotations

import unittest
from datetime import datetime, timezone

from protobuf.wkt.google.protobuf.timestamp_pb import Timestamp

from pethost._runtime import time_from_wire, time_to_wire


class Times(unittest.TestCase):
    def test_finer_than_a_microsecond(self) -> None:
        """A time's digits below the microsecond are cut, never rounded into the next one."""
        read = time_from_wire(Timestamp(seconds=1, nanos=999_999_999))
        self.assertEqual(read, datetime(1970, 1, 1, 0, 0, 1, 999_999, tzinfo=timezone.utc))
        self.assertEqual(read.utcoffset(), timezone.utc.utcoffset(None))

    def test_before_the_epoch(self) -> None:
        """A time before 1970 counts its fraction forward, as the wire does: -1 s + 0.5 s."""
        read = time_from_wire(Timestamp(seconds=-1, nanos=500_000_000))
        self.assertEqual(read, datetime(1969, 12, 31, 23, 59, 59, 500_000, tzinfo=timezone.utc))
        self.assertEqual(time_to_wire(read), Timestamp(seconds=-1, nanos=500_000_000))
