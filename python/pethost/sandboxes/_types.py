"""The API's messages and enums. Generated from v1/sandboxes.proto: do not edit."""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass
from datetime import datetime
from typing import Any, final, overload

from .._runtime import OpenEnum
from .._runtime import one_of as _one_of


class Meter(OpenEnum):
    """What usage counts (USAGE). Templates are not billed: Limits.template_gib bounds them.

    Attributes:
        RUNNING: A second of a RUNNING sandbox, at its size (UsageRow.size).
        PAUSED: A second of a PAUSED sandbox, at its size (UsageRow.size).
        STORED_GIB: A GiB a STOPPED sandbox holds in object storage: what its disk holds of its own.
    """

    UNSPECIFIED = 0

    RUNNING = 5
    """A second of a RUNNING sandbox, at its size (UsageRow.size)."""

    PAUSED = 9
    """A second of a PAUSED sandbox, at its size (UsageRow.size)."""

    STORED_GIB = 7
    """A GiB a STOPPED sandbox holds in object storage: what its disk holds of its own."""


class SandboxState(OpenEnum):
    """
    Attributes:
        PAUSED: Memory, processes and disk kept on its server.
        STOPPED: Disk kept, memory and processes lost: it starts again when it resumes, its files as it left
            them.
        DELETED: Memory and disk gone; the record stays 30 days, its events and metrics a day.
    """

    UNSPECIFIED = 0

    RUNNING = 1

    PAUSED = 2
    """Memory, processes and disk kept on its server."""

    STOPPED = 3
    """Disk kept, memory and processes lost: it starts again when it resumes, its files as it left
    them.
    """

    DELETED = 4
    """Memory and disk gone; the record stays 30 days, its events and metrics a day."""


class StateReason(OpenEnum):
    """Why a sandbox is in its state, or changed state.

    Attributes:
        REQUEST: A call asked for it.
        IDLE: Nothing happened in it for its lifecycle's time, or, RUNNING, for a minute when its server's
            memory ran short, or, PAUSED, its server's disk ran short, or its server could not resume it
            after its machine restarted (state_message says so).
        WAKE: A call into it, an SSH login or a request to a port resumed it.
        CRASH: Stopped: its VM or its server failed ("its server ran out of memory" when that ended its VM,
            "its server ran out of disk space" when its server stopped it for its disk, which grew
            most), or it did not start (state_message says why, e2fsck's words for a disk its guest could
            not mend). Its disk is as last written. Only resume_sandbox starts it again: a call into it, an
            SSH login or a request to a port does not.
        MAINTENANCE: Its server's machine restarted: PAUSED before, counting nothing, and RUNNING again after;
            STOPPED if its memory could not be kept, and PAUSED (IDLE), counting again, if its server
            could not resume it then. A restart of the server alone, as an update's, keeps a running
            sandbox running.
        UNPAID: Nothing pays for its workspace's usage (Billing.suspended): STOPPED, from RUNNING or PAUSED.
            Once something pays, resume_sandbox starts it, as any STOPPED sandbox; a call wakes it only
            when its lifecycle says wake_when_stopped.
    """

    UNSPECIFIED = 0

    REQUEST = 1
    """A call asked for it."""

    IDLE = 2
    """Nothing happened in it for its lifecycle's time, or, RUNNING, for a minute when its server's
    memory ran short, or, PAUSED, its server's disk ran short, or its server could not resume it
    after its machine restarted (state_message says so).
    """

    WAKE = 3
    """A call into it, an SSH login or a request to a port resumed it."""

    CRASH = 5
    """Stopped: its VM or its server failed ("its server ran out of memory" when that ended its VM,
    "its server ran out of disk space" when its server stopped it for its disk, which grew
    most), or it did not start (state_message says why, e2fsck's words for a disk its guest could
    not mend). Its disk is as last written. Only resume_sandbox starts it again: a call into it, an
    SSH login or a request to a port does not.
    """

    MAINTENANCE = 6
    """Its server's machine restarted: PAUSED before, counting nothing, and RUNNING again after;
    STOPPED if its memory could not be kept, and PAUSED (IDLE), counting again, if its server
    could not resume it then. A restart of the server alone, as an update's, keeps a running
    sandbox running.
    """

    UNPAID = 7
    """Nothing pays for its workspace's usage (Billing.suspended): STOPPED, from RUNNING or PAUSED.
    Once something pays, resume_sandbox starts it, as any STOPPED sandbox; a call wakes it only
    when its lifecycle says wake_when_stopped.
    """


class Size(OpenEnum):
    """Its vCPUs, memory and disk (SizeInfo)."""

    UNSPECIFIED = 0

    SMALL = 1

    DEFAULT = 2

    LARGE = 3

    XLARGE = 4


class SandboxEventKind(OpenEnum):
    UNSPECIFIED = 0

    LIFECYCLE = 1

    COMMAND = 2

    EGRESS = 3

    PORT = 4

    AGENT_TURN = 5


class LifecycleChange(OpenEnum):
    UNSPECIFIED = 0

    CREATED = 1

    PAUSED = 2

    STOPPED = 3

    RESUMED = 4

    RESIZED = 5

    DELETED = 6


class TemplateState(OpenEnum):
    """
    Attributes:
        SAVING: Its disk is taken; it is shrunk and uploaded. No sandbox starts from it yet.
        FAILED: Its save failed (failure_message): it holds nothing, counts toward nothing, and goes a day
            later.
    """

    UNSPECIFIED = 0

    SAVING = 1
    """Its disk is taken; it is shrunk and uploaded. No sandbox starts from it yet."""

    READY = 2

    FAILED = 3
    """Its save failed (failure_message): it holds nothing, counts toward nothing, and goes a day
    later.
    """


class CommandState(OpenEnum):
    """
    Attributes:
        TIMED_OUT: timeout_seconds ended it.
        STOPPED: stop_command ended it.
        LOST: Its end is not known: its sandbox lost its memory (STOPPED) while it ran, or it ran on
            through a restart of the sandbox's daemon and has ended since. What the sandbox's disk
            holds of its last seconds before it lost its memory may be gone: a command that began then
            may be `NOT_FOUND`, and one that ended then may be LOST.
    """

    UNSPECIFIED = 0

    RUNNING = 1

    EXITED = 2

    TIMED_OUT = 3
    """timeout_seconds ended it."""

    STOPPED = 4
    """stop_command ended it."""

    LOST = 5
    """Its end is not known: its sandbox lost its memory (STOPPED) while it ran, or it ran on
    through a restart of the sandbox's daemon and has ended since. What the sandbox's disk
    holds of its last seconds before it lost its memory may be gone: a command that began then
    may be `NOT_FOUND`, and one that ended then may be LOST.
    """


class StartedBy(OpenEnum):
    """
    Attributes:
        TERMINAL: A terminal link (create_link).
        AGENT: Not given yet: an agent's commands are its own.
    """

    UNSPECIFIED = 0

    API = 1

    SSH = 2

    TERMINAL = 3
    """A terminal link (create_link)."""

    AGENT = 4
    """Not given yet: an agent's commands are its own."""


class FileKind(OpenEnum):
    UNSPECIFIED = 0

    FILE = 1

    DIRECTORY = 2

    SYMLINK = 3


class FileFailure(OpenEnum):
    """
    Attributes:
        UNSPECIFIED: None failed, or for no reason below: see failure_message.
        NOT_FOUND: The path, or its directory, is not there.
        NOT_A_DIRECTORY: A part of the path is a file.
        EDIT_NOT_FOUND: old_text does not occur in the file.
        EDIT_AMBIGUOUS: old_text occurs more than once.
    """

    UNSPECIFIED = 0
    """None failed, or for no reason below: see failure_message."""

    NOT_FOUND = 1
    """The path, or its directory, is not there."""

    PERMISSION_DENIED = 2

    NOT_A_DIRECTORY = 3
    """A part of the path is a file."""

    IS_A_DIRECTORY = 4

    NO_SPACE = 5

    EDIT_NOT_FOUND = 6
    """old_text does not occur in the file."""

    EDIT_AMBIGUOUS = 7
    """old_text occurs more than once."""


class FileEventKind(OpenEnum):
    """
    Attributes:
        OVERFLOW: Events under `path` were lost, or it holds a directory that is not watched: list it again.
    """

    UNSPECIFIED = 0

    CREATED = 1

    WRITTEN = 2

    REMOVED = 3

    RENAMED = 4

    OVERFLOW = 5
    """Events under `path` were lost, or it holds a directory that is not watched: list it again."""


class DesktopFailure(OpenEnum):
    """
    Attributes:
        UNSPECIFIED: None failed, or for no reason below: see failure_message.
        OFF_SCREEN: A point outside the screen.
        UNKNOWN_KEY: A key name it does not know.
    """

    UNSPECIFIED = 0
    """None failed, or for no reason below: see failure_message."""

    OFF_SCREEN = 1
    """A point outside the screen."""

    UNKNOWN_KEY = 2
    """A key name it does not know."""


class MouseButton(OpenEnum):
    """
    Attributes:
        BACK: A browser's back.
    """

    UNSPECIFIED = 0

    LEFT = 1

    RIGHT = 2

    MIDDLE = 3

    BACK = 4
    """A browser's back."""

    FORWARD = 5


class Agent(OpenEnum):
    """Coding agents in every sandbox, from our base. One signs in with a secret bound to its variable
    (ANTHROPIC_API_KEY, OPENAI_API_KEY), or as a person signed it in in a terminal. A conversation's
    history stays on the sandbox's disk: a pause keeps it.
    """

    UNSPECIFIED = 0

    CLAUDE_CODE = 1

    CODEX = 2

    OPENCODE = 3


class AgentTurnState(OpenEnum):
    """
    Attributes:
        QUEUED: Waits for the conversation's running turn.
        STOPPED: stop_agent_turn ended it.
        LOST: Its sandbox lost its memory (STOPPED) while it ran, or within its last seconds before:
            what its disk holds of those may be gone.
    """

    UNSPECIFIED = 0

    QUEUED = 1
    """Waits for the conversation's running turn."""

    RUNNING = 2

    DONE = 3

    FAILED = 4

    STOPPED = 5
    """stop_agent_turn ended it."""

    LOST = 6
    """Its sandbox lost its memory (STOPPED) while it ran, or within its last seconds before:
    what its disk holds of those may be gone.
    """


class RoomBound(OpenEnum):
    """What a sandbox server lacked for a call it refused, UnavailableError + NoCapacity.

    Attributes:
        MEMORY: The memory it sells is held by the sandboxes running or paused there: try again later.
        SHORT_MEMORY: Its own memory runs short, so it starts no sandbox for now: try again later.
        DISK: Its disk has no more free space than it keeps, what it could evict gone: try again later.
        DISK_CAP: The disks it holds reach as much as it holds: try again later.
    """

    UNSPECIFIED = 0

    MEMORY = 1
    """The memory it sells is held by the sandboxes running or paused there: try again later."""

    SHORT_MEMORY = 2
    """Its own memory runs short, so it starts no sandbox for now: try again later."""

    DISK = 3
    """Its disk has no more free space than it keeps, what it could evict gone: try again later."""

    DISK_CAP = 4
    """The disks it holds reach as much as it holds: try again later."""


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Workspace:
    """
    Attributes:
        ssh_keys: Public keys that sign in to every sandbox over SSH.
        secrets: Never their values.
        billing: Absent = its usage is not billed.
        sizes: Every size, smallest first: the header's SIZES.
        template_bytes: What its own template versions take in object storage now (Template.size_bytes, SAVING ones
            counted as 0): what Limits.template_gib holds.
        vcpus_used: What its sandboxes count of Limits.vcpus now.
    """

    workspace_id: str = ""

    name: str = ""

    limits: Limits | None = None

    ssh_keys: Sequence[SshKey] = ()
    """Public keys that sign in to every sandbox over SSH."""

    secrets: Sequence[Secret] = ()
    """Never their values."""

    billing: Billing | None = None
    """Absent = its usage is not billed."""

    sizes: Sequence[SizeInfo] = ()
    """Every size, smallest first: the header's SIZES."""

    template_bytes: int = 0
    """What its own template versions take in object storage now (Template.size_bytes, SAVING ones
    counted as 0): what Limits.template_gib holds.
    """

    vcpus_used: int = 0
    """What its sandboxes count of Limits.vcpus now."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.workspace_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Workspace:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.workspace_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class SizeInfo:
    """What a size is: the header's SIZES. A sandbox runs in a VM of its size, of that VM's whole life,
    which keeps it: a new size restarts a RUNNING sandbox (update_sandbox), its processes ended and
    its files kept, is refused while PAUSED, and is taken at a STOPPED sandbox's next start. The
    disk is what the sandbox may write: its base's files do not count. It is its size's at the
    create, and a new size keeps it unless grow_disk grows it to the new size's: a size is allowed
    while its disk is at least the sandbox's (Sandbox.disk_gib), else it is refused
    (InvalidArgumentError, naming the smallest size that holds it), and a template's sandboxes take any
    size from its min_size up, the smallest whose disk holds what it saved.

    Attributes:
        running_hour: What a RUNNING sandbox of it costs for an hour, in the unit of Workspace.billing's currency,
            by the second (USAGE). Absent while the workspace is not billed.
        paused_hour: What a PAUSED one costs for an hour, as running_hour is: the same share of it for every size.
    """

    size: Size = Size.UNSPECIFIED

    vcpus: int = 0

    memory_mib: int = 0

    disk_gib: int = 0

    running_hour: float | None = None
    """What a RUNNING sandbox of it costs for an hour, in the unit of Workspace.billing's currency,
    by the second (USAGE). Absent while the workspace is not billed.
    """

    paused_hour: float | None = None
    """What a PAUSED one costs for an hour, as running_hour is: the same share of it for every size."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.size_info_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SizeInfo:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.size_info_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Billing:
    """What pays for a workspace's usage: the usage its plan includes each period, used first, and
    then its balance. Every amount is in `currency`, in millionths of its unit: 1500000 = 1.50.

    Attributes:
        currency: ISO 4217, lowercase: "usd".
        included_micros: What is left of the usage the plan includes in the period that ends at period_end_time. What
            is left then is gone, and the next period begins with the plan's whole amount, less what a
            balance below zero owes, which it pays first.
        included_total_micros: What the period began with.
        balance_micros: The balance, which pays once the included usage is used up: what its owner added less what
            was used from it. It does not expire. Below zero by what ran between its last cent and the
            stop, and by what is stored meanwhile; the next period's amount pays that first.
        suspended: True = nothing pays for its usage now: the included usage is used up and the balance is
            empty. Its RUNNING and PAUSED sandboxes were STOPPED (STATE_REASON_UNPAID), no sandbox
            starts, resumes or wakes, and no template is made (UsageUnpaid), until its owner
            adds to the balance or the plan's next period begins.
            What it stores is still counted.
        trial: True = it is in its plan's free trial: the included usage is the trial's, and the plan's
            first payment comes at period_end_time.
    """

    currency: str = ""
    """ISO 4217, lowercase: "usd"."""

    included_micros: int = 0
    """What is left of the usage the plan includes in the period that ends at period_end_time. What
    is left then is gone, and the next period begins with the plan's whole amount, less what a
    balance below zero owes, which it pays first.
    """

    included_total_micros: int = 0
    """What the period began with."""

    period_end_time: datetime | None = None

    balance_micros: int = 0
    """The balance, which pays once the included usage is used up: what its owner added less what
    was used from it. It does not expire. Below zero by what ran between its last cent and the
    stop, and by what is stored meanwhile; the next period's amount pays that first.
    """

    suspended: bool = False
    """True = nothing pays for its usage now: the included usage is used up and the balance is
    empty. Its RUNNING and PAUSED sandboxes were STOPPED (STATE_REASON_UNPAID), no sandbox
    starts, resumes or wakes, and no template is made (UsageUnpaid), until its owner
    adds to the balance or the plan's next period begins.
    What it stores is still counted.
    """

    trial: bool = False
    """True = it is in its plan's free trial: the included usage is the trial's, and the plan's
    first payment comes at period_end_time.
    """

    rates: Rates | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.billing_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Billing:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.billing_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Rates:
    """What a GiB of each meter that counts bytes costs for a month of 730 hours, by the second, in
    the currency's unit: 0.03 = 3 cents. The same number in every currency. What a RUNNING or a
    PAUSED sandbox costs is its size's (SizeInfo.running_hour, paused_hour).

    Attributes:
        stored_gib_month: Meter.STORED_GIB: what a STOPPED sandbox holds in object storage.
    """

    stored_gib_month: float = 0.0
    """Meter.STORED_GIB: what a STOPPED sandbox holds in object storage."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.rates_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Rates:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.rates_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class SshKey:
    """
    Attributes:
        public_key: As set_ssh_keys takes it: "ssh-ed25519 AAAA… laptop".
        comment: What follows the key: "laptop". Absent when it has none.
        fingerprint: As `ssh-keygen -l` prints it: "SHA256:…".
    """

    public_key: str = ""
    """As set_ssh_keys takes it: "ssh-ed25519 AAAA… laptop"."""

    comment: str = ""
    """What follows the key: "laptop". Absent when it has none."""

    fingerprint: str = ""
    """As `ssh-keygen -l` prints it: "SHA256:…"."""

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
class Limits:
    """What the workspace's plan allows (its trial's while it lasts). A call past one is refused
    ResourceExhaustedError + LimitReached, naming it.

    Attributes:
        vcpus: The most vCPUs its sandboxes may have together (SIZES) while they count: RUNNING, PAUSED,
            STOPPED with Lifecycle.wake_when_stopped, and every create, start or move under way.
            Checked by create_sandbox, resume_sandbox of a STOPPED sandbox, update_sandbox's new
            size of one that counts, and wake_when_stopped turned on for a STOPPED one. A sandbox that
            counts is never refused for it: a call into a PAUSED one, or into a STOPPED one that wakes
            when stopped, wakes it. Stopping one frees its vCPUs, but for one that wakes when stopped.
        largest_size: The largest size it may create, start or change a sandbox to.
        template_versions: The workspace's own templates: at most template_versions versions of one name, FAILED ones
            aside, and template_gib GiB in all of what its versions take in object storage
            (Workspace.template_bytes), which is not billed. A create_template past either, or while
            another version is SAVING, is refused (LimitReached); a version whose own bytes would pass
            template_gib is FAILED before its upload. delete_template makes room at once. A FAILED version
            takes nothing, and goes a day after it failed.
    """

    vcpus: int = 0
    """The most vCPUs its sandboxes may have together (SIZES) while they count: RUNNING, PAUSED,
    STOPPED with Lifecycle.wake_when_stopped, and every create, start or move under way.
    Checked by create_sandbox, resume_sandbox of a STOPPED sandbox, update_sandbox's new
    size of one that counts, and wake_when_stopped turned on for a STOPPED one. A sandbox that
    counts is never refused for it: a call into a PAUSED one, or into a STOPPED one that wakes
    when stopped, wakes it. Stopping one frees its vCPUs, but for one that wakes when stopped.
    """

    largest_size: Size = Size.UNSPECIFIED
    """The largest size it may create, start or change a sandbox to."""

    template_versions: int = 0
    """The workspace's own templates: at most template_versions versions of one name, FAILED ones
    aside, and template_gib GiB in all of what its versions take in object storage
    (Workspace.template_bytes), which is not billed. A create_template past either, or while
    another version is SAVING, is refused (LimitReached); a version whose own bytes would pass
    template_gib is FAILED before its upload. delete_template makes room at once. A FAILED version
    takes nothing, and goes a day after it failed.
    """

    template_gib: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.limits_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Limits:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.limits_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Secret:
    """A value the workspace keeps and no sandbox holds.

    Attributes:
        name: a-z, 0-9 and "-": "anthropic".
        hosts: Where the egress proxy swaps the value in, in the headers of HTTPS requests:
            "api.anthropic.com".
    """

    name: str = ""
    """a-z, 0-9 and "-": "anthropic"."""

    hosts: Sequence[str] = ()
    """Where the egress proxy swaps the value in, in the headers of HTTPS requests:
    "api.anthropic.com".
    """

    update_time: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.secret_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Secret:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.secret_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Sandbox:
    """A sandbox as a record: its state and why, its settings in force, how to reach it, its usage.

    States, idle and wake: RUNNING lives in its server's memory, PAUSED on its server's disk,
    STOPPED in object storage. PAUSED keeps memory, processes and disk, and its place on its
    server: it resumes where it was, never refused for room. STOPPED is a shut-down sandbox: its
    disk stays, its processes ended, and it starts again when it resumes, its files as it left
    them. A sandbox stopped by a CRASH (its VM failed, its server ran out of memory or of disk
    space, or it did not start: StateReason) starts again only by resume_sandbox, never by a call
    into it.

    A sandbox is idle while nothing happens in it: no call or open stream of
    SandboxRuntimeService, no open link, SSH session or request to a port, no agent turn running,
    and no command running that was started with keep_awake. Its lifecycle's three timers run on
    that one clock (Lifecycle): idle pause_after_idle_seconds, a RUNNING sandbox pauses; idle
    stop_after_idle_seconds, a RUNNING or PAUSED one stops, and one whose stop comes no later than
    its pause stops without pausing; idle delete_after_idle_seconds, one in any state is deleted,
    for a sandbox that should cost no storage once done. Idle a minute or more, a RUNNING one may
    pause sooner, whatever its lifecycle, when its server's memory runs short (IDLE, "paused early:
    its server's memory ran short").

    Any call of SandboxRuntimeService, SSH login or request to a port first resumes a PAUSED
    sandbox, on its server. A STOPPED one wakes so only when its lifecycle says wake_when_stopped,
    stopped by a call or by its timer, for a project that wakes now and then, a webhook's; its
    vCPUs then count while it is STOPPED (Limits.vcpus), so turning it on for a STOPPED sandbox is
    refused past the limit, and turning it off frees them. Without it such a call is
    FailedPreconditionError + Stopped, a request to a port is answered 503 "stopped: resume it", and
    only resume_sandbox starts it. A wake runs on the sandbox's own server: a PAUSED one keeps its
    place there and is never refused for room; a STOPPED one without room for it is UnavailableError +
    NoCapacity, and resume_sandbox may start it elsewhere. Of SandboxService, only resume_sandbox
    resumes one.

    A stopped sandbox's disk is copied to object storage a minute after it stops, and its server
    lets its own copy go when it needs the room: its next start fetches the disk whole first, about
    10 s a GiB of what it holds of its own. resume_sandbox waits up to 45 s for it, then answers the
    sandbox STOPPED with how far the fetch is (restore), which goes on and starts it; a call into
    it, an SSH login or a request to a port is UnavailableError + Restoring meanwhile (HTTP 503 with the
    same words).

    A server's disk holds only what its sandboxes use. When it runs short, the server stops the
    PAUSED sandboxes idle the longest ahead of their lifecycles (IDLE, "stopped early: its server's
    disk ran short"), and a pause is a stop meanwhile ("stopped instead of paused"); when it runs
    out, it stops the RUNNING sandbox whose disk grew most (CRASH, "its server ran out of disk
    space"), its disk kept.

    A STOPPED sandbox, its copy current, starts on another server when its own has no room for it
    (resume_sandbox), its addresses with it. If a server is lost, each of its sandboxes with a copy
    is STOPPED from its last copy, saying when that was if it ran since, and starts on another
    server at its next resume_sandbox; one without a copy is DELETED. While nothing pays for its
    workspace (Billing.suspended), its RUNNING and PAUSED sandboxes are STOPPED (UNPAID), and none of them
    starts.

    Attributes:
        sandbox_id: 16 characters, a-z and 0-9: also its DNS label.
        state_message: Prose for people whenever set: what failed, why it stopped or paused early, or what became of
            it when its server was lost. Never parsed: state_reason is the fact.
        state_time: When it entered its state.
        template: The exact version it started from: "my-app@3".
        settings: In force: every group, its defaults filled in.
        revision: Grows with every change of its settings (update_sandbox(if_revision=)).
        disk_gib: What it may write: its size's disk at its create, which a new size keeps unless grow_disk
            grows it to the new size's. No size whose disk is smaller is allowed
            (SIZES).
        desktop: Its screen: every sandbox has one (control_desktop).
        ssh_command: "ssh <id>@<server> -p 2222": signs in with a key of the workspace, or a connect_sandbox token
            as the password.
        panel_url: Its page in the panel, where a person signs in to see its terminal, desktop and events. Give
            a person this, not a link.
        connection: In create_sandbox's answer only: what connect_sandbox would answer. An MCP
            tool's answer leaves it out: connect_sandbox gives it to an agent that asks.
        restore: STOPPED while its disk is fetched from object storage for a start: how far that is. Absent
            otherwise.
        next_state: What its lifecycle makes of it next if nothing happens before (IDLE AND WAKE), and when:
            PAUSED, STOPPED or DELETED. Absent while something keeps it awake, or when no timer of its
            lifecycle runs in its state. get_sandbox only.
        stored_bytes: PAUSED or STOPPED: what it holds of its own, as its server measured it when it entered its
            state: PAUSED, its memory and its disk on its server; STOPPED, its disk, which object storage
            keeps and Meter.STORED_GIB counts (USAGE).
        name: What people call it, if anything (create_sandbox, update_sandbox): unique among the
            workspace's sandboxes that are not DELETED, and a DELETED one keeps it in its record. A call
            names a sandbox by sandbox_id, never by this: list_sandboxes with `name` finds its id.
    """

    sandbox_id: str = ""
    """16 characters, a-z and 0-9: also its DNS label."""

    state: SandboxState = SandboxState.UNSPECIFIED

    state_reason: StateReason = StateReason.UNSPECIFIED

    state_message: str = ""
    """Prose for people whenever set: what failed, why it stopped or paused early, or what became of
    it when its server was lost. Never parsed: state_reason is the fact.
    """

    state_time: datetime | None = None
    """When it entered its state."""

    template: str = ""
    """The exact version it started from: "my-app@3"."""

    labels: Sequence[Label] = ()

    settings: SandboxSettings | None = None
    """In force: every group, its defaults filled in."""

    revision: int = 0
    """Grows with every change of its settings (update_sandbox(if_revision=))."""

    disk_gib: int = 0
    """What it may write: its size's disk at its create, which a new size keeps unless grow_disk
    grows it to the new size's. No size whose disk is smaller is allowed
    (SIZES).
    """

    desktop: Desktop | None = None
    """Its screen: every sandbox has one (control_desktop)."""

    ssh_command: str = ""
    """"ssh <id>@<server> -p 2222": signs in with a key of the workspace, or a connect_sandbox token
    as the password.
    """

    panel_url: str = ""
    """Its page in the panel, where a person signs in to see its terminal, desktop and events. Give
    a person this, not a link.
    """

    create_time: datetime | None = None

    usage: Usage | None = None

    connection: Connection | None = None
    """In create_sandbox's answer only: what connect_sandbox would answer. An MCP
    tool's answer leaves it out: connect_sandbox gives it to an agent that asks.
    """

    restore: Restore | None = None
    """STOPPED while its disk is fetched from object storage for a start: how far that is. Absent
    otherwise.
    """

    next_state: SandboxState = SandboxState.UNSPECIFIED
    """What its lifecycle makes of it next if nothing happens before (IDLE AND WAKE), and when:
    PAUSED, STOPPED or DELETED. Absent while something keeps it awake, or when no timer of its
    lifecycle runs in its state. get_sandbox only.
    """

    next_state_time: datetime | None = None

    stored_bytes: int = 0
    """PAUSED or STOPPED: what it holds of its own, as its server measured it when it entered its
    state: PAUSED, its memory and its disk on its server; STOPPED, its disk, which object storage
    keeps and Meter.STORED_GIB counts (USAGE).
    """

    name: str = ""
    """What people call it, if anything (create_sandbox, update_sandbox): unique among the
    workspace's sandboxes that are not DELETED, and a DELETED one keeps it in its record. A call
    names a sandbox by sandbox_id, never by this: list_sandboxes with `name` finds its id.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.sandbox_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Sandbox:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.sandbox_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Restore:
    """A STOPPED sandbox's disk being fetched from object storage, which starts it once it is whole.

    Attributes:
        total_bytes: What it holds of its own: its template's files are on the server.
    """

    fetched_bytes: int = 0

    total_bytes: int = 0
    """What it holds of its own: its template's files are on the server."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.restore_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Restore:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.restore_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Usage:
    """What a sandbox has used so far, by the meters of USAGE: as its server counted it, up to the
    last word the panel had from that server, some 10 seconds ago at most while it is in reach. One
    that moved to another server counts from its move there; cost_micros is what it was charged on
    every server.

    Four meters (Meter), each priced at Workspace.billing's rates. A RUNNING sandbox counts its
    size's seconds, each run rounded up to a whole second and 10 seconds at least, unless its
    server ended it (out of memory or of disk space, its machine's restart, an unpaid workspace, a
    new size), and a second counts at one size only. A PAUSED sandbox counts its size's seconds at
    its paused price (SizeInfo.paused_hour, a share of running_hour), since its server keeps its
    place for it; one paused for its server's restart counts nothing. A STOPPED sandbox counts the
    bytes of its own its disk holds (Sandbox.stored_bytes), which object storage keeps, never its
    empty space: a long sleep costs least STOPPED. No other minimum: pausing and waking never
    turns running time into a cheaper one, nor counts a second twice, since a stretch counts from
    where the one before it was counted to (Sandbox.usage, list_usage).

    Attributes:
        running_seconds: At every size, each run 10 seconds at least.
        paused_seconds: At every size.
        stored_gib_hours: GiB held in object storage while STOPPED.
        cost_micros: What it was charged so far, in millionths of the unit of Workspace.billing's currency.
            Absent while its workspace is not billed.
    """

    running_seconds: int = 0
    """At every size, each run 10 seconds at least."""

    paused_seconds: int = 0
    """At every size."""

    stored_gib_hours: float = 0.0
    """GiB held in object storage while STOPPED."""

    cost_micros: int = 0
    """What it was charged so far, in millionths of the unit of Workspace.billing's currency.
    Absent while its workspace is not billed.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.usage_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Usage:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.usage_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListSandboxesResponse:
    """
    Attributes:
        next_page_token: Absent on the last page.
    """

    sandboxes: Sequence[Sandbox] = ()

    next_page_token: str = ""
    """Absent on the last page."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_sandboxes_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListSandboxesResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_sandboxes_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Connection:
    """
    Attributes:
        url: https://<server>: the sandbox's server, shared by every sandbox there.
        token: `Authorization: Bearer <token>` for SandboxRuntimeService; the password for its SSH. It opens
            no port: a private port takes a token of its own (create_link port), which a page may hold
            where this one, a root credential, must not.
        ssh_command: Sandbox.ssh_command, which takes the token as its password.
    """

    url: str = ""
    """https://<server>: the sandbox's server, shared by every sandbox there."""

    token: str = ""
    """`Authorization: Bearer <token>` for SandboxRuntimeService; the password for its SSH. It opens
    no port: a private port takes a token of its own (create_link port), which a page may hold
    where this one, a root credential, must not.
    """

    expire_time: datetime | None = None

    ssh_command: str = ""
    """Sandbox.ssh_command, which takes the token as its password."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.connection_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Connection:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.connection_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class SandboxSettings:
    """A sandbox's settings, in groups: a group sent replaces the whole group, a group left out stays
    as it is (in create_sandbox: the template's, else the default beside it).

    Attributes:
        size: Default: DEFAULT.
        egress: Default: allow "*".
        ingress: Default: no public port.
        environment: Default: no variables.
    """

    size: Size = Size.UNSPECIFIED
    """Default: DEFAULT."""

    lifecycle: Lifecycle | None = None

    egress: Egress | None = None
    """Default: allow "*"."""

    ingress: Ingress | None = None
    """Default: no public port."""

    environment: Environment | None = None
    """Default: no variables."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.sandbox_settings_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SandboxSettings:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.sandbox_settings_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Lifecycle:
    """When an idle sandbox pauses, stops and is deleted: three timers on one clock.

    Attributes:
        pause_after_idle_seconds: RUNNING becomes PAUSED (IDLE). Absent = 300; 0 = never.
        stop_after_idle_seconds: RUNNING or PAUSED becomes STOPPED (IDLE). Absent = 1800; 0 = never.
        delete_after_idle_seconds: Any state becomes DELETED (IDLE). 0 = never.
        wake_when_stopped: True = a STOPPED sandbox wakes as a PAUSED one does, its vCPUs counted while STOPPED.
    """

    pause_after_idle_seconds: int | None = None
    """RUNNING becomes PAUSED (IDLE). Absent = 300; 0 = never."""

    stop_after_idle_seconds: int | None = None
    """RUNNING or PAUSED becomes STOPPED (IDLE). Absent = 1800; 0 = never."""

    delete_after_idle_seconds: int = 0
    """Any state becomes DELETED (IDLE). 0 = never."""

    wake_when_stopped: bool = False
    """True = a STOPPED sandbox wakes as a PAUSED one does, its vCPUs counted while STOPPED."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.lifecycle_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Lifecycle:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.lifecycle_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Egress:
    """Where a sandbox may connect: TCP and DNS only. A change closes connections it no longer allows.

    Attributes:
        allow: "*" (anywhere), a domain ("pypi.org"), its subdomains ("*.github.com"), an IP or a CIDR. A
            domain means its ports 80 and 443 unless ":port" names another ("github.com:22"). Empty:
            nowhere. The sandbox's DNS resolves only the names a domain entry (or "*") allows. With deny,
            at most 100 entries, each at most 255 bytes. update_sandbox says how a connection is judged.
        deny: Exceptions to allow, written the same way; they win. Sent alone, allow is empty: nowhere. To
            block a few hosts, send allow ["*"] with them.
    """

    allow: Sequence[str] = ()
    """"*" (anywhere), a domain ("pypi.org"), its subdomains ("*.github.com"), an IP or a CIDR. A
    domain means its ports 80 and 443 unless ":port" names another ("github.com:22"). Empty:
    nowhere. The sandbox's DNS resolves only the names a domain entry (or "*") allows. With deny,
    at most 100 entries, each at most 255 bytes. update_sandbox says how a connection is judged.
    """

    deny: Sequence[str] = ()
    """Exceptions to allow, written the same way; they win. Sent alone, allow is empty: nowhere. To
    block a few hosts, send allow ["*"] with them.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.egress_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Egress:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.egress_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Ingress:
    """The ports anyone may open at their own address; any other port needs `Pethost-Token`
    (create_link port).

    Attributes:
        public_ports: At most 20. The desktop's own ports, its views' 5900, 5901, 6080 and 6081 and its browser's 9222
            and 9223, answer nobody at a port's address, public or with a token: the desktop and browser
            links reach them (create_link).
    """

    public_ports: Sequence[PublicPort] = ()
    """At most 20. The desktop's own ports, its views' 5900, 5901, 6080 and 6081 and its browser's 9222
    and 9223, answer nobody at a port's address, public or with a token: the desktop and browser
    links reach them (create_link).
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.ingress_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Ingress:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.ingress_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PublicPort:
    """
    Attributes:
        url: Output: https://<port>-<sandbox id>.<server>
    """

    port: int = 0

    url: str = ""
    """Output: https://<port>-<sandbox id>.<server>"""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.public_port_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PublicPort:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.public_port_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Environment:
    """What every process started in the sandbox gets, over its template image's ENV.

    Attributes:
        variables: At most 100; their names, values and secrets' names 32 KiB in all.
    """

    variables: Sequence[EnvVar] = ()
    """At most 100; their names, values and secrets' names 32 KiB in all."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.environment_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Environment:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.environment_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class EnvVar:
    """At most one of `value`, `secret`. The others are None.

    Attributes:
        name: DEBUG, ANTHROPIC_API_KEY
        secret: A workspace secret's name (get_workspace lists them): the variable holds a placeholder,
            which the egress proxy swaps for the value in requests to the secret's hosts. egress must
            allow them.
    """

    name: str = ""
    """DEBUG, ANTHROPIC_API_KEY"""

    value: str | None = None

    secret: str | None = None
    """A workspace secret's name (get_workspace lists them): the variable holds a placeholder,
    which the egress proxy swaps for the value in requests to the secret's hosts. egress must
    allow them.
    """

    @overload
    def __init__(
        self,
        *,
        name: str = "",
        value: None = None,
        secret: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        name: str = "",
        value: str,
        secret: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        name: str = "",
        value: None = None,
        secret: str,
    ) -> None: ...

    def __init__(
        self,
        *,
        name: str = "",
        value: str | None = None,
        secret: str | None = None,
    ) -> None:
        _one_of("EnvVar", value=value, secret=secret)
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "value", value)
        object.__setattr__(self, "secret", secret)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.env_var_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EnvVar:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.env_var_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Label:
    """One of the caller's labels: user=42.

    Attributes:
        key: 1 to 255 bytes; unique among a sandbox's labels.
        value: At most 255 bytes.
    """

    key: str = ""
    """1 to 255 bytes; unique among a sandbox's labels."""

    value: str = ""
    """At most 255 bytes."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.label_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Label:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.label_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class GetSandboxMetricsResponse:
    points: Sequence[MetricsPoint] = ()

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.get_sandbox_metrics_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> GetSandboxMetricsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.get_sandbox_metrics_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MetricsPoint:
    """
    Attributes:
        cpu_percent: Of all its vCPUs: 100 = every vCPU busy.
        network_in_bytes: Since the previous point.
    """

    time: datetime | None = None

    cpu_percent: float = 0.0
    """Of all its vCPUs: 100 = every vCPU busy."""

    memory_used_bytes: int = 0

    disk_used_bytes: int = 0

    network_in_bytes: int = 0
    """Since the previous point."""

    network_out_bytes: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.metrics_point_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MetricsPoint:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.metrics_point_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListSandboxEventsResponse:
    """
    Attributes:
        more: More events match than `limit`.
    """

    events: Sequence[SandboxEvent] = ()

    more: bool = False
    """More events match than `limit`."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_sandbox_events_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListSandboxEventsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_sandbox_events_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class SandboxEvent:
    """At most one of `lifecycle`, `command`, `egress`, `port`, `agent_turn`. The others are None.

    Attributes:
        event_id: 16 digits: a later event's id is greater, compared as text or as a number.
    """

    event_id: str = ""
    """16 digits: a later event's id is greater, compared as text or as a number."""

    time: datetime | None = None

    lifecycle: LifecycleEvent | None = None

    command: CommandEvent | None = None

    egress: EgressEvent | None = None

    port: PortEvent | None = None

    agent_turn: AgentTurnEvent | None = None

    @overload
    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: None = None,
        command: None = None,
        egress: None = None,
        port: None = None,
        agent_turn: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: LifecycleEvent,
        command: None = None,
        egress: None = None,
        port: None = None,
        agent_turn: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: None = None,
        command: CommandEvent,
        egress: None = None,
        port: None = None,
        agent_turn: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: None = None,
        command: None = None,
        egress: EgressEvent,
        port: None = None,
        agent_turn: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: None = None,
        command: None = None,
        egress: None = None,
        port: PortEvent,
        agent_turn: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: None = None,
        command: None = None,
        egress: None = None,
        port: None = None,
        agent_turn: AgentTurnEvent,
    ) -> None: ...

    def __init__(
        self,
        *,
        event_id: str = "",
        time: datetime | None = None,
        lifecycle: LifecycleEvent | None = None,
        command: CommandEvent | None = None,
        egress: EgressEvent | None = None,
        port: PortEvent | None = None,
        agent_turn: AgentTurnEvent | None = None,
    ) -> None:
        _one_of("SandboxEvent", lifecycle=lifecycle, command=command, egress=egress, port=port, agent_turn=agent_turn)
        object.__setattr__(self, "event_id", event_id)
        object.__setattr__(self, "time", time)
        object.__setattr__(self, "lifecycle", lifecycle)
        object.__setattr__(self, "command", command)
        object.__setattr__(self, "egress", egress)
        object.__setattr__(self, "port", port)
        object.__setattr__(self, "agent_turn", agent_turn)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.sandbox_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> SandboxEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.sandbox_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class LifecycleEvent:
    """It was created, paused, stopped, resumed, resized or deleted.

    Attributes:
        size: CREATED, RESIZED: its size from then on. RESIZED: a RUNNING sandbox restarted at it, a
            STOPPED one takes it at its next start.
        disk_gib: CREATED, RESIZED: its disk from then on.
        state_message: Prose for people, as Sandbox.state_message.
    """

    change: LifecycleChange = LifecycleChange.UNSPECIFIED

    reason: StateReason = StateReason.UNSPECIFIED

    size: Size = Size.UNSPECIFIED
    """CREATED, RESIZED: its size from then on. RESIZED: a RUNNING sandbox restarted at it, a
    STOPPED one takes it at its next start.
    """

    disk_gib: int = 0
    """CREATED, RESIZED: its disk from then on."""

    state_message: str = ""
    """Prose for people, as Sandbox.state_message."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.lifecycle_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> LifecycleEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.lifecycle_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CommandEvent:
    """A command that ended.

    Attributes:
        command: Its first 1024 bytes; "…" ends a longer one.
        exit_code: As Command's: absent when LOST.
    """

    command_id: str = ""

    command: str = ""
    """Its first 1024 bytes; "…" ends a longer one."""

    state: CommandState = CommandState.UNSPECIFIED

    exit_code: int | None = None
    """As Command's: absent when LOST."""

    duration_ms: int = 0

    started_by: StartedBy = StartedBy.UNSPECIFIED

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.command_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CommandEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.command_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class EgressEvent:
    """Its connections out to one host in one minute. A minute keeps 200 hosts and ports apart: the
    connections to any more are counted together, in one event with no host and port 0.

    Attributes:
        host: The name it asked for (TLS SNI, HTTP Host or DNS), else the IP.
        secrets: The secrets swapped into its requests, by name.
    """

    host: str = ""
    """The name it asked for (TLS SNI, HTTP Host or DNS), else the IP."""

    port: int = 0

    allowed: bool = False

    connections: int = 0

    bytes_out: int = 0

    bytes_in: int = 0

    secrets: Sequence[str] = ()
    """The secrets swapped into its requests, by name."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.egress_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> EgressEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.egress_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class PortEvent:
    """Requests to one of its ports in one minute. A minute keeps 200 ports apart: the requests to
    any more are counted together, in one event with port 0.

    Attributes:
        server_errors: Answered 5xx.
    """

    port: int = 0

    requests: int = 0

    server_errors: int = 0
    """Answered 5xx."""

    bytes_in: int = 0

    bytes_out: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.port_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> PortEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.port_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class AgentTurnEvent:
    """A coding agent's turn, once ended.

    Attributes:
        prompt: Its first 200 characters.
    """

    turn_id: str = ""

    conversation_id: str = ""

    agent: Agent = Agent.UNSPECIFIED

    prompt: str = ""
    """Its first 200 characters."""

    state: AgentTurnState = AgentTurnState.UNSPECIFIED

    input_tokens: int = 0

    output_tokens: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.agent_turn_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AgentTurnEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.agent_turn_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Template:
    """One version of a template: ours, "base" (Ubuntu with build tools, Python, Node.js, the coding
    agents, Docker and a desktop with Chrome, its version named by what it holds: base), or the
    workspace's, a sandbox's disk saved over ours, shrunk to what it holds and kept in object
    storage, which every server starts sandboxes from (create_template). A sandbox starts with no
    process of its template's, and with its own hostname (its id), machine-id and randomness. Its
    desktop starts at its first control_desktop or desktop link (some seconds), and Docker's daemon
    at the first connection to /var/run/docker.sock: neither costs anything until then. Docker's
    images and containers are on the sandbox's disk, so a stop keeps them and a template carries
    them.

    Attributes:
        name: a-z, 0-9 and "-": "base", "my-app".
        version: create_sandbox takes "my-app@3" for exactly this one.
        failure_message: FAILED: what failed.
        built_in: Ours, for every workspace.
        settings: What its sandboxes get unless create_sandbox says.
        size_bytes: A workspace's READY version: what it takes in object storage, its own chunks compressed and
            encrypted, what Limits.template_gib counts. 0 while SAVING, when FAILED, and for ours.
        base: The version of our base its sandboxes start on, named by the sha256 of what it holds: the
            operating system, its packages and the guest kernel. A version saved from a sandbox keeps the
            base that sandbox started on, and a sandbox keeps its base for as long as it lives.
        min_size: A workspace's READY version: the smallest size whose disk holds what it saved. Its sandboxes
            take any size from it up, the one it was saved from among them.
    """

    name: str = ""
    """a-z, 0-9 and "-": "base", "my-app"."""

    version: int = 0
    """create_sandbox takes "my-app@3" for exactly this one."""

    state: TemplateState = TemplateState.UNSPECIFIED

    failure_message: str = ""
    """FAILED: what failed."""

    built_in: bool = False
    """Ours, for every workspace."""

    description: str = ""

    settings: SandboxSettings | None = None
    """What its sandboxes get unless create_sandbox says."""

    create_time: datetime | None = None

    size_bytes: int = 0
    """A workspace's READY version: what it takes in object storage, its own chunks compressed and
    encrypted, what Limits.template_gib counts. 0 while SAVING, when FAILED, and for ours.
    """

    base: str = ""
    """The version of our base its sandboxes start on, named by the sha256 of what it holds: the
    operating system, its packages and the guest kernel. A version saved from a sandbox keeps the
    base that sandbox started on, and a sandbox keeps its base for as long as it lives.
    """

    min_size: Size = Size.UNSPECIFIED
    """A workspace's READY version: the smallest size whose disk holds what it saved. Its sandboxes
    take any size from it up, the one it was saved from among them.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.template_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Template:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.template_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListTemplatesResponse:
    """
    Attributes:
        next_page_token: Absent on the last page.
    """

    templates: Sequence[Template] = ()

    next_page_token: str = ""
    """Absent on the last page."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_templates_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListTemplatesResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_templates_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListUsageResponse:
    """
    Attributes:
        next_page_token: Absent on the last page.
    """

    rows: Sequence[UsageRow] = ()

    next_page_token: str = ""
    """Absent on the last page."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_usage_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListUsageResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_usage_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class UsageRow:
    """
    Attributes:
        day: Midnight UTC.
        unit_hours: RUNNING and PAUSED: hours of sandboxes of size; the others: GiB-hours.
        size: RUNNING's and PAUSED's.
        cost_micros: What it cost, at the rates of the time it was used, in millionths of the unit of
            Workspace.billing's currency. Absent = it was not billed. Below zero: a credit, for what a
            server counted again lower than it was charged.
    """

    day: datetime | None = None
    """Midnight UTC."""

    meter: Meter = Meter.UNSPECIFIED

    unit_hours: float = 0.0
    """RUNNING and PAUSED: hours of sandboxes of size; the others: GiB-hours."""

    size: Size = Size.UNSPECIFIED
    """RUNNING's and PAUSED's."""

    cost_micros: int = 0
    """What it cost, at the rates of the time it was used, in millionths of the unit of
    Workspace.billing's currency. Absent = it was not billed. Below zero: a credit, for what a
    server counted again lower than it was charged.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.usage_row_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> UsageRow:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.usage_row_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Command:
    """
    Attributes:
        command: Its first 1024 bytes; "…" ends a longer one.
        exit_code: EXITED or STOPPED, as a shell has it: 128 + n when signal n ended it. Absent while it runs
            and when LOST.
        stdout: The last 32 KiB it wrote after get_command's stdout_after_bytes, as UTF-8 (other bytes
            replaced).
        stderr: Likewise, after stderr_after_bytes.
        stdout_bytes: All it has written: pass it as stdout_after_bytes to read only what is new.
        output_truncated: stdout or stderr lost its beginning to the 32 KiB.
        end_time: Absent while RUNNING.
    """

    command_id: str = ""

    command: str = ""
    """Its first 1024 bytes; "…" ends a longer one."""

    state: CommandState = CommandState.UNSPECIFIED

    exit_code: int | None = None
    """EXITED or STOPPED, as a shell has it: 128 + n when signal n ended it. Absent while it runs
    and when LOST.
    """

    stdout: str = ""
    """The last 32 KiB it wrote after get_command's stdout_after_bytes, as UTF-8 (other bytes
    replaced).
    """

    stderr: str = ""
    """Likewise, after stderr_after_bytes."""

    stdout_bytes: int = 0
    """All it has written: pass it as stdout_after_bytes to read only what is new."""

    stderr_bytes: int = 0

    output_truncated: bool = False
    """stdout or stderr lost its beginning to the 32 KiB."""

    started_by: StartedBy = StartedBy.UNSPECIFIED

    start_time: datetime | None = None

    end_time: datetime | None = None
    """Absent while RUNNING."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.command_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Command:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.command_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListCommandsResponse:
    """
    Attributes:
        commands: Without stdout and stderr.
    """

    commands: Sequence[Command] = ()
    """Without stdout and stderr."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_commands_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListCommandsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_commands_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class CommandOutput:
    """At most one of `stdout`, `stderr`, `ended`. The others are None.

    Attributes:
        ended: The last message: the command as it ended.
    """

    stdout: bytes | None = None

    stderr: bytes | None = None

    ended: Command | None = None
    """The last message: the command as it ended."""

    @overload
    def __init__(
        self,
        *,
        stdout: None = None,
        stderr: None = None,
        ended: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        stdout: bytes,
        stderr: None = None,
        ended: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        stdout: None = None,
        stderr: bytes,
        ended: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        stdout: None = None,
        stderr: None = None,
        ended: Command,
    ) -> None: ...

    def __init__(
        self,
        *,
        stdout: bytes | None = None,
        stderr: bytes | None = None,
        ended: Command | None = None,
    ) -> None:
        _one_of("CommandOutput", stdout=stdout, stderr=stderr, ended=ended)
        object.__setattr__(self, "stdout", stdout)
        object.__setattr__(self, "stderr", stderr)
        object.__setattr__(self, "ended", ended)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.command_output_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CommandOutput:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.command_output_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class File:
    """At most one of `text`, `data`. The others are None.

    Attributes:
        text: What was read, when it is UTF-8.
        data: Otherwise. An MCP tool's answer leaves it out: a model cannot read it.
        size_bytes: The whole file's.
    """

    path: str = ""

    text: str | None = None
    """What was read, when it is UTF-8."""

    data: bytes | None = None
    """Otherwise. An MCP tool's answer leaves it out: a model cannot read it."""

    size_bytes: int = 0
    """The whole file's."""

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        size_bytes: int = 0,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: str,
        data: None = None,
        size_bytes: int = 0,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: bytes,
        size_bytes: int = 0,
    ) -> None: ...

    def __init__(
        self,
        *,
        path: str = "",
        text: str | None = None,
        data: bytes | None = None,
        size_bytes: int = 0,
    ) -> None:
        _one_of("File", text=text, data=data)
        object.__setattr__(self, "path", path)
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "data", data)
        object.__setattr__(self, "size_bytes", size_bytes)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.file_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> File:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.file_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListFilesResponse:
    """
    Attributes:
        next_page_token: Absent on the last page.
    """

    files: Sequence[FileInfo] = ()

    next_page_token: str = ""
    """Absent on the last page."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_files_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListFilesResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_files_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class FileInfo:
    """
    Attributes:
        mode: "0644\"
    """

    path: str = ""

    kind: FileKind = FileKind.UNSPECIFIED

    size_bytes: int = 0

    mode: str = ""
    """"0644\""""

    owner: str = ""

    modify_time: datetime | None = None

    symlink_target: str = ""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.file_info_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FileInfo:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.file_info_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class FileChange:
    """One change at a path. Missing parent directories are made.

    At most one of `text`, `data`, `edit`, `move_to`, `delete`, `make_directory`. The others are None.

    Attributes:
        text: Creates or replaces the file with this text.
        data: Creates or replaces the file with these bytes.
        move_to: Moves or renames it; replaces a file there.
        delete: A file, or a directory and all in it. Nothing there is no error.
        make_directory: An existing one is no error.
        mode: text or data: absent = "0644", or the replaced file's.
    """

    path: str = ""

    text: str | None = None
    """Creates or replaces the file with this text."""

    data: bytes | None = None
    """Creates or replaces the file with these bytes."""

    edit: TextEdit | None = None

    move_to: str | None = None
    """Moves or renames it; replaces a file there."""

    delete: Delete | None = None
    """A file, or a directory and all in it. Nothing there is no error."""

    make_directory: MakeDirectory | None = None
    """An existing one is no error."""

    mode: str = ""
    """text or data: absent = "0644", or the replaced file's."""

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        edit: None = None,
        move_to: None = None,
        delete: None = None,
        make_directory: None = None,
        mode: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: str,
        data: None = None,
        edit: None = None,
        move_to: None = None,
        delete: None = None,
        make_directory: None = None,
        mode: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: bytes,
        edit: None = None,
        move_to: None = None,
        delete: None = None,
        make_directory: None = None,
        mode: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        edit: TextEdit,
        move_to: None = None,
        delete: None = None,
        make_directory: None = None,
        mode: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        edit: None = None,
        move_to: str,
        delete: None = None,
        make_directory: None = None,
        mode: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        edit: None = None,
        move_to: None = None,
        delete: Delete,
        make_directory: None = None,
        mode: str = "",
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        path: str = "",
        text: None = None,
        data: None = None,
        edit: None = None,
        move_to: None = None,
        delete: None = None,
        make_directory: MakeDirectory,
        mode: str = "",
    ) -> None: ...

    def __init__(
        self,
        *,
        path: str = "",
        text: str | None = None,
        data: bytes | None = None,
        edit: TextEdit | None = None,
        move_to: str | None = None,
        delete: Delete | None = None,
        make_directory: MakeDirectory | None = None,
        mode: str = "",
    ) -> None:
        _one_of("FileChange", text=text, data=data, edit=edit, move_to=move_to, delete=delete, make_directory=make_directory)
        object.__setattr__(self, "path", path)
        object.__setattr__(self, "text", text)
        object.__setattr__(self, "data", data)
        object.__setattr__(self, "edit", edit)
        object.__setattr__(self, "move_to", move_to)
        object.__setattr__(self, "delete", delete)
        object.__setattr__(self, "make_directory", make_directory)
        object.__setattr__(self, "mode", mode)

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
class Delete:
    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.delete_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Delete:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.delete_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MakeDirectory:
    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.make_directory_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MakeDirectory:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.make_directory_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class TextEdit:
    """Replaces text in the file: old_text must occur in it exactly once. The file is at most
    16 MiB.
    """

    old_text: str = ""

    new_text: str = ""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.text_edit_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TextEdit:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.text_edit_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class WriteFilesResponse:
    """
    Attributes:
        done_count: Fewer than sent when one failed.
        failure_message: Why the next one failed.
        failure: Why the next one failed, to branch on.
    """

    done_count: int = 0
    """Fewer than sent when one failed."""

    failure_message: str = ""
    """Why the next one failed."""

    failure: FileFailure = FileFailure.UNSPECIFIED
    """Why the next one failed, to branch on."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.write_files_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WriteFilesResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.write_files_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class FileEvent:
    """
    Attributes:
        path: RENAMED: where it was.
        to_path: RENAMED: where it went, when that is under the watched path too.
    """

    path: str = ""
    """RENAMED: where it was."""

    kind: FileEventKind = FileEventKind.UNSPECIFIED

    to_path: str = ""
    """RENAMED: where it went, when that is under the watched path too."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.file_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> FileEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.file_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ScreenRegion:
    """A rectangle of the screen, in its pixels.

    Attributes:
        x: Its left edge.
        y: Its top edge.
    """

    x: int = 0
    """Its left edge."""

    y: int = 0
    """Its top edge."""

    width: int = 0

    height: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.screen_region_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ScreenRegion:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.screen_region_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ControlDesktopResponse:
    """
    Attributes:
        done_count: Fewer than asked when one failed.
        failure_message: Why the next one failed.
        failure: Why the next one failed, to branch on.
    """

    done_count: int = 0
    """Fewer than asked when one failed."""

    failure_message: str = ""
    """Why the next one failed."""

    screenshot: Screenshot | None = None

    failure: DesktopFailure = DesktopFailure.UNSPECIFIED
    """Why the next one failed, to branch on."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.control_desktop_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ControlDesktopResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.control_desktop_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Screenshot:
    """Coordinates are pixels of the screen (Sandbox.desktop), from the top left.

    Attributes:
        image: Empty with skip_screenshot.
        mime_type: "image/png"
        width: The image's, the screen's with skip_screenshot.
        scale: How many times larger than the screen's pixels the image's are: 1, or more for a
            screenshot_region.
    """

    image: bytes = b""
    """Empty with skip_screenshot."""

    mime_type: str = ""
    """"image/png\""""

    width: int = 0
    """The image's, the screen's with skip_screenshot."""

    height: int = 0

    cursor_x: int = 0

    cursor_y: int = 0

    scale: int = 0
    """How many times larger than the screen's pixels the image's are: 1, or more for a
    screenshot_region.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.screenshot_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Screenshot:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.screenshot_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class DesktopAction:
    """At most one of `click`, `move_mouse`, `drag`, `scroll`, `type_text`, `press_keys`, `wait_ms`, `mouse_down`, `mouse_up`, `hold_keys`. The others are None.

    Attributes:
        type_text: Text to type.
        press_keys: Keys pressed together, joined by "+": "Return", "ctrl+c", "ctrl+shift+t"; several such,
            apart by spaces, one after the other: "ctrl+a BackSpace", "Down Down Down".
        wait_ms: At most 30000.
        mouse_down: Presses a button where the pointer is (move_mouse first) and leaves it down, across calls,
            until its mouse_up: a drag the caller moves itself.
        mouse_up: Lets a button go where the pointer is.
    """

    click: Click | None = None

    move_mouse: Point | None = None

    drag: Drag | None = None

    scroll: Scroll | None = None

    type_text: str | None = None
    """Text to type."""

    press_keys: str | None = None
    """Keys pressed together, joined by "+": "Return", "ctrl+c", "ctrl+shift+t"; several such,
    apart by spaces, one after the other: "ctrl+a BackSpace", "Down Down Down".
    """

    wait_ms: int | None = None
    """At most 30000."""

    mouse_down: MouseButtonChange | None = None
    """Presses a button where the pointer is (move_mouse first) and leaves it down, across calls,
    until its mouse_up: a drag the caller moves itself.
    """

    mouse_up: MouseButtonChange | None = None
    """Lets a button go where the pointer is."""

    hold_keys: HoldKeys | None = None

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: Click,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: Point,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: Drag,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: Scroll,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: str,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: str,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: int,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: MouseButtonChange,
        mouse_up: None = None,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: MouseButtonChange,
        hold_keys: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        click: None = None,
        move_mouse: None = None,
        drag: None = None,
        scroll: None = None,
        type_text: None = None,
        press_keys: None = None,
        wait_ms: None = None,
        mouse_down: None = None,
        mouse_up: None = None,
        hold_keys: HoldKeys,
    ) -> None: ...

    def __init__(
        self,
        *,
        click: Click | None = None,
        move_mouse: Point | None = None,
        drag: Drag | None = None,
        scroll: Scroll | None = None,
        type_text: str | None = None,
        press_keys: str | None = None,
        wait_ms: int | None = None,
        mouse_down: MouseButtonChange | None = None,
        mouse_up: MouseButtonChange | None = None,
        hold_keys: HoldKeys | None = None,
    ) -> None:
        _one_of("DesktopAction", click=click, move_mouse=move_mouse, drag=drag, scroll=scroll, type_text=type_text, press_keys=press_keys, wait_ms=wait_ms, mouse_down=mouse_down, mouse_up=mouse_up, hold_keys=hold_keys)
        object.__setattr__(self, "click", click)
        object.__setattr__(self, "move_mouse", move_mouse)
        object.__setattr__(self, "drag", drag)
        object.__setattr__(self, "scroll", scroll)
        object.__setattr__(self, "type_text", type_text)
        object.__setattr__(self, "press_keys", press_keys)
        object.__setattr__(self, "wait_ms", wait_ms)
        object.__setattr__(self, "mouse_down", mouse_down)
        object.__setattr__(self, "mouse_up", mouse_up)
        object.__setattr__(self, "hold_keys", hold_keys)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.desktop_action_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DesktopAction:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.desktop_action_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class MouseButtonChange:
    """
    Attributes:
        button: Absent = LEFT.
    """

    button: MouseButton = MouseButton.UNSPECIFIED
    """Absent = LEFT."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.mouse_button_change_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> MouseButtonChange:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.mouse_button_change_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class HoldKeys:
    """Keys held down together for a time, then let go.

    Attributes:
        keys: Joined by "+": "shift", "ctrl+alt".
        duration_ms: At most 30000.
    """

    keys: str = ""
    """Joined by "+": "shift", "ctrl+alt"."""

    duration_ms: int = 0
    """At most 30000."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.hold_keys_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> HoldKeys:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.hold_keys_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Point:
    x: int = 0

    y: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.point_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Point:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.point_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Click:
    """
    Attributes:
        button: Absent = LEFT.
        count: Absent = 1; 2 double-clicks, 3 triple-clicks.
        hold_keys: Held while clicking: "shift", "ctrl+alt".
        at_pointer: True = where the pointer is, whatever x and y say.
    """

    x: int = 0

    y: int = 0

    button: MouseButton = MouseButton.UNSPECIFIED
    """Absent = LEFT."""

    count: int = 0
    """Absent = 1; 2 double-clicks, 3 triple-clicks."""

    hold_keys: str = ""
    """Held while clicking: "shift", "ctrl+alt"."""

    at_pointer: bool = False
    """True = where the pointer is, whatever x and y say."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.click_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Click:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.click_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Drag:
    """
    Attributes:
        path: From the first point to the last, the left button down.
        hold_keys: Held while dragging: "shift", "ctrl+alt".
    """

    path: Sequence[Point] = ()
    """From the first point to the last, the left button down."""

    hold_keys: str = ""
    """Held while dragging: "shift", "ctrl+alt"."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.drag_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Drag:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.drag_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Scroll:
    """
    Attributes:
        down: Wheel clicks; negative scrolls up.
        right: Negative scrolls left.
        hold_keys: Held while scrolling: "shift", "ctrl".
        at_pointer: True = where the pointer is, whatever x and y say.
    """

    x: int = 0

    y: int = 0

    down: int = 0
    """Wheel clicks; negative scrolls up."""

    right: int = 0
    """Negative scrolls left."""

    hold_keys: str = ""
    """Held while scrolling: "shift", "ctrl"."""

    at_pointer: bool = False
    """True = where the pointer is, whatever x and y say."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.scroll_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Scroll:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.scroll_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Desktop:
    """A screen, in pixels."""

    width: int = 0

    height: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.desktop_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Desktop:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.desktop_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class TerminalLink:
    """A terminal page; a WebSocket to the same URL carries its bytes both ways, and the text message
    {"resize":{"cols":C,"rows":R}} resizes it.

    Attributes:
        command: Run instead of a login shell: "claude". Absent = bash.
    """

    command: str = ""
    """Run instead of a login shell: "claude". Absent = bash."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.terminal_link_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> TerminalLink:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.terminal_link_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class DesktopLink:
    """A page that shows the screen live, the desktop started first if it does not run.

    Attributes:
        view_only: True = the viewer cannot click or type.
    """

    view_only: bool = False
    """True = the viewer cannot click or type."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.desktop_link_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> DesktopLink:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.desktop_link_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class BrowserLink:
    """The browser on the sandbox's desktop, for a program that drives it: Link.url is the WebSocket of
    the Chrome DevTools Protocol, "wss://browser-<id>.<server>/<token>", which Playwright's
    chromium.connectOverCDP(url), Puppeteer's connect({browserWSEndpoint: url}), browser-use and
    Stagehand take as it is; "https://" in its place answers <that>/json/version and
    <that>/json/list, for a client that adds those to an HTTP address as Playwright does (Puppeteer
    takes the WebSocket: browserWSEndpoint), and every WebSocket path under it reaches the same
    browser. It is the Chrome the desktop shows, started with the desktop if it does not run (some
    seconds), so a desktop link watches what the program does, and control_desktop acts on the same
    pages; inside the sandbox a program takes http://localhost:9222, where the browser starts at the
    first connection, and the coding agents have it as their "browser" MCP server. Its profile is on
    the sandbox's disk: a stop keeps the sites it is signed in to, and a template saved from the
    sandbox carries them to every sandbox started from it. One browser a sandbox: a program that
    wants several at once uses several sandboxes. Whoever holds the link drives the browser as the
    sandbox's person, its files and signed-in sites within reach: give it only to a program you
    trust. A connection is a session, as a terminal is: the sandbox does not idle while one is open,
    and revoke_tokens ends it. A sandbox on a base before this link is refused, saying so: one
    created from the template "base" has it, while a template saved on an older base keeps that base.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.browser_link_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> BrowserLink:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.browser_link_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Link:
    """
    Attributes:
        url: The link itself, its token in it; a port's address, for a port.
        token: A port's token, sent as `Pethost-Token: <token>`; empty for any other link.
    """

    url: str = ""
    """The link itself, its token in it; a port's address, for a port."""

    expire_time: datetime | None = None

    token: str = ""
    """A port's token, sent as `Pethost-Token: <token>`; empty for any other link."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.link_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Link:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.link_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class AgentTurn:
    """
    Attributes:
        model: As the agent reported it; absent when it did not say (Codex on its default).
        reply: DONE: its last message, up to 16 KiB.
        failure_message: FAILED: why.
        input_tokens: Every prompt token of the turn, read from a cache or not.
        output_tokens: Reasoning included.
        end_time: Absent until it ends.
    """

    turn_id: str = ""

    conversation_id: str = ""

    agent: Agent = Agent.UNSPECIFIED

    model: str = ""
    """As the agent reported it; absent when it did not say (Codex on its default)."""

    state: AgentTurnState = AgentTurnState.UNSPECIFIED

    reply: str = ""
    """DONE: its last message, up to 16 KiB."""

    failure_message: str = ""
    """FAILED: why."""

    input_tokens: int = 0
    """Every prompt token of the turn, read from a cache or not."""

    output_tokens: int = 0
    """Reasoning included."""

    start_time: datetime | None = None

    end_time: datetime | None = None
    """Absent until it ends."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.agent_turn_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AgentTurn:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.agent_turn_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ListConversationsResponse:
    """
    Attributes:
        next_page_token: Absent on the last page.
    """

    conversations: Sequence[Conversation] = ()

    next_page_token: str = ""
    """Absent on the last page."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.list_conversations_response_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ListConversationsResponse:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.list_conversations_response_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Conversation:
    """
    Attributes:
        running_turn_id: Absent when it waits for a prompt.
        input_tokens: All its turns.
    """

    conversation_id: str = ""

    agent: Agent = Agent.UNSPECIFIED

    model: str = ""

    cwd: str = ""

    running_turn_id: str = ""
    """Absent when it waits for a prompt."""

    input_tokens: int = 0
    """All its turns."""

    output_tokens: int = 0

    create_time: datetime | None = None

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.conversation_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Conversation:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.conversation_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True, init=False)
class AgentEvent:
    """What an agent did, the same for every agent.

    At most one of `prompt`, `message`, `tool_call`, `tool_result`, `turn_end`, `caught_up`. The others are None.

    Attributes:
        seq: 1, 2, 3, ... within the conversation.
        message: Text it wrote: the first 64 KiB.
        tool_call: A command it ran, a file it read or edited, a search...
        turn_end: The turn as it ended.
        caught_up: watch_conversation only, once: the events before it were there when the stream opened;
            what follows is live. Its seq is the last one sent, or after_seq when none was; or the
            conversation's last, when that is before after_seq: a sandbox that lost its memory may
            have lost its last events, and the next ones take their seq again.
    """

    seq: int = 0
    """1, 2, 3, ... within the conversation."""

    time: datetime | None = None

    turn_id: str = ""

    prompt: str | None = None

    message: str | None = None
    """Text it wrote: the first 64 KiB."""

    tool_call: ToolCall | None = None
    """A command it ran, a file it read or edited, a search..."""

    tool_result: ToolResult | None = None

    turn_end: AgentTurn | None = None
    """The turn as it ended."""

    caught_up: CaughtUp | None = None
    """watch_conversation only, once: the events before it were there when the stream opened;
    what follows is live. Its seq is the last one sent, or after_seq when none was; or the
    conversation's last, when that is before after_seq: a sandbox that lost its memory may
    have lost its last events, and the next ones take their seq again.
    """

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: None = None,
        message: None = None,
        tool_call: None = None,
        tool_result: None = None,
        turn_end: None = None,
        caught_up: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: str,
        message: None = None,
        tool_call: None = None,
        tool_result: None = None,
        turn_end: None = None,
        caught_up: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: None = None,
        message: str,
        tool_call: None = None,
        tool_result: None = None,
        turn_end: None = None,
        caught_up: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: None = None,
        message: None = None,
        tool_call: ToolCall,
        tool_result: None = None,
        turn_end: None = None,
        caught_up: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: None = None,
        message: None = None,
        tool_call: None = None,
        tool_result: ToolResult,
        turn_end: None = None,
        caught_up: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: None = None,
        message: None = None,
        tool_call: None = None,
        tool_result: None = None,
        turn_end: AgentTurn,
        caught_up: None = None,
    ) -> None: ...

    @overload
    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: None = None,
        message: None = None,
        tool_call: None = None,
        tool_result: None = None,
        turn_end: None = None,
        caught_up: CaughtUp,
    ) -> None: ...

    def __init__(
        self,
        *,
        seq: int = 0,
        time: datetime | None = None,
        turn_id: str = "",
        prompt: str | None = None,
        message: str | None = None,
        tool_call: ToolCall | None = None,
        tool_result: ToolResult | None = None,
        turn_end: AgentTurn | None = None,
        caught_up: CaughtUp | None = None,
    ) -> None:
        _one_of("AgentEvent", prompt=prompt, message=message, tool_call=tool_call, tool_result=tool_result, turn_end=turn_end, caught_up=caught_up)
        object.__setattr__(self, "seq", seq)
        object.__setattr__(self, "time", time)
        object.__setattr__(self, "turn_id", turn_id)
        object.__setattr__(self, "prompt", prompt)
        object.__setattr__(self, "message", message)
        object.__setattr__(self, "tool_call", tool_call)
        object.__setattr__(self, "tool_result", tool_result)
        object.__setattr__(self, "turn_end", turn_end)
        object.__setattr__(self, "caught_up", caught_up)

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.agent_event_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AgentEvent:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.agent_event_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class CaughtUp:
    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.caught_up_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> CaughtUp:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.caught_up_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ToolCall:
    """A call may have no ToolResult: an agent can leave a command running and go on without it.

    Attributes:
        name: As the agent names it: "Bash", "Edit", "shell".
        input: JSON; over 64 KiB: {"truncated": true, "bytes": <its size>}.
    """

    tool_call_id: str = ""

    name: str = ""
    """As the agent names it: "Bash", "Edit", "shell"."""

    input: str = ""
    """JSON; over 64 KiB: {"truncated": true, "bytes": <its size>}."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.tool_call_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ToolCall:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.tool_call_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class ToolResult:
    """
    Attributes:
        output: The first 64 KiB.
    """

    tool_call_id: str = ""

    output: str = ""
    """The first 64 KiB."""

    failed: bool = False

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.tool_result_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> ToolResult:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.tool_result_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class LimitReached:
    """ResourceExhaustedError: a limit of the workspace.

    Attributes:
        limit: A field of Workspace.limits: "vcpus", "largest_size" (max is that Size's number),
            "template_versions", "template_gib"; or a bound of every workspace: "secrets"
            (set_secret), or "starts_per_minute", the sandboxes it may start in any minute, against
            abuse. A start is free: a create_sandbox, or a resume_sandbox of a STOPPED sandbox. A
            resume_sandbox of a PAUSED one, and a wake by a call into one (IDLE AND WAKE), are none.
        retry_time: starts_per_minute: when enough starts have left the minute for the call to fit, which may
            be retried then.
    """

    limit: str = ""
    """A field of Workspace.limits: "vcpus", "largest_size" (max is that Size's number),
    "template_versions", "template_gib"; or a bound of every workspace: "secrets"
    (set_secret), or "starts_per_minute", the sandboxes it may start in any minute, against
    abuse. A start is free: a create_sandbox, or a resume_sandbox of a STOPPED sandbox. A
    resume_sandbox of a PAUSED one, and a wake by a call into one (IDLE AND WAKE), are none.
    """

    max: int = 0

    retry_time: datetime | None = None
    """starts_per_minute: when enough starts have left the minute for the call to fit, which may
    be retried then.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.limit_reached_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> LimitReached:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.limit_reached_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Stopped:
    """FailedPreconditionError from a call into a sandbox, an SSH login or a request to a port while it
    is STOPPED and its lifecycle does not wake it (Lifecycle.wake_when_stopped): resume_sandbox
    starts it.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.stopped_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Stopped:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.stopped_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class UsageUnpaid:
    """FailedPreconditionError: nothing pays for the workspace's usage now (Billing.suspended), so the
    call starts, resumes or wakes no sandbox, and makes no template: its owner adds to
    the balance, or starts the plan if it is in its trial, in the workspace's settings.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.usage_unpaid_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> UsageUnpaid:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.usage_unpaid_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class Restoring:
    """UnavailableError from a call into a sandbox, an SSH login or a request to a port while its disk is
    fetched from object storage for its start (Sandbox.restore): try again in a while.
    """

    fetched_bytes: int = 0

    total_bytes: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.restoring_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Restoring:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.restoring_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class NoCapacity:
    """UnavailableError: no room for it now.

    Attributes:
        bound: What the server that refused it lacked; absent when no server was asked, none having room
            by what they report.
    """

    bound: RoomBound = RoomBound.UNSPECIFIED
    """What the server that refused it lacked; absent when no server was asked, none having room
    by what they report.
    """

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.no_capacity_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> NoCapacity:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.no_capacity_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class NameTaken:
    """AlreadyExistsError: a sandbox of the workspace that is not DELETED has the name.

    Attributes:
        sandbox_id: The sandbox that has it.
    """

    sandbox_id: str = ""
    """The sandbox that has it."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.name_taken_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> NameTaken:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.name_taken_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class WorkspaceChoice:
    """FailedPreconditionError: the call must name its `workspace`.

    Attributes:
        workspaces: Their workspace_id and name, at most 20.
    """

    workspaces: Sequence[Workspace] = ()
    """Their workspace_id and name, at most 20."""

    total: int = 0

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.workspace_choice_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> WorkspaceChoice:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.workspace_choice_from_dict(data)


@final
@dataclass(frozen=True, slots=True, kw_only=True)
class AgentSignIn:
    """FailedPreconditionError from prompt_agent: the agent cannot reach its model.

    Attributes:
        variable: Bind a secret to it (settings.environment): "ANTHROPIC_API_KEY".
        sign_in_command: Or a person runs this in the sandbox's terminal: "claude auth login".
    """

    variable: str = ""
    """Bind a secret to it (settings.environment): "ANTHROPIC_API_KEY"."""

    sign_in_command: str = ""
    """Or a person runs this in the sandbox's terminal: "claude auth login"."""

    def to_dict(self) -> dict[str, Any]:
        """This message as the API's JSON has it, for `json.dumps`: a key is the API's name of a field, an
        enum its value's full name, a 64-bit integer a string, a time RFC 3339, bytes base64. What is
        absent is left out, a zero where the type has no None too, and an enum's value this version does
        not know is its number.
        """
        from . import _convert

        return _convert.agent_sign_in_to_dict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> AgentSignIn:
        """The message the API's JSON says, as `json.loads` read it: what `to_dict` gives, and what the API
        answers over HTTP. A key that is no field of the message is a ValueError, as the API refuses it,
        and so is an enum's name this version does not know; a value that is not of its field's kind is
        a ValueError or a TypeError, an integer out of its kind's range an OverflowError.
        """
        from . import _convert

        return _convert.agent_sign_in_from_dict(data)
