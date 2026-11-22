"""What a failed call raises. Generated from v1/sandboxes.proto: do not edit."""

from __future__ import annotations

from typing import TypeAlias

from ._types import AgentSignIn, LimitReached, NameTaken, NoCapacity, Restoring, Stopped, UsageUnpaid, WorkspaceChoice

ErrorDetail: TypeAlias = LimitReached | Stopped | UsageUnpaid | Restoring | NoCapacity | NameTaken | WorkspaceChoice | AgentSignIn
"""What an error may carry beside its message: `match` on its class."""


class SandboxesError(Exception):
    """The API refused a call, or could not be reached. Catch a subclass for one code: what the
    code means for a call is in the method's documentation and in the package's.

    Attributes:
        message: Prose for people: branch on the class and on `detail`, never on this.
        detail: What to branch on, when the API sent one: `LimitReached`, `Stopped`, `UsageUnpaid`, `Restoring`, `NoCapacity`, `NameTaken`, `WorkspaceChoice`, `AgentSignIn`.
            None = none, or one this version does not know.
    """

    message: str
    """Prose for people: branch on the class and on `detail`, never on this."""

    detail: ErrorDetail | None
    """What to branch on, when the API sent one: `LimitReached`, `Stopped`, `UsageUnpaid`, `Restoring`, `NoCapacity`, `NameTaken`, `WorkspaceChoice`, `AgentSignIn`.
    None = none, or one this version does not know.
    """

    def __init__(self, message: str, detail: ErrorDetail | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.detail = detail


class CanceledError(SandboxesError):
    """CANCELED: the call was cancelled, usually by the caller."""


class UnknownError(SandboxesError):
    """UNKNOWN: an error without a code of its own."""


class InvalidArgumentError(SandboxesError):
    """INVALID_ARGUMENT: the request is invalid, whatever the state of what it is about."""


class DeadlineExceededError(SandboxesError):
    """DEADLINE_EXCEEDED: the client's `timeout` ran out before the answer came."""


class NotFoundError(SandboxesError):
    """NOT_FOUND: what the call names does not exist."""


class AlreadyExistsError(SandboxesError):
    """ALREADY_EXISTS: what the call would create exists already."""


class PermissionDeniedError(SandboxesError):
    """PERMISSION_DENIED: the caller may not do this."""


class ResourceExhaustedError(SandboxesError):
    """RESOURCE_EXHAUSTED: a limit or a quota is used up."""


class FailedPreconditionError(SandboxesError):
    """FAILED_PRECONDITION: the state of what the call is about does not allow it."""


class AbortedError(SandboxesError):
    """ABORTED: the call lost to a concurrent change."""


class OutOfRangeError(SandboxesError):
    """OUT_OF_RANGE: the call asks past the valid range."""


class UnimplementedError(SandboxesError):
    """UNIMPLEMENTED: the API does not have this call."""


class InternalError(SandboxesError):
    """INTERNAL: the API itself failed."""


class UnavailableError(SandboxesError):
    """UNAVAILABLE: the API cannot answer now, or was not reached: retry later."""


class DataLossError(SandboxesError):
    """DATA_LOSS: data was lost or damaged beyond repair."""


class UnauthenticatedError(SandboxesError):
    """UNAUTHENTICATED: the token is missing, wrong or revoked."""
