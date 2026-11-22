"""What tests/api.py, generated, says of each proto file the package is made of, as the checks
read it. Each surface is a package of its own (pethost, pethost.sandboxes), and the checks run on
every one."""

from __future__ import annotations

from dataclasses import dataclass
from types import ModuleType


@dataclass(frozen=True)
class Seed:
    """A method whose answer holds connections the client keeps: the fields from its response
    down to the message that holds one (a repeated field is each of its elements)."""

    method: str
    path: tuple[str, ...]


@dataclass(frozen=True)
class Runtime:
    """A service answered at a Connection: what a client connects by and how."""

    service: str  # Its full name, the path of its calls.
    connect: str  # The method that answers a Connection.
    key: str  # Its request's field 1, and every request's of the service: what a call is at.
    url: str  # The Connection's fields: where the service answers, the bearer, until when.
    token: str
    expire: str
    margin_seconds: int  # A connection is used until its expiry less this.
    request_id_bytes: int
    retry: tuple[str, ...]  # The codes a call is made again after, as the protocol's JSON writes them.
    seeds: tuple[Seed, ...]


@dataclass(frozen=True)
class Facts:
    """One proto file as the package has it."""

    name: str  # "" for the root, pethost; a module's name, its package's last word.
    public: ModuleType  # The package a user imports.
    wire: ModuleType  # Its messages in the wire layer.
    client: str  # Its client's class: Async<client> is the asyncio one, <client>Error its error.
    methods: dict[str, str]  # Each method's RPC.
    optional: frozenset[str]  # "Message.field" of every field marked (optional).
    details: tuple[str, ...]  # The messages an error carries.
    workspace: str  # What a request names its workspace by, and a client its own.
    workspaced: frozenset[str]  # The methods whose request's workspace a client made with one fills.
    request_ids: dict[str, str]  # The methods whose request's field the client fills with a new request_id.
    runtime: Runtime | None  # None = every method is called at the base URL.
