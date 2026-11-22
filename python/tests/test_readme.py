"""The README's program of a module whose methods are called at a Connection, run as it is
written against the fakes: the API's fake answers each call with a sample of its response, and
the connections the answers hold send the rest to the server's fake."""

from __future__ import annotations

import contextlib
import io
import os
import pathlib
import re
import unittest.mock
from typing import Any

from .facts import Runtime
from .harness import TOKEN, Case, by_surface, connection
from .samples import Plan, pair
from .test_connections import seeded

README = pathlib.Path(__file__).resolve().parent.parent / "README.md"


class Readme(Case):
    def program(self) -> str:
        """The README's program that imports the surface's package."""
        found = re.findall(r"^```python\n(.*?)^```$", README.read_text(), re.MULTILINE | re.DOTALL)
        imports = f"from {self.surface.facts.public.__name__} import "
        (program,) = [text for text in found if imports in text]
        return str(program)

    def runtime(self) -> Runtime:
        runtime = self.surface.runtime
        assert runtime is not None
        return runtime

    def answer_every_call(self) -> None:
        """Each RPC's path answers a sample of its response; one whose answer holds connections,
        with a connection to the server's fake for its sample's key."""
        runtime = self.runtime()
        seeds = {seed.method: seed for seed in runtime.seeds}
        for method in self.surface.facts.methods:
            if method == runtime.connect:
                continue
            desc = self.surface.responses[method]
            sample, _ = pair(desc, Plan())
            if method in seeds:
                sample = seeded(desc, runtime, seeds[method], runtime.key, connection(runtime, self.server, token="sbc.held"))
            fake = self.fake_of(method)
            fake.route(self.surface.path(method), sample.to_binary())
            self.addCleanup(fake.routes.pop, self.surface.path(method))

    def test_the_program_runs(self) -> None:
        """The program runs to its end as written, with PETHOST_TOKEN and the client's own
        defaults but its address; its calls at the sandbox carry the connection its first answer
        held, and none asked for another."""
        self.answer_every_call()
        # The client's own default address, set to the fake's for the run: the program names none.
        defaults: dict[str, Any] = vars(self.surface.client())["__init__"].__kwdefaults__
        printed = io.StringIO()
        with (
            unittest.mock.patch.dict(os.environ, {"PETHOST_TOKEN": TOKEN}),
            unittest.mock.patch.dict(defaults, {"base_url": self.fake.url}),
            contextlib.redirect_stdout(printed),
        ):
            exec(compile(self.program(), str(README), "exec"), {"__name__": "__readme__"})

        self.assertTrue(printed.getvalue())
        self.assertTrue(self.server.calls)
        self.assertNotIn(self.surface.path(self.runtime().connect), [call.path for call in self.fake.calls])
        self.assertEqual({call.headers["authorization"] for call in self.server.calls}, {"Bearer sbc.held"})


load_tests = by_surface(Readme, connected=True)
