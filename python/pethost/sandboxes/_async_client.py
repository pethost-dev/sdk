"""The asyncio client. Generated from v1/sandboxes.proto by the template that also writes
_client.py: do not edit."""

from __future__ import annotations

import asyncio
from collections.abc import AsyncGenerator, AsyncIterator, Awaitable, Callable, Iterator, Mapping, Sequence
from datetime import datetime
from typing import Protocol, TypeVar, overload

from connectrpc.code import Code as _Code
from connectrpc.errors import ConnectError as _ConnectError

import pethost._connections as _connections
import pethost._runtime as _rt
import pethost.sandboxes._convert as _convert
from pethost.sandboxes._types import (
    Agent,
    AgentEvent,
    AgentTurn,
    Command,
    CommandOutput,
    Connection,
    ControlDesktopResponse,
    DesktopAction,
    DesktopLink,
    File,
    FileChange,
    FileEvent,
    GetSandboxMetricsResponse,
    Label,
    Link,
    ListCommandsResponse,
    ListConversationsResponse,
    ListFilesResponse,
    ListSandboxEventsResponse,
    ListSandboxesResponse,
    ListTemplatesResponse,
    ListUsageResponse,
    Sandbox,
    SandboxEvent,
    SandboxEventKind,
    SandboxSettings,
    SandboxState,
    Secret,
    Template,
    TerminalLink,
    Workspace,
    WriteFilesResponse,
)
from pethost._wire.v1.sandboxes_connect import SandboxServiceClient as _Wire
from pethost._wire.v1.sandboxes_connect import SandboxRuntimeServiceClient as _Runtime

_Request = TypeVar("_Request")
_Response = TypeVar("_Response")
_Self = TypeVar("_Self", bound="AsyncSandboxes")
_RequestIn = TypeVar("_RequestIn", contravariant=True)
_ResponseOut = TypeVar("_ResponseOut", covariant=True)
_Answer = TypeVar("_Answer")

# The codes that answer a call that did nothing: a kept connection is then dropped, and the call
# made once more on a new one.
_RETRY = frozenset({_Code.UNAUTHENTICATED, _Code.PERMISSION_DENIED, _Code.NOT_FOUND})


class _Unary(Protocol[_RequestIn, _ResponseOut]):
    """A method of SandboxRuntimeService's wire client, called with the client of a server."""

    def __call__(
        self, wire: _Runtime, request: _RequestIn, /, *, headers: Mapping[str, str], timeout_ms: int | None
    ) -> Awaitable[_ResponseOut]: ...


class _Streamed(Protocol[_RequestIn, _ResponseOut]):
    """A stream of SandboxRuntimeService's wire client, called with the client of a server."""

    def __call__(self, wire: _Runtime, request: _RequestIn, /, *, headers: Mapping[str, str]) -> AsyncIterator[_ResponseOut]: ...


class AsyncSandboxes:
    """Pethost Agent Sandboxes' API for asyncio: `Sandboxes`'s methods, each awaited, and its streams, each read
    with `async for`.

        async with AsyncSandboxes() as sandboxes:
            print(await sandboxes.get_workspace())
    """

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = "https://console.pethost.dev",
        timeout: float | None = 60.0,
        workspace: str = "",
    ) -> None:
        """
        Args:
            token: The API token, "pth_...": a person makes one in the panel's Settings, under "API tokens". None = the environment's PETHOST_TOKEN.
            base_url: The API's address.
            timeout: Seconds one call may take, the API's own waiting included: a call that waits for an operation or runs a command can be told to take longer than this. None = no limit. A stream has no limit: it lasts as long as its loop.
            workspace: The workspace of every call whose request names none: its id or name. A request's own workspace goes before it, and a call that names a sandbox acts on the sandbox's. Empty = none: the API then takes the account's only workspace of this kind, and refuses a call with WorkspaceChoice when it has several.
        """
        caller = _rt.Caller(_rt.token_or_environment(token))
        self._workspace = workspace
        self._wire = _Wire(base_url, interceptors=[caller], timeout_ms=_rt.timeout_ms(timeout))
        # The servers' wire clients send the bearer each call names: never the API token.
        self._agent = _rt.Caller(None)
        self._timeout_ms = _rt.timeout_ms(timeout)
        self._kept = _connections.Connections(60)
        self._runtimes: dict[str, _Runtime] = {}
        # The wire layer's timeout is a call's whole time, and a call cannot lift its client's:
        # the streams have a client of their own, without one.
        self._streams = _Wire(base_url, interceptors=[caller])

    async def aclose(self) -> None:
        """Closes its connections; `async with` does it."""
        await self._wire.close()
        await self._streams.close()
        for wire in list(self._runtimes.values()):
            await wire.close()

    async def __aenter__(self: _Self) -> _Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def _call(self, method: Callable[[_Request], Awaitable[_Response]], request: _Request) -> _Response:
        try:
            return await method(request)
        except _ConnectError as error:
            raise _convert.error_from_wire(error) from None

    async def _stream(
        self,
        method: Callable[[_Request], AsyncIterator[_rt.Wire]],
        request: _Request,
        read: Callable[[_rt.Wire], _Response],
    ) -> AsyncGenerator[_Response, None]:
        """A stream's responses, each as the API sends it, without its pulses, and its failure
        as the package's error. However it is left, it closes the wire layer's stream, which
        ends the call."""
        wired = method(request)
        try:
            async for response in wired:
                if not _rt.is_pulse(response):
                    yield read(response)
        except _ConnectError as error:
            # The wire layer reports its task's cancelling as a failed call. To asyncio it is
            # none: the task ends cancelled, as with any other await.
            if isinstance(error.__cause__, asyncio.CancelledError):
                raise error.__cause__ from None
            raise _convert.error_from_wire(error) from None
        finally:
            if isinstance(wired, AsyncGenerator):  # It is one, though the wire layer types it an iterator.
                await wired.aclose()

    async def _run(self, sandbox_id: str, method: _Unary[_Request, _Response], request: _Request) -> _Response:
        """A call at the connection of its sandbox: the one kept for it, else a new one. Refused
        with a code of _RETRY on a kept one, it is made once more, the same request, on a new one."""
        connection, kept = await self._connection(sandbox_id)
        try:
            return await method(self._at(connection.url), request, headers=connection.headers, timeout_ms=self._timeout_ms)
        except _ConnectError as error:
            if not kept or error.code not in _RETRY:
                raise _convert.error_from_wire(error) from None
        connection = await self._reconnect(sandbox_id, connection)
        try:
            return await method(self._at(connection.url), request, headers=connection.headers, timeout_ms=self._timeout_ms)
        except _ConnectError as error:
            raise _convert.error_from_wire(error) from None

    async def _run_stream(
        self,
        sandbox_id: str,
        method: _Streamed[_Request, _rt.Wire],
        request: _Request,
        read: Callable[[_rt.Wire], _Response],
    ) -> AsyncGenerator[_Response, None]:
        """A stream at the connection of its sandbox, read as _stream reads one. Refused with a
        code of _RETRY on a kept connection before its first response, it is called once more on a
        new one; after a response, a failure is the stream's."""
        connection, kept = await self._connection(sandbox_id)
        while True:
            wired = method(self._at(connection.url), request, headers=connection.headers)
            started = False
            try:
                async for response in wired:
                    started = True
                    if not _rt.is_pulse(response):
                        yield read(response)
                return
            except _ConnectError as error:
                if isinstance(error.__cause__, asyncio.CancelledError):
                    raise error.__cause__ from None
                if started or not kept or error.code not in _RETRY:
                    raise _convert.error_from_wire(error) from None
            finally:
                if isinstance(wired, AsyncGenerator):  # It is one, though the wire layer types it an iterator.
                    await wired.aclose()
            connection, kept = await self._reconnect(sandbox_id, connection), False

    async def _connection(self, sandbox_id: str) -> tuple[_connections.Kept, bool]:
        """The connection kept for a sandbox, and True; else a new one, and False."""
        kept = self._kept.get(sandbox_id)
        if kept is not None:
            return kept, True
        return await self._connect(sandbox_id), False

    async def _connect(self, sandbox_id: str) -> _connections.Kept:
        """A new connection for a sandbox, which the client keeps: connect_sandbox's answer."""
        request = _convert.connect_request(sandbox_id)
        connection = _convert.kept(await self._call(self._wire.connect_sandbox, request))
        self._kept.keep(sandbox_id, connection)
        return connection

    async def _reconnect(self, sandbox_id: str, refused: _connections.Kept) -> _connections.Kept:
        """A new connection in place of one a server refused."""
        self._kept.drop(sandbox_id, refused)
        return await self._connect(sandbox_id)

    def _keep(self, seeds: Callable[[_Answer], Iterator[tuple[str, _connections.Kept]]], answer: _Answer) -> _Answer:
        """An answer, whose connections the client keeps: one is good for the calls that follow."""
        for sandbox_id, connection in seeds(answer):
            self._kept.keep(sandbox_id, connection)
        return answer

    def _at(self, url: str) -> _Runtime:
        """The wire client of the server at a URL: one for each, shared by everything there."""
        wire = self._runtimes.get(url)
        if wire is None:
            wire = self._runtimes.setdefault(url, _Runtime(url, interceptors=[self._agent]))
        return wire

    async def get_workspace(
        self,
        *,
        workspace: str = "",
    ) -> Workspace:
        """Read the workspace.

        Its limits, sizes and their prices, secrets (never their values) and SSH keys.

        Read-only.

        Args:
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.workspace_from_wire(await self._call(self._wire.get_workspace, _convert.get_workspace_request(workspace=workspace or self._workspace)))

    async def set_ssh_keys(
        self,
        *,
        ssh_keys: Sequence[str] = (),
        workspace: str = "",
    ) -> Workspace:
        """Set the SSH keys.

        Replaces the workspace's SSH keys. A removed key's sessions end.

        Args:
            ssh_keys: OpenSSH public keys: "ssh-ed25519 AAAA… laptop".
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.workspace_from_wire(await self._call(self._wire.set_ssh_keys, _convert.set_ssh_keys_request(ssh_keys=ssh_keys, workspace=workspace or self._workspace)))

    async def set_secret(
        self,
        name: str = "",
        *,
        value: str = "",
        hosts: Sequence[str] = (),
        workspace: str = "",
    ) -> Secret:
        """Set a secret.

        Creates or replaces a workspace secret, its value and its hosts together, so its hosts change
        only with its value. Sandboxes that bind it use the new value at once.

        Args:
            value: Never enters a sandbox; never returned.
            hosts: Domains, written as Egress.allow writes them.
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.secret_from_wire(await self._call(self._wire.set_secret, _convert.set_secret_request(name=name, value=value, hosts=hosts, workspace=workspace or self._workspace)))

    async def delete_secret(
        self,
        name: str = "",
        *,
        workspace: str = "",
    ) -> Secret:
        """Delete a secret.

        Refused while a sandbox that is not DELETED binds it.

        Args:
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.secret_from_wire(await self._call(self._wire.delete_secret, _convert.delete_secret_request(name=name, workspace=workspace or self._workspace)))

    async def create_sandbox(
        self,
        template: str = "",
        *,
        settings: SandboxSettings | None = None,
        labels: Sequence[Label] = (),
        name: str = "",
        request_id: str = "",
        workspace: str = "",
    ) -> Sandbox:
        """Create a sandbox.

        Starts a sandbox from a template and answers once it runs, with a Connection to it. It is
        asked of each server with room for it in turn, those that hold its template first, until
        one takes it: when none does, UnavailableError + NoCapacity at once, naming what the last one
        lacked. The first sandbox of a workspace's template version on a server fetches the version,
        about 10 s a GiB of what it holds. A size below the version's min_size is InvalidArgumentError,
        naming it.

        Args:
            template: "name" (its newest READY version) or "name@version". Absent = "base".
            settings: To add to the template's variables, send them too (list_templates: Template.settings).
            labels: For list_sandboxes' filter. At most 32.
            name: Unique in the workspace (AlreadyExistsError + NameTaken names the sandbox that has it): a-z, 0-9 and "-", at most 63, not 16 of a-z and 0-9 alone, a sandbox_id's shape. Absent = none.
            request_id: Any new string; send it again on a retry after a timeout or a lost answer: the retry does nothing again and answers what the first call did (24 h).
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.create_sandbox, _convert.create_sandbox_request(template=template, settings=settings, labels=labels, name=name, request_id=request_id or _rt.request_id(16), workspace=workspace or self._workspace))))

    async def get_sandbox(
        self,
        sandbox_id: str,
    ) -> Sandbox:
        """Read a sandbox.

        One sandbox as it is now: its state and why, its settings in force, how to reach it and its
        usage.

        Read-only.
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.get_sandbox, _convert.get_sandbox_request(sandbox_id=sandbox_id))))

    async def list_sandboxes(
        self,
        *,
        states: Sequence[SandboxState] = (),
        labels: Sequence[Label] = (),
        page_size: int = 0,
        page_token: str = "",
        name: str = "",
        workspace: str = "",
    ) -> ListSandboxesResponse:
        """List sandboxes.

        The workspace's sandboxes, newest first.

        Read-only.

        Args:
            states: Absent = all but DELETED.
            labels: Only sandboxes with all these labels.
            page_size: Absent = 50; at most 500.
            name: Only the sandbox of this name (and DELETED ones, if states has DELETED).
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.list_sandboxes_response_from_wire(self._keep(_convert.list_sandboxes_response_seeds, await self._call(self._wire.list_sandboxes, _convert.list_sandboxes_request(states=states, labels=labels, page_size=page_size, page_token=page_token, name=name, workspace=workspace or self._workspace))))

    async def update_sandbox(
        self,
        sandbox_id: str,
        *,
        settings: SandboxSettings | None = None,
        if_revision: int = 0,
        revoke_tokens: bool = False,
        grow_disk: bool = False,
        name: str | None = None,
    ) -> Sandbox:
        """Change a sandbox's settings.

        Read the sandbox first, and send each group you change whole, as you read it: a group sent
        replaces the sandbox's whole group, and groups left out stay.

        Changes its settings: egress at once, the environment for processes started after, and a
        new size (Size): a RUNNING sandbox restarts at it, a STOPPED one takes it at its next start,
        and a PAUSED one is refused (FailedPreconditionError: resume or stop it first). Answers with the
        sandbox.

        Answers carry every group (SandboxSettings) with its defaults filled in: what you read is
        what you send back. A field a group gains in a later version is a message or a scalar
        with presence, and a request that leaves it out keeps its value: an older client never clears
        it. The settings with the sandbox's labels are at most 48 KiB serialized: the record that
        carries both fits a response.

        How egress judges a connection: an entry is kept with the spaces around it trimmed. Only TCP
        and DNS leave a sandbox, no UDP and no ping, whatever Egress says, and DNS only through the
        sandbox's own resolver, which answers REFUSED for a name no entry allows without asking
        further; an IP or a CIDR opens those addresses, dialed by address, not the names that resolve
        to them. Always refused: private and link-local addresses, port 25, and HTTP/2 without TLS
        (h2c), whose requests name their hosts only after the connection is open. Plain HTTP is read
        request by request: a request for another host than the one its connection was judged on never
        leaves, and is answered 421, Misdirected Request, whatever the list says of that host: the
        client opens a new connection for it, which is judged by it and answered 403 if the list does
        not allow it. TLS is judged on the name the client sends and then passes unread, so a domain
        trusts whatever is served behind that name's addresses (a CDN's other sites, a client that
        hides its name with ECH): a fence that must hold there names IPs, or binds a secret to the
        host, whose TLS the server then terminates, judging each request. A connection that is neither
        TLS nor HTTP (SSH) names no host, and passes to a domain's addresses, as the sandbox's DNS
        returned them, only on a port the entry names ("github.com:22"): a domain without one opens the
        web alone.

        Destructive: it may delete or overwrite something.

        Args:
            settings: Groups sent replace the sandbox's; the rest stay.
            if_revision: Refused with AbortedError unless Sandbox.revision is this. Absent: no check.
            revoke_tokens: True = every connect_sandbox token and link made for it so far stops working.
            grow_disk: True = its disk grows to its size's (the new one's, with settings.size), as a new size does: a RUNNING sandbox restarts, a STOPPED one grows at its next start, a PAUSED one is refused. A disk never shrinks: smaller sizes are refused from then on (SIZES).
            name: Its new name, as create_sandbox takes one; "" = none. Absent: kept. A rename is a call of its own, with nothing but sandbox_id and if_revision (else InvalidArgumentError), and changes no revision.
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.update_sandbox, _convert.update_sandbox_request(sandbox_id=sandbox_id, settings=settings, if_revision=if_revision, revoke_tokens=revoke_tokens, grow_disk=grow_disk, name=name))))

    async def pause_sandbox(
        self,
        sandbox_id: str,
    ) -> Sandbox:
        """Pause a sandbox.

        Saves memory, processes and disk on its server, which keeps its place for it, so that its
        resume is never refused for room (USAGE prices that). A PAUSED or STOPPED sandbox is answered
        as it is.
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.pause_sandbox, _convert.pause_sandbox_request(sandbox_id=sandbox_id))))

    async def stop_sandbox(
        self,
        sandbox_id: str,
    ) -> Sandbox:
        """Stop a sandbox.

        Shuts it down: its processes are asked to end (SIGTERM) and killed after 5 s, its disk is
        written out and kept, and its vCPUs and memory are freed. A PAUSED sandbox drops the memory
        it saved. A STOPPED one is answered as it is.

        Destructive: it may delete or overwrite something.
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.stop_sandbox, _convert.stop_sandbox_request(sandbox_id=sandbox_id))))

    async def resume_sandbox(
        self,
        sandbox_id: str,
    ) -> Sandbox:
        """Resume a sandbox.

        Resumes a PAUSED or STOPPED sandbox without doing anything in it; any call into a PAUSED one,
        or a STOPPED one whose lifecycle says wake_when_stopped, does as much. A RUNNING one is
        answered as it is. A PAUSED one counts against Limits.vcpus already, and is refused
        (ResourceExhaustedError + LimitReached) only where the workspace counts more than its plan allows
        now; it resumes on its server, which kept its place, never refused for room. A STOPPED one
        counts against Limits.vcpus and
        largest_size from here on (ResourceExhaustedError + LimitReached past them), and starts on its
        own server when that server has room for it, else
        on another with room, when its copy is current: its server lets it go
        first, and one its server cannot be reached for is UnavailableError, saying so. Its disk, when it is
        in object storage alone, is fetched first: waited for up to 45 s, after which it is answered
        STOPPED with how far that is (Sandbox.restore), and starts once whole; call again to wait on.
        A STOPPED one whose server is gone (state_message says so) starts on a server from its last
        copy in object storage. A sandbox that starts on another server changes its addresses with it
        (connection.url, its ports' URLs, ssh_command), and its events and metrics begin again there.
        While it moves, resume_sandbox waits for the move within its 45 s, and the calls that change it
        are UnavailableError ("moving"): try again in a moment. UnavailableError without NoCapacity: no server
        answers now; try again.
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.resume_sandbox, _convert.resume_sandbox_request(sandbox_id=sandbox_id))))

    async def delete_sandbox(
        self,
        sandbox_id: str,
    ) -> Sandbox:
        """Delete a sandbox.

        Drops its memory and disk for good. Answers its final record, usage included. A DELETED sandbox is answered with that record.

        Destructive: it may delete or overwrite something.
        """
        return _convert.sandbox_from_wire(self._keep(_convert.sandbox_seeds, await self._call(self._wire.delete_sandbox, _convert.delete_sandbox_request(sandbox_id=sandbox_id))))

    async def connect_sandbox(
        self,
        sandbox_id: str,
        *,
        ttl_seconds: int = 0,
    ) -> Connection:
        """Get a sandbox's address and root token.

        Where SandboxRuntimeService answers for this one sandbox (url), a token for it, which expires,
        and the SSH command the token is the password of: the header says how to call it. The token
        is root in the sandbox: give it to a program, never to a page or a message. create_sandbox answers
        with one already.

        Args:
            ttl_seconds: Absent = 3600; at most 86400.
        """
        return _convert.connection_from_wire(await self._call(self._wire.connect_sandbox, _convert.connect_sandbox_request(sandbox_id=sandbox_id, ttl_seconds=ttl_seconds)))

    async def get_sandbox_metrics(
        self,
        sandbox_id: str,
        *,
        since: datetime | None = None,
        until: datetime | None = None,
        step_seconds: int = 0,
    ) -> GetSandboxMetricsResponse:
        """Read a sandbox's metrics.

        CPU, memory, disk and network over time.

        Read-only.

        Args:
            since: Absent = an hour ago.
            until: Absent = now.
            step_seconds: One point per step, averaged. Absent = the range ÷ 100; at least 5, and raised so that there are at most 1000 points.
        """
        return _convert.get_sandbox_metrics_response_from_wire(await self._call(self._wire.get_sandbox_metrics, _convert.get_sandbox_metrics_request(sandbox_id=sandbox_id, since=since, until=until, step_seconds=step_seconds)))

    async def list_sandbox_events(
        self,
        sandbox_id: str,
        *,
        kinds: Sequence[SandboxEventKind] = (),
        after: str = "",
        newest_first: bool = False,
        limit: int = 0,
    ) -> ListSandboxEventsResponse:
        """List a sandbox's events.

        What happened in a sandbox, oldest first: its lifecycle, the commands that ended, its
        connections out and the requests to its ports a minute at a time, its agents' turns. A
        sandbox keeps the newest 10,000 of each kind, and records 600 commands and agent turns a
        minute at most: those past that are recorded in the minutes after.

        Read-only.

        Args:
            kinds: Absent = all.
            after: An event's id: only later ones, oldest first from it.
            newest_first: True = the latest events, newest first: what just happened. With `after`: the latest of those after it.
            limit: Absent = 100; at most 1000.
        """
        return _convert.list_sandbox_events_response_from_wire(await self._call(self._wire.list_sandbox_events, _convert.list_sandbox_events_request(sandbox_id=sandbox_id, kinds=kinds, after=after, newest_first=newest_first, limit=limit)))

    def watch_sandbox_events(
        self,
        sandbox_id: str,
        *,
        kinds: Sequence[SandboxEventKind] = (),
        after: str = "",
    ) -> AsyncGenerator[SandboxEvent, None]:
        """Follow a sandbox's events, as a stream.

        list_sandbox_events, then the new events live.

        Read it with `async for`: the call is made when the loop starts, and each response comes as the
        API sends it. A stream that fails raises its SandboxesError from the loop, once; one that ends
        by itself just ends the loop. Leaving the loop ends the call, as asyncio then closes the
        generator, and so does cancelling its task; where a variable holds the generator, awaiting its
        `aclose()` ends the call.

            async for response in sandboxes.watch_sandbox_events("..."):
                ...

        Args:
            kinds: Absent = all.
            after: An event's id: only later ones. Absent = from the first.
        """
        return self._stream(self._streams.watch_sandbox_events, _convert.watch_sandbox_events_request(sandbox_id=sandbox_id, kinds=kinds, after=after), _convert.sandbox_event_from_wire)

    async def create_template(
        self,
        name: str = "",
        *,
        sandbox_id: str = "",
        description: str = "",
        request_id: str = "",
    ) -> Template:
        """Save a template.

        Saves a sandbox's disk as a new version of a template: its files, no memory and no process.
        It answers the version SAVING once it holds the disk as it is now: a RUNNING sandbox goes on
        running, halted for some milliseconds. Its server then shrinks the version's filesystem to
        what it holds and uploads it to object storage, about 5 s and 10 s a GiB of what it holds of
        its own, after which it is READY, with its min_size, or FAILED, saying why: list_templates
        with `name` says which. Start its sandboxes from the "name@version" it answers: "name" alone
        is the newest READY version, the one before while this one saves.
        Refused (LimitReached, template_gib) while the workspace's templates take its template_gib,
        or while another of its versions is SAVING; one whose own bytes would pass what is left is
        FAILED before its upload. Refused while nothing pays for the workspace (UsageUnpaid).
        Sandboxes keep the version they started from.

        Args:
            name: A name the workspace has gets its next version.
            sandbox_id: The sandbox whose disk the version holds, as it is now: its files, never its memory or its processes, and nothing of its guest daemon's commands or conversations, which its sandboxes start without; and its settings as they are now, which its sandboxes start with unless a create says otherwise (update_sandbox first, to save others). Required.
            description: At most 1 KiB.
            request_id: Any new string; send it again on a retry after a timeout or a lost answer: the retry does nothing again and answers what the first call did (24 h).
        """
        return _convert.template_from_wire(await self._call(self._wire.create_template, _convert.create_template_request(name=name, sandbox_id=sandbox_id, description=description, request_id=request_id or _rt.request_id(16))))

    async def get_template(
        self,
        template: str = "",
        *,
        workspace: str = "",
    ) -> Template:
        """Read a template version.

        One version.

        Read-only.

        Args:
            template: "name@version", or "name" for its newest version in any state (create_sandbox starts from the newest READY).
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.template_from_wire(await self._call(self._wire.get_template, _convert.get_template_request(template=template, workspace=workspace or self._workspace)))

    async def list_templates(
        self,
        name: str = "",
        *,
        page_size: int = 0,
        page_token: str = "",
        workspace: str = "",
    ) -> ListTemplatesResponse:
        """List templates.

        Ours and the workspace's: each one's newest version; with `name`, its versions, newest
        first.

        Read-only.

        Args:
            name: Its versions, newest first. Absent = each template's newest version.
            page_size: Absent = 50; at most 500.
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.list_templates_response_from_wire(await self._call(self._wire.list_templates, _convert.list_templates_request(name=name, page_size=page_size, page_token=page_token, workspace=workspace or self._workspace)))

    async def delete_template(
        self,
        name: str = "",
        *,
        workspace: str = "",
    ) -> Template:
        """Delete a template.

        Deletes every version: no sandbox starts from them from then on, and what they take stops
        counting in template_gib at once. Sandboxes made from them go on running, pausing, stopping
        and resuming: object storage keeps a version until the last of them is deleted.
        FailedPreconditionError while a version of it is SAVING.

        Args:
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.template_from_wire(await self._call(self._wire.delete_template, _convert.delete_template_request(name=name, workspace=workspace or self._workspace)))

    async def list_usage(
        self,
        *,
        since: datetime | None = None,
        until: datetime | None = None,
        page_size: int = 0,
        page_token: str = "",
        workspace: str = "",
    ) -> ListUsageResponse:
        """List usage.

        What the workspace used: a row per day, meter and size, as it was charged.

        Read-only.

        Args:
            since: Absent = 30 days ago.
            until: Absent = now.
            page_size: Absent = 100; at most 1000.
            workspace: The workspace: its id or name. Omit when the account has one (WorkspaceChoice lists them).
        """
        return _convert.list_usage_response_from_wire(await self._call(self._wire.list_usage, _convert.list_usage_request(since=since, until=until, page_size=page_size, page_token=page_token, workspace=workspace or self._workspace)))

    async def run_command(
        self,
        sandbox_id: str,
        *,
        command: str = "",
        cwd: str = "",
        user: str = "",
        stdin: str = "",
        wait_seconds: int | None = None,
        wait_for_port: int = 0,
        timeout_seconds: int = 0,
        keep_awake: bool = False,
        request_id: str = "",
    ) -> Command:
        """Run a command.

        Runs a shell command and waits for it (wait_seconds): its exit and output, or RUNNING with
        its output so far while it runs on. Only timeout_seconds or stop_command ends it early.

        Destructive: it may delete or overwrite something.

        Args:
            command: Run by `bash -lc`: "npm ci && npm test", "PORT=3000 npm run dev".
            cwd: Absent = /home/user.
            user: Absent = "user"; "root".
            stdin: Written to its stdin, which then closes.
            wait_seconds: How long this call waits for it to end: absent or more than 45 = 45; 0 = answer once it started. It runs on after.
            wait_for_port: Answers as soon as something listens on this port (within wait_seconds), while the command runs on: "npm run dev" and 5173.
            timeout_seconds: Kills it after this long. Absent = never.
            keep_awake: True = the sandbox does not pause for idleness while it runs: a build, or a job nobody waits on. A server needs none: a request to its port wakes the sandbox.
            request_id: Any new string; send it again on a retry after a timeout or a lost answer: the retry does nothing again and answers what the first call did (24 h).
        """
        return _convert.command_from_wire(await self._run(sandbox_id, _Runtime.run_command, _convert.run_command_request(sandbox_id=sandbox_id, command=command, cwd=cwd, user=user, stdin=stdin, wait_seconds=wait_seconds, wait_for_port=wait_for_port, timeout_seconds=timeout_seconds, keep_awake=keep_awake, request_id=request_id or _rt.request_id(16))))

    async def get_command(
        self,
        sandbox_id: str,
        *,
        command_id: str = "",
        wait_seconds: int | None = None,
        stdout_after_bytes: int = 0,
        stderr_after_bytes: int = 0,
    ) -> Command:
        """Wait for a command.

        A command, after waiting for it to end (wait_seconds). The last 100 that ended are kept.

        Read-only.

        Args:
            wait_seconds: How long this call waits for it to end: absent or more than 45 = 45; 0 = answer at once.
            stdout_after_bytes: The stdout_bytes of the answer you last read: only what came after it.
            stderr_after_bytes: Likewise, stderr_bytes.
        """
        return _convert.command_from_wire(await self._run(sandbox_id, _Runtime.get_command, _convert.get_command_request(sandbox_id=sandbox_id, command_id=command_id, wait_seconds=wait_seconds, stdout_after_bytes=stdout_after_bytes, stderr_after_bytes=stderr_after_bytes)))

    async def stop_command(
        self,
        sandbox_id: str,
        *,
        command_id: str = "",
    ) -> Command:
        """Stop a command.

        SIGTERM, then SIGKILL 10 s later if it still runs. Answers once it has ended. A command that
        has ended has what it left running killed at once: its background jobs, or a fork bomb.

        Destructive: it may delete or overwrite something.
        """
        return _convert.command_from_wire(await self._run(sandbox_id, _Runtime.stop_command, _convert.stop_command_request(sandbox_id=sandbox_id, command_id=command_id)))

    async def list_commands(
        self,
        sandbox_id: str,
    ) -> ListCommandsResponse:
        """List running commands.

        The commands running now, started by the API, SSH or a terminal, without their
        output.

        Read-only.
        """
        return _convert.list_commands_response_from_wire(await self._run(sandbox_id, _Runtime.list_commands, _convert.list_commands_request(sandbox_id=sandbox_id)))

    def watch_command(
        self,
        sandbox_id: str,
        *,
        command_id: str = "",
    ) -> AsyncGenerator[CommandOutput, None]:
        """Follow a command's output, as a stream.

        A command's output from the last 64 KiB, then live, until it ends.

        Read it with `async for`: the call is made when the loop starts, and each response comes as the
        API sends it. A stream that fails raises its SandboxesError from the loop, once; one that ends
        by itself just ends the loop. Leaving the loop ends the call, as asyncio then closes the
        generator, and so does cancelling its task; where a variable holds the generator, awaiting its
        `aclose()` ends the call.

            async for response in sandboxes.watch_command("..."):
                ...
        """
        return self._run_stream(sandbox_id, _Runtime.watch_command, _convert.watch_command_request(sandbox_id=sandbox_id, command_id=command_id), _convert.command_output_from_wire)

    async def read_file(
        self,
        sandbox_id: str,
        *,
        path: str = "",
        offset_bytes: int = 0,
        length_bytes: int = 0,
    ) -> File:
        """Read a file.

        A file's text (its bytes, if it is not UTF-8), from offset_bytes. A file that is not UTF-8 is
        answered to an MCP tool by its size alone: create_link download_path fetches it, run_command
        (`file`, `xxd`) looks inside.

        Read-only.

        Args:
            length_bytes: Absent = 64 KiB; at most 1 MiB. Larger: create_link's download_path.
        """
        return _convert.file_from_wire(await self._run(sandbox_id, _Runtime.read_file, _convert.read_file_request(sandbox_id=sandbox_id, path=path, offset_bytes=offset_bytes, length_bytes=length_bytes)))

    async def list_files(
        self,
        sandbox_id: str,
        *,
        path: str = "",
        depth: int = 0,
        page_token: str = "",
    ) -> ListFilesResponse:
        """List files.

        A directory's entries, `depth` levels deep, 1000 a page. A file's path lists that file alone.

        Read-only.

        Args:
            depth: Absent = 1.
        """
        return _convert.list_files_response_from_wire(await self._run(sandbox_id, _Runtime.list_files, _convert.list_files_request(sandbox_id=sandbox_id, path=path, depth=depth, page_token=page_token)))

    async def write_files(
        self,
        sandbox_id: str,
        *,
        changes: Sequence[FileChange] = (),
    ) -> WriteFilesResponse:
        """Write files.

        Changes files in order (writes, edits, moves, deletes, directories), and stops at the first
        that fails. A write replaces the file whole, keeping its owner and mode: a hard link to it
        keeps the old content; a symbolic link is written through to its target.

        Destructive: it may delete or overwrite something.

        Args:
            changes: Done in order.
        """
        return _convert.write_files_response_from_wire(await self._run(sandbox_id, _Runtime.write_files, _convert.write_files_request(sandbox_id=sandbox_id, changes=changes)))

    def watch_files(
        self,
        sandbox_id: str,
        *,
        path: str = "",
        recursive: bool = False,
    ) -> AsyncGenerator[FileEvent, None]:
        """Follow file changes, as a stream.

        Changes under a directory, live, until the stream is closed.

        Read it with `async for`: the call is made when the loop starts, and each response comes as the
        API sends it. A stream that fails raises its SandboxesError from the loop, once; one that ends
        by itself just ends the loop. Leaving the loop ends the call, as asyncio then closes the
        generator, and so does cancelling its task; where a variable holds the generator, awaiting its
        `aclose()` ends the call.

            async for response in sandboxes.watch_files("..."):
                ...

        Args:
            recursive: The directories under it too. One that appears is told with what it holds already, CREATED each, up to 1000; an entry made as its directory appears may be told twice.
        """
        return self._run_stream(sandbox_id, _Runtime.watch_files, _convert.watch_files_request(sandbox_id=sandbox_id, path=path, recursive=recursive), _convert.file_event_from_wire)

    async def control_desktop(
        self,
        sandbox_id: str,
        *,
        actions: Sequence[DesktopAction] = (),
    ) -> ControlDesktopResponse:
        """Use the desktop.

        Does the actions in order, then answers with a screenshot of the screen as they left it.
        Stops at the first that fails; with no actions, just the screenshot. The first starts the
        desktop, which takes some seconds. FailedPreconditionError = the desktop did not start (its
        words).

        Destructive: it may delete or overwrite something.
        """
        return _convert.control_desktop_response_from_wire(await self._run(sandbox_id, _Runtime.control_desktop, _convert.control_desktop_request(sandbox_id=sandbox_id, actions=actions)))

    @overload
    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: None = None,
        terminal: None = None,
        desktop: None = None,
        download_path: None = None,
        upload_path: None = None,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        ...

    @overload
    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: int,
        terminal: None = None,
        desktop: None = None,
        download_path: None = None,
        upload_path: None = None,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        ...

    @overload
    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: None = None,
        terminal: TerminalLink,
        desktop: None = None,
        download_path: None = None,
        upload_path: None = None,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        ...

    @overload
    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: None = None,
        terminal: None = None,
        desktop: DesktopLink,
        download_path: None = None,
        upload_path: None = None,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        ...

    @overload
    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: None = None,
        terminal: None = None,
        desktop: None = None,
        download_path: str,
        upload_path: None = None,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        ...

    @overload
    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: None = None,
        terminal: None = None,
        desktop: None = None,
        download_path: None = None,
        upload_path: str,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        ...

    async def create_link(
        self,
        sandbox_id: str,
        *,
        port: int | None = None,
        terminal: TerminalLink | None = None,
        desktop: DesktopLink | None = None,
        download_path: str | None = None,
        upload_path: str | None = None,
        ttl_seconds: int = 0,
    ) -> Link:
        """Make a link.

        A URL, for a browser or curl, into one thing of the sandbox: a terminal, the screen, a file
        to download or upload; or a private port's address and a token for it. It expires. A
        download or upload link works once. Making one wakes nothing.

        A private port answers only a request that sends its token as the header `Pethost-Token:
        <token>`: a program's, curl's, a page's fetch. The server checks it before anything wakes and
        takes the header off; the rest reaches the program as it was sent, Authorization and Cookie
        included. A preflight that names the header is answered 204 by the server itself, and the
        answer to a request whose token it took carries Access-Control-Allow-Origin with the request's
        origin, without credentials, so that a page of any origin may call the port with a token it
        holds. A browser's tab, a WebSocket or an image sends no such header: what a browser opens is a
        public port (Ingress), or a port forwarded by `ssh -L`. Every sandbox's address is under one
        domain: the server takes the Domain off a cookie an answer sets, and an app keeps the cookies
        its pages set to its own address with the `__Host-` prefix.

        At most one of `port`, `terminal`, `desktop`, `download_path`, `upload_path`.

        Args:
            port: A private port, for a program or curl, not a browser tab: a person's browser opens a public port (update_sandbox settings.ingress.public_ports, whose url the answer holds). Link.url is its address and Link.token a token for it alone, which each request sends as `Pethost-Token: <token>`: one without it, or with another token, is answered 401.
            download_path: GET the URL: the file, or a directory as a .tar.
            upload_path: PUT the file's bytes to the URL; missing directories are made.
            ttl_seconds: Absent = 3600; at most 86400.
        """
        return _convert.link_from_wire(await self._run(sandbox_id, _Runtime.create_link, _convert.create_link_request(sandbox_id=sandbox_id, port=port, terminal=terminal, desktop=desktop, download_path=download_path, upload_path=upload_path, ttl_seconds=ttl_seconds)))

    async def prompt_agent(
        self,
        sandbox_id: str,
        *,
        prompt: str = "",
        agent: Agent = Agent.UNSPECIFIED,
        conversation_id: str = "",
        model: str = "",
        cwd: str = "",
        wait_seconds: int | None = None,
        request_id: str = "",
    ) -> AgentTurn:
        """Prompt a coding agent.

        Gives a coding agent a prompt, in a new conversation or conversation_id's, and waits for its
        turn (wait_seconds). A conversation runs one turn at a time: a prompt to a busy one is
        QUEUED. When a turn ends, the agent and its helpers end with it; what its commands left
        running in the background (a dev server, say) runs on unless the agent ends it itself.
        FailedPreconditionError + AgentSignIn = the agent cannot reach its model.

        Destructive: it may delete or overwrite something.

        Args:
            agent: Absent = the conversation's; for a new one, CLAUDE_CODE.
            conversation_id: Absent = a new conversation.
            model: Absent = the agent's default. As the agent names models: "claude-opus-5-5" (Claude Code), "gpt-6.1" (Codex), "anthropic/claude-opus-5-5" (OpenCode: provider/model). Given for an existing conversation: its model from this turn on.
            cwd: A new conversation's working directory. Absent = /home/user. For an existing one: absent or its own, else InvalidArgumentError.
            wait_seconds: How long this call waits for it to end: absent or more than 45 = 45; 0 = answer once it started. It runs on after.
            request_id: Any new string; send it again on a retry after a timeout or a lost answer: the retry does nothing again and answers what the first call did (24 h).
        """
        return _convert.agent_turn_from_wire(await self._run(sandbox_id, _Runtime.prompt_agent, _convert.prompt_agent_request(sandbox_id=sandbox_id, prompt=prompt, agent=agent, conversation_id=conversation_id, model=model, cwd=cwd, wait_seconds=wait_seconds, request_id=request_id or _rt.request_id(16))))

    async def get_agent_turn(
        self,
        sandbox_id: str,
        *,
        turn_id: str = "",
        wait_seconds: int | None = None,
    ) -> AgentTurn:
        """Wait for an agent's turn.

        A turn, after waiting for it to end (wait_seconds).

        Read-only.

        Args:
            wait_seconds: How long this call waits for it to end: absent or more than 45 = 45; 0 = answer at once.
        """
        return _convert.agent_turn_from_wire(await self._run(sandbox_id, _Runtime.get_agent_turn, _convert.get_agent_turn_request(sandbox_id=sandbox_id, turn_id=turn_id, wait_seconds=wait_seconds)))

    async def stop_agent_turn(
        self,
        sandbox_id: str,
        *,
        turn_id: str = "",
    ) -> AgentTurn:
        """Stop an agent's turn.

        Ends a turn now, or takes a QUEUED one off the queue. What it changed stays changed.
        """
        return _convert.agent_turn_from_wire(await self._run(sandbox_id, _Runtime.stop_agent_turn, _convert.stop_agent_turn_request(sandbox_id=sandbox_id, turn_id=turn_id)))

    async def list_conversations(
        self,
        sandbox_id: str,
        *,
        page_size: int = 0,
        page_token: str = "",
    ) -> ListConversationsResponse:
        """List agent conversations.

        The sandbox's conversations, newest first, 50 a page.

        Read-only.

        Args:
            page_size: Absent = 50; at most 500.
        """
        return _convert.list_conversations_response_from_wire(await self._run(sandbox_id, _Runtime.list_conversations, _convert.list_conversations_request(sandbox_id=sandbox_id, page_size=page_size, page_token=page_token)))

    def watch_conversation(
        self,
        sandbox_id: str,
        *,
        conversation_id: str = "",
        after_seq: int = 0,
    ) -> AsyncGenerator[AgentEvent, None]:
        """Follow an agent conversation, as a stream.

        A conversation's events after after_seq, then live: prompts, messages, tool calls with their
        input and output, and the end of each turn.

        Read it with `async for`: the call is made when the loop starts, and each response comes as the
        API sends it. A stream that fails raises its SandboxesError from the loop, once; one that ends
        by itself just ends the loop. Leaving the loop ends the call, as asyncio then closes the
        generator, and so does cancelling its task; where a variable holds the generator, awaiting its
        `aclose()` ends the call.

            async for response in sandboxes.watch_conversation("..."):
                ...

        Args:
            after_seq: Only later events. Absent = from the first.
        """
        return self._run_stream(sandbox_id, _Runtime.watch_conversation, _convert.watch_conversation_request(sandbox_id=sandbox_id, conversation_id=conversation_id, after_seq=after_seq), _convert.agent_event_from_wire)
