"""A stream's method: each response as the API sends it, the pulses it passes over, how the
stream ends, and that a caller who leaves ends the call."""

from __future__ import annotations

import asyncio
import threading
from typing import Any

import pethost
from pethost._version import VERSION

from .api import DETAILS, METHODS
from .fake import PATIENCE, STREAM
from .harness import MESSAGES, RESPONSES, SERVICE, STREAMS, AsyncCase, Case
from .samples import Plan, empty, pair, public_class

PACKAGE = SERVICE.type_name.rsplit(".", 1)[0]


class Streams(Case):
    # How a caller leaves a stream it has read one response of: each a method here, which
    # answers with that response and with whether the fake then saw its caller gone.
    ways: tuple[str, ...] = ("leaves_the_loop", "closes")

    def stream(self, method: str) -> Any:
        return getattr(self.client, method)(**self.required(method))

    def samples(self, method: str) -> tuple[tuple[bytes, ...], list[Any]]:
        """Three responses of a stream, as the wire carries them and as the package must yield
        them. The middle one has only what this version does not know, so that their order
        shows: it reads as a response with nothing set, and is no pulse, as none of them is."""
        desc = RESPONSES[method]
        pairs = [pair(desc, plan) for plan in (Plan(), empty(desc, Plan(unknown=True)), Plan(member=1))]
        sent = tuple(wired.to_binary() for wired, _ in pairs)
        assert all(sent), "a sample with no bytes is a pulse"
        return sent, [public_class(desc)(**given) for _, given in pairs]

    def test_who_calls(self) -> None:
        """The method calls nothing: the loop does. The call carries the token and the package's
        name, as any call, says that it is a stream of the Connect protocol, and does not carry
        the client's timeout: a stream lasts as long as its loop."""
        for method in sorted(STREAMS):
            with self.subTest(method=method):
                self.fake.answer()
                calls = len(self.fake.calls)
                stream = self.stream(method)
                self.assertEqual(len(self.fake.calls), calls)
                self.read(stream)

                headers = self.fake.calls[-1].headers
                self.assertEqual(headers["authorization"], "Bearer pth_check")
                self.assertEqual(headers["user-agent"], f"pethost-python/{VERSION}")
                self.assertEqual(headers["content-type"], STREAM)
                self.assertNotIn("connect-timeout-ms", headers)

        for method in sorted(set(METHODS) - STREAMS)[:1]:  # The header a call that is no stream has.
            self.fake.answer(b"")
            self.call(method, **self.required(method))
            self.assertIn("connect-timeout-ms", self.fake.calls[-1].headers)

    def test_each_response_then_the_failure(self) -> None:
        """A stream yields each response in the API's order. The failure that ends it is raised
        once, after them: the class of its code, with the API's message and detail."""
        sent_detail, given_detail = pair(MESSAGES[DETAILS[0]], Plan())
        detail = (f"{PACKAGE}.{DETAILS[0]}", sent_detail.to_binary())
        for method in sorted(STREAMS):
            with self.subTest(method=method):
                sent, expected = self.samples(method)
                self.fake.fail("out_of_range", "no longer kept", [detail], after=sent)
                stream = self.stream(method)
                responses, error = self.read(stream)

                self.assertEqual(responses, expected)
                assert isinstance(error, pethost.PethostError), error
                self.assertIs(type(error), pethost.OutOfRangeError)
                self.assertEqual((error.message, error.detail), ("no longer kept", public_class(MESSAGES[DETAILS[0]])(**given_detail)))
                self.assertIsNone(error.__cause__)
                self.assertEqual(self.read(stream), ([], None))

    def test_a_call_that_fails(self) -> None:
        """A stream whose call the API refuses raises that, and yields nothing."""
        for method in sorted(STREAMS):
            with self.subTest(method=method):
                self.fake.fail("not_found", "no such thing")
                responses, error = self.read(self.stream(method))
                self.assertEqual(responses, [])
                self.assertIs(type(error), pethost.NotFoundError)

    def test_a_stream_that_ends(self) -> None:
        """A stream that ends by itself ends the loop, without an error."""
        for method in sorted(STREAMS):
            with self.subTest(method=method):
                sent, expected = self.samples(method)
                self.fake.answer(*sent)
                self.assertEqual(self.read(self.stream(method)), (expected, None))

    def test_pulses(self) -> None:
        """A response with nothing set is the API's pulse, which keeps a quiet stream open. A
        stream passes over it wherever it stands: before, between and after its responses, which
        are yielded in the API's order and alone. A stream of pulses alone yields nothing and
        ends as any other, and a failure after pulses is raised as after responses."""
        pulse = b""
        for method in sorted(STREAMS):
            with self.subTest(method=method):
                sent, expected = self.samples(method)
                self.fake.answer(pulse, sent[0], pulse, pulse, sent[1], pulse, sent[2], pulse)
                self.assertEqual(self.read(self.stream(method)), (expected, None))

                self.fake.answer(pulse, pulse, pulse)
                self.assertEqual(self.read(self.stream(method)), ([], None))

                self.fake.fail("unavailable", "call again", after=(pulse, sent[0], pulse))
                responses, error = self.read(self.stream(method))
                self.assertEqual(responses, expected[:1])
                self.assertIs(type(error), pethost.UnavailableError)

    def test_leaving_ends_the_call(self) -> None:
        """A response is yielded while the stream is still open, and a caller that then leaves
        ends the call, in each way there is to leave: the fake sees its caller gone. The client
        goes on to its next call."""
        for method in sorted(STREAMS):
            sent, expected = self.samples(method)
            for way in self.ways:
                with self.subTest(method=method, way=way):
                    left = self.fake.hold(sent[0])
                    response, gone = getattr(self, way)(method, left)
                    self.assertEqual(response, expected[0])
                    self.assertTrue(gone, "the API still streams to a caller that left")

                    self.fake.answer(sent[1])
                    self.assertEqual(self.read(self.stream(method)), (expected[1:2], None))

    def leaves_the_loop(self, method: str, left: threading.Event) -> tuple[Any, bool]:
        """Nothing holds the generator but the loop: Python closes it as the loop is left."""
        response = None
        for response in self.stream(method):
            break
        return response, left.wait(PATIENCE)

    def closes(self, method: str, left: threading.Event) -> tuple[Any, bool]:
        """A variable holds the generator, also while the fake waits: close() ends the call."""
        stream = self.stream(method)
        response = next(stream)
        stream.close()
        return response, left.wait(PATIENCE)


class AsyncStreams(AsyncCase, Streams):
    """The asyncio client's streams, through the checks of the synchronous one's."""

    ways = (*Streams.ways, "cancels")

    def leaves_the_loop(self, method: str, left: threading.Event) -> tuple[Any, bool]:
        """Nothing holds the generator but the loop: asyncio closes it on the event loop's next
        turn, so the loop runs on while the fake waits."""

        async def leave() -> Any:
            async for response in self.stream(method):
                return response

        response = self.loop.run_until_complete(leave())
        return response, self.loop.run_until_complete(self.loop.run_in_executor(None, left.wait, PATIENCE))

    def closes(self, method: str, left: threading.Event) -> tuple[Any, bool]:
        """A variable holds the generator: aclose() ends the call itself, and leaves nothing for
        the event loop to do, which does not run while the fake waits."""
        stream = self.stream(method)

        async def close() -> Any:
            response = await stream.__anext__()
            await stream.aclose()
            return response

        return self.loop.run_until_complete(close()), left.wait(PATIENCE)

    def cancels(self, method: str, left: threading.Event) -> tuple[Any, bool]:
        """The task is cancelled while it waits for the next response: it ends cancelled, as
        with any other await, and the call with it."""

        async def cancel() -> Any:
            first: asyncio.Future[Any] = self.loop.create_future()

            async def follow() -> None:
                async for response in self.stream(method):
                    first.set_result(response)

            task = self.loop.create_task(follow())
            response = await first
            task.cancel()
            with self.assertRaises(asyncio.CancelledError):
                await task
            return response

        return self.loop.run_until_complete(cancel()), left.wait(PATIENCE)
