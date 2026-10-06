"""The asyncio client. Generated from v1/panel.proto by the template that also writes
_client.py: do not edit."""

from __future__ import annotations

from collections.abc import Awaitable, Callable, Sequence
from datetime import datetime
from typing import TypeVar, overload

from connectrpc.errors import ConnectError as _ConnectError

import pethost._convert as _convert
import pethost._runtime as _rt
from pethost._types import (
    ArchiveUpload,
    BackUpAction,
    CancelOperationAction,
    ContainerLogFilter,
    CreateProjectResponse,
    CreateTransferResponse,
    DeleteProjectAction,
    DeployProjectResponse,
    FileChange,
    FileUpload,
    GetMachineResponse,
    GetOperationResponse,
    GetProjectResponse,
    HttpTrafficFilter,
    ListCommitsResponse,
    MountVolume,
    PathDownload,
    ProjectExtension,
    ProjectSource,
    QueryContainerLogsResponse,
    QueryHttpTrafficResponse,
    ReadPathResponse,
    RecreateServiceAction,
    RestartMachineAction,
    RestoreSnapshotAction,
    RunMachineActionResponse,
    RunProjectActionResponse,
    RunServiceCommandResponse,
    ServicesAction,
    SshKey,
)
from pethost._wire.v1.panel_connect import PanelServiceClient as _Wire

_Request = TypeVar("_Request")
_Response = TypeVar("_Response")
_Self = TypeVar("_Self", bound="AsyncPethost")


class AsyncPethost:
    """Pethost's API for asyncio: `Pethost`'s methods, each awaited.

        async with AsyncPethost() as pethost:
            print(await pethost.get_machine())
    """

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str = "https://console.pethost.dev",
        timeout: float | None = 60.0,
    ) -> None:
        """
        Args:
            token: The API token, "pth_...": a person makes one in the panel's Settings, under "API tokens". None = the environment's PETHOST_TOKEN.
            base_url: The API's address.
            timeout: Seconds one call may take, the API's own waiting included: a call that waits for an operation or runs a command can be told to take longer than this. None = no limit.
        """
        self._wire = _Wire(
            base_url,
            interceptors=[_rt.Caller(_rt.token_or_environment(token))],
            timeout_ms=_rt.timeout_ms(timeout),
        )

    async def aclose(self) -> None:
        """Closes its connections; `async with` does it."""
        await self._wire.close()

    async def __aenter__(self: _Self) -> _Self:
        return self

    async def __aexit__(self, *_: object) -> None:
        await self.aclose()

    async def _call(self, method: Callable[[_Request], Awaitable[_Response]], request: _Request) -> _Response:
        try:
            return await method(request)
        except _ConnectError as error:
            raise _convert.error_from_wire(error) from None

    async def get_machine(self) -> GetMachineResponse:
        """Get the machine.

        Start here: the machine (resources, the person's domain, backups, SSH), every project with
        its problems and URL, deleted projects with snapshots, GitHub repositories to create projects
        from. Figures are the latest sample; disk sizes and the day's traffic lag a few minutes.

        Read-only.
        """
        return _convert.get_machine_response_from_wire(await self._call(self._wire.get_machine, _convert.get_machine_request()))

    @overload
    async def run_machine_action(
        self,
        *,
        add_ssh_key: None = None,
        remove_ssh_key_fingerprint: None = None,
        restart_machine: None = None,
        cancel_restart: None = None,
        end_session_id: None = None,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        ...

    @overload
    async def run_machine_action(
        self,
        *,
        add_ssh_key: SshKey,
        remove_ssh_key_fingerprint: None = None,
        restart_machine: None = None,
        cancel_restart: None = None,
        end_session_id: None = None,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        ...

    @overload
    async def run_machine_action(
        self,
        *,
        add_ssh_key: None = None,
        remove_ssh_key_fingerprint: str,
        restart_machine: None = None,
        cancel_restart: None = None,
        end_session_id: None = None,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        ...

    @overload
    async def run_machine_action(
        self,
        *,
        add_ssh_key: None = None,
        remove_ssh_key_fingerprint: None = None,
        restart_machine: RestartMachineAction,
        cancel_restart: None = None,
        end_session_id: None = None,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        ...

    @overload
    async def run_machine_action(
        self,
        *,
        add_ssh_key: None = None,
        remove_ssh_key_fingerprint: None = None,
        restart_machine: None = None,
        cancel_restart: bool,
        end_session_id: None = None,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        ...

    @overload
    async def run_machine_action(
        self,
        *,
        add_ssh_key: None = None,
        remove_ssh_key_fingerprint: None = None,
        restart_machine: None = None,
        cancel_restart: None = None,
        end_session_id: str,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        ...

    async def run_machine_action(
        self,
        *,
        add_ssh_key: SshKey | None = None,
        remove_ssh_key_fingerprint: str | None = None,
        restart_machine: RestartMachineAction | None = None,
        cancel_restart: bool | None = None,
        end_session_id: str | None = None,
    ) -> RunMachineActionResponse:
        """Run a machine action.

        One machine action: add or remove the person's SSH public key (for SSH and SFTP to their
        projects' containers: Service.ssh_command), end a session, schedule or cancel a restart.
        Returns the machine.

        Destructive: it may delete or overwrite something.

        At most one of `add_ssh_key`, `remove_ssh_key_fingerprint`, `restart_machine`, `cancel_restart`, `end_session_id`.

        Args:
            add_ssh_key: label: one line, ≤100 chars; empty = the key's comment. An existing key gets the new label.
            remove_ssh_key_fingerprint: A Machine.ssh_keys fingerprint; its sessions end. NotFoundError = no such key.
            restart_machine: Containers come back per restart policy. A new call before the restart replaces it; after (Machine.boot_time changed), restarts again.
            cancel_restart: True = cancels the scheduled restart.
            end_session_id: A Machine.sessions id: ends it now (its key can open new ones until removed). NotFoundError = ended.
        """
        return _convert.run_machine_action_response_from_wire(await self._call(self._wire.run_machine_action, _convert.run_machine_action_request(add_ssh_key=add_ssh_key, remove_ssh_key_fingerprint=remove_ssh_key_fingerprint, restart_machine=restart_machine, cancel_restart=cancel_restart, end_session_id=end_session_id)))

    async def get_project(
        self,
        project_id: str,
        *,
        include_secret_values: bool = False,
        snapshots_before: datetime | None = None,
        snapshots_volume: str = "",
    ) -> GetProjectResponse:
        """Get a project.

        One project in full: services (state, health, image, the ports it listens on, volumes,
        environment, the SSH command), volumes, routes, hosts with certificates, recent operations,
        snapshots, the last day's HTTP traffic. Env-file values only with include_secret_values. Its
        files: read_path.

        Read-only.

        Args:
            include_secret_values: True = include env-file values (EnvironmentVariable.secret). To edit .env: read_path /.env.
            snapshots_before: Only older snapshots: the oldest create_time seen, to page back. Absent = the newest.
            snapshots_volume: Only snapshots holding this volume (Volume.snapshot_count). Empty = all.
        """
        return _convert.get_project_response_from_wire(await self._call(self._wire.get_project, _convert.get_project_request(project_id=project_id, include_secret_values=include_secret_values, snapshots_before=snapshots_before, snapshots_volume=snapshots_volume)))

    async def create_project(
        self,
        project_id: str,
        *,
        source: ProjectSource | None = None,
        upload_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> CreateProjectResponse:
        """Create a project.

        Creates a project from its files and deploys it. Waits for the deploy (wait_seconds) and
        answers with the operation and, once it ended, the project: its URL, its services' states,
        its problems. `violations` instead = nothing was created: change what each says, call again.
        SUCCEEDED says the containers run and listen, not what a page answers: open the URL once
        (401 = its password page).

        Files, one of: the directory as it is on your disk, as an archive (create_transfer, then
        `upload_id`): nothing is retyped; `files`, text you send yourself, when there is no directory
        or no shell (never a file you have not read); `source.github`. /.env holds the secrets
        (`env_file: .env`). The compose file is the root's pethost.compose.yaml (so the repository's
        compose.yaml stays for development), else compose.yaml, compose.yml, docker-compose.yml or
        docker-compose.yaml; it becomes /compose.yaml, other compose and override files are dropped.
        Without one, a Dockerfile yields service `app` (reading /.env if any, its EXPOSE ports, a
        named volume per VOLUME of its last stage).

        compose.yaml rules. Data lives in named volumes; all else a container writes is lost when it
        is recreated. Project files are bind-mounted read-only. Public traffic comes only through
        the proxy, set in `x-pethost`, the one extension read, in the file or as `x_pethost`:

          x-pethost:
            metadata: {name: Recipe Box, emoji: "🥗", description: One line, notes: Free text}
            routes:
              - {host: recipes.sam.pethost.app, service: web, port: 3000}
              - {host: recipes.sam.pethost.app, path: /api, service: api, port: 8000, strip_path: true}

        A service without a route is private: the project's services reach it at `<service>:<port>`.
        A password for visitors goes only as `x_pethost.password`, never into the file: every route
        then answers 401 with a password page, over HTTPS only; nothing returns it
        (`Project.password_protected` says it is set); and `files` that write /compose.yaml keep the
        `password_hash` line the machine put in its `x-pethost`.
        All of compose.yaml is interpolated: $$ for $.

        The file runs as written, or is refused: the machine corrects nothing in it, in any version.
        Refused, each violation saying what to write instead:
        - `container_name`, `profiles`; `name`, `driver`, `driver_opts`, `external` or `ipam` of a
          volume or network: remove them.
        - `ports:` with a port a route sends to (remove the entry: the proxy serves it), or with a
          machine port the machine keeps, such as 22, 80, 443 (publish another, or use a route).
        - a writable bind mount (`.:/app`, `./data:/data`): project files take `:ro`, data a named
          volume (`data:/data`, with `data:` under `volumes:`).
        - a volume with no name (`- /data`): name it. Below a bind mount it is allowed, as scratch
          space (`/app/node_modules`).
        - `env_file` naming a file the files lack: write it, empty if it sets nothing, or give the
          entry `required: false`.
        - `privileged`, `cap_add`, `security_opt`, `devices`, host namespaces, the Docker socket, a
          path outside the directory; more than one replica; `include` or `extends` from a URL; a
          git URL as a build context.
        An image's VOLUME that no mount covers fails the deploy (UNCOVERED_IMAGE_VOLUME): mount a
        named volume or a tmpfs there.

        AlreadyExistsError = the id is taken (a retry with its operation_id returns that operation).
        FailedPreconditionError = the GitHub App cannot read the repository (see GetMachineResponse.github), or no
        such branch or directory. A deleted project's id inherits its snapshots.

        Args:
            project_id: New, [a-z0-9][a-z0-9_-]*, ≤63 chars; immutable.
            source: Set = a GitHub project: {github: {repository}}. Absent = the files of this request.
            upload_id: An archive of the project's directory, from create_transfer(upload_archive=), unpacked first. FailedPreconditionError = not arrived; NotFoundError = expired or used. One the machine refused (its PUT said why) answers with its `violations`.
            files: The project's files, e.g. [{path: "/compose.yaml", text: "…"}, {path: "/.env", text: "…"}], or those to write over the archive's or the commit's. A github source takes only /.env.
            x_pethost: Changes to the files' x-pethost: the name people see, the routes, a password.
            timeout_seconds: As deploy_project's timeout_seconds.
            operation_id: As deploy_project's operation_id.
            wait_seconds: As deploy_project's wait_seconds.
        """
        return _convert.create_project_response_from_wire(await self._call(self._wire.create_project, _convert.create_project_request(project_id=project_id, source=source, upload_id=upload_id, files=files, x_pethost=x_pethost, timeout_seconds=timeout_seconds, operation_id=operation_id, wait_seconds=wait_seconds)))

    @overload
    async def deploy_project(
        self,
        project_id: str,
        *,
        base_deploy_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        mount_volume: MountVolume | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        upload_id: None = None,
        commit: None = None,
        newest_commit: None = None,
        rollback_deploy_id: None = None,
        wait_seconds: int | None = None,
    ) -> DeployProjectResponse:
        """Deploy a project.

        Deploys a new version of a project and answers as create_project does: `files` written over
        its own (/.env, /compose.yaml, a source file), `x_pethost` (name, routes, password),
        `mount_volume`, a new archive (`upload_id`), a commit, or an earlier deploy's files again
        (`rollback_deploy_id`). compose.yaml rules: create_project's.

        It builds `build:` images, pulls missing ones, runs `compose up` on the whole project and waits
        until each service runs (healthy, if it has a healthcheck) or each job exits 0, and until each
        routed service listens on its route's port (up to 15 s: one that does not is the project's
        SERVICE_PORT_CLOSED problem, its route answering 502, not a failed deploy). So it also starts
        stopped services, reruns jobs, recreates changed services and those bind-mounting project
        files, and fails on an unhealthy service. While Project.x_pethost_applies_at_once, a version
        differing only in `x-pethost` (or not at all) applies at once, restarting nothing. Any other
        deploy applies its routes and password as it ends: to hide new content from its first second,
        set the password first, in a call of its own, then deploy the content.

        A commit other than GithubSource.newest_commit turns auto_deploy off (pinned), even if it
        fails; only set_source turns it back on.

        NotFoundError = no such project, or no such kept deploy. AbortedError = base_deploy_id is not
        Project.deploy_id: reread, redo. FailedPreconditionError = as create_project, or `commit` not on
        the branch. ResourceExhaustedError = too many or too large `files`: send them with create_transfer.
        AlreadyExistsError = operation_id started another kind of operation. When it FAILED, Operation.made_current says whether the files were applied: then
        fix them, or roll back.

        Destructive: it may delete or overwrite something.

        A new version of the files; none = the current one.
        At most one of `upload_id`, `commit`, `newest_commit`, `rollback_deploy_id`.

        Args:
            base_deploy_id: Project.deploy_id as you read it: AbortedError if the project was deployed since. Empty = no check.
            files: Written in order over the current files, or over the new version's: e.g. [{path: "/.env", text: "…"}] writes that file whole, and the files not named stay. With no new version pethost.compose.yaml is refused: write /compose.yaml. github: only /.env. None = redeploy.
            x_pethost: Edits x-pethost by part, after `files`: metadata by key; routes all at once.
            mount_volume: Not with upload_id, or github.
            timeout_seconds: For the whole deploy, builds included; 0 = default.
            operation_id: For a safe retry: the same id returns the first call's operation and starts nothing. [A-Za-z0-9][A-Za-z0-9._-]*, ≤128 chars; empty = generated.
            upload_id: files project: an archive from create_transfer; replaces all files but /.env and x-pethost.
            commit: github project: a commit of its branch (SHA, ≥7 chars), from list_commits.
            newest_commit: github project: true = GithubSource.newest_commit, read now.
            rollback_deploy_id: files project, a rollback: the operation_id of an earlier deploy with files_kept (Project.operations). Its files return as a new version; /.env, x-pethost and volumes stay.
            wait_seconds: Seconds to wait for the deploy's end, ≤45. Absent = 45; 0 = answer once it started. Still IN_PROGRESS then: get_operation waits on.
        """
        ...

    @overload
    async def deploy_project(
        self,
        project_id: str,
        *,
        base_deploy_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        mount_volume: MountVolume | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        upload_id: str,
        commit: None = None,
        newest_commit: None = None,
        rollback_deploy_id: None = None,
        wait_seconds: int | None = None,
    ) -> DeployProjectResponse:
        """Deploy a project.

        Deploys a new version of a project and answers as create_project does: `files` written over
        its own (/.env, /compose.yaml, a source file), `x_pethost` (name, routes, password),
        `mount_volume`, a new archive (`upload_id`), a commit, or an earlier deploy's files again
        (`rollback_deploy_id`). compose.yaml rules: create_project's.

        It builds `build:` images, pulls missing ones, runs `compose up` on the whole project and waits
        until each service runs (healthy, if it has a healthcheck) or each job exits 0, and until each
        routed service listens on its route's port (up to 15 s: one that does not is the project's
        SERVICE_PORT_CLOSED problem, its route answering 502, not a failed deploy). So it also starts
        stopped services, reruns jobs, recreates changed services and those bind-mounting project
        files, and fails on an unhealthy service. While Project.x_pethost_applies_at_once, a version
        differing only in `x-pethost` (or not at all) applies at once, restarting nothing. Any other
        deploy applies its routes and password as it ends: to hide new content from its first second,
        set the password first, in a call of its own, then deploy the content.

        A commit other than GithubSource.newest_commit turns auto_deploy off (pinned), even if it
        fails; only set_source turns it back on.

        NotFoundError = no such project, or no such kept deploy. AbortedError = base_deploy_id is not
        Project.deploy_id: reread, redo. FailedPreconditionError = as create_project, or `commit` not on
        the branch. ResourceExhaustedError = too many or too large `files`: send them with create_transfer.
        AlreadyExistsError = operation_id started another kind of operation. When it FAILED, Operation.made_current says whether the files were applied: then
        fix them, or roll back.

        Destructive: it may delete or overwrite something.

        A new version of the files; none = the current one.
        At most one of `upload_id`, `commit`, `newest_commit`, `rollback_deploy_id`.

        Args:
            base_deploy_id: Project.deploy_id as you read it: AbortedError if the project was deployed since. Empty = no check.
            files: Written in order over the current files, or over the new version's: e.g. [{path: "/.env", text: "…"}] writes that file whole, and the files not named stay. With no new version pethost.compose.yaml is refused: write /compose.yaml. github: only /.env. None = redeploy.
            x_pethost: Edits x-pethost by part, after `files`: metadata by key; routes all at once.
            mount_volume: Not with upload_id, or github.
            timeout_seconds: For the whole deploy, builds included; 0 = default.
            operation_id: For a safe retry: the same id returns the first call's operation and starts nothing. [A-Za-z0-9][A-Za-z0-9._-]*, ≤128 chars; empty = generated.
            upload_id: files project: an archive from create_transfer; replaces all files but /.env and x-pethost.
            commit: github project: a commit of its branch (SHA, ≥7 chars), from list_commits.
            newest_commit: github project: true = GithubSource.newest_commit, read now.
            rollback_deploy_id: files project, a rollback: the operation_id of an earlier deploy with files_kept (Project.operations). Its files return as a new version; /.env, x-pethost and volumes stay.
            wait_seconds: Seconds to wait for the deploy's end, ≤45. Absent = 45; 0 = answer once it started. Still IN_PROGRESS then: get_operation waits on.
        """
        ...

    @overload
    async def deploy_project(
        self,
        project_id: str,
        *,
        base_deploy_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        mount_volume: MountVolume | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        upload_id: None = None,
        commit: str,
        newest_commit: None = None,
        rollback_deploy_id: None = None,
        wait_seconds: int | None = None,
    ) -> DeployProjectResponse:
        """Deploy a project.

        Deploys a new version of a project and answers as create_project does: `files` written over
        its own (/.env, /compose.yaml, a source file), `x_pethost` (name, routes, password),
        `mount_volume`, a new archive (`upload_id`), a commit, or an earlier deploy's files again
        (`rollback_deploy_id`). compose.yaml rules: create_project's.

        It builds `build:` images, pulls missing ones, runs `compose up` on the whole project and waits
        until each service runs (healthy, if it has a healthcheck) or each job exits 0, and until each
        routed service listens on its route's port (up to 15 s: one that does not is the project's
        SERVICE_PORT_CLOSED problem, its route answering 502, not a failed deploy). So it also starts
        stopped services, reruns jobs, recreates changed services and those bind-mounting project
        files, and fails on an unhealthy service. While Project.x_pethost_applies_at_once, a version
        differing only in `x-pethost` (or not at all) applies at once, restarting nothing. Any other
        deploy applies its routes and password as it ends: to hide new content from its first second,
        set the password first, in a call of its own, then deploy the content.

        A commit other than GithubSource.newest_commit turns auto_deploy off (pinned), even if it
        fails; only set_source turns it back on.

        NotFoundError = no such project, or no such kept deploy. AbortedError = base_deploy_id is not
        Project.deploy_id: reread, redo. FailedPreconditionError = as create_project, or `commit` not on
        the branch. ResourceExhaustedError = too many or too large `files`: send them with create_transfer.
        AlreadyExistsError = operation_id started another kind of operation. When it FAILED, Operation.made_current says whether the files were applied: then
        fix them, or roll back.

        Destructive: it may delete or overwrite something.

        A new version of the files; none = the current one.
        At most one of `upload_id`, `commit`, `newest_commit`, `rollback_deploy_id`.

        Args:
            base_deploy_id: Project.deploy_id as you read it: AbortedError if the project was deployed since. Empty = no check.
            files: Written in order over the current files, or over the new version's: e.g. [{path: "/.env", text: "…"}] writes that file whole, and the files not named stay. With no new version pethost.compose.yaml is refused: write /compose.yaml. github: only /.env. None = redeploy.
            x_pethost: Edits x-pethost by part, after `files`: metadata by key; routes all at once.
            mount_volume: Not with upload_id, or github.
            timeout_seconds: For the whole deploy, builds included; 0 = default.
            operation_id: For a safe retry: the same id returns the first call's operation and starts nothing. [A-Za-z0-9][A-Za-z0-9._-]*, ≤128 chars; empty = generated.
            upload_id: files project: an archive from create_transfer; replaces all files but /.env and x-pethost.
            commit: github project: a commit of its branch (SHA, ≥7 chars), from list_commits.
            newest_commit: github project: true = GithubSource.newest_commit, read now.
            rollback_deploy_id: files project, a rollback: the operation_id of an earlier deploy with files_kept (Project.operations). Its files return as a new version; /.env, x-pethost and volumes stay.
            wait_seconds: Seconds to wait for the deploy's end, ≤45. Absent = 45; 0 = answer once it started. Still IN_PROGRESS then: get_operation waits on.
        """
        ...

    @overload
    async def deploy_project(
        self,
        project_id: str,
        *,
        base_deploy_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        mount_volume: MountVolume | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        upload_id: None = None,
        commit: None = None,
        newest_commit: bool,
        rollback_deploy_id: None = None,
        wait_seconds: int | None = None,
    ) -> DeployProjectResponse:
        """Deploy a project.

        Deploys a new version of a project and answers as create_project does: `files` written over
        its own (/.env, /compose.yaml, a source file), `x_pethost` (name, routes, password),
        `mount_volume`, a new archive (`upload_id`), a commit, or an earlier deploy's files again
        (`rollback_deploy_id`). compose.yaml rules: create_project's.

        It builds `build:` images, pulls missing ones, runs `compose up` on the whole project and waits
        until each service runs (healthy, if it has a healthcheck) or each job exits 0, and until each
        routed service listens on its route's port (up to 15 s: one that does not is the project's
        SERVICE_PORT_CLOSED problem, its route answering 502, not a failed deploy). So it also starts
        stopped services, reruns jobs, recreates changed services and those bind-mounting project
        files, and fails on an unhealthy service. While Project.x_pethost_applies_at_once, a version
        differing only in `x-pethost` (or not at all) applies at once, restarting nothing. Any other
        deploy applies its routes and password as it ends: to hide new content from its first second,
        set the password first, in a call of its own, then deploy the content.

        A commit other than GithubSource.newest_commit turns auto_deploy off (pinned), even if it
        fails; only set_source turns it back on.

        NotFoundError = no such project, or no such kept deploy. AbortedError = base_deploy_id is not
        Project.deploy_id: reread, redo. FailedPreconditionError = as create_project, or `commit` not on
        the branch. ResourceExhaustedError = too many or too large `files`: send them with create_transfer.
        AlreadyExistsError = operation_id started another kind of operation. When it FAILED, Operation.made_current says whether the files were applied: then
        fix them, or roll back.

        Destructive: it may delete or overwrite something.

        A new version of the files; none = the current one.
        At most one of `upload_id`, `commit`, `newest_commit`, `rollback_deploy_id`.

        Args:
            base_deploy_id: Project.deploy_id as you read it: AbortedError if the project was deployed since. Empty = no check.
            files: Written in order over the current files, or over the new version's: e.g. [{path: "/.env", text: "…"}] writes that file whole, and the files not named stay. With no new version pethost.compose.yaml is refused: write /compose.yaml. github: only /.env. None = redeploy.
            x_pethost: Edits x-pethost by part, after `files`: metadata by key; routes all at once.
            mount_volume: Not with upload_id, or github.
            timeout_seconds: For the whole deploy, builds included; 0 = default.
            operation_id: For a safe retry: the same id returns the first call's operation and starts nothing. [A-Za-z0-9][A-Za-z0-9._-]*, ≤128 chars; empty = generated.
            upload_id: files project: an archive from create_transfer; replaces all files but /.env and x-pethost.
            commit: github project: a commit of its branch (SHA, ≥7 chars), from list_commits.
            newest_commit: github project: true = GithubSource.newest_commit, read now.
            rollback_deploy_id: files project, a rollback: the operation_id of an earlier deploy with files_kept (Project.operations). Its files return as a new version; /.env, x-pethost and volumes stay.
            wait_seconds: Seconds to wait for the deploy's end, ≤45. Absent = 45; 0 = answer once it started. Still IN_PROGRESS then: get_operation waits on.
        """
        ...

    @overload
    async def deploy_project(
        self,
        project_id: str,
        *,
        base_deploy_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        mount_volume: MountVolume | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        upload_id: None = None,
        commit: None = None,
        newest_commit: None = None,
        rollback_deploy_id: str,
        wait_seconds: int | None = None,
    ) -> DeployProjectResponse:
        """Deploy a project.

        Deploys a new version of a project and answers as create_project does: `files` written over
        its own (/.env, /compose.yaml, a source file), `x_pethost` (name, routes, password),
        `mount_volume`, a new archive (`upload_id`), a commit, or an earlier deploy's files again
        (`rollback_deploy_id`). compose.yaml rules: create_project's.

        It builds `build:` images, pulls missing ones, runs `compose up` on the whole project and waits
        until each service runs (healthy, if it has a healthcheck) or each job exits 0, and until each
        routed service listens on its route's port (up to 15 s: one that does not is the project's
        SERVICE_PORT_CLOSED problem, its route answering 502, not a failed deploy). So it also starts
        stopped services, reruns jobs, recreates changed services and those bind-mounting project
        files, and fails on an unhealthy service. While Project.x_pethost_applies_at_once, a version
        differing only in `x-pethost` (or not at all) applies at once, restarting nothing. Any other
        deploy applies its routes and password as it ends: to hide new content from its first second,
        set the password first, in a call of its own, then deploy the content.

        A commit other than GithubSource.newest_commit turns auto_deploy off (pinned), even if it
        fails; only set_source turns it back on.

        NotFoundError = no such project, or no such kept deploy. AbortedError = base_deploy_id is not
        Project.deploy_id: reread, redo. FailedPreconditionError = as create_project, or `commit` not on
        the branch. ResourceExhaustedError = too many or too large `files`: send them with create_transfer.
        AlreadyExistsError = operation_id started another kind of operation. When it FAILED, Operation.made_current says whether the files were applied: then
        fix them, or roll back.

        Destructive: it may delete or overwrite something.

        A new version of the files; none = the current one.
        At most one of `upload_id`, `commit`, `newest_commit`, `rollback_deploy_id`.

        Args:
            base_deploy_id: Project.deploy_id as you read it: AbortedError if the project was deployed since. Empty = no check.
            files: Written in order over the current files, or over the new version's: e.g. [{path: "/.env", text: "…"}] writes that file whole, and the files not named stay. With no new version pethost.compose.yaml is refused: write /compose.yaml. github: only /.env. None = redeploy.
            x_pethost: Edits x-pethost by part, after `files`: metadata by key; routes all at once.
            mount_volume: Not with upload_id, or github.
            timeout_seconds: For the whole deploy, builds included; 0 = default.
            operation_id: For a safe retry: the same id returns the first call's operation and starts nothing. [A-Za-z0-9][A-Za-z0-9._-]*, ≤128 chars; empty = generated.
            upload_id: files project: an archive from create_transfer; replaces all files but /.env and x-pethost.
            commit: github project: a commit of its branch (SHA, ≥7 chars), from list_commits.
            newest_commit: github project: true = GithubSource.newest_commit, read now.
            rollback_deploy_id: files project, a rollback: the operation_id of an earlier deploy with files_kept (Project.operations). Its files return as a new version; /.env, x-pethost and volumes stay.
            wait_seconds: Seconds to wait for the deploy's end, ≤45. Absent = 45; 0 = answer once it started. Still IN_PROGRESS then: get_operation waits on.
        """
        ...

    async def deploy_project(
        self,
        project_id: str,
        *,
        base_deploy_id: str = "",
        files: Sequence[FileChange] = (),
        x_pethost: ProjectExtension | None = None,
        mount_volume: MountVolume | None = None,
        timeout_seconds: int = 0,
        operation_id: str = "",
        upload_id: str | None = None,
        commit: str | None = None,
        newest_commit: bool | None = None,
        rollback_deploy_id: str | None = None,
        wait_seconds: int | None = None,
    ) -> DeployProjectResponse:
        """Deploy a project.

        Deploys a new version of a project and answers as create_project does: `files` written over
        its own (/.env, /compose.yaml, a source file), `x_pethost` (name, routes, password),
        `mount_volume`, a new archive (`upload_id`), a commit, or an earlier deploy's files again
        (`rollback_deploy_id`). compose.yaml rules: create_project's.

        It builds `build:` images, pulls missing ones, runs `compose up` on the whole project and waits
        until each service runs (healthy, if it has a healthcheck) or each job exits 0, and until each
        routed service listens on its route's port (up to 15 s: one that does not is the project's
        SERVICE_PORT_CLOSED problem, its route answering 502, not a failed deploy). So it also starts
        stopped services, reruns jobs, recreates changed services and those bind-mounting project
        files, and fails on an unhealthy service. While Project.x_pethost_applies_at_once, a version
        differing only in `x-pethost` (or not at all) applies at once, restarting nothing. Any other
        deploy applies its routes and password as it ends: to hide new content from its first second,
        set the password first, in a call of its own, then deploy the content.

        A commit other than GithubSource.newest_commit turns auto_deploy off (pinned), even if it
        fails; only set_source turns it back on.

        NotFoundError = no such project, or no such kept deploy. AbortedError = base_deploy_id is not
        Project.deploy_id: reread, redo. FailedPreconditionError = as create_project, or `commit` not on
        the branch. ResourceExhaustedError = too many or too large `files`: send them with create_transfer.
        AlreadyExistsError = operation_id started another kind of operation. When it FAILED, Operation.made_current says whether the files were applied: then
        fix them, or roll back.

        Destructive: it may delete or overwrite something.

        A new version of the files; none = the current one.
        At most one of `upload_id`, `commit`, `newest_commit`, `rollback_deploy_id`.

        Args:
            base_deploy_id: Project.deploy_id as you read it: AbortedError if the project was deployed since. Empty = no check.
            files: Written in order over the current files, or over the new version's: e.g. [{path: "/.env", text: "…"}] writes that file whole, and the files not named stay. With no new version pethost.compose.yaml is refused: write /compose.yaml. github: only /.env. None = redeploy.
            x_pethost: Edits x-pethost by part, after `files`: metadata by key; routes all at once.
            mount_volume: Not with upload_id, or github.
            timeout_seconds: For the whole deploy, builds included; 0 = default.
            operation_id: For a safe retry: the same id returns the first call's operation and starts nothing. [A-Za-z0-9][A-Za-z0-9._-]*, ≤128 chars; empty = generated.
            upload_id: files project: an archive from create_transfer; replaces all files but /.env and x-pethost.
            commit: github project: a commit of its branch (SHA, ≥7 chars), from list_commits.
            newest_commit: github project: true = GithubSource.newest_commit, read now.
            rollback_deploy_id: files project, a rollback: the operation_id of an earlier deploy with files_kept (Project.operations). Its files return as a new version; /.env, x-pethost and volumes stay.
            wait_seconds: Seconds to wait for the deploy's end, ≤45. Absent = 45; 0 = answer once it started. Still IN_PROGRESS then: get_operation waits on.
        """
        return _convert.deploy_project_response_from_wire(await self._call(self._wire.deploy_project, _convert.deploy_project_request(project_id=project_id, base_deploy_id=base_deploy_id, files=files, x_pethost=x_pethost, mount_volume=mount_volume, timeout_seconds=timeout_seconds, operation_id=operation_id, upload_id=upload_id, commit=commit, newest_commit=newest_commit, rollback_deploy_id=rollback_deploy_id, wait_seconds=wait_seconds)))

    async def list_commits(
        self,
        project_id: str,
        *,
        before_commit: str = "",
    ) -> ListCommitsResponse:
        """List a project's commits.

        A github project's branch commits that change its directory, newest first, 30 a page, with
        whether the files are at it and its last deploy. To roll back: deploy_project with an older
        commit (volumes keep their current data). FailedPreconditionError = a files project (it rolls
        back with deploy_project(rollback_deploy_id=)), no such branch, or before_commit not on it.

        Read-only.

        Args:
            before_commit: The previous page's last sha. Empty = from the newest.
        """
        return _convert.list_commits_response_from_wire(await self._call(self._wire.list_commits, _convert.list_commits_request(project_id=project_id, before_commit=before_commit)))

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: ServicesAction,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: ServicesAction,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: ServicesAction,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: RecreateServiceAction,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: BackUpAction,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: RestoreSnapshotAction,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: CancelOperationAction,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: DeleteProjectAction,
        set_source: None = None,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: ProjectSource,
        delete_volume: None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    @overload
    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: None = None,
        stop_services: None = None,
        restart_services: None = None,
        recreate_service: None = None,
        back_up: None = None,
        restore_snapshot: None = None,
        cancel_operation: None = None,
        delete_project: None = None,
        set_source: None = None,
        delete_volume: str,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        ...

    async def run_project_action(
        self,
        project_id: str,
        *,
        start_services: ServicesAction | None = None,
        stop_services: ServicesAction | None = None,
        restart_services: ServicesAction | None = None,
        recreate_service: RecreateServiceAction | None = None,
        back_up: BackUpAction | None = None,
        restore_snapshot: RestoreSnapshotAction | None = None,
        cancel_operation: CancelOperationAction | None = None,
        delete_project: DeleteProjectAction | None = None,
        set_source: ProjectSource | None = None,
        delete_volume: str | None = None,
        operation_id: str = "",
        wait_seconds: int | None = None,
    ) -> RunProjectActionResponse:
        """Run a project action.

        One project action: start, stop or restart services, recreate one, back up, restore, cancel an
        operation, change the source, delete an undeclared volume or the project. Recreate, back up,
        restore, delete and set_source's deploy run as operations, waited for (wait_seconds), as is
        the end of a cancelled one; the others are done on return. Answers with the project as it
        then is.

        Destructive: it may delete or overwrite something.

        At most one of `start_services`, `stop_services`, `restart_services`, `recreate_service`, `back_up`, `restore_snapshot`, `cancel_operation`, `delete_project`, `set_source`, `delete_volume`.

        Args:
            start_services: Starts stopped services and reruns jobs, not their dependencies. FailedPreconditionError = no container yet (deploy or recreate_service), or a published machine port is taken.
            stop_services: Stops services, each with its grace period. A machine restart may start them, per restart policy.
            restart_services: Restarts processes in the same containers. Codes as start_services.
            recreate_service: A new container: a fresh filesystem outside volumes. An operation.
            back_up: Backs up the directory and volumes now, live. An operation. FailedPreconditionError = backups off (Machine.backups_enabled).
            restore_snapshot: From a snapshot of this project. An operation.
            cancel_operation: Stops a running or starting operation: it ends CANCELLED, leaving what a failure would; one only starting answers CANCELLED from its own call. FailedPreconditionError = a delete past its final backup.
            delete_project: An operation: a final backup while backups are on, then containers, volumes, files, hosts, logs. Snapshots stay (GetMachineResponse.deleted_projects), and restoring one brings the project back, source included; with backups off there is none, and it is gone for good.
            set_source: Changes the source. To files: keeps the current files. To github: only the fields set change, e.g. {github: {auto_deploy: true}} follows pushes again; from files, repository is required. Deploys the newest commit if auto_deploy is on and the files are not at it. FailedPreconditionError = as create_project.
            delete_volume: A volume compose.yaml no longer declares (Volume.declared false). Its data then lives only in snapshots. FailedPreconditionError = declared or in use.
            operation_id: As deploy_project's, for the actions that run as operations.
            wait_seconds: As deploy_project's, for the actions that run as operations.
        """
        return _convert.run_project_action_response_from_wire(await self._call(self._wire.run_project_action, _convert.run_project_action_request(project_id=project_id, start_services=start_services, stop_services=stop_services, restart_services=restart_services, recreate_service=recreate_service, back_up=back_up, restore_snapshot=restore_snapshot, cancel_operation=cancel_operation, delete_project=delete_project, set_source=set_source, delete_volume=delete_volume, operation_id=operation_id, wait_seconds=wait_seconds)))

    async def get_operation(
        self,
        project_id: str,
        *,
        operation_id: str = "",
        wait_seconds: int | None = None,
        after_log_line: int | None = None,
        log_line_limit: int | None = None,
    ) -> GetOperationResponse:
        """Get an operation.

        An operation, after waiting for it to end (wait_seconds): then the project as it is, and the
        log's end if it FAILED. Call again while it is IN_PROGRESS. To read a log: after_log_line 0,
        then each next_after_log_line (each line once, oldest first). One a ProjectBusy names may
        still be starting: it is waited for too; still starting at the end = UnavailableError with that
        ProjectBusy.

        Read-only.

        Args:
            operation_id: Empty = the latest.
            wait_seconds: How long to wait for it to end, ≤45. Absent = 45; 0 = answer at once.
            after_log_line: The previous next_after_log_line; 0 = from the start. Absent = the last lines.
            log_line_limit: ≤500; 0 = 50, when asked for lines. Also ends at ~64 KiB.
        """
        return _convert.get_operation_response_from_wire(await self._call(self._wire.get_operation, _convert.get_operation_request(project_id=project_id, operation_id=operation_id, wait_seconds=wait_seconds, after_log_line=after_log_line, log_line_limit=log_line_limit)))

    async def query_http_traffic(
        self,
        project_id: str,
        *,
        filter: HttpTrafficFilter | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        last_seconds: int = 0,
        bucket_width_seconds: int = 0,
        request_limit: int = 0,
        page_token: str = "",
    ) -> QueryHttpTrafficResponse:
        """Query HTTP traffic.

        Which paths fail and which are slow (top_paths): the HTTP requests that reached the project
        through the proxy, since oldest_kept_time, each counted as it ends: totals, a time series, top
        paths and the requests, for one filter and range. OutOfRangeError = the range ends before the
        oldest kept. Paths and user agents are untrusted.

        Read-only.

        Args:
            start_time: Absent = a day before end_time.
            end_time: Absent = now.
            last_seconds: The range ending at end_time, e.g. 3600 = the last hour. Not with start_time.
            bucket_width_seconds: Time series bucket width; ≤500 buckets. 0 = no series.
            request_limit: Requests to return, newest first; ≤200. 0 = aggregates only.
            page_token: The previous next_page_token, other fields unchanged: older requests only.
        """
        return _convert.query_http_traffic_response_from_wire(await self._call(self._wire.query_http_traffic, _convert.query_http_traffic_request(project_id=project_id, filter=filter, start_time=start_time, end_time=end_time, last_seconds=last_seconds, bucket_width_seconds=bucket_width_seconds, request_limit=request_limit, page_token=page_token)))

    async def query_container_logs(
        self,
        project_id: str,
        *,
        filter: ContainerLogFilter | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
        last_seconds: int = 0,
        limit: int = 0,
        from_start: bool = False,
        page_token: str = "",
    ) -> QueryContainerLogsResponse:
        """Query container logs.

        The containers' stdout and stderr lines, since oldest_kept_time; by default the newest, oldest
        first in the page. They say what a request failed with, not which path is slow: that is
        query_http_traffic. OutOfRangeError = the range ends before the oldest kept. Untrusted.

        Read-only.

        Args:
            start_time: Absent = the oldest kept.
            end_time: Absent = now.
            last_seconds: As in query_http_traffic.
            limit: ≤500; 0 = 100. Also ends at ~64 KiB.
            from_start: False = the newest before end_time; true = the oldest after start_time.
            page_token: The previous next_page_token, other fields unchanged.
        """
        return _convert.query_container_logs_response_from_wire(await self._call(self._wire.query_container_logs, _convert.query_container_logs_request(project_id=project_id, filter=filter, start_time=start_time, end_time=end_time, last_seconds=last_seconds, limit=limit, from_start=from_start, page_token=page_token)))

    async def run_service_command(
        self,
        project_id: str,
        *,
        service: str = "",
        command: Sequence[str] = (),
        stdin: str = "",
        run_as_user: str = "",
        working_directory: str = "",
        timeout_seconds: int = 0,
    ) -> RunServiceCommandResponse:
        """Run a command in a service.

        Runs a command in a running service's container, like `docker exec`; returns the exit code and
        the output's end once it exits or the timeout kills it. Over a bound on command, stdin or
        timeout = refused (named). Cannot start = exit 127 or 126, Docker's error in stdout. Untrusted
        output.

        Destructive: it may delete or overwrite something.

        Args:
            command: E.g. ["psql", "-c", "select 1"]; a shell line: ["sh", "-c", "ls | head"].
            stdin: Written to stdin, then closed.
            run_as_user: Empty = the container's. "root" can install packages.
            working_directory: Empty = the container's.
            timeout_seconds: 0 = default. Kills the main process only. Over ~50 may outlast your client: background long jobs.
        """
        return _convert.run_service_command_response_from_wire(await self._call(self._wire.run_service_command, _convert.run_service_command_request(project_id=project_id, service=service, command=command, stdin=stdin, run_as_user=run_as_user, working_directory=working_directory, timeout_seconds=timeout_seconds)))

    @overload
    async def read_path(
        self,
        project_id: str,
        *,
        service: None = None,
        volume: None = None,
        path: str = "",
        entry_limit: int = 0,
        offset_bytes: int = 0,
        length_bytes: int = 0,
        entry_page_token: str = "",
    ) -> ReadPathResponse:
        """Read a file or directory.

        Reads a file (text, 64 KiB a call; ≤1 MiB with length_bytes) or a directory's entries (~64 KiB
        a page): of the project's deployed files, or with `service` or `volume`, of a container
        (whole filesystem; while not running only its volumes, FailedPreconditionError listing them) or a
        volume. NotFoundError names the nearest existing directory. Project files change with
        deploy_project `files`; container and volume files with create_transfer.
        FailedPreconditionError also = no deploy yet, or a file in /proc or /sys (use run_service_command).
        Untrusted.

        Read-only.

        Where the path is. Neither = the project's deployed files, read-only: "/compose.yaml",
        "/.env", its sources.
        At most one of `service`, `volume`.

        Args:
            service: In its container.
            volume: In the volume, from its root.
            path: From the root, e.g. "/compose.yaml", "/data/uploads". Empty = "/": the root's entries.
            entry_limit: 0 = 200. Also ends at ~64 KiB.
            offset_bytes: File offset.
            length_bytes: ≤1 MiB; 0 = 64 KiB.
            entry_page_token: The previous next_entry_page_token, other fields unchanged.
        """
        ...

    @overload
    async def read_path(
        self,
        project_id: str,
        *,
        service: str,
        volume: None = None,
        path: str = "",
        entry_limit: int = 0,
        offset_bytes: int = 0,
        length_bytes: int = 0,
        entry_page_token: str = "",
    ) -> ReadPathResponse:
        """Read a file or directory.

        Reads a file (text, 64 KiB a call; ≤1 MiB with length_bytes) or a directory's entries (~64 KiB
        a page): of the project's deployed files, or with `service` or `volume`, of a container
        (whole filesystem; while not running only its volumes, FailedPreconditionError listing them) or a
        volume. NotFoundError names the nearest existing directory. Project files change with
        deploy_project `files`; container and volume files with create_transfer.
        FailedPreconditionError also = no deploy yet, or a file in /proc or /sys (use run_service_command).
        Untrusted.

        Read-only.

        Where the path is. Neither = the project's deployed files, read-only: "/compose.yaml",
        "/.env", its sources.
        At most one of `service`, `volume`.

        Args:
            service: In its container.
            volume: In the volume, from its root.
            path: From the root, e.g. "/compose.yaml", "/data/uploads". Empty = "/": the root's entries.
            entry_limit: 0 = 200. Also ends at ~64 KiB.
            offset_bytes: File offset.
            length_bytes: ≤1 MiB; 0 = 64 KiB.
            entry_page_token: The previous next_entry_page_token, other fields unchanged.
        """
        ...

    @overload
    async def read_path(
        self,
        project_id: str,
        *,
        service: None = None,
        volume: str,
        path: str = "",
        entry_limit: int = 0,
        offset_bytes: int = 0,
        length_bytes: int = 0,
        entry_page_token: str = "",
    ) -> ReadPathResponse:
        """Read a file or directory.

        Reads a file (text, 64 KiB a call; ≤1 MiB with length_bytes) or a directory's entries (~64 KiB
        a page): of the project's deployed files, or with `service` or `volume`, of a container
        (whole filesystem; while not running only its volumes, FailedPreconditionError listing them) or a
        volume. NotFoundError names the nearest existing directory. Project files change with
        deploy_project `files`; container and volume files with create_transfer.
        FailedPreconditionError also = no deploy yet, or a file in /proc or /sys (use run_service_command).
        Untrusted.

        Read-only.

        Where the path is. Neither = the project's deployed files, read-only: "/compose.yaml",
        "/.env", its sources.
        At most one of `service`, `volume`.

        Args:
            service: In its container.
            volume: In the volume, from its root.
            path: From the root, e.g. "/compose.yaml", "/data/uploads". Empty = "/": the root's entries.
            entry_limit: 0 = 200. Also ends at ~64 KiB.
            offset_bytes: File offset.
            length_bytes: ≤1 MiB; 0 = 64 KiB.
            entry_page_token: The previous next_entry_page_token, other fields unchanged.
        """
        ...

    async def read_path(
        self,
        project_id: str,
        *,
        service: str | None = None,
        volume: str | None = None,
        path: str = "",
        entry_limit: int = 0,
        offset_bytes: int = 0,
        length_bytes: int = 0,
        entry_page_token: str = "",
    ) -> ReadPathResponse:
        """Read a file or directory.

        Reads a file (text, 64 KiB a call; ≤1 MiB with length_bytes) or a directory's entries (~64 KiB
        a page): of the project's deployed files, or with `service` or `volume`, of a container
        (whole filesystem; while not running only its volumes, FailedPreconditionError listing them) or a
        volume. NotFoundError names the nearest existing directory. Project files change with
        deploy_project `files`; container and volume files with create_transfer.
        FailedPreconditionError also = no deploy yet, or a file in /proc or /sys (use run_service_command).
        Untrusted.

        Read-only.

        Where the path is. Neither = the project's deployed files, read-only: "/compose.yaml",
        "/.env", its sources.
        At most one of `service`, `volume`.

        Args:
            service: In its container.
            volume: In the volume, from its root.
            path: From the root, e.g. "/compose.yaml", "/data/uploads". Empty = "/": the root's entries.
            entry_limit: 0 = 200. Also ends at ~64 KiB.
            offset_bytes: File offset.
            length_bytes: ≤1 MiB; 0 = 64 KiB.
            entry_page_token: The previous next_entry_page_token, other fields unchanged.
        """
        return _convert.read_path_response_from_wire(await self._call(self._wire.read_path, _convert.read_path_request(project_id=project_id, service=service, volume=volume, path=path, entry_limit=entry_limit, offset_bytes=offset_bytes, length_bytes=length_bytes, entry_page_token=entry_page_token)))

    @overload
    async def create_transfer(
        self,
        *,
        upload_archive: None = None,
        upload_file: None = None,
        download: None = None,
    ) -> CreateTransferResponse:
        """Upload or download a file.

        A one-request URL moving one file straight between you and the machine: run `command` in a
        shell, or send `http_method` to `url` yourself, before expire_time.
        - upload_archive: the project's directory, packed, for create_project's or deploy_project's
          upload_id once the PUT answered 200 with what it holds.
        - upload_file: one file into a container or volume, replacing any file there (replaces),
          creating parents.
        - download: a file, or a directory as a .tar (file_name).
        Plain-text answers: 404 used or expired URL, 409 FailedPreconditionError, 413 archive over 2
        GiB, 422 unsafe archive (a reason per line), 507 disk full. A failed transfer keeps nothing:
        get a new URL. Errors as read_path; FailedPreconditionError also = downloading neither a file nor
        a directory, uploading onto a non-file, a mount point, /proc or /sys, or the hostname not yet
        certified. ResourceExhaustedError = disk full, or too many transfers.

        Destructive: it may delete or overwrite something.

        At most one of `upload_archive`, `upload_file`, `download`.
        """
        ...

    @overload
    async def create_transfer(
        self,
        *,
        upload_archive: ArchiveUpload,
        upload_file: None = None,
        download: None = None,
    ) -> CreateTransferResponse:
        """Upload or download a file.

        A one-request URL moving one file straight between you and the machine: run `command` in a
        shell, or send `http_method` to `url` yourself, before expire_time.
        - upload_archive: the project's directory, packed, for create_project's or deploy_project's
          upload_id once the PUT answered 200 with what it holds.
        - upload_file: one file into a container or volume, replacing any file there (replaces),
          creating parents.
        - download: a file, or a directory as a .tar (file_name).
        Plain-text answers: 404 used or expired URL, 409 FailedPreconditionError, 413 archive over 2
        GiB, 422 unsafe archive (a reason per line), 507 disk full. A failed transfer keeps nothing:
        get a new URL. Errors as read_path; FailedPreconditionError also = downloading neither a file nor
        a directory, uploading onto a non-file, a mount point, /proc or /sys, or the hostname not yet
        certified. ResourceExhaustedError = disk full, or too many transfers.

        Destructive: it may delete or overwrite something.

        At most one of `upload_archive`, `upload_file`, `download`.
        """
        ...

    @overload
    async def create_transfer(
        self,
        *,
        upload_archive: None = None,
        upload_file: FileUpload,
        download: None = None,
    ) -> CreateTransferResponse:
        """Upload or download a file.

        A one-request URL moving one file straight between you and the machine: run `command` in a
        shell, or send `http_method` to `url` yourself, before expire_time.
        - upload_archive: the project's directory, packed, for create_project's or deploy_project's
          upload_id once the PUT answered 200 with what it holds.
        - upload_file: one file into a container or volume, replacing any file there (replaces),
          creating parents.
        - download: a file, or a directory as a .tar (file_name).
        Plain-text answers: 404 used or expired URL, 409 FailedPreconditionError, 413 archive over 2
        GiB, 422 unsafe archive (a reason per line), 507 disk full. A failed transfer keeps nothing:
        get a new URL. Errors as read_path; FailedPreconditionError also = downloading neither a file nor
        a directory, uploading onto a non-file, a mount point, /proc or /sys, or the hostname not yet
        certified. ResourceExhaustedError = disk full, or too many transfers.

        Destructive: it may delete or overwrite something.

        At most one of `upload_archive`, `upload_file`, `download`.
        """
        ...

    @overload
    async def create_transfer(
        self,
        *,
        upload_archive: None = None,
        upload_file: None = None,
        download: PathDownload,
    ) -> CreateTransferResponse:
        """Upload or download a file.

        A one-request URL moving one file straight between you and the machine: run `command` in a
        shell, or send `http_method` to `url` yourself, before expire_time.
        - upload_archive: the project's directory, packed, for create_project's or deploy_project's
          upload_id once the PUT answered 200 with what it holds.
        - upload_file: one file into a container or volume, replacing any file there (replaces),
          creating parents.
        - download: a file, or a directory as a .tar (file_name).
        Plain-text answers: 404 used or expired URL, 409 FailedPreconditionError, 413 archive over 2
        GiB, 422 unsafe archive (a reason per line), 507 disk full. A failed transfer keeps nothing:
        get a new URL. Errors as read_path; FailedPreconditionError also = downloading neither a file nor
        a directory, uploading onto a non-file, a mount point, /proc or /sys, or the hostname not yet
        certified. ResourceExhaustedError = disk full, or too many transfers.

        Destructive: it may delete or overwrite something.

        At most one of `upload_archive`, `upload_file`, `download`.
        """
        ...

    async def create_transfer(
        self,
        *,
        upload_archive: ArchiveUpload | None = None,
        upload_file: FileUpload | None = None,
        download: PathDownload | None = None,
    ) -> CreateTransferResponse:
        """Upload or download a file.

        A one-request URL moving one file straight between you and the machine: run `command` in a
        shell, or send `http_method` to `url` yourself, before expire_time.
        - upload_archive: the project's directory, packed, for create_project's or deploy_project's
          upload_id once the PUT answered 200 with what it holds.
        - upload_file: one file into a container or volume, replacing any file there (replaces),
          creating parents.
        - download: a file, or a directory as a .tar (file_name).
        Plain-text answers: 404 used or expired URL, 409 FailedPreconditionError, 413 archive over 2
        GiB, 422 unsafe archive (a reason per line), 507 disk full. A failed transfer keeps nothing:
        get a new URL. Errors as read_path; FailedPreconditionError also = downloading neither a file nor
        a directory, uploading onto a non-file, a mount point, /proc or /sys, or the hostname not yet
        certified. ResourceExhaustedError = disk full, or too many transfers.

        Destructive: it may delete or overwrite something.

        At most one of `upload_archive`, `upload_file`, `download`.
        """
        return _convert.create_transfer_response_from_wire(await self._call(self._wire.create_transfer, _convert.create_transfer_request(upload_archive=upload_archive, upload_file=upload_file, download=download)))
