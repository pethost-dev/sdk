"""The API's messages and enums. Generated from v1/panel.proto: do not edit."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime
from typing import Any, final, overload

from ._runtime import OpenEnum
from ._runtime import one_of as _one_of


class MachineSessionKind(OpenEnum):
    """
    Attributes:
        WEB_TERMINAL: The web panel's terminal.
        SSH_TERMINAL: A program in a terminal, such as `ssh`'s shell.
        SSH_COMMAND: A program without a terminal, such as `ssh ... <command>` or rsync.
        SFTP: scp, sftp or sshfs.
        TUNNEL: One connection of an `ssh -L` tunnel to `port`.
    """

    UNSPECIFIED = 0

    WEB_TERMINAL = 1
    """The web panel's terminal."""

    SSH_TERMINAL = 2
    """A program in a terminal, such as `ssh`'s shell."""

    SSH_COMMAND = 3
    """A program without a terminal, such as `ssh ... <command>` or rsync."""

    SFTP = 4
    """scp, sftp or sshfs."""

    TUNNEL = 5
    """One connection of an `ssh -L` tunnel to `port`."""


class ProjectProblemKind(OpenEnum):
    """
    Attributes:
        DEPLOY_FAILED: The latest deploy failed. Its operation says why, and with made_current whether its files
            were applied (then some containers may run the old configuration).
        SERVICE_UNHEALTHY: Running; its healthcheck fails.
        SERVICE_RESTARTING: Docker is restarting it, or it runs and Docker restarted it recently: likely a crash
            loop.
        SERVICE_OUT_OF_MEMORY: Its last run was killed for exceeding its memory, or a process of it was since it started.
            A loop whose runs last 10 s or more shows as RESTARTING: Docker forgets the kill when it
            starts it again.
        BACKUP_FAILED: The latest backup failed; its operation says why.
        DEPLOY_CANCELLED: The latest deploy was cancelled; its operation says, with made_current, whether its files
            were applied.
        SERVICE_EXITED: It exited on its own with a non-zero code (Service.exit_code) and stays down: its restart
            policy does not restart it. A service a person stopped is no problem.
        RESTORE_FAILED: A restore failed or was cancelled, or a machine restart cut it short, and its harm remains:
            services it stopped are still stopped (starting them ends it); unless a restore that
            succeeded since replaced them, its volumes may be partly restored, and its operation's
            undo_snapshot_id holds them as they were. Or it brought a
            deleted project back, and no deploy has replaced it. The newest such restore counts; one
            that changed nothing does not.
        AUTO_DEPLOY_REFUSED: Auto-deploy is on, and the machine refused the commit it last tried, the branch's newest
            then, which the files are not; the message says why. Each commit is tried once: fix it and
            push, or deploy_project with newest_commit, whose refusal gives the violations.
        SERVICE_PORT_CLOSED: It runs and does not listen on the port a route sends to (or only at 127.0.0.1, which the
            proxy cannot reach): the route answers 502. The message names the ports it does listen on
            (Service.listening_ports): change the route's port with deploy_project(x_pethost=), or the app.
    """

    UNSPECIFIED = 0

    DEPLOY_FAILED = 1
    """The latest deploy failed. Its operation says why, and with made_current whether its files
    were applied (then some containers may run the old configuration).
    """

    SERVICE_UNHEALTHY = 2
    """Running; its healthcheck fails."""

    SERVICE_RESTARTING = 3
    """Docker is restarting it, or it runs and Docker restarted it recently: likely a crash
    loop.
    """

    SERVICE_OUT_OF_MEMORY = 4
    """Its last run was killed for exceeding its memory, or a process of it was since it started.
    A loop whose runs last 10 s or more shows as RESTARTING: Docker forgets the kill when it
    starts it again.
    """

    BACKUP_FAILED = 5
    """The latest backup failed; its operation says why."""

    DEPLOY_CANCELLED = 6
    """The latest deploy was cancelled; its operation says, with made_current, whether its files
    were applied.
    """

    SERVICE_EXITED = 7
    """It exited on its own with a non-zero code (Service.exit_code) and stays down: its restart
    policy does not restart it. A service a person stopped is no problem.
    """

    RESTORE_FAILED = 8
    """A restore failed or was cancelled, or a machine restart cut it short, and its harm remains:
    services it stopped are still stopped (starting them ends it); unless a restore that
    succeeded since replaced them, its volumes may be partly restored, and its operation's
    undo_snapshot_id holds them as they were. Or it brought a
    deleted project back, and no deploy has replaced it. The newest such restore counts; one
    that changed nothing does not.
    """

    AUTO_DEPLOY_REFUSED = 9
    """Auto-deploy is on, and the machine refused the commit it last tried, the branch's newest
    then, which the files are not; the message says why. Each commit is tried once: fix it and
    push, or deploy_project with newest_commit, whose refusal gives the violations.
    """

    SERVICE_PORT_CLOSED = 10
    """It runs and does not listen on the port a route sends to (or only at 127.0.0.1, which the
    proxy cannot reach): the route answers 502. The message names the ports it does listen on
    (Service.listening_ports): change the route's port with deploy_project(x_pethost=), or the app.
    """


class ServicesActionKind(OpenEnum):
    UNSPECIFIED = 0

    START = 1

    STOP = 2

    RESTART = 3


class ServiceState(OpenEnum):
    """
    Attributes:
        NOT_CREATED: Declared; no container yet.
        STARTING: Starting, or created while an operation that starts containers runs (deploy,
            recreate_service, restore); its healthcheck has not passed yet.
        RUNNING: Running, without a healthcheck.
        HEALTHY: Running; its healthcheck passes.
        UNHEALTHY: Running; its healthcheck fails.
        RESTARTING: Exited and Docker is restarting it.
        STOPPED: Not running: stopped by stop_services or a restore, never started, paused or dead.
        EXITED: Not running: it exited on its own (see exit_code; 0 = a job that finished).
    """

    UNSPECIFIED = 0

    NOT_CREATED = 1
    """Declared; no container yet."""

    STARTING = 2
    """Starting, or created while an operation that starts containers runs (deploy,
    recreate_service, restore); its healthcheck has not passed yet.
    """

    RUNNING = 3
    """Running, without a healthcheck."""

    HEALTHY = 4
    """Running; its healthcheck passes."""

    UNHEALTHY = 5
    """Running; its healthcheck fails."""

    RESTARTING = 6
    """Exited and Docker is restarting it."""

    STOPPED = 7
    """Not running: stopped by stop_services or a restore, never started, paused or dead."""

    EXITED = 8
    """Not running: it exited on its own (see exit_code; 0 = a job that finished)."""


class RestartPolicy(OpenEnum):
    """Docker's restart policies: what happens when the process exits, and when the machine starts.

    Attributes:
        NO: Never restarted.
        ON_FAILURE: Restarted when it exits non-zero. When the machine or Docker restarts it comes back unless it
            exited 0 (a finished job), so one stopped with stop_services comes back too. The default when
            compose.yaml sets none.
        UNLESS_STOPPED: Always restarted, unless stopped with run_project_action(stop_services=).
    """

    UNSPECIFIED = 0

    NO = 1
    """Never restarted."""

    ON_FAILURE = 2
    """Restarted when it exits non-zero. When the machine or Docker restarts it comes back unless it
    exited 0 (a finished job), so one stopped with stop_services comes back too. The default when
    compose.yaml sets none.
    """

    UNLESS_STOPPED = 3
    """Always restarted, unless stopped with run_project_action(stop_services=)."""

    ALWAYS = 4


class HealthStatus(OpenEnum):
    UNSPECIFIED = 0

    STARTING = 1

    HEALTHY = 2

    UNHEALTHY = 3


class CertificateSource(OpenEnum):
    """
    Attributes:
        NONE: No certificate will come: plain HTTP only. As when Machine.acme_enabled is off, or for an IP
            address or another name Let's Encrypt does not issue for.
        INSTALLED: A certificate installed on the machine covers it.
        AUTOMATIC: From Let's Encrypt, renewed automatically.
    """

    UNSPECIFIED = 0

    NONE = 1
    """No certificate will come: plain HTTP only. As when Machine.acme_enabled is off, or for an IP
    address or another name Let's Encrypt does not issue for.
    """

    INSTALLED = 2
    """A certificate installed on the machine covers it."""

    AUTOMATIC = 3
    """From Let's Encrypt, renewed automatically."""


class OperationKind(OpenEnum):
    UNSPECIFIED = 0

    DEPLOY = 1

    RECREATE_SERVICE = 2

    BACKUP = 3

    RESTORE = 4

    DELETE = 5


class OperationStatus(OpenEnum):
    UNSPECIFIED = 0

    IN_PROGRESS = 1

    SUCCEEDED = 2

    FAILED = 3

    CANCELLED = 4


class DeployFailureReason(OpenEnum):
    """
    Attributes:
        IMAGE_PULL_FAILED: A wrong name or tag, or a private image.
        CONTAINER_START_FAILED: E.g. the command does not exist.
        INTERNAL: Includes a machine restart during the operation.
        PORT_UNAVAILABLE: A `ports:` machine port is taken.
        CONTAINER_EXITED: Exited, or kept restarting, after starting.
        UNCOVERED_IMAGE_VOLUME: The image declares a VOLUME no mount covers: it would never be backed up. Mount a named
            volume there.
        BUILD_MEMORY_UNAVAILABLE: The running projects leave too little memory for a build; the message says how much.
    """

    UNSPECIFIED = 0

    IMAGE_PULL_FAILED = 1
    """A wrong name or tag, or a private image."""

    IMAGE_BUILD_FAILED = 2

    CONTAINER_START_FAILED = 3
    """E.g. the command does not exist."""

    DISK_FULL = 4

    INTERNAL = 5
    """Includes a machine restart during the operation."""

    PORT_UNAVAILABLE = 6
    """A `ports:` machine port is taken."""

    CONTAINER_EXITED = 7
    """Exited, or kept restarting, after starting."""

    CONTAINER_UNHEALTHY = 8

    TIMED_OUT = 9

    UNCOVERED_IMAGE_VOLUME = 10
    """The image declares a VOLUME no mount covers: it would never be backed up. Mount a named
    volume there.
    """

    BUILD_MEMORY_UNAVAILABLE = 11
    """The running projects leave too little memory for a build; the message says how much."""


class OutputStream(OpenEnum):
    UNSPECIFIED = 0

    STDOUT = 1

    STDERR = 2


class FileType(OpenEnum):
    """
    Attributes:
        OTHER: A device, socket or FIFO.
    """

    UNSPECIFIED = 0

    FILE = 1

    DIRECTORY = 2

    SYMLINK = 3

    OTHER = 4
    """A device, socket or FIFO."""


class FileLocation(OpenEnum):
    """Where a path of a service's container lies, which says whether it lasts.

    Attributes:
        CONTAINER: The container's own files, its image and what it wrote outside volumes, and its scratch
            space (an anonymous volume, a tmpfs): lost when it is recreated.
        VOLUME: A named volume (ReadPathResponse.volume): kept across deploys and backed up.
        PROJECT_FILES: The project's files, mounted read-only from its source as deployed: change them with
            deploy_project.
    """

    UNSPECIFIED = 0

    CONTAINER = 1
    """The container's own files, its image and what it wrote outside volumes, and its scratch
    space (an anonymous volume, a tmpfs): lost when it is recreated.
    """

    VOLUME = 2
    """A named volume (ReadPathResponse.volume): kept across deploys and backed up."""

    PROJECT_FILES = 3
    """The project's files, mounted read-only from its source as deployed: change them with
    deploy_project.
    """


class NoMachineReason(OpenEnum):
    """
    Attributes:
        NO_PLAN: The person has not chosen and paid for a plan: they do it at url.
        BEING_PREPARED: The plan is paid and a machine is being prepared for the account: Pethost emails the person
            when it is ready. Call again later.
    """

    UNSPECIFIED = 0

    NO_PLAN = 1
    """The person has not chosen and paid for a plan: they do it at url."""

    BEING_PREPARED = 2
    """The plan is paid and a machine is being prepared for the account: Pethost emails the person
    when it is ready. Call again later.
    """


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GetMachineResponse:
    """
    Attributes:
        projects: By project_id.
        deleted_projects: Projects no longer on the machine whose snapshots remain, the most recently backed up first;
            restore one with run_project_action(restore_snapshot=) and its project_id. Current after the
            machine's own backups and deletes; changes made to the backup repository elsewhere show
            later. Not known while Machine.snapshot_list_time is absent.
    """

    machine: Machine | None = None

    projects: Sequence[ProjectSummary] = ()
    """By project_id."""

    deleted_projects: Sequence[DeletedProject] = ()
    """Projects no longer on the machine whose snapshots remain, the most recently backed up first;
    restore one with run_project_action(restore_snapshot=) and its project_id. Current after the
    machine's own backups and deletes; changes made to the backup repository elsewhere show
    later. Not known while Machine.snapshot_list_time is absent.
    """

    github: GithubConnection | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.get_machine_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GetMachineResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.get_machine_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Machine:
    """
    Attributes:
        name: Its plan's name, e.g. "Starter".
        location: Where it runs, e.g. "Europe". Empty = not known.
        sample_time: When the figures below were read.
        cpu_used_cores: By projects and builds.
        memory_used_bytes: Without page cache, as `docker stats` counts.
        memory_total_bytes: The machine's, less a reserve for the system.
        disk_used_bytes: The projects' disk. The operating system has its own partition outside it, and the
            machine's own files are left out: a new machine uses 0.
        hostname: The machine's name: what the person's own domains point at (a CNAME), and where they log in
            to a service's container (Service.ssh_command). create_transfer's URLs are on it as well, and
            no route can take it.
        ssh_host_key_fingerprint: "SHA256:...", to check on the first connection.
        ssh_keys: The person's public keys: each logs in to every container. Empty = none yet: nobody can
            log in until run_machine_action(add_ssh_key=) adds one.
        backups_enabled: True = every project is backed up nightly, and on demand. False, always written = nothing is
            backed up: there are no snapshots, and a deleted project or volume is gone for good.
        snapshot_list_time: When the machine last read the backup repository's list of snapshots whole. Absent = not
            yet (snapshot_list_failure_message says why, once a read failed), or backups are off:
            snapshot counts, Volume.last_backup_time, Project.snapshots and GetMachineResponse.deleted_projects
            are then not known, rather than none.
        snapshot_list_failure_message: Why the machine could not read that list, while backups are on and snapshot_list_time is
            absent: the backup repository's error, e.g. a wrong password or a host that does not answer.
            The machine keeps trying. Empty = no read has failed, or the list is known, or backups are
            off.
        backup_retention_hours: Snapshots are pruned once they are this many hours older than their project's newest.
            0 = kept forever: nothing deletes them.
        acme_enabled: True = a host that no certificate installed on the machine covers gets one from Let's Encrypt
            once it resolves to the machine. False, always written = such a host serves plain HTTP only.
        apps_domain: The person's domain on Pethost, e.g. "sam.pethost.app": theirs alone, so "my domain" or "my
            Pethost domain" means this one unless they name another. A route's host
            `<name>.<apps_domain>`, or apps_domain itself, works at once over HTTPS, with no DNS record
            to make. Only the person changes it, in the panel's settings. Empty = there is none: every
            host is a domain the person owns.
        restart_required_time: When an update started to need a machine restart. Absent = none is needed.
        scheduled_restart_time: When run_machine_action(restart_machine=) will restart it; later while what it waits for is still
            going on (RestartMachineAction.interrupt_operations). Absent = not scheduled.
        sessions: What people have open in the containers now, oldest first: at most 100, the most the machine
            holds at once.
    """

    name: str = ""
    """Its plan's name, e.g. "Starter"."""

    location: str = ""
    """Where it runs, e.g. "Europe". Empty = not known."""

    sample_time: datetime | None = None
    """When the figures below were read."""

    cpu_used_cores: float = 0.0
    """By projects and builds."""

    cpu_total_cores: float = 0.0

    memory_used_bytes: int = 0
    """Without page cache, as `docker stats` counts."""

    memory_total_bytes: int = 0
    """The machine's, less a reserve for the system."""

    disk_used_bytes: int = 0
    """The projects' disk. The operating system has its own partition outside it, and the
    machine's own files are left out: a new machine uses 0.
    """

    disk_total_bytes: int = 0

    disk_usage: DiskUsage | None = None

    hostname: str = ""
    """The machine's name: what the person's own domains point at (a CNAME), and where they log in
    to a service's container (Service.ssh_command). create_transfer's URLs are on it as well, and
    no route can take it.
    """

    ssh_host_key_fingerprint: str = ""
    """"SHA256:...", to check on the first connection."""

    ssh_keys: Sequence[SshKey] = ()
    """The person's public keys: each logs in to every container. Empty = none yet: nobody can
    log in until run_machine_action(add_ssh_key=) adds one.
    """

    backups_enabled: bool = False
    """True = every project is backed up nightly, and on demand. False, always written = nothing is
    backed up: there are no snapshots, and a deleted project or volume is gone for good.
    """

    snapshot_list_time: datetime | None = None
    """When the machine last read the backup repository's list of snapshots whole. Absent = not
    yet (snapshot_list_failure_message says why, once a read failed), or backups are off:
    snapshot counts, Volume.last_backup_time, Project.snapshots and GetMachineResponse.deleted_projects
    are then not known, rather than none.
    """

    snapshot_list_failure_message: str = ""
    """Why the machine could not read that list, while backups are on and snapshot_list_time is
    absent: the backup repository's error, e.g. a wrong password or a host that does not answer.
    The machine keeps trying. Empty = no read has failed, or the list is known, or backups are
    off.
    """

    backup_retention_hours: int = 0
    """Snapshots are pruned once they are this many hours older than their project's newest.
    0 = kept forever: nothing deletes them.
    """

    acme_enabled: bool = False
    """True = a host that no certificate installed on the machine covers gets one from Let's Encrypt
    once it resolves to the machine. False, always written = such a host serves plain HTTP only.
    """

    apps_domain: str = ""
    """The person's domain on Pethost, e.g. "sam.pethost.app": theirs alone, so "my domain" or "my
    Pethost domain" means this one unless they name another. A route's host
    `<name>.<apps_domain>`, or apps_domain itself, works at once over HTTPS, with no DNS record
    to make. Only the person changes it, in the panel's settings. Empty = there is none: every
    host is a domain the person owns.
    """

    daemon_version: str = ""

    docker_version: str = ""

    boot_time: datetime | None = None

    restart_required_time: datetime | None = None
    """When an update started to need a machine restart. Absent = none is needed."""

    scheduled_restart_time: datetime | None = None
    """When run_machine_action(restart_machine=) will restart it; later while what it waits for is still
    going on (RestartMachineAction.interrupt_operations). Absent = not scheduled.
    """

    sessions: Sequence[MachineSession] = ()
    """What people have open in the containers now, oldest first: at most 100, the most the machine
    holds at once.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.machine_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Machine:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.machine_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MachineSession:
    """Something a person has open in a container: a web terminal (OpenTerminal), or, through SSH, a
    program, SFTP or one connection of a tunnel. It lasts until the program exits or the
    connection closes; run_machine_action(end_session_id=) ends it sooner.

    Attributes:
        session_id: For run_machine_action(end_session_id=).
        port: TUNNEL: the container's port.
        client_address: The person's IP address.
        ssh_key_label: Through SSH: the key they logged in with, as it was then. Empty for WEB_TERMINAL.
    """

    session_id: str = ""
    """For run_machine_action(end_session_id=)."""

    kind: MachineSessionKind = MachineSessionKind.UNSPECIFIED

    project_id: str = ""

    service: str = ""

    port: int = 0
    """TUNNEL: the container's port."""

    start_time: datetime | None = None

    client_address: str = ""
    """The person's IP address."""

    ssh_key_label: str = ""
    """Through SSH: the key they logged in with, as it was then. Empty for WEB_TERMINAL."""

    ssh_key_fingerprint: str = ""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.machine_session_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MachineSession:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.machine_session_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class DiskUsage:
    """Where the disk goes; the rest of disk_used_bytes is the filesystem's own metadata and the
    machine's small files. Measured every few minutes.

    Attributes:
        build_cache_bytes: Absent = not known: Docker cannot size the build cache.
        container_layers_bytes: What containers wrote outside volumes.
        project_files_bytes: Project directories and operation logs.
        container_logs_bytes: Kept on the operating system's partition, outside disk_used_bytes; the machine bounds their
            age and size (QueryContainerLogsResponse.oldest_kept_time).
        http_traffic_bytes: The HTTP request log.
    """

    images_bytes: int = 0

    build_cache_bytes: int | None = None
    """Absent = not known: Docker cannot size the build cache."""

    volumes_bytes: int = 0

    container_layers_bytes: int = 0
    """What containers wrote outside volumes."""

    project_files_bytes: int = 0
    """Project directories and operation logs."""

    container_logs_bytes: int = 0
    """Kept on the operating system's partition, outside disk_used_bytes; the machine bounds their
    age and size (QueryContainerLogsResponse.oldest_kept_time).
    """

    http_traffic_bytes: int = 0
    """The HTTP request log."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.disk_usage_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DiskUsage:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.disk_usage_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class SshKey:
    """
    Attributes:
        public_key: The public key, as in authorized_keys: "ssh-ed25519 AAAA..."; never a private key.
        label: Shown in the panel and session logs, e.g. "MacBook Pro".
        fingerprint: "SHA256:...". Ignored on input.
    """

    public_key: str = ""
    """The public key, as in authorized_keys: "ssh-ed25519 AAAA..."; never a private key."""

    label: str = ""
    """Shown in the panel and session logs, e.g. "MacBook Pro"."""

    fingerprint: str = ""
    """"SHA256:...". Ignored on input."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.ssh_key_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SshKey:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.ssh_key_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GithubConnection:
    """The panel's GitHub App, one for every account: projects are created from the repositories of
    the account's own installations of it. Absent = GitHub is not set up on this panel.

    Attributes:
        app_name: As in https://github.com/apps/<app_name>.
        install_url: The panel's page that sends a signed-in person to GitHub to install the app on their
            repositories, or to change which.
        repositories: The repositories of the account's installations, most recently pushed first, at most 200.
        repository_count: In all.
        webhooks_enabled: False = pushes reach the panel only by its check every 5 minutes, not at once.
    """

    app_name: str = ""
    """As in https://github.com/apps/<app_name>."""

    install_url: str = ""
    """The panel's page that sends a signed-in person to GitHub to install the app on their
    repositories, or to change which.
    """

    repositories: Sequence[GithubRepository] = ()
    """The repositories of the account's installations, most recently pushed first, at most 200."""

    repository_count: int = 0
    """In all."""

    webhooks_enabled: bool = False
    """False = pushes reach the panel only by its check every 5 minutes, not at once."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.github_connection_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GithubConnection:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.github_connection_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GithubRepository:
    """
    Attributes:
        repository: "owner/name".
    """

    repository: str = ""
    """"owner/name"."""

    default_branch: str = ""

    private: bool = False

    push_time: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.github_repository_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GithubRepository:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.github_repository_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class DeletedProject:
    """
    Attributes:
        newest_snapshot: Restore it to bring the project back as it was last backed up; get_project then pages the
            older ones (snapshots_before).
        snapshot_count: In all.
    """

    project_id: str = ""

    newest_snapshot: Snapshot | None = None
    """Restore it to bring the project back as it was last backed up; get_project then pages the
    older ones (snapshots_before).
    """

    snapshot_count: int = 0
    """In all."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.deleted_project_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DeletedProject:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.deleted_project_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RestartMachineAction:
    """
    Attributes:
        restart_time: Absent = now, or at_maintenance_window. InvalidArgumentError = in the past.
        at_maintenance_window: True = the next nightly window (Machine.scheduled_restart_time). Not with restart_time.
        interrupt_operations: False = wait for operations and nightly backups to end; true = cut them short.
    """

    restart_time: datetime | None = None
    """Absent = now, or at_maintenance_window. InvalidArgumentError = in the past."""

    at_maintenance_window: bool = False
    """True = the next nightly window (Machine.scheduled_restart_time). Not with restart_time."""

    interrupt_operations: bool = False
    """False = wait for operations and nightly backups to end; true = cut them short."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.restart_machine_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RestartMachineAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.restart_machine_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RunMachineActionResponse:
    """
    Attributes:
        machine: As changed.
    """

    machine: Machine | None = None
    """As changed."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.run_machine_action_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RunMachineActionResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.run_machine_action_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectMetadata:
    """
    Attributes:
        name: Empty = none: people see the id.
        description: One line.
        notes: Free text.
    """

    name: str | None = None
    """Empty = none: people see the id."""

    emoji: str | None = None

    description: str | None = None
    """One line."""

    notes: str | None = None
    """Free text."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_metadata_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectMetadata:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_metadata_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectSummary:
    """
    Attributes:
        problems: Most urgent first. Empty = nothing wrong.
        services: By name.
        url: The first route's host as a URL, e.g. "https://recipes.example.com". Empty = no route.
        hosts: Every host its routes use, in the routes' order.
        http_traffic_last_day: The last day's requests, 5xx responses and latency, as in Project: query_http_traffic says
            which paths. Absent = no request.
        deploy_time: As in Project.
        running_operations: Operations in progress, newest first: a backup can run beside another one.
        pinned: A github project stays on its commit: GithubSource.pinned.
        disk_used_bytes: Its volumes, files, what its containers wrote outside volumes, and its images: one it shares
            with another project counts in both. Measured every few minutes.
    """

    project_id: str = ""

    metadata: ProjectMetadata | None = None

    problems: Sequence[ProjectProblem] = ()
    """Most urgent first. Empty = nothing wrong."""

    services: Sequence[ServiceSummary] = ()
    """By name."""

    url: str = ""
    """The first route's host as a URL, e.g. "https://recipes.example.com". Empty = no route."""

    hosts: Sequence[str] = ()
    """Every host its routes use, in the routes' order."""

    http_traffic_last_day: HttpTrafficSummary | None = None
    """The last day's requests, 5xx responses and latency, as in Project: query_http_traffic says
    which paths. Absent = no request.
    """

    cpu_used_cores: float = 0.0

    memory_used_bytes: int = 0

    deploy_time: datetime | None = None
    """As in Project."""

    running_operations: Sequence[Operation] = ()
    """Operations in progress, newest first: a backup can run beside another one."""

    pinned: bool = False
    """A github project stays on its commit: GithubSource.pinned."""

    disk_used_bytes: int = 0
    """Its volumes, files, what its containers wrote outside volumes, and its images: one it shares
    with another project counts in both. Measured every few minutes.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_summary_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectSummary:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_summary_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ServiceSummary:
    service: str = ""

    state: ServiceState = ServiceState.UNSPECIFIED

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.service_summary_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ServiceSummary:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.service_summary_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectProblem:
    """Something that needs attention. A service has at most one, its cause first.

    Attributes:
        service: Empty = not about one service. DEPLOY_FAILED: the service that failed it, when one did.
        operation_id: DEPLOY_FAILED, DEPLOY_CANCELLED, BACKUP_FAILED, RESTORE_FAILED: the operation; get_operation
            gives its log.
        since_time: DEPLOY_FAILED, DEPLOY_CANCELLED, BACKUP_FAILED, RESTORE_FAILED: the operation's end.
            SERVICE_EXITED, RESTARTING and OUT_OF_MEMORY: when its last run ended, once it did; else its
            last start. AUTO_DEPLOY_REFUSED: when auto-deploy tried the commit. Absent = not known, as
            for UNHEALTHY.
        problem_message: One sentence for people, without a time of day (since_time has it), e.g. "bot fails its
            healthcheck: 11 failures in a row". A failed or cancelled deploy's also says whether it
            changed the project.
    """

    kind: ProjectProblemKind = ProjectProblemKind.UNSPECIFIED

    service: str = ""
    """Empty = not about one service. DEPLOY_FAILED: the service that failed it, when one did."""

    operation_id: str = ""
    """DEPLOY_FAILED, DEPLOY_CANCELLED, BACKUP_FAILED, RESTORE_FAILED: the operation; get_operation
    gives its log.
    """

    since_time: datetime | None = None
    """DEPLOY_FAILED, DEPLOY_CANCELLED, BACKUP_FAILED, RESTORE_FAILED: the operation's end.
    SERVICE_EXITED, RESTARTING and OUT_OF_MEMORY: when its last run ended, once it did; else its
    last start. AUTO_DEPLOY_REFUSED: when auto-deploy tried the commit. Absent = not known, as
    for UNHEALTHY.
    """

    problem_message: str = ""
    """One sentence for people, without a time of day (since_time has it), e.g. "bot fails its
    healthcheck: 11 failures in a row". A failed or cancelled deploy's also says whether it
    changed the project.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_problem_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectProblem:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_problem_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GetProjectResponse:
    project: Project | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.get_project_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GetProjectResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.get_project_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Project:
    """
    Attributes:
        url: As in ProjectSummary.
        deploy_id: The operation_id of the deploy whose files the project has. For a deleted project brought
            back, the RESTORE that did it. Empty = no deploy yet.
        deploy_status: How that operation went, or is going. Unspecified = no deploy yet.
        deploy_time: When the current deploy made its files the project's. Absent = no deploy yet, or one that
            failed or was cancelled leaving no service with a container: nothing runs.
        x_pethost_applies_at_once: True = the current deploy succeeded and every service has a container, so a deploy whose
            files differ only inside `x-pethost` (or not at all) applies at once, with no build, pull or
            restart. False = the next deploy runs in full (see deploy_project).
        services: By name.
        volumes: Every one the machine holds for the project, by name.
        routes: x-pethost.routes as the machine holds them, in order: the list x_pethost.routes replaces, so
            send these back with your change to add, change or remove one.
        hosts: Every host of the routes, in the order of its first route.
        password_protected: True = every route asks visitors for the project's password (`x_pethost.password`). The
            password itself is never returned.
        operations: Newest first, every one the machine keeps: the newest 20, any still in progress, and however
            old, the current deploy's (deploy_id) and those whose files it keeps for a rollback
            (Operation.files_kept). Older ones are gone.
        snapshots: The newest 10, newest first, of those get_project's snapshots_before and
            snapshots_volume select. Empty while backups are off or the list is not read yet
            (snapshot_list_time).
        snapshot_count: The project's, in all; see snapshot_list_time.
        snapshot_list_time: When the machine read the list of snapshots that snapshot_count, Volume.snapshot_count and
            Volume.last_backup_time come from (Machine.snapshot_list_time, as sampled with them).
            Absent = the list is not known: backups are off, or it is not read yet
            (Machine.snapshot_list_failure_message says why); a count of 0 then does not mean none.
        http_traffic_last_day: Measured every few minutes.
        running_services_action: The start_services, stop_services or restart_services that runs now, whoever called it
            (run_project_action waits for its end). Until then the project takes no other action or
            deploy, and Service.state is still what it was before. Absent = none.
    """

    project_id: str = ""

    metadata: ProjectMetadata | None = None

    problems: Sequence[ProjectProblem] = ()

    url: str = ""
    """As in ProjectSummary."""

    cpu_used_cores: float = 0.0

    memory_used_bytes: int = 0

    deploy_id: str = ""
    """The operation_id of the deploy whose files the project has. For a deleted project brought
    back, the RESTORE that did it. Empty = no deploy yet.
    """

    deploy_status: OperationStatus = OperationStatus.UNSPECIFIED
    """How that operation went, or is going. Unspecified = no deploy yet."""

    deploy_time: datetime | None = None
    """When the current deploy made its files the project's. Absent = no deploy yet, or one that
    failed or was cancelled leaving no service with a container: nothing runs.
    """

    x_pethost_applies_at_once: bool = False
    """True = the current deploy succeeded and every service has a container, so a deploy whose
    files differ only inside `x-pethost` (or not at all) applies at once, with no build, pull or
    restart. False = the next deploy runs in full (see deploy_project).
    """

    services: Sequence[Service] = ()
    """By name."""

    volumes: Sequence[Volume] = ()
    """Every one the machine holds for the project, by name."""

    routes: Sequence[Route] = ()
    """x-pethost.routes as the machine holds them, in order: the list x_pethost.routes replaces, so
    send these back with your change to add, change or remove one.
    """

    hosts: Sequence[Host] = ()
    """Every host of the routes, in the order of its first route."""

    password_protected: bool = False
    """True = every route asks visitors for the project's password (`x_pethost.password`). The
    password itself is never returned.
    """

    operations: Sequence[Operation] = ()
    """Newest first, every one the machine keeps: the newest 20, any still in progress, and however
    old, the current deploy's (deploy_id) and those whose files it keeps for a rollback
    (Operation.files_kept). Older ones are gone.
    """

    snapshots: Sequence[Snapshot] = ()
    """The newest 10, newest first, of those get_project's snapshots_before and
    snapshots_volume select. Empty while backups are off or the list is not read yet
    (snapshot_list_time).
    """

    snapshot_count: int = 0
    """The project's, in all; see snapshot_list_time."""

    snapshot_list_time: datetime | None = None
    """When the machine read the list of snapshots that snapshot_count, Volume.snapshot_count and
    Volume.last_backup_time come from (Machine.snapshot_list_time, as sampled with them).
    Absent = the list is not known: backups are off, or it is not read yet
    (Machine.snapshot_list_failure_message says why); a count of 0 then does not mean none.
    """

    http_traffic_last_day: HttpTrafficSummary | None = None
    """Measured every few minutes."""

    source: ProjectSource | None = None

    running_services_action: RunningServicesAction | None = None
    """The start_services, stop_services or restart_services that runs now, whoever called it
    (run_project_action waits for its end). Until then the project takes no other action or
    deploy, and Service.state is still what it was before. Absent = none.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Project:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RunningServicesAction:
    """A start, stop or restart of services that has not ended yet.

    Attributes:
        services: Those it acts on.
    """

    kind: ServicesActionKind = ServicesActionKind.UNSPECIFIED

    services: Sequence[str] = ()
    """Those it acts on."""

    start_time: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.running_services_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RunningServicesAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.running_services_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class ProjectSource:
    """Where the files come from (THE PROJECT IS ITS DIRECTORY).

    At most one of `files`, `github`. The others are None.

    Attributes:
        files: True = the files live on the machine.
    """

    files: bool | None = None
    """True = the files live on the machine."""

    github: GithubSource | None = None

    @overload
    def __init__(
        self,
        *,
        files: None = None,
        github: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        files: bool,
        github: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        files: None = None,
        github: GithubSource,
    ) -> None: ...

    def __init__(
        self,
        *,
        files: bool | None = None,
        github: GithubSource | None = None,
    ) -> None:
        _one_of("ProjectSource", files=files, github=github)
        object.__setattr__(self, "files", files)
        object.__setattr__(self, "github", github)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_source_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectSource:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_source_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GithubSource:
    """Input: an absent field keeps its value (set_source) or takes its default (new source).

    Attributes:
        repository: "owner/name", one of GetMachineResponse.github.repositories.
        branch: Empty = the default branch, also when absent on a new source.
        directory: The project's directory in it, e.g. "apps/web"; empty = the root.
        auto_deploy: True = deploy each new newest_commit, each tried once. Deploying another commit turns it off;
            only set_source turns it on. Default true; always written on output.
        newest_commit: Output: the branch's newest commit touching the directory, as of the last push or 5-minute
            check.
        deployed_commit: Output: the commit the files are at. Absent = no deploy, or the files came from another source.
        pinned: Output: deployed_commit set and auto_deploy off, e.g. after a rollback.
        auto_deploy_pending: Output: true = auto-deploy will deploy newest_commit (not yet tried) once the project is free.
            A tried commit that failed or was refused waits for a person: deploy_project or a new push.
    """

    repository: str | None = None
    """"owner/name", one of GetMachineResponse.github.repositories."""

    branch: str | None = None
    """Empty = the default branch, also when absent on a new source."""

    directory: str | None = None
    """The project's directory in it, e.g. "apps/web"; empty = the root."""

    auto_deploy: bool | None = None
    """True = deploy each new newest_commit, each tried once. Deploying another commit turns it off;
    only set_source turns it on. Default true; always written on output.
    """

    newest_commit: GithubCommit | None = None
    """Output: the branch's newest commit touching the directory, as of the last push or 5-minute
    check.
    """

    deployed_commit: GithubCommit | None = None
    """Output: the commit the files are at. Absent = no deploy, or the files came from another source."""

    pinned: bool = False
    """Output: deployed_commit set and auto_deploy off, e.g. after a rollback."""

    auto_deploy_pending: bool = False
    """Output: true = auto-deploy will deploy newest_commit (not yet tried) once the project is free.
    A tried commit that failed or was refused waits for a person: deploy_project or a new push.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.github_source_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GithubSource:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.github_source_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GithubCommit:
    """
    Attributes:
        sha: Full.
        title: First line of its message. Untrusted.
        url: On github.com.
    """

    sha: str = ""
    """Full."""

    title: str = ""
    """First line of its message. Untrusted."""

    url: str = ""
    """On github.com."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.github_commit_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GithubCommit:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.github_commit_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Service:
    """
    Attributes:
        container_running: True = its container runs, as run_service_command, OpenTerminal and read_path of its own files
            (outside volumes) need: in RUNNING, HEALTHY and UNHEALTHY, and in STARTING once its process
            started.
        image: The image as compose.yaml names it; for `build:` without `image:`, the name Compose gives.
        builds_image: Built on the machine from a `build:` section.
        image_digest: The registry digest it was pulled as, "sha256:...". Empty for a built image.
        image_size_bytes: Absent until the machine next measures sizes, every few minutes, as after a build or pull.
        command: What the main process runs, as compose.yaml writes it (entrypoint, then command), `${...}`
            not interpolated, so that no value of an env file shows; the image's own argv when
            compose.yaml writes neither. Empty = not known without those values: compose.yaml loads only
            interpolated, e.g. with an `include` path from .env.
        start_time: Of the current or last run.
        finish_time: Set once it exited, and while Docker waits to restart it: when, with what code (0 = a clean
            exit: a job that finished, or a server stopped; 137 = killed), and whether a process of it was
            killed for exceeding its memory.
        restart_count: Restarts by Docker since the container was created.
        memory_limit_bytes: 0 = no limit: it shares the machine.
        cpu_limit_cores: 0 = no limit.
        writable_layer_bytes: Written outside volumes: lost on a recreate.
        ports: The ports it is reached at, as far as the machine knows: those compose.yaml or its image
            declares and those its routes send to. The project's other services reach it at
            `<service>:<port>`.
        listening_ports: The TCP ports its processes listen on now, at an address the proxy and the other services
            reach: a route's port must be one of them. Empty = it does not run, or listens on none.
        health_check: Absent = no healthcheck.
        environment: What the container is configured with, not what its image sets.
        env_files: The files its `env_file:` names, as compose.yaml writes them, e.g. "./.env": relative to the
            project directory. Change them with deploy_project(files=).
        ssh_command: What the person runs in their own terminal for a shell in its container, e.g.
            "ssh web.notes@m1.pethost.dev"; scp, sftp, rsync and `ssh -L` tunnels take the same address.
            It works once one of their public keys is among Machine.ssh_keys.
    """

    service: str = ""

    state: ServiceState = ServiceState.UNSPECIFIED

    container_running: bool = False
    """True = its container runs, as run_service_command, OpenTerminal and read_path of its own files
    (outside volumes) need: in RUNNING, HEALTHY and UNHEALTHY, and in STARTING once its process
    started.
    """

    image: str = ""
    """The image as compose.yaml names it; for `build:` without `image:`, the name Compose gives."""

    builds_image: bool = False
    """Built on the machine from a `build:` section."""

    image_digest: str = ""
    """The registry digest it was pulled as, "sha256:...". Empty for a built image."""

    image_size_bytes: int = 0
    """Absent until the machine next measures sizes, every few minutes, as after a build or pull."""

    command: Sequence[str] = ()
    """What the main process runs, as compose.yaml writes it (entrypoint, then command), `${...}`
    not interpolated, so that no value of an env file shows; the image's own argv when
    compose.yaml writes neither. Empty = not known without those values: compose.yaml loads only
    interpolated, e.g. with an `include` path from .env.
    """

    run_as_user: str = ""

    start_time: datetime | None = None
    """Of the current or last run."""

    finish_time: datetime | None = None
    """Set once it exited, and while Docker waits to restart it: when, with what code (0 = a clean
    exit: a job that finished, or a server stopped; 137 = killed), and whether a process of it was
    killed for exceeding its memory.
    """

    exit_code: int | None = None

    out_of_memory: bool = False

    restart_count: int = 0
    """Restarts by Docker since the container was created."""

    cpu_used_cores: float = 0.0

    memory_used_bytes: int = 0

    memory_limit_bytes: int = 0
    """0 = no limit: it shares the machine."""

    cpu_limit_cores: float = 0.0
    """0 = no limit."""

    writable_layer_bytes: int = 0
    """Written outside volumes: lost on a recreate."""

    ports: Sequence[int] = ()
    """The ports it is reached at, as far as the machine knows: those compose.yaml or its image
    declares and those its routes send to. The project's other services reach it at
    `<service>:<port>`.
    """

    listening_ports: Sequence[int] = ()
    """The TCP ports its processes listen on now, at an address the proxy and the other services
    reach: a route's port must be one of them. Empty = it does not run, or listens on none.
    """

    published_ports: Sequence[PublishedPort] = ()

    volume_mounts: Sequence[VolumeMount] = ()

    restart_policy: RestartPolicy = RestartPolicy.UNSPECIFIED

    health_check: HealthCheck | None = None
    """Absent = no healthcheck."""

    environment: Sequence[EnvironmentVariable] = ()
    """What the container is configured with, not what its image sets."""

    env_files: Sequence[str] = ()
    """The files its `env_file:` names, as compose.yaml writes them, e.g. "./.env": relative to the
    project directory. Change them with deploy_project(files=).
    """

    ssh_command: str = ""
    """What the person runs in their own terminal for a shell in its container, e.g.
    "ssh web.notes@m1.pethost.dev"; scp, sftp, rsync and `ssh -L` tunnels take the same address.
    It works once one of their public keys is among Machine.ssh_keys.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.service_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Service:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.service_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PublishedPort:
    """A port that `ports:` opens on the machine directly, bypassing the proxy.

    Attributes:
        machine_port: 0 = Docker picks one when the container starts.
        protocol: "tcp", "udp" or "sctp".
        machine_only: True = bound to 127.0.0.1: reachable only through an SSH tunnel.
    """

    machine_port: int = 0
    """0 = Docker picks one when the container starts."""

    container_port: int = 0

    protocol: str = ""
    """"tcp", "udp" or "sctp"."""

    machine_only: bool = False
    """True = bound to 127.0.0.1: reachable only through an SSH tunnel."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.published_port_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PublishedPort:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.published_port_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class VolumeMount:
    """
    Attributes:
        container_path: E.g. "/var/lib/postgresql/data".
    """

    volume: str = ""

    container_path: str = ""
    """E.g. "/var/lib/postgresql/data"."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.volume_mount_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> VolumeMount:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.volume_mount_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HealthCheck:
    """The healthcheck Docker runs: compose.yaml's, else the image's HEALTHCHECK.

    Attributes:
        command: The program and its arguments, e.g. ["curl", "-f", "http://localhost:8000/health"]; a test
            written as a shell line is ["/bin/sh", "-c", <line>]. Written and known as Service.command
            is: compose.yaml's `healthcheck.test`, else the image's.
        interval_seconds: How often Docker runs it.
        status: Absent while the service is not running.
        recent_results_passed: Up to the last 5 checks, oldest first.
        last_failure_output: Of the latest failed check, at most 4 KiB. Untrusted.
    """

    command: Sequence[str] = ()
    """The program and its arguments, e.g. ["curl", "-f", "http://localhost:8000/health"]; a test
    written as a shell line is ["/bin/sh", "-c", <line>]. Written and known as Service.command
    is: compose.yaml's `healthcheck.test`, else the image's.
    """

    interval_seconds: int = 0
    """How often Docker runs it."""

    status: HealthStatus = HealthStatus.UNSPECIFIED
    """Absent while the service is not running."""

    consecutive_failure_count: int = 0

    recent_results_passed: Sequence[bool] = ()
    """Up to the last 5 checks, oldest first."""

    last_failure_output: str = ""
    """Of the latest failed check, at most 4 KiB. Untrusted."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.health_check_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HealthCheck:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.health_check_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class EnvironmentVariable:
    """
    Attributes:
        value: Absent when empty, when `secret` and get_project had no include_secret_values, or when
            value_left_out.
        secret: True = its value is not empty and comes from an env file, directly or through `${...}` in
            compose.yaml: env files hold the secrets. Empty values, and values written in compose.yaml
            itself, are not secret. The machine hides these values in operation logs too.
        source_file: The file to edit to change it, absolute in the project's directory: "/compose.yaml" (the
            service's `environment:`, which wins) or the env file it comes from, e.g. "/.env",
            "/web.env". Empty = the machine cannot tell, as when compose.yaml takes that file's path
            from .env.
        from_env_file_variables: When compose.yaml builds it from `${...}`: the .env variables to edit to change it.
        value_left_out: True = the value is left out: the project's values together hold more than about 64 KiB.
            Read source_file with read_path.
    """

    name: str = ""

    value: str = ""
    """Absent when empty, when `secret` and get_project had no include_secret_values, or when
    value_left_out.
    """

    secret: bool = False
    """True = its value is not empty and comes from an env file, directly or through `${...}` in
    compose.yaml: env files hold the secrets. Empty values, and values written in compose.yaml
    itself, are not secret. The machine hides these values in operation logs too.
    """

    source_file: str = ""
    """The file to edit to change it, absolute in the project's directory: "/compose.yaml" (the
    service's `environment:`, which wins) or the env file it comes from, e.g. "/.env",
    "/web.env". Empty = the machine cannot tell, as when compose.yaml takes that file's path
    from .env.
    """

    from_env_file_variables: Sequence[str] = ()
    """When compose.yaml builds it from `${...}`: the .env variables to edit to change it."""

    value_left_out: bool = False
    """True = the value is left out: the project's values together hold more than about 64 KiB.
    Read source_file with read_path.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.environment_variable_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EnvironmentVariable:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.environment_variable_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Volume:
    """
    Attributes:
        size_bytes: Measured every few minutes.
        last_backup_time: Of the newest snapshot that holds this volume. Absent = no snapshot holds it, or the list is
            not known (Project.snapshot_list_time).
        snapshot_count: The snapshots that hold it, in all; get_project(snapshots_volume=) lists them. See
            Project.snapshot_list_time.
        declared: False, always written = compose.yaml no longer declares it, so no service mounts it: it
            keeps its data and is in every backup until run_project_action(delete_volume=) or the project is
            deleted. read_path
            reads it with the volume root, restore_snapshot restores it, and declaring it again mounts it
            as it is.
    """

    volume: str = ""

    size_bytes: int = 0
    """Measured every few minutes."""

    mounted_by: Sequence[VolumeMountedBy] = ()

    last_backup_time: datetime | None = None
    """Of the newest snapshot that holds this volume. Absent = no snapshot holds it, or the list is
    not known (Project.snapshot_list_time).
    """

    snapshot_count: int = 0
    """The snapshots that hold it, in all; get_project(snapshots_volume=) lists them. See
    Project.snapshot_list_time.
    """

    declared: bool = False
    """False, always written = compose.yaml no longer declares it, so no service mounts it: it
    keeps its data and is in every backup until run_project_action(delete_volume=) or the project is
    deleted. read_path
    reads it with the volume root, restore_snapshot restores it, and declaring it again mounts it
    as it is.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.volume_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Volume:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.volume_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class VolumeMountedBy:
    service: str = ""

    container_path: str = ""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.volume_mounted_by_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> VolumeMountedBy:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.volume_mounted_by_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Host:
    """A host of Project.routes, with its certificate.

    Attributes:
        host: As x-pethost.routes[].host.
        url: "https://<host>" once its certificate is served, and plain HTTP is redirected there; until
            then "http://<host>", which reaches the services. For AUTOMATIC, the host must resolve to
            the machine first. A protected project (Project.password_protected) is never served over
            plain HTTP: it is always redirected, so the host answers only once its certificate is served.
        certificate_expire_time: When the certificate served expires. Absent = none is served yet.
        unavailable_message: Why the host answers nobody: a name under the panel's domain that is not one label under
            Machine.apps_domain (another account's, a former apps_domain of this one, or two labels
            deep). Change its host. Empty = it answers, or it is the person's own domain.
    """

    host: str = ""
    """As x-pethost.routes[].host."""

    url: str = ""
    """"https://<host>" once its certificate is served, and plain HTTP is redirected there; until
    then "http://<host>", which reaches the services. For AUTOMATIC, the host must resolve to
    the machine first. A protected project (Project.password_protected) is never served over
    plain HTTP: it is always redirected, so the host answers only once its certificate is served.
    """

    certificate_source: CertificateSource = CertificateSource.UNSPECIFIED

    certificate_expire_time: datetime | None = None
    """When the certificate served expires. Absent = none is served yet."""

    unavailable_message: str = ""
    """Why the host answers nobody: a name under the panel's domain that is not one label under
    Machine.apps_domain (another account's, a former apps_domain of this one, or two labels
    deep). Change its host. Empty = it answers, or it is the person's own domain.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.host_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Host:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.host_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Route:
    """An x-pethost route: requests for `host` under `path` go to `port` of `service`. The field
    names are the YAML keys.

    Attributes:
        host: `<name>.<Machine.apps_domain>`, the person's domain on Pethost: HTTPS at once, nothing to set
            up. Or a domain they own: a CNAME to Machine.hostname (an ALIAS at the apex, never an IP
            address), certified once it resolves.
        path: Whole segments, the longest wins. Empty = "/": every path.
        port: The port the service listens on in its container, at 0.0.0.0.
        strip_path: True = the path's prefix is removed from the request.
    """

    host: str = ""
    """`<name>.<Machine.apps_domain>`, the person's domain on Pethost: HTTPS at once, nothing to set
    up. Or a domain they own: a CNAME to Machine.hostname (an ALIAS at the apex, never an IP
    address), certified once it resolves.
    """

    path: str = ""
    """Whole segments, the longest wins. Empty = "/": every path."""

    service: str = ""

    port: int = 0
    """The port the service listens on in its container, at 0.0.0.0."""

    strip_path: bool = False
    """True = the path's prefix is removed from the request."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.route_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Route:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.route_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Operation:
    """
    Attributes:
        finish_time: Absent while in progress.
        failure_message: When FAILED: why, for people. The log says more.
        deploy_failure_reason: DEPLOY or RECREATE_SERVICE that FAILED: why, to branch on.
        made_current: DEPLOY, or a RESTORE that brought a deleted project back: true = it made its files the
            project's. It stays true once a later deploy replaces them: Project.deploy_id names the one
            whose files the project has now. A deploy switches the files partway, when it starts the
            containers, so one that FAILED or was CANCELLED without it left the files as they were: to
            retry, send all its changes again. A project's first deploy has it from its start: its files
            stay however it ends, to fix and deploy again.
        service: RECREATE_SERVICE: the service. A failed DEPLOY or RECREATE_SERVICE: the service that failed.
        failed_exit_code: DEPLOY or RECREATE_SERVICE that failed CONTAINER_EXITED.
        snapshot_id: BACKUP, or DELETE's final backup, that succeeded: the snapshot taken. RESTORE: the snapshot
            restored.
        restored_volumes: RESTORE: the volumes it replaced.
        undo_snapshot_id: RESTORE: the backup taken first; restore it to undo. Empty = none was taken.
        github_commit: DEPLOY of a github project: the commit its files are, also when it changed only /.env or
            x-pethost.
        archive_name: DEPLOY of an uploaded archive: its file name.
        adjustments: DEPLOY: what making that version changed that its request did not write, for people: the
            earlier deploy whose files it took, the compose file it took or wrote for a Dockerfile, the
            compose files it left out, the project's /.env and x-pethost kept in place of the version's
            own. Nothing else in the compose file is changed: it runs as written.
        changed_paths: DEPLOY: the paths its request changed, for people, the first 10: deploy_project(files=), or
            create_project's files; a move lists both paths. A commit's or an
            archive's own files are not listed: github_commit or archive_name says what they brought.
        changed_path_count: DEPLOY: the paths its request changed, in all.
        files_kept: DEPLOY: true = the machine keeps the files it deployed, which are no longer the project's:
            deploy_project(rollback_deploy_id=) puts them back. It keeps the 3 newest versions of the files
            before the current one; of deploys that changed only /.env or x-pethost, whose files are the
            same, the newest has it.
    """

    operation_id: str = ""

    kind: OperationKind = OperationKind.UNSPECIFIED

    status: OperationStatus = OperationStatus.UNSPECIFIED

    start_time: datetime | None = None

    finish_time: datetime | None = None
    """Absent while in progress."""

    failure_message: str = ""
    """When FAILED: why, for people. The log says more."""

    deploy_failure_reason: DeployFailureReason = DeployFailureReason.UNSPECIFIED
    """DEPLOY or RECREATE_SERVICE that FAILED: why, to branch on."""

    made_current: bool = False
    """DEPLOY, or a RESTORE that brought a deleted project back: true = it made its files the
    project's. It stays true once a later deploy replaces them: Project.deploy_id names the one
    whose files the project has now. A deploy switches the files partway, when it starts the
    containers, so one that FAILED or was CANCELLED without it left the files as they were: to
    retry, send all its changes again. A project's first deploy has it from its start: its files
    stay however it ends, to fix and deploy again.
    """

    service: str = ""
    """RECREATE_SERVICE: the service. A failed DEPLOY or RECREATE_SERVICE: the service that failed."""

    failed_exit_code: int = 0
    """DEPLOY or RECREATE_SERVICE that failed CONTAINER_EXITED."""

    snapshot_id: str = ""
    """BACKUP, or DELETE's final backup, that succeeded: the snapshot taken. RESTORE: the snapshot
    restored.
    """

    restored_volumes: Sequence[str] = ()
    """RESTORE: the volumes it replaced."""

    undo_snapshot_id: str = ""
    """RESTORE: the backup taken first; restore it to undo. Empty = none was taken."""

    github_commit: GithubCommit | None = None
    """DEPLOY of a github project: the commit its files are, also when it changed only /.env or
    x-pethost.
    """

    archive_name: str = ""
    """DEPLOY of an uploaded archive: its file name."""

    adjustments: Sequence[str] = ()
    """DEPLOY: what making that version changed that its request did not write, for people: the
    earlier deploy whose files it took, the compose file it took or wrote for a Dockerfile, the
    compose files it left out, the project's /.env and x-pethost kept in place of the version's
    own. Nothing else in the compose file is changed: it runs as written.
    """

    changed_paths: Sequence[str] = ()
    """DEPLOY: the paths its request changed, for people, the first 10: deploy_project(files=), or
    create_project's files; a move lists both paths. A commit's or an
    archive's own files are not listed: github_commit or archive_name says what they brought.
    """

    changed_path_count: int = 0
    """DEPLOY: the paths its request changed, in all."""

    files_kept: bool = False
    """DEPLOY: true = the machine keeps the files it deployed, which are no longer the project's:
    deploy_project(rollback_deploy_id=) puts them back. It keeps the 3 newest versions of the files
    before the current one; of deploys that changed only /.env or x-pethost, whose files are the
    same, the newest has it.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.operation_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Operation:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.operation_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Snapshot:
    """
    Attributes:
        size_bytes: Of its files, the directory and every volume. 0 = not known.
        volumes: The volumes it holds, besides the project's directory.
    """

    snapshot_id: str = ""

    create_time: datetime | None = None

    size_bytes: int = 0
    """Of its files, the directory and every volume. 0 = not known."""

    volumes: Sequence[str] = ()
    """The volumes it holds, besides the project's directory."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.snapshot_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Snapshot:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.snapshot_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HttpTrafficSummary:
    """
    Attributes:
        server_error_count: 5xx responses.
        latency_p50_ms: Of responses: WebSockets, logged when they close, count as requests but not here.
    """

    request_count: int = 0

    server_error_count: int = 0
    """5xx responses."""

    latency_p50_ms: int = 0
    """Of responses: WebSockets, logged when they close, count as requests but not here."""

    latency_p95_ms: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.http_traffic_summary_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HttpTrafficSummary:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.http_traffic_summary_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CreateProjectResponse:
    """
    Attributes:
        operation: The first deploy: finished, or IN_PROGRESS when wait_seconds ran out (then get_operation).
            Absent when violations stopped it: nothing was created.
        adjustments: With violations: what the machine had changed, as in Operation.adjustments. A deploy that
            started lists them in operation.adjustments only.
        project: Once the operation ended, however it did: the project as get_project returns it.
        log: The log's last lines, unless it SUCCEEDED: why it FAILED, or what it is doing.
    """

    operation: Operation | None = None
    """The first deploy: finished, or IN_PROGRESS when wait_seconds ran out (then get_operation).
    Absent when violations stopped it: nothing was created.
    """

    violations: Sequence[SpecViolation] = ()

    adjustments: Sequence[str] = ()
    """With violations: what the machine had changed, as in Operation.adjustments. A deploy that
    started lists them in operation.adjustments only.
    """

    project: Project | None = None
    """Once the operation ended, however it did: the project as get_project returns it."""

    log: Sequence[OperationLogLine] = ()
    """The log's last lines, unless it SUCCEEDED: why it FAILED, or what it is doing."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.create_project_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CreateProjectResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.create_project_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MountVolume:
    """Adds `<volume>:<container_path>` to the service, declaring the volume if needed.

    Attributes:
        service: A service of compose.yaml.
        volume: New, or one of Project.volumes.
        container_path: Absolute, e.g. "/data".
    """

    service: str = ""
    """A service of compose.yaml."""

    volume: str = ""
    """New, or one of Project.volumes."""

    container_path: str = ""
    """Absolute, e.g. "/data"."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.mount_volume_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MountVolume:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.mount_volume_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectExtension:
    """x-pethost as data. Absent parts stay.

    Attributes:
        metadata: Sets the fields given; an empty one is removed.
        routes: The project's routes from now on: these replace all it has, so send Project.routes with your
            change to add, change or remove one. Empty = they stay.
        remove_routes: True = the project has no route from now on. Not with routes.
        password: Visitors of every route must enter it. Empty = it stays.
        remove_password: True = no password. Not with password.
    """

    metadata: ProjectMetadata | None = None
    """Sets the fields given; an empty one is removed."""

    routes: Sequence[Route] = ()
    """The project's routes from now on: these replace all it has, so send Project.routes with your
    change to add, change or remove one. Empty = they stay.
    """

    remove_routes: bool = False
    """True = the project has no route from now on. Not with routes."""

    password: str = ""
    """Visitors of every route must enter it. Empty = it stays."""

    remove_password: bool = False
    """True = no password. Not with password."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_extension_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectExtension:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_extension_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class FileChange:
    """`path` and exactly one change.

    At most one of `text`, `data`, `make_directory`, `delete`, `delete_tree`, `rename_to`. The others are None.

    Attributes:
        path: Absolute in the project's directory.
        text: Writes the file as UTF-8 text, creating parents.
        data: Writes the file as bytes, likewise.
        make_directory: True = creates it and its parents.
        delete: True = deletes the file, symlink or empty directory.
        delete_tree: True = deletes a directory recursively, if present.
        rename_to: Moves it to this path.
        executable: With text or data: mode 0755, not 0644.
    """

    path: str = ""
    """Absolute in the project's directory."""

    text: str | None = None
    """Writes the file as UTF-8 text, creating parents."""

    data: bytes | None = None
    """Writes the file as bytes, likewise."""

    make_directory: bool | None = None
    """True = creates it and its parents."""

    delete: bool | None = None
    """True = deletes the file, symlink or empty directory."""

    delete_tree: bool | None = None
    """True = deletes a directory recursively, if present."""

    rename_to: str | None = None
    """Moves it to this path."""

    executable: bool = False
    """With text or data: mode 0755, not 0644."""

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        make_directory: None = None,
        delete: None = None,
        delete_tree: None = None,
        rename_to: None = None,
        executable: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: str,
        data: None = None,
        make_directory: None = None,
        delete: None = None,
        delete_tree: None = None,
        rename_to: None = None,
        executable: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: bytes,
        make_directory: None = None,
        delete: None = None,
        delete_tree: None = None,
        rename_to: None = None,
        executable: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        make_directory: bool,
        delete: None = None,
        delete_tree: None = None,
        rename_to: None = None,
        executable: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        make_directory: None = None,
        delete: bool,
        delete_tree: None = None,
        rename_to: None = None,
        executable: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        make_directory: None = None,
        delete: None = None,
        delete_tree: bool,
        rename_to: None = None,
        executable: bool = False,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        make_directory: None = None,
        delete: None = None,
        delete_tree: None = None,
        rename_to: str,
        executable: bool = False,
    ) -> None: ...

    def __init__(
        self,
        *,
        path: str = "",
        text: str | None = None,
        data: bytes | None = None,
        make_directory: bool | None = None,
        delete: bool | None = None,
        delete_tree: bool | None = None,
        rename_to: str | None = None,
        executable: bool = False,
    ) -> None:
        _one_of("FileChange", text=text, data=data, make_directory=make_directory, delete=delete, delete_tree=delete_tree, rename_to=rename_to)
        object.__setattr__(self, "path", path)
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "data", data)
        object.__setattr__(self, "make_directory", make_directory)
        object.__setattr__(self, "delete", delete)
        object.__setattr__(self, "delete_tree", delete_tree)
        object.__setattr__(self, "rename_to", rename_to)
        object.__setattr__(self, "executable", executable)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.file_change_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FileChange:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.file_change_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class DeployProjectResponse:
    """
    Attributes:
        operation: The deploy: finished, or IN_PROGRESS when wait_seconds ran out (then get_operation). Absent
            when violations stopped it.
        violations: Why the files cannot be deployed: nothing changed and no operation started.
        adjustments: As in CreateProjectResponse: with violations only.
        project: Once the operation ended, however it did: the project as get_project returns it.
        log: The log's last lines, unless it SUCCEEDED: why it FAILED, or what it is doing.
    """

    operation: Operation | None = None
    """The deploy: finished, or IN_PROGRESS when wait_seconds ran out (then get_operation). Absent
    when violations stopped it.
    """

    violations: Sequence[SpecViolation] = ()
    """Why the files cannot be deployed: nothing changed and no operation started."""

    adjustments: Sequence[str] = ()
    """As in CreateProjectResponse: with violations only."""

    project: Project | None = None
    """Once the operation ended, however it did: the project as get_project returns it."""

    log: Sequence[OperationLogLine] = ()
    """The log's last lines, unless it SUCCEEDED: why it FAILED, or what it is doing."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.deploy_project_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DeployProjectResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.deploy_project_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class SpecViolation:
    """
    Attributes:
        service: Empty = not about one service.
        location: In compose.yaml, down to the key it is about, e.g. "services.db.volumes[0]",
            "x-pethost.routes[2].host"; or a file's absolute path, e.g. "/.env".
        violation_message: What is wrong and what to write instead.
    """

    service: str = ""
    """Empty = not about one service."""

    location: str = ""
    """In compose.yaml, down to the key it is about, e.g. "services.db.volumes[0]",
    "x-pethost.routes[2].host"; or a file's absolute path, e.g. "/.env".
    """

    violation_message: str = ""
    """What is wrong and what to write instead."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.spec_violation_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SpecViolation:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.spec_violation_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListCommitsResponse:
    """
    Attributes:
        commits: Newest first, at most 30.
        more: Older ones exist: pass the last one's sha as before_commit.
    """

    commits: Sequence[BranchCommit] = ()
    """Newest first, at most 30."""

    more: bool = False
    """Older ones exist: pass the last one's sha as before_commit."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_commits_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListCommitsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_commits_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class BranchCommit:
    """
    Attributes:
        author: The author's GitHub login, else their name. Untrusted.
        commit_time: When it was committed.
        deployed: The project's files are this commit (GithubSource.deployed_commit).
        last_deploy: The newest deploy of it among the operations the machine keeps; its status says how it went.
            Absent = none.
        newest: True = the branch's newest commit that changes the directory, as GitHub answered this call:
            deploying any other turns auto_deploy off (see deploy_project).
    """

    commit: GithubCommit | None = None

    author: str = ""
    """The author's GitHub login, else their name. Untrusted."""

    commit_time: datetime | None = None
    """When it was committed."""

    deployed: bool = False
    """The project's files are this commit (GithubSource.deployed_commit)."""

    last_deploy: Operation | None = None
    """The newest deploy of it among the operations the machine keeps; its status says how it went.
    Absent = none.
    """

    newest: bool = False
    """True = the branch's newest commit that changes the directory, as GitHub answered this call:
    deploying any other turns auto_deploy off (see deploy_project).
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.branch_commit_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BranchCommit:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.branch_commit_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ServicesAction:
    """
    Attributes:
        services: Empty = all (start: those with a container; restart: running ones).
    """

    services: Sequence[str] = ()
    """Empty = all (start: those with a container; restart: running ones)."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.services_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ServicesAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.services_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RecreateServiceAction:
    """
    Attributes:
        pull_latest_image: True = pull the tag's newest image, or rebuild on the newest base images.
    """

    service: str = ""

    pull_latest_image: bool = False
    """True = pull the tag's newest image, or rebuild on the newest base images."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.recreate_service_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RecreateServiceAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.recreate_service_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class BackUpAction:
    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.back_up_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BackUpAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.back_up_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RestoreSnapshotAction:
    """
    Attributes:
        volumes: Existing project: the volumes to replace (≥1); it is backed up first
            (Operation.undo_snapshot_id), stopped and restarted; files stay. Deleted project: files, source
            and volumes return, then it deploys.
    """

    snapshot_id: str = ""

    volumes: Sequence[str] = ()
    """Existing project: the volumes to replace (≥1); it is backed up first
    (Operation.undo_snapshot_id), stopped and restarted; files stay. Deleted project: files, source
    and volumes return, then it deploys.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.restore_snapshot_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RestoreSnapshotAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.restore_snapshot_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CancelOperationAction:
    """
    Attributes:
        operation_id: Required.
    """

    operation_id: str = ""
    """Required."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.cancel_operation_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CancelOperationAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.cancel_operation_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class DeleteProjectAction:
    """
    Attributes:
        skip_final_backup: True = no final backup, while backups are on: changes since the newest snapshot are lost.
    """

    skip_final_backup: bool = False
    """True = no final backup, while backups are on: changes since the newest snapshot are lost."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.delete_project_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DeleteProjectAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.delete_project_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RunProjectActionResponse:
    """
    Attributes:
        operation: Set when the action runs as an operation: finished, or IN_PROGRESS when wait_seconds ran out
            (then get_operation); for set_source, the deploy it started, if any; for cancel_operation,
            the operation it stopped, if the machine had recorded it (see cancel_operation).
        project: The project as get_project returns it, after the action, or once its operation ended: after
            set_source, its source says what it now is. Absent while the operation runs, and once
            delete_project has deleted it.
        log: The operation's last log lines, unless it SUCCEEDED.
    """

    operation: Operation | None = None
    """Set when the action runs as an operation: finished, or IN_PROGRESS when wait_seconds ran out
    (then get_operation); for set_source, the deploy it started, if any; for cancel_operation,
    the operation it stopped, if the machine had recorded it (see cancel_operation).
    """

    project: Project | None = None
    """The project as get_project returns it, after the action, or once its operation ended: after
    set_source, its source says what it now is. Absent while the operation runs, and once
    delete_project has deleted it.
    """

    log: Sequence[OperationLogLine] = ()
    """The operation's last log lines, unless it SUCCEEDED."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.run_project_action_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RunProjectActionResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.run_project_action_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GetOperationResponse:
    """
    Attributes:
        project: Once it ended, however it did: the project as get_project returns it. Absent once a delete
            has deleted it.
        log: Oldest first. Unless after_log_line or log_line_limit asks for lines: the last 50 of one that
            FAILED, the last 5 of one IN_PROGRESS (what it is doing), none of one that SUCCEEDED.
        log_line_count: Lines in the whole log so far.
        next_after_log_line: Pass it as after_log_line to get the lines after these; absent = 0. The machine keeps every
            line of the log.
    """

    operation: Operation | None = None

    project: Project | None = None
    """Once it ended, however it did: the project as get_project returns it. Absent once a delete
    has deleted it.
    """

    log: Sequence[OperationLogLine] = ()
    """Oldest first. Unless after_log_line or log_line_limit asks for lines: the last 50 of one that
    FAILED, the last 5 of one IN_PROGRESS (what it is doing), none of one that SUCCEEDED.
    """

    log_line_count: int = 0
    """Lines in the whole log so far."""

    next_after_log_line: int = 0
    """Pass it as after_log_line to get the lines after these; absent = 0. The machine keeps every
    line of the log.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.get_operation_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GetOperationResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.get_operation_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class OperationLogLine:
    """
    Attributes:
        text: From Compose, BuildKit, restic or the daemon, as LogLine.text is kept; at most 2 KiB, a
            longer line is cut.
    """

    time: datetime | None = None

    text: str = ""
    """From Compose, BuildKit, restic or the daemon, as LogLine.text is kept; at most 2 KiB, a
    longer line is cut.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.operation_log_line_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> OperationLogLine:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.operation_log_line_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HttpTrafficFilter:
    """
    Attributes:
        host: As Host.host; a removed host still matches.
        method: E.g. "GET".
        path_contains: Without the query; any case.
        path_pattern: As HttpPathTraffic.path_pattern, e.g. "/recipes/*".
        status_class: 1-5: 5 = 5xx.
    """

    host: str = ""
    """As Host.host; a removed host still matches."""

    method: str = ""
    """E.g. "GET"."""

    path_contains: str = ""
    """Without the query; any case."""

    path_pattern: str = ""
    """As HttpPathTraffic.path_pattern, e.g. "/recipes/*"."""

    status_class: int = 0
    """1-5: 5 = 5xx."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.http_traffic_filter_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HttpTrafficFilter:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.http_traffic_filter_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class QueryHttpTrafficResponse:
    """
    Attributes:
        start_time: The range queried, as the machine resolved it: defaults applied, on its clock.
        oldest_kept_time: Of the oldest request the machine keeps for the project. Absent = none is kept.
        buckets: Oldest first, each bucket_width_seconds wide; one with no request is left out.
        top_paths: The 10 busiest, busiest first.
        newest_sequence: The sequence of the newest request the machine had logged: summary, buckets and top_paths
            count every one up to it, and tail_http_traffic streams the later ones. 0 = none was logged.
        next_page_token: Empty = no more requests.
        tail_sequence: Where tail_http_traffic goes on from (after_sequence), so it misses no request newer than
            these: set on a first page with request_limit, empty or not. 0 = the machine had logged
            none.
    """

    start_time: datetime | None = None
    """The range queried, as the machine resolved it: defaults applied, on its clock."""

    end_time: datetime | None = None

    oldest_kept_time: datetime | None = None
    """Of the oldest request the machine keeps for the project. Absent = none is kept."""

    summary: HttpTrafficSummary | None = None

    buckets: Sequence[HttpTrafficBucket] = ()
    """Oldest first, each bucket_width_seconds wide; one with no request is left out."""

    top_paths: Sequence[HttpPathTraffic] = ()
    """The 10 busiest, busiest first."""

    newest_sequence: int = 0
    """The sequence of the newest request the machine had logged: summary, buckets and top_paths
    count every one up to it, and tail_http_traffic streams the later ones. 0 = none was logged.
    """

    requests: Sequence[HttpRequest] = ()

    next_page_token: str = ""
    """Empty = no more requests."""

    tail_sequence: int = 0
    """Where tail_http_traffic goes on from (after_sequence), so it misses no request newer than
    these: set on a first page with request_limit, empty or not. 0 = the machine had logged
    none.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.query_http_traffic_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> QueryHttpTrafficResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.query_http_traffic_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HttpTrafficBucket:
    start_time: datetime | None = None

    summary: HttpTrafficSummary | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.http_traffic_bucket_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HttpTrafficBucket:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.http_traffic_bucket_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HttpPathTraffic:
    """
    Attributes:
        path_pattern: The path with id-like segments as `*`, e.g. "/recipes/*": requests to one endpoint.
    """

    method: str = ""

    path_pattern: str = ""
    """The path with id-like segments as `*`, e.g. "/recipes/*": requests to one endpoint."""

    summary: HttpTrafficSummary | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.http_path_traffic_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HttpPathTraffic:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.http_path_traffic_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HttpRequest:
    """
    Attributes:
        sequence: Unique and increasing on the machine: tail_http_traffic's cursor.
        finish_time: When the response finished. A WebSocket is logged when it closes, with status 0.
        path: With the query. Untrusted.
        route_path: The route that matched.
        service: That answered. Empty = of a route the project no longer has.
        status_code: 0 = a WebSocket; 499 = the client left before the response. A 401, 303 or 429 of a protected
            project (Project.password_protected) may be its password page's, not the service's.
        duration_ms: In total.
        service_duration_ms: Of which inside the service.
        user_agent: Untrusted.
    """

    sequence: int = 0
    """Unique and increasing on the machine: tail_http_traffic's cursor."""

    finish_time: datetime | None = None
    """When the response finished. A WebSocket is logged when it closes, with status 0."""

    host: str = ""

    method: str = ""

    path: str = ""
    """With the query. Untrusted."""

    path_pattern: str = ""

    route_path: str = ""
    """The route that matched."""

    service: str = ""
    """That answered. Empty = of a route the project no longer has."""

    port: int = 0

    status_code: int = 0
    """0 = a WebSocket; 499 = the client left before the response. A 401, 303 or 429 of a protected
    project (Project.password_protected) may be its password page's, not the service's.
    """

    response_size_bytes: int = 0

    duration_ms: int = 0
    """In total."""

    service_duration_ms: int = 0
    """Of which inside the service."""

    client_ip_address: str = ""

    user_agent: str = ""
    """Untrusted."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.http_request_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HttpRequest:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.http_request_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ContainerLogFilter:
    """
    Attributes:
        service: Empty = all, removed services too.
        stream: Absent = both.
        text_contains: Literal, any ASCII case, ignoring escape sequences. Length limited (InvalidArgumentError).
    """

    service: str = ""
    """Empty = all, removed services too."""

    stream: OutputStream = OutputStream.UNSPECIFIED
    """Absent = both."""

    text_contains: str = ""
    """Literal, any ASCII case, ignoring escape sequences. Length limited (InvalidArgumentError)."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.container_log_filter_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ContainerLogFilter:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.container_log_filter_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class QueryContainerLogsResponse:
    """
    Attributes:
        start_time: The range queried, as the machine resolved it: defaults applied, on its clock.
        oldest_kept_time: Of the oldest line of container output the machine keeps: nothing older can be queried.
            Absent = none is kept.
        next_page_token: Empty = no more.
        tail_cursor: Where tail_container_logs goes on from (after_cursor), so it misses no line newer than these:
            set on every page, an empty one too. Empty = the machine had logged no line.
    """

    start_time: datetime | None = None
    """The range queried, as the machine resolved it: defaults applied, on its clock."""

    end_time: datetime | None = None

    oldest_kept_time: datetime | None = None
    """Of the oldest line of container output the machine keeps: nothing older can be queried.
    Absent = none is kept.
    """

    lines: Sequence[LogLine] = ()

    next_page_token: str = ""
    """Empty = no more."""

    tail_cursor: str = ""
    """Where tail_container_logs goes on from (after_cursor), so it misses no line newer than these:
    set on every page, an empty one too. Empty = the machine had logged no line.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.query_container_logs_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> QueryContainerLogsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.query_container_logs_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class LogLine:
    """
    Attributes:
        text: A line as written, with its colour codes (SGR escape sequences); other escape sequences, and
            control characters but tab, are removed. A line over 4 KiB is cut (over 16 KiB in streams).
            Untrusted.
    """

    time: datetime | None = None

    service: str = ""

    stream: OutputStream = OutputStream.UNSPECIFIED

    text: str = ""
    """A line as written, with its colour codes (SGR escape sequences); other escape sequences, and
    control characters but tab, are removed. A line over 4 KiB is cut (over 16 KiB in streams).
    Untrusted.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.log_line_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> LogLine:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.log_line_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class RunServiceCommandResponse:
    """
    Attributes:
        timed_out: True = the machine killed it at the timeout; exit_code is then -1.
        stdout: The last 32 KiB of each, as the machine kept them. Invalid UTF-8, and control characters
            other than tab, newline and carriage return (colour codes included), become U+FFFD.
            Untrusted.
        output_truncated: True = the start of stdout or stderr was cut.
    """

    exit_code: int = 0

    timed_out: bool = False
    """True = the machine killed it at the timeout; exit_code is then -1."""

    stdout: str = ""
    """The last 32 KiB of each, as the machine kept them. Invalid UTF-8, and control characters
    other than tab, newline and carriage return (colour codes included), become U+FFFD.
    Untrusted.
    """

    stderr: str = ""

    output_truncated: bool = False
    """True = the start of stdout or stderr was cut."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.run_service_command_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> RunServiceCommandResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.run_service_command_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class FileEntry:
    """
    Attributes:
        name: Without its directory.
        size_bytes: Of a regular file; 0 otherwise.
        mode: Permission bits in octal, e.g. "0644".
        owner_uid: As inside the container.
        symlink_target: When SYMLINK.
    """

    name: str = ""
    """Without its directory."""

    type: FileType = FileType.UNSPECIFIED

    size_bytes: int = 0
    """Of a regular file; 0 otherwise."""

    modify_time: datetime | None = None

    mode: str = ""
    """Permission bits in octal, e.g. "0644"."""

    owner_uid: int = 0
    """As inside the container."""

    owner_gid: int = 0

    symlink_target: str = ""
    """When SYMLINK."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.file_entry_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FileEntry:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.file_entry_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ReadPathResponse:
    """
    Attributes:
        entry: The path itself, symlinks followed; a symlink whose target does not exist is its own entry.
        location: With `service`: where the path lies. Unspecified otherwise: the request says it.
        volume: With `service`: the volume the path lies on, when location is VOLUME. Else empty.
        entries: A directory's: directories first, then by name (bytewise).
        entry_count: A directory's in all.
        next_entry_page_token: Set = more entries follow these: pass it as entry_page_token.
        text: A text file's contents from offset_bytes, ending on a whole character. Untrusted.
        binary: True = the file is binary (a NUL byte in its first 8 KiB): no text. Download it with
            create_transfer.
        next_offset_bytes: Where the next read of the file starts. 0 = the read reached its end.
        deploy_id: The project's files: the deploy whose files these are. Pass it as deploy_project's
            base_deploy_id to be refused if they changed since you read them.
    """

    entry: FileEntry | None = None
    """The path itself, symlinks followed; a symlink whose target does not exist is its own entry."""

    location: FileLocation = FileLocation.UNSPECIFIED
    """With `service`: where the path lies. Unspecified otherwise: the request says it."""

    volume: str = ""
    """With `service`: the volume the path lies on, when location is VOLUME. Else empty."""

    entries: Sequence[FileEntry] = ()
    """A directory's: directories first, then by name (bytewise)."""

    entry_count: int = 0
    """A directory's in all."""

    next_entry_page_token: str = ""
    """Set = more entries follow these: pass it as entry_page_token."""

    text: str = ""
    """A text file's contents from offset_bytes, ending on a whole character. Untrusted."""

    binary: bool = False
    """True = the file is binary (a NUL byte in its first 8 KiB): no text. Download it with
    create_transfer.
    """

    next_offset_bytes: int = 0
    """Where the next read of the file starts. 0 = the read reached its end."""

    deploy_id: str = ""
    """The project's files: the deploy whose files these are. Pass it as deploy_project's
    base_deploy_id to be refused if they changed since you read them.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.read_path_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ReadPathResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.read_path_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ArchiveUpload:
    """The project's directory as a zip, tar or tar.gz (told by content), for create_project's or
    deploy_project's upload_id: {} is enough. A single top folder is unwrapped; .git, __MACOSX,
    .DS_Store, ._* are dropped. Leave out what the build makes again (node_modules, .venv, target).

    Attributes:
        file_name: The archive's name for people, e.g. "recipes.zip". Empty = "archive.tgz".
    """

    file_name: str = ""
    """The archive's name for people, e.g. "recipes.zip". Empty = "archive.tgz"."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.archive_upload_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ArchiveUpload:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.archive_upload_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class FileUpload:
    """At most one of `service`, `volume`. The others are None.

    Attributes:
        service: In its container.
        volume: In the volume, from its root.
        path: From the root, e.g. "/data/uploads/a.jpg".
    """

    project_id: str = ""

    service: str | None = None
    """In its container."""

    volume: str | None = None
    """In the volume, from its root."""

    path: str = ""
    """From the root, e.g. "/data/uploads/a.jpg"."""

    @overload
    def __init__(
        self,
        *,
        project_id: str = "",
        service: None = None,
        volume: None = None,
        path: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        project_id: str = "",
        service: str,
        volume: None = None,
        path: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        project_id: str = "",
        service: None = None,
        volume: str,
        path: str = "",
    ) -> None: ...

    def __init__(
        self,
        *,
        project_id: str = "",
        service: str | None = None,
        volume: str | None = None,
        path: str = "",
    ) -> None:
        _one_of("FileUpload", service=service, volume=volume)
        object.__setattr__(self, "project_id", project_id)
        object.__setattr__(self, "service", service)
        object.__setattr__(self, "volume", volume)
        object.__setattr__(self, "path", path)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.file_upload_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FileUpload:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.file_upload_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class PathDownload:
    """A directory comes as a .tar of what read_path shows; symlinks kept.

    Where the path is. Neither = the project's deployed files.
    At most one of `service`, `volume`. The others are None.

    Attributes:
        service: In its container.
        volume: In the volume, from its root.
        path: From the root. Empty = "/": the whole root.
    """

    project_id: str = ""

    service: str | None = None
    """In its container."""

    volume: str | None = None
    """In the volume, from its root."""

    path: str = ""
    """From the root. Empty = "/": the whole root."""

    @overload
    def __init__(
        self,
        *,
        project_id: str = "",
        service: None = None,
        volume: None = None,
        path: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        project_id: str = "",
        service: str,
        volume: None = None,
        path: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        project_id: str = "",
        service: None = None,
        volume: str,
        path: str = "",
    ) -> None: ...

    def __init__(
        self,
        *,
        project_id: str = "",
        service: str | None = None,
        volume: str | None = None,
        path: str = "",
    ) -> None:
        _one_of("PathDownload", service=service, volume=volume)
        object.__setattr__(self, "project_id", project_id)
        object.__setattr__(self, "service", service)
        object.__setattr__(self, "volume", volume)
        object.__setattr__(self, "path", path)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.path_download_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PathDownload:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.path_download_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CreateTransferResponse:
    """
    Attributes:
        url: On the machine's hostname (Machine.hostname); it works once.
        http_method: "PUT" or "GET".
        expire_time: Start the request before this.
        command: Does it in a shell. upload_archive: packs the current directory and sends it, e.g.
            "tar czf - --exclude=.git --exclude=node_modules . | curl -sS --fail-with-body -T - '<url>'":
            run it in the project's directory (a ready archive: curl --fail-with-body -T <file> '<url>').
            upload_file: "curl -sS --fail-with-body -T '<file>' '<url>'", with your file's path in place
            of its name. download: "curl -sS --fail-with-body -o 'photo.jpg' '<url>'".
        upload_id: upload_archive: for create_project(upload_id=) or deploy_project(upload_id=) once the machine
            answered the PUT with 200.
        replaces: upload_file: a file is at path now; the upload replaces it.
        file_name: download: the name it saves as: a file's own; a directory's ends in ".tar", and "/" is named
            after the project and its service or volume. Empty for an upload.
        exclude_names: upload_archive: the names `command` leaves out of the archive, wherever they lie in the
            directory. A program that packs the directory itself leaves out the same.
    """

    url: str = ""
    """On the machine's hostname (Machine.hostname); it works once."""

    http_method: str = ""
    """"PUT" or "GET"."""

    expire_time: datetime | None = None
    """Start the request before this."""

    command: str = ""
    """Does it in a shell. upload_archive: packs the current directory and sends it, e.g.
    "tar czf - --exclude=.git --exclude=node_modules . | curl -sS --fail-with-body -T - '<url>'":
    run it in the project's directory (a ready archive: curl --fail-with-body -T <file> '<url>').
    upload_file: "curl -sS --fail-with-body -T '<file>' '<url>'", with your file's path in place
    of its name. download: "curl -sS --fail-with-body -o 'photo.jpg' '<url>'".
    """

    upload_id: str = ""
    """upload_archive: for create_project(upload_id=) or deploy_project(upload_id=) once the machine
    answered the PUT with 200.
    """

    replaces: bool = False
    """upload_file: a file is at path now; the upload replaces it."""

    file_name: str = ""
    """download: the name it saves as: a file's own; a directory's ends in ".tar", and "/" is named
    after the project and its service or volume. Empty for an upload.
    """

    exclude_names: Sequence[str] = ()
    """upload_archive: the names `command` leaves out of the archive, wherever they lie in the
    directory. A program that packs the directory itself leaves out the same.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.create_transfer_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CreateTransferResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.create_transfer_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectBusy:
    """Detail of an UnavailableError error: an operation, or a short action, holds the project. The
    message says the same in words.

    Attributes:
        operation_id: Empty = a short action, done while its caller waits: call again in a few seconds. Else wait
            for it with get_operation, even while it is still starting; when it is your own
            operation_id, the first call with it is still starting it: call again.
        kind: Unspecified when operation_id is empty.
        start_time: Since when it holds the project.
    """

    operation_id: str = ""
    """Empty = a short action, done while its caller waits: call again in a few seconds. Else wait
    for it with get_operation, even while it is still starting; when it is your own
    operation_id, the first call with it is still starting it: call again.
    """

    kind: OperationKind = OperationKind.UNSPECIFIED
    """Unspecified when operation_id is empty."""

    start_time: datetime | None = None
    """Since when it holds the project."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_busy_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectBusy:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_busy_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectChanged:
    """Detail of an AbortedError error: base_deploy_id is not the current deploy: the project was deployed
    since you read it. Read it again (Project.deploy_id) and redo your change on its files.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.project_changed_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ProjectChanged:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.project_changed_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MachineUnreachable:
    """Detail of an UnavailableError error: the machine does not answer now, as while it restarts. Call
    again later.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.machine_unreachable_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MachineUnreachable:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.machine_unreachable_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class NoMachine:
    """Detail of a FailedPreconditionError error: the account has no machine to run projects on yet.

    Attributes:
        url: Where the person goes on in the browser.
    """

    reason: NoMachineReason = NoMachineReason.UNSPECIFIED

    url: str = ""
    """Where the person goes on in the browser."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.no_machine_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> NoMachine:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.no_machine_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class WatchOperationResponse:
    """At most one of `log`, `finished_operation`. The others are None.

    Attributes:
        finished_operation: Always the last message.
    """

    log: OperationLogLine | None = None

    finished_operation: Operation | None = None
    """Always the last message."""

    @overload
    def __init__(
        self,
        *,
        log: None = None,
        finished_operation: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        log: OperationLogLine,
        finished_operation: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        log: None = None,
        finished_operation: Operation,
    ) -> None: ...

    def __init__(
        self,
        *,
        log: OperationLogLine | None = None,
        finished_operation: Operation | None = None,
    ) -> None:
        _one_of("WatchOperationResponse", log=log, finished_operation=finished_operation)
        object.__setattr__(self, "log", log)
        object.__setattr__(self, "finished_operation", finished_operation)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.watch_operation_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WatchOperationResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.watch_operation_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class TailContainerLogsResponse:
    """
    Attributes:
        cursor: To reconnect after this line.
    """

    line: LogLine | None = None

    cursor: str = ""
    """To reconnect after this line."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.tail_container_logs_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TailContainerLogsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.tail_container_logs_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class TailHttpTrafficResponse:
    request: HttpRequest | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.tail_http_traffic_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TailHttpTrafficResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.tail_http_traffic_response_from_dict(data)
