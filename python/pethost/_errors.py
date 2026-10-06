"""What a failed call raises. Generated from v1/panel.proto: do not edit."""

from __future__ import annotations

from typing import TypeAlias

from ._types import MachineUnreachable, NoMachine, ProjectBusy, ProjectChanged

ErrorDetail: TypeAlias = ProjectBusy | ProjectChanged | MachineUnreachable | NoMachine
"""What an error may carry beside its message: `match` on its class."""


class PethostError(Exception):
    """The API refused a call, or could not be reached. Catch a subclass for one code: what the
    code means for a call is in the method's documentation and in the package's.

    Attributes:
        message: Prose for people: branch on the class and on `detail`, never on this.
        detail: What to branch on, when the API sent one: `ProjectBusy`, `ProjectChanged`, `MachineUnreachable`, `NoMachine`.
            None = none, or one this version does not know.
    """

    message: str
    """Prose for people: branch on the class and on `detail`, never on this."""

    detail: ErrorDetail | None
    """What to branch on, when the API sent one: `ProjectBusy`, `ProjectChanged`, `MachineUnreachable`, `NoMachine`.
    None = none, or one this version does not know.
    """

    def __init__(self, message: str, detail: ErrorDetail | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.detail = detail


class CanceledError(PethostError):
    """CANCELED: the call was cancelled, usually by the caller."""


class UnknownError(PethostError):
    """UNKNOWN: an error without a code of its own."""


class InvalidArgumentError(PethostError):
    """INVALID_ARGUMENT: the request is invalid, whatever the state of what it is about."""


class DeadlineExceededError(PethostError):
    """DEADLINE_EXCEEDED: the client's `timeout` ran out before the answer came."""


class NotFoundError(PethostError):
    """NOT_FOUND: what the call names does not exist."""


class AlreadyExistsError(PethostError):
    """ALREADY_EXISTS: what the call would create exists already."""


class PermissionDeniedError(PethostError):
    """PERMISSION_DENIED: the caller may not do this."""


class ResourceExhaustedError(PethostError):
    """RESOURCE_EXHAUSTED: a limit or a quota is used up."""


class FailedPreconditionError(PethostError):
    """FAILED_PRECONDITION: the state of what the call is about does not allow it."""


class AbortedError(PethostError):
    """ABORTED: the call lost to a concurrent change."""


class OutOfRangeError(PethostError):
    """OUT_OF_RANGE: the call asks past the valid range."""


class UnimplementedError(PethostError):
    """UNIMPLEMENTED: the API does not have this call."""


class InternalError(PethostError):
    """INTERNAL: the API itself failed."""


class UnavailableError(PethostError):
    """UNAVAILABLE: the API cannot answer now, or was not reached: retry later."""


class DataLossError(PethostError):
    """DATA_LOSS: data was lost or damaged beyond repair."""


class UnauthenticatedError(PethostError):
    """UNAUTHENTICATED: the token is missing, wrong or revoked."""
