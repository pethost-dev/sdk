"""Between the public types and the wire layer: the type checker holds every line here against
both. Generated from v1/sandboxes.proto: do not edit."""

from __future__ import annotations

from collections.abc import Iterator, Sequence
from datetime import datetime
from typing import Any as _Any
from typing import Literal as _Literal

from connectrpc.code import Code as _Code
from connectrpc.errors import ConnectError as _ConnectError
from protobuf import Oneof as _Oneof

import pethost._connections as _connections
import pethost._runtime as _rt
import pethost._wire.v1.sandboxes_pb as _pb
import pethost.sandboxes._errors as _errors
import pethost.sandboxes._types as _t


def meter_from_wire(_w: _pb.Meter) -> _t.Meter:
    return _t.Meter(_w.value)


def meter_to_wire(_v: _t.Meter) -> _pb.Meter:
    return _pb.Meter(_v.value)


def sandbox_state_from_wire(_w: _pb.SandboxState) -> _t.SandboxState:
    return _t.SandboxState(_w.value)


def sandbox_state_to_wire(_v: _t.SandboxState) -> _pb.SandboxState:
    return _pb.SandboxState(_v.value)


def state_reason_from_wire(_w: _pb.StateReason) -> _t.StateReason:
    return _t.StateReason(_w.value)


def state_reason_to_wire(_v: _t.StateReason) -> _pb.StateReason:
    return _pb.StateReason(_v.value)


def size_from_wire(_w: _pb.Size) -> _t.Size:
    return _t.Size(_w.value)


def size_to_wire(_v: _t.Size) -> _pb.Size:
    return _pb.Size(_v.value)


def sandbox_event_kind_from_wire(_w: _pb.SandboxEventKind) -> _t.SandboxEventKind:
    return _t.SandboxEventKind(_w.value)


def sandbox_event_kind_to_wire(_v: _t.SandboxEventKind) -> _pb.SandboxEventKind:
    return _pb.SandboxEventKind(_v.value)


def lifecycle_change_from_wire(_w: _pb.LifecycleChange) -> _t.LifecycleChange:
    return _t.LifecycleChange(_w.value)


def lifecycle_change_to_wire(_v: _t.LifecycleChange) -> _pb.LifecycleChange:
    return _pb.LifecycleChange(_v.value)


def template_state_from_wire(_w: _pb.TemplateState) -> _t.TemplateState:
    return _t.TemplateState(_w.value)


def template_state_to_wire(_v: _t.TemplateState) -> _pb.TemplateState:
    return _pb.TemplateState(_v.value)


def command_state_from_wire(_w: _pb.CommandState) -> _t.CommandState:
    return _t.CommandState(_w.value)


def command_state_to_wire(_v: _t.CommandState) -> _pb.CommandState:
    return _pb.CommandState(_v.value)


def started_by_from_wire(_w: _pb.StartedBy) -> _t.StartedBy:
    return _t.StartedBy(_w.value)


def started_by_to_wire(_v: _t.StartedBy) -> _pb.StartedBy:
    return _pb.StartedBy(_v.value)


def file_kind_from_wire(_w: _pb.FileKind) -> _t.FileKind:
    return _t.FileKind(_w.value)


def file_kind_to_wire(_v: _t.FileKind) -> _pb.FileKind:
    return _pb.FileKind(_v.value)


def file_failure_from_wire(_w: _pb.FileFailure) -> _t.FileFailure:
    return _t.FileFailure(_w.value)


def file_failure_to_wire(_v: _t.FileFailure) -> _pb.FileFailure:
    return _pb.FileFailure(_v.value)


def file_event_kind_from_wire(_w: _pb.FileEventKind) -> _t.FileEventKind:
    return _t.FileEventKind(_w.value)


def file_event_kind_to_wire(_v: _t.FileEventKind) -> _pb.FileEventKind:
    return _pb.FileEventKind(_v.value)


def desktop_failure_from_wire(_w: _pb.DesktopFailure) -> _t.DesktopFailure:
    return _t.DesktopFailure(_w.value)


def desktop_failure_to_wire(_v: _t.DesktopFailure) -> _pb.DesktopFailure:
    return _pb.DesktopFailure(_v.value)


def mouse_button_from_wire(_w: _pb.MouseButton) -> _t.MouseButton:
    return _t.MouseButton(_w.value)


def mouse_button_to_wire(_v: _t.MouseButton) -> _pb.MouseButton:
    return _pb.MouseButton(_v.value)


def agent_from_wire(_w: _pb.Agent) -> _t.Agent:
    return _t.Agent(_w.value)


def agent_to_wire(_v: _t.Agent) -> _pb.Agent:
    return _pb.Agent(_v.value)


def agent_turn_state_from_wire(_w: _pb.AgentTurnState) -> _t.AgentTurnState:
    return _t.AgentTurnState(_w.value)


def agent_turn_state_to_wire(_v: _t.AgentTurnState) -> _pb.AgentTurnState:
    return _pb.AgentTurnState(_v.value)


def room_bound_from_wire(_w: _pb.RoomBound) -> _t.RoomBound:
    return _t.RoomBound(_w.value)


def room_bound_to_wire(_v: _t.RoomBound) -> _pb.RoomBound:
    return _pb.RoomBound(_v.value)


def workspace_from_wire(_w: _pb.Workspace) -> _t.Workspace:
    return _t.Workspace(
        workspace_id=_w.workspace_id,
        name=_w.name,
        limits=limits_from_wire(_w.limits) if _w.limits is not None else None,
        ssh_keys=tuple(ssh_key_from_wire(_x) for _x in _w.ssh_keys),
        secrets=tuple(secret_from_wire(_x) for _x in _w.secrets),
        billing=billing_from_wire(_w.billing) if _w.billing is not None else None,
        sizes=tuple(size_info_from_wire(_x) for _x in _w.sizes),
        template_bytes=_w.template_bytes,
        vcpus_used=_w.vcpus_used,
    )


def workspace_to_wire(_v: _t.Workspace) -> _pb.Workspace:
    return _pb.Workspace(
        workspace_id=_v.workspace_id or None,
        name=_v.name or None,
        limits=limits_to_wire(_v.limits) if _v.limits is not None else None,
        ssh_keys=[ssh_key_to_wire(_x) for _x in _v.ssh_keys],
        secrets=[secret_to_wire(_x) for _x in _v.secrets],
        billing=billing_to_wire(_v.billing) if _v.billing is not None else None,
        sizes=[size_info_to_wire(_x) for _x in _v.sizes],
        template_bytes=_v.template_bytes or None,
        vcpus_used=_v.vcpus_used or None,
    )


def workspace_to_dict(_v: _t.Workspace) -> dict[str, _Any]:
    return _rt.to_dict(workspace_to_wire(_v))


def workspace_from_dict(_j: dict[str, _Any]) -> _t.Workspace:
    return workspace_from_wire(_rt.from_dict(_pb.Workspace, _j))


def size_info_from_wire(_w: _pb.SizeInfo) -> _t.SizeInfo:
    return _t.SizeInfo(
        size=size_from_wire(_w.size),
        vcpus=_w.vcpus,
        memory_mib=_w.memory_mib,
        disk_gib=_w.disk_gib,
        running_hour=_w.running_hour if _w.has_field("running_hour") else None,
        paused_hour=_w.paused_hour if _w.has_field("paused_hour") else None,
    )


def size_info_to_wire(_v: _t.SizeInfo) -> _pb.SizeInfo:
    return _pb.SizeInfo(
        size=size_to_wire(_v.size) if _v.size.value else None,
        vcpus=_v.vcpus or None,
        memory_mib=_v.memory_mib or None,
        disk_gib=_v.disk_gib or None,
        running_hour=_v.running_hour,
        paused_hour=_v.paused_hour,
    )


def size_info_to_dict(_v: _t.SizeInfo) -> dict[str, _Any]:
    return _rt.to_dict(size_info_to_wire(_v))


def size_info_from_dict(_j: dict[str, _Any]) -> _t.SizeInfo:
    return size_info_from_wire(_rt.from_dict(_pb.SizeInfo, _j))


def billing_from_wire(_w: _pb.Billing) -> _t.Billing:
    return _t.Billing(
        currency=_w.currency,
        included_micros=_w.included_micros,
        included_total_micros=_w.included_total_micros,
        period_end_time=_rt.time_from_wire(_w.period_end_time) if _w.period_end_time is not None else None,
        balance_micros=_w.balance_micros,
        suspended=_w.suspended,
        trial=_w.trial,
        rates=rates_from_wire(_w.rates) if _w.rates is not None else None,
    )


def billing_to_wire(_v: _t.Billing) -> _pb.Billing:
    return _pb.Billing(
        currency=_v.currency or None,
        included_micros=_v.included_micros or None,
        included_total_micros=_v.included_total_micros or None,
        period_end_time=_rt.time_to_wire(_v.period_end_time) if _v.period_end_time is not None else None,
        balance_micros=_v.balance_micros or None,
        suspended=_v.suspended or None,
        trial=_v.trial or None,
        rates=rates_to_wire(_v.rates) if _v.rates is not None else None,
    )


def billing_to_dict(_v: _t.Billing) -> dict[str, _Any]:
    return _rt.to_dict(billing_to_wire(_v))


def billing_from_dict(_j: dict[str, _Any]) -> _t.Billing:
    return billing_from_wire(_rt.from_dict(_pb.Billing, _j))


def rates_from_wire(_w: _pb.Rates) -> _t.Rates:
    return _t.Rates(
        stored_gib_month=_w.stored_gib_month,
    )


def rates_to_wire(_v: _t.Rates) -> _pb.Rates:
    return _pb.Rates(
        stored_gib_month=_v.stored_gib_month or None,
    )


def rates_to_dict(_v: _t.Rates) -> dict[str, _Any]:
    return _rt.to_dict(rates_to_wire(_v))


def rates_from_dict(_j: dict[str, _Any]) -> _t.Rates:
    return rates_from_wire(_rt.from_dict(_pb.Rates, _j))


def ssh_key_from_wire(_w: _pb.SshKey) -> _t.SshKey:
    return _t.SshKey(
        public_key=_w.public_key,
        comment=_w.comment,
        fingerprint=_w.fingerprint,
    )


def ssh_key_to_wire(_v: _t.SshKey) -> _pb.SshKey:
    return _pb.SshKey(
        public_key=_v.public_key or None,
        comment=_v.comment or None,
        fingerprint=_v.fingerprint or None,
    )


def ssh_key_to_dict(_v: _t.SshKey) -> dict[str, _Any]:
    return _rt.to_dict(ssh_key_to_wire(_v))


def ssh_key_from_dict(_j: dict[str, _Any]) -> _t.SshKey:
    return ssh_key_from_wire(_rt.from_dict(_pb.SshKey, _j))


def limits_from_wire(_w: _pb.Limits) -> _t.Limits:
    return _t.Limits(
        vcpus=_w.vcpus,
        largest_size=size_from_wire(_w.largest_size),
        template_versions=_w.template_versions,
        template_gib=_w.template_gib,
    )


def limits_to_wire(_v: _t.Limits) -> _pb.Limits:
    return _pb.Limits(
        vcpus=_v.vcpus or None,
        largest_size=size_to_wire(_v.largest_size) if _v.largest_size.value else None,
        template_versions=_v.template_versions or None,
        template_gib=_v.template_gib or None,
    )


def limits_to_dict(_v: _t.Limits) -> dict[str, _Any]:
    return _rt.to_dict(limits_to_wire(_v))


def limits_from_dict(_j: dict[str, _Any]) -> _t.Limits:
    return limits_from_wire(_rt.from_dict(_pb.Limits, _j))


def secret_from_wire(_w: _pb.Secret) -> _t.Secret:
    return _t.Secret(
        name=_w.name,
        hosts=tuple(_w.hosts),
        update_time=_rt.time_from_wire(_w.update_time) if _w.update_time is not None else None,
    )


def secret_to_wire(_v: _t.Secret) -> _pb.Secret:
    return _pb.Secret(
        name=_v.name or None,
        hosts=_rt.strings("Secret.hosts", _v.hosts),
        update_time=_rt.time_to_wire(_v.update_time) if _v.update_time is not None else None,
    )


def secret_to_dict(_v: _t.Secret) -> dict[str, _Any]:
    return _rt.to_dict(secret_to_wire(_v))


def secret_from_dict(_j: dict[str, _Any]) -> _t.Secret:
    return secret_from_wire(_rt.from_dict(_pb.Secret, _j))


def sandbox_from_wire(_w: _pb.Sandbox) -> _t.Sandbox:
    return _t.Sandbox(
        sandbox_id=_w.sandbox_id,
        state=sandbox_state_from_wire(_w.state),
        state_reason=state_reason_from_wire(_w.state_reason),
        state_message=_w.state_message,
        state_time=_rt.time_from_wire(_w.state_time) if _w.state_time is not None else None,
        template=_w.template,
        labels=tuple(label_from_wire(_x) for _x in _w.labels),
        settings=sandbox_settings_from_wire(_w.settings) if _w.settings is not None else None,
        revision=_w.revision,
        disk_gib=_w.disk_gib,
        desktop=desktop_from_wire(_w.desktop) if _w.desktop is not None else None,
        ssh_command=_w.ssh_command,
        panel_url=_w.panel_url,
        create_time=_rt.time_from_wire(_w.create_time) if _w.create_time is not None else None,
        usage=usage_from_wire(_w.usage) if _w.usage is not None else None,
        connection=connection_from_wire(_w.connection) if _w.connection is not None else None,
        restore=restore_from_wire(_w.restore) if _w.restore is not None else None,
        next_state=sandbox_state_from_wire(_w.next_state),
        next_state_time=_rt.time_from_wire(_w.next_state_time) if _w.next_state_time is not None else None,
        stored_bytes=_w.stored_bytes,
        name=_w.name,
    )


def sandbox_to_wire(_v: _t.Sandbox) -> _pb.Sandbox:
    return _pb.Sandbox(
        sandbox_id=_v.sandbox_id or None,
        state=sandbox_state_to_wire(_v.state) if _v.state.value else None,
        state_reason=state_reason_to_wire(_v.state_reason) if _v.state_reason.value else None,
        state_message=_v.state_message or None,
        state_time=_rt.time_to_wire(_v.state_time) if _v.state_time is not None else None,
        template=_v.template or None,
        labels=[label_to_wire(_x) for _x in _v.labels],
        settings=sandbox_settings_to_wire(_v.settings) if _v.settings is not None else None,
        revision=_v.revision or None,
        disk_gib=_v.disk_gib or None,
        desktop=desktop_to_wire(_v.desktop) if _v.desktop is not None else None,
        ssh_command=_v.ssh_command or None,
        panel_url=_v.panel_url or None,
        create_time=_rt.time_to_wire(_v.create_time) if _v.create_time is not None else None,
        usage=usage_to_wire(_v.usage) if _v.usage is not None else None,
        connection=connection_to_wire(_v.connection) if _v.connection is not None else None,
        restore=restore_to_wire(_v.restore) if _v.restore is not None else None,
        next_state=sandbox_state_to_wire(_v.next_state) if _v.next_state.value else None,
        next_state_time=_rt.time_to_wire(_v.next_state_time) if _v.next_state_time is not None else None,
        stored_bytes=_v.stored_bytes or None,
        name=_v.name or None,
    )


def sandbox_to_dict(_v: _t.Sandbox) -> dict[str, _Any]:
    return _rt.to_dict(sandbox_to_wire(_v))


def sandbox_from_dict(_j: dict[str, _Any]) -> _t.Sandbox:
    return sandbox_from_wire(_rt.from_dict(_pb.Sandbox, _j))


def restore_from_wire(_w: _pb.Restore) -> _t.Restore:
    return _t.Restore(
        fetched_bytes=_w.fetched_bytes,
        total_bytes=_w.total_bytes,
    )


def restore_to_wire(_v: _t.Restore) -> _pb.Restore:
    return _pb.Restore(
        fetched_bytes=_v.fetched_bytes or None,
        total_bytes=_v.total_bytes or None,
    )


def restore_to_dict(_v: _t.Restore) -> dict[str, _Any]:
    return _rt.to_dict(restore_to_wire(_v))


def restore_from_dict(_j: dict[str, _Any]) -> _t.Restore:
    return restore_from_wire(_rt.from_dict(_pb.Restore, _j))


def usage_from_wire(_w: _pb.Usage) -> _t.Usage:
    return _t.Usage(
        running_seconds=_w.running_seconds,
        paused_seconds=_w.paused_seconds,
        stored_gib_hours=_w.stored_gib_hours,
        cost_micros=_w.cost_micros,
    )


def usage_to_wire(_v: _t.Usage) -> _pb.Usage:
    return _pb.Usage(
        running_seconds=_v.running_seconds or None,
        paused_seconds=_v.paused_seconds or None,
        stored_gib_hours=_v.stored_gib_hours or None,
        cost_micros=_v.cost_micros or None,
    )


def usage_to_dict(_v: _t.Usage) -> dict[str, _Any]:
    return _rt.to_dict(usage_to_wire(_v))


def usage_from_dict(_j: dict[str, _Any]) -> _t.Usage:
    return usage_from_wire(_rt.from_dict(_pb.Usage, _j))


def list_sandboxes_response_from_wire(_w: _pb.ListSandboxesResponse) -> _t.ListSandboxesResponse:
    return _t.ListSandboxesResponse(
        sandboxes=tuple(sandbox_from_wire(_x) for _x in _w.sandboxes),
        next_page_token=_w.next_page_token,
    )


def list_sandboxes_response_to_wire(_v: _t.ListSandboxesResponse) -> _pb.ListSandboxesResponse:
    return _pb.ListSandboxesResponse(
        sandboxes=[sandbox_to_wire(_x) for _x in _v.sandboxes],
        next_page_token=_v.next_page_token or None,
    )


def list_sandboxes_response_to_dict(_v: _t.ListSandboxesResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_sandboxes_response_to_wire(_v))


def list_sandboxes_response_from_dict(_j: dict[str, _Any]) -> _t.ListSandboxesResponse:
    return list_sandboxes_response_from_wire(_rt.from_dict(_pb.ListSandboxesResponse, _j))


def connection_from_wire(_w: _pb.Connection) -> _t.Connection:
    return _t.Connection(
        url=_w.url,
        token=_w.token,
        expire_time=_rt.time_from_wire(_w.expire_time) if _w.expire_time is not None else None,
        ssh_command=_w.ssh_command,
    )


def connection_to_wire(_v: _t.Connection) -> _pb.Connection:
    return _pb.Connection(
        url=_v.url or None,
        token=_v.token or None,
        expire_time=_rt.time_to_wire(_v.expire_time) if _v.expire_time is not None else None,
        ssh_command=_v.ssh_command or None,
    )


def connection_to_dict(_v: _t.Connection) -> dict[str, _Any]:
    return _rt.to_dict(connection_to_wire(_v))


def connection_from_dict(_j: dict[str, _Any]) -> _t.Connection:
    return connection_from_wire(_rt.from_dict(_pb.Connection, _j))


def sandbox_settings_from_wire(_w: _pb.SandboxSettings) -> _t.SandboxSettings:
    return _t.SandboxSettings(
        size=size_from_wire(_w.size),
        lifecycle=lifecycle_from_wire(_w.lifecycle) if _w.lifecycle is not None else None,
        egress=egress_from_wire(_w.egress) if _w.egress is not None else None,
        ingress=ingress_from_wire(_w.ingress) if _w.ingress is not None else None,
        environment=environment_from_wire(_w.environment) if _w.environment is not None else None,
    )


def sandbox_settings_to_wire(_v: _t.SandboxSettings) -> _pb.SandboxSettings:
    return _pb.SandboxSettings(
        size=size_to_wire(_v.size) if _v.size.value else None,
        lifecycle=lifecycle_to_wire(_v.lifecycle) if _v.lifecycle is not None else None,
        egress=egress_to_wire(_v.egress) if _v.egress is not None else None,
        ingress=ingress_to_wire(_v.ingress) if _v.ingress is not None else None,
        environment=environment_to_wire(_v.environment) if _v.environment is not None else None,
    )


def sandbox_settings_to_dict(_v: _t.SandboxSettings) -> dict[str, _Any]:
    return _rt.to_dict(sandbox_settings_to_wire(_v))


def sandbox_settings_from_dict(_j: dict[str, _Any]) -> _t.SandboxSettings:
    return sandbox_settings_from_wire(_rt.from_dict(_pb.SandboxSettings, _j))


def lifecycle_from_wire(_w: _pb.Lifecycle) -> _t.Lifecycle:
    return _t.Lifecycle(
        pause_after_idle_seconds=_w.pause_after_idle_seconds if _w.has_field("pause_after_idle_seconds") else None,
        stop_after_idle_seconds=_w.stop_after_idle_seconds if _w.has_field("stop_after_idle_seconds") else None,
        delete_after_idle_seconds=_w.delete_after_idle_seconds,
        wake_when_stopped=_w.wake_when_stopped,
    )


def lifecycle_to_wire(_v: _t.Lifecycle) -> _pb.Lifecycle:
    return _pb.Lifecycle(
        pause_after_idle_seconds=_v.pause_after_idle_seconds,
        stop_after_idle_seconds=_v.stop_after_idle_seconds,
        delete_after_idle_seconds=_v.delete_after_idle_seconds or None,
        wake_when_stopped=_v.wake_when_stopped or None,
    )


def lifecycle_to_dict(_v: _t.Lifecycle) -> dict[str, _Any]:
    return _rt.to_dict(lifecycle_to_wire(_v))


def lifecycle_from_dict(_j: dict[str, _Any]) -> _t.Lifecycle:
    return lifecycle_from_wire(_rt.from_dict(_pb.Lifecycle, _j))


def egress_from_wire(_w: _pb.Egress) -> _t.Egress:
    return _t.Egress(
        allow=tuple(_w.allow),
        deny=tuple(_w.deny),
    )


def egress_to_wire(_v: _t.Egress) -> _pb.Egress:
    return _pb.Egress(
        allow=_rt.strings("Egress.allow", _v.allow),
        deny=_rt.strings("Egress.deny", _v.deny),
    )


def egress_to_dict(_v: _t.Egress) -> dict[str, _Any]:
    return _rt.to_dict(egress_to_wire(_v))


def egress_from_dict(_j: dict[str, _Any]) -> _t.Egress:
    return egress_from_wire(_rt.from_dict(_pb.Egress, _j))


def ingress_from_wire(_w: _pb.Ingress) -> _t.Ingress:
    return _t.Ingress(
        public_ports=tuple(public_port_from_wire(_x) for _x in _w.public_ports),
    )


def ingress_to_wire(_v: _t.Ingress) -> _pb.Ingress:
    return _pb.Ingress(
        public_ports=[public_port_to_wire(_x) for _x in _v.public_ports],
    )


def ingress_to_dict(_v: _t.Ingress) -> dict[str, _Any]:
    return _rt.to_dict(ingress_to_wire(_v))


def ingress_from_dict(_j: dict[str, _Any]) -> _t.Ingress:
    return ingress_from_wire(_rt.from_dict(_pb.Ingress, _j))


def public_port_from_wire(_w: _pb.PublicPort) -> _t.PublicPort:
    return _t.PublicPort(
        port=_w.port,
        url=_w.url,
    )


def public_port_to_wire(_v: _t.PublicPort) -> _pb.PublicPort:
    return _pb.PublicPort(
        port=_v.port or None,
        url=_v.url or None,
    )


def public_port_to_dict(_v: _t.PublicPort) -> dict[str, _Any]:
    return _rt.to_dict(public_port_to_wire(_v))


def public_port_from_dict(_j: dict[str, _Any]) -> _t.PublicPort:
    return public_port_from_wire(_rt.from_dict(_pb.PublicPort, _j))


def environment_from_wire(_w: _pb.Environment) -> _t.Environment:
    return _t.Environment(
        variables=tuple(env_var_from_wire(_x) for _x in _w.variables),
    )


def environment_to_wire(_v: _t.Environment) -> _pb.Environment:
    return _pb.Environment(
        variables=[env_var_to_wire(_x) for _x in _v.variables],
    )


def environment_to_dict(_v: _t.Environment) -> dict[str, _Any]:
    return _rt.to_dict(environment_to_wire(_v))


def environment_from_dict(_j: dict[str, _Any]) -> _t.Environment:
    return environment_from_wire(_rt.from_dict(_pb.Environment, _j))


def env_var_from_wire(_w: _pb.EnvVar) -> _t.EnvVar:
    _k = _w.source
    if _k is None:
        return _t.EnvVar(
            name=_w.name,
        )
    if _k.field == "value":
        return _t.EnvVar(
            name=_w.name,
            value=_k.value,
        )
    if _k.field == "secret":
        return _t.EnvVar(
            name=_w.name,
            secret=_k.value,
        )
    _rt.never(_k)


def env_var_to_wire(_v: _t.EnvVar) -> _pb.EnvVar:
    _w = _pb.EnvVar(
        name=_v.name or None,
    )
    if _v.value is not None:
        _w.source = _Oneof[_Literal["value"], str]("value", _v.value)
    elif _v.secret is not None:
        _w.source = _Oneof[_Literal["secret"], str]("secret", _v.secret)
    return _w


def env_var_to_dict(_v: _t.EnvVar) -> dict[str, _Any]:
    return _rt.to_dict(env_var_to_wire(_v))


def env_var_from_dict(_j: dict[str, _Any]) -> _t.EnvVar:
    return env_var_from_wire(_rt.from_dict(_pb.EnvVar, _j))


def label_from_wire(_w: _pb.Label) -> _t.Label:
    return _t.Label(
        key=_w.key,
        value=_w.value,
    )


def label_to_wire(_v: _t.Label) -> _pb.Label:
    return _pb.Label(
        key=_v.key or None,
        value=_v.value or None,
    )


def label_to_dict(_v: _t.Label) -> dict[str, _Any]:
    return _rt.to_dict(label_to_wire(_v))


def label_from_dict(_j: dict[str, _Any]) -> _t.Label:
    return label_from_wire(_rt.from_dict(_pb.Label, _j))


def get_sandbox_metrics_response_from_wire(_w: _pb.GetSandboxMetricsResponse) -> _t.GetSandboxMetricsResponse:
    return _t.GetSandboxMetricsResponse(
        points=tuple(metrics_point_from_wire(_x) for _x in _w.points),
    )


def get_sandbox_metrics_response_to_wire(_v: _t.GetSandboxMetricsResponse) -> _pb.GetSandboxMetricsResponse:
    return _pb.GetSandboxMetricsResponse(
        points=[metrics_point_to_wire(_x) for _x in _v.points],
    )


def get_sandbox_metrics_response_to_dict(_v: _t.GetSandboxMetricsResponse) -> dict[str, _Any]:
    return _rt.to_dict(get_sandbox_metrics_response_to_wire(_v))


def get_sandbox_metrics_response_from_dict(_j: dict[str, _Any]) -> _t.GetSandboxMetricsResponse:
    return get_sandbox_metrics_response_from_wire(_rt.from_dict(_pb.GetSandboxMetricsResponse, _j))


def metrics_point_from_wire(_w: _pb.MetricsPoint) -> _t.MetricsPoint:
    return _t.MetricsPoint(
        time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
        cpu_percent=_w.cpu_percent,
        memory_used_bytes=_w.memory_used_bytes,
        disk_used_bytes=_w.disk_used_bytes,
        network_in_bytes=_w.network_in_bytes,
        network_out_bytes=_w.network_out_bytes,
    )


def metrics_point_to_wire(_v: _t.MetricsPoint) -> _pb.MetricsPoint:
    return _pb.MetricsPoint(
        time=_rt.time_to_wire(_v.time) if _v.time is not None else None,
        cpu_percent=_v.cpu_percent or None,
        memory_used_bytes=_v.memory_used_bytes or None,
        disk_used_bytes=_v.disk_used_bytes or None,
        network_in_bytes=_v.network_in_bytes or None,
        network_out_bytes=_v.network_out_bytes or None,
    )


def metrics_point_to_dict(_v: _t.MetricsPoint) -> dict[str, _Any]:
    return _rt.to_dict(metrics_point_to_wire(_v))


def metrics_point_from_dict(_j: dict[str, _Any]) -> _t.MetricsPoint:
    return metrics_point_from_wire(_rt.from_dict(_pb.MetricsPoint, _j))


def list_sandbox_events_response_from_wire(_w: _pb.ListSandboxEventsResponse) -> _t.ListSandboxEventsResponse:
    return _t.ListSandboxEventsResponse(
        events=tuple(sandbox_event_from_wire(_x) for _x in _w.events),
        more=_w.more,
    )


def list_sandbox_events_response_to_wire(_v: _t.ListSandboxEventsResponse) -> _pb.ListSandboxEventsResponse:
    return _pb.ListSandboxEventsResponse(
        events=[sandbox_event_to_wire(_x) for _x in _v.events],
        more=_v.more or None,
    )


def list_sandbox_events_response_to_dict(_v: _t.ListSandboxEventsResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_sandbox_events_response_to_wire(_v))


def list_sandbox_events_response_from_dict(_j: dict[str, _Any]) -> _t.ListSandboxEventsResponse:
    return list_sandbox_events_response_from_wire(_rt.from_dict(_pb.ListSandboxEventsResponse, _j))


def sandbox_event_from_wire(_w: _pb.SandboxEvent) -> _t.SandboxEvent:
    _k = _w.event
    if _k is None:
        return _t.SandboxEvent(
            event_id=_w.event_id,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
        )
    if _k.field == "lifecycle":
        return _t.SandboxEvent(
            event_id=_w.event_id,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            lifecycle=lifecycle_event_from_wire(_k.value),
        )
    if _k.field == "command":
        return _t.SandboxEvent(
            event_id=_w.event_id,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            command=command_event_from_wire(_k.value),
        )
    if _k.field == "egress":
        return _t.SandboxEvent(
            event_id=_w.event_id,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            egress=egress_event_from_wire(_k.value),
        )
    if _k.field == "port":
        return _t.SandboxEvent(
            event_id=_w.event_id,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            port=port_event_from_wire(_k.value),
        )
    if _k.field == "agent_turn":
        return _t.SandboxEvent(
            event_id=_w.event_id,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            agent_turn=agent_turn_event_from_wire(_k.value),
        )
    _rt.never(_k)


def sandbox_event_to_wire(_v: _t.SandboxEvent) -> _pb.SandboxEvent:
    _w = _pb.SandboxEvent(
        event_id=_v.event_id or None,
        time=_rt.time_to_wire(_v.time) if _v.time is not None else None,
    )
    if _v.lifecycle is not None:
        _w.event = _Oneof[_Literal["lifecycle"], _pb.LifecycleEvent]("lifecycle", lifecycle_event_to_wire(_v.lifecycle))
    elif _v.command is not None:
        _w.event = _Oneof[_Literal["command"], _pb.CommandEvent]("command", command_event_to_wire(_v.command))
    elif _v.egress is not None:
        _w.event = _Oneof[_Literal["egress"], _pb.EgressEvent]("egress", egress_event_to_wire(_v.egress))
    elif _v.port is not None:
        _w.event = _Oneof[_Literal["port"], _pb.PortEvent]("port", port_event_to_wire(_v.port))
    elif _v.agent_turn is not None:
        _w.event = _Oneof[_Literal["agent_turn"], _pb.AgentTurnEvent]("agent_turn", agent_turn_event_to_wire(_v.agent_turn))
    return _w


def sandbox_event_to_dict(_v: _t.SandboxEvent) -> dict[str, _Any]:
    return _rt.to_dict(sandbox_event_to_wire(_v))


def sandbox_event_from_dict(_j: dict[str, _Any]) -> _t.SandboxEvent:
    return sandbox_event_from_wire(_rt.from_dict(_pb.SandboxEvent, _j))


def lifecycle_event_from_wire(_w: _pb.LifecycleEvent) -> _t.LifecycleEvent:
    return _t.LifecycleEvent(
        change=lifecycle_change_from_wire(_w.change),
        reason=state_reason_from_wire(_w.reason),
        size=size_from_wire(_w.size),
        disk_gib=_w.disk_gib,
        state_message=_w.state_message,
    )


def lifecycle_event_to_wire(_v: _t.LifecycleEvent) -> _pb.LifecycleEvent:
    return _pb.LifecycleEvent(
        change=lifecycle_change_to_wire(_v.change) if _v.change.value else None,
        reason=state_reason_to_wire(_v.reason) if _v.reason.value else None,
        size=size_to_wire(_v.size) if _v.size.value else None,
        disk_gib=_v.disk_gib or None,
        state_message=_v.state_message or None,
    )


def lifecycle_event_to_dict(_v: _t.LifecycleEvent) -> dict[str, _Any]:
    return _rt.to_dict(lifecycle_event_to_wire(_v))


def lifecycle_event_from_dict(_j: dict[str, _Any]) -> _t.LifecycleEvent:
    return lifecycle_event_from_wire(_rt.from_dict(_pb.LifecycleEvent, _j))


def command_event_from_wire(_w: _pb.CommandEvent) -> _t.CommandEvent:
    return _t.CommandEvent(
        command_id=_w.command_id,
        command=_w.command,
        state=command_state_from_wire(_w.state),
        exit_code=_w.exit_code if _w.has_field("exit_code") else None,
        duration_ms=_w.duration_ms,
        started_by=started_by_from_wire(_w.started_by),
    )


def command_event_to_wire(_v: _t.CommandEvent) -> _pb.CommandEvent:
    return _pb.CommandEvent(
        command_id=_v.command_id or None,
        command=_v.command or None,
        state=command_state_to_wire(_v.state) if _v.state.value else None,
        exit_code=_v.exit_code,
        duration_ms=_v.duration_ms or None,
        started_by=started_by_to_wire(_v.started_by) if _v.started_by.value else None,
    )


def command_event_to_dict(_v: _t.CommandEvent) -> dict[str, _Any]:
    return _rt.to_dict(command_event_to_wire(_v))


def command_event_from_dict(_j: dict[str, _Any]) -> _t.CommandEvent:
    return command_event_from_wire(_rt.from_dict(_pb.CommandEvent, _j))


def egress_event_from_wire(_w: _pb.EgressEvent) -> _t.EgressEvent:
    return _t.EgressEvent(
        host=_w.host,
        port=_w.port,
        allowed=_w.allowed,
        connections=_w.connections,
        bytes_out=_w.bytes_out,
        bytes_in=_w.bytes_in,
        secrets=tuple(_w.secrets),
    )


def egress_event_to_wire(_v: _t.EgressEvent) -> _pb.EgressEvent:
    return _pb.EgressEvent(
        host=_v.host or None,
        port=_v.port or None,
        allowed=_v.allowed or None,
        connections=_v.connections or None,
        bytes_out=_v.bytes_out or None,
        bytes_in=_v.bytes_in or None,
        secrets=_rt.strings("EgressEvent.secrets", _v.secrets),
    )


def egress_event_to_dict(_v: _t.EgressEvent) -> dict[str, _Any]:
    return _rt.to_dict(egress_event_to_wire(_v))


def egress_event_from_dict(_j: dict[str, _Any]) -> _t.EgressEvent:
    return egress_event_from_wire(_rt.from_dict(_pb.EgressEvent, _j))


def port_event_from_wire(_w: _pb.PortEvent) -> _t.PortEvent:
    return _t.PortEvent(
        port=_w.port,
        requests=_w.requests,
        server_errors=_w.server_errors,
        bytes_in=_w.bytes_in,
        bytes_out=_w.bytes_out,
    )


def port_event_to_wire(_v: _t.PortEvent) -> _pb.PortEvent:
    return _pb.PortEvent(
        port=_v.port or None,
        requests=_v.requests or None,
        server_errors=_v.server_errors or None,
        bytes_in=_v.bytes_in or None,
        bytes_out=_v.bytes_out or None,
    )


def port_event_to_dict(_v: _t.PortEvent) -> dict[str, _Any]:
    return _rt.to_dict(port_event_to_wire(_v))


def port_event_from_dict(_j: dict[str, _Any]) -> _t.PortEvent:
    return port_event_from_wire(_rt.from_dict(_pb.PortEvent, _j))


def agent_turn_event_from_wire(_w: _pb.AgentTurnEvent) -> _t.AgentTurnEvent:
    return _t.AgentTurnEvent(
        turn_id=_w.turn_id,
        conversation_id=_w.conversation_id,
        agent=agent_from_wire(_w.agent),
        prompt=_w.prompt,
        state=agent_turn_state_from_wire(_w.state),
        input_tokens=_w.input_tokens,
        output_tokens=_w.output_tokens,
    )


def agent_turn_event_to_wire(_v: _t.AgentTurnEvent) -> _pb.AgentTurnEvent:
    return _pb.AgentTurnEvent(
        turn_id=_v.turn_id or None,
        conversation_id=_v.conversation_id or None,
        agent=agent_to_wire(_v.agent) if _v.agent.value else None,
        prompt=_v.prompt or None,
        state=agent_turn_state_to_wire(_v.state) if _v.state.value else None,
        input_tokens=_v.input_tokens or None,
        output_tokens=_v.output_tokens or None,
    )


def agent_turn_event_to_dict(_v: _t.AgentTurnEvent) -> dict[str, _Any]:
    return _rt.to_dict(agent_turn_event_to_wire(_v))


def agent_turn_event_from_dict(_j: dict[str, _Any]) -> _t.AgentTurnEvent:
    return agent_turn_event_from_wire(_rt.from_dict(_pb.AgentTurnEvent, _j))


def template_from_wire(_w: _pb.Template) -> _t.Template:
    return _t.Template(
        name=_w.name,
        version=_w.version,
        state=template_state_from_wire(_w.state),
        failure_message=_w.failure_message,
        built_in=_w.built_in,
        description=_w.description,
        settings=sandbox_settings_from_wire(_w.settings) if _w.settings is not None else None,
        create_time=_rt.time_from_wire(_w.create_time) if _w.create_time is not None else None,
        size_bytes=_w.size_bytes,
        base=_w.base,
        min_size=size_from_wire(_w.min_size),
    )


def template_to_wire(_v: _t.Template) -> _pb.Template:
    return _pb.Template(
        name=_v.name or None,
        version=_v.version or None,
        state=template_state_to_wire(_v.state) if _v.state.value else None,
        failure_message=_v.failure_message or None,
        built_in=_v.built_in or None,
        description=_v.description or None,
        settings=sandbox_settings_to_wire(_v.settings) if _v.settings is not None else None,
        create_time=_rt.time_to_wire(_v.create_time) if _v.create_time is not None else None,
        size_bytes=_v.size_bytes or None,
        base=_v.base or None,
        min_size=size_to_wire(_v.min_size) if _v.min_size.value else None,
    )


def template_to_dict(_v: _t.Template) -> dict[str, _Any]:
    return _rt.to_dict(template_to_wire(_v))


def template_from_dict(_j: dict[str, _Any]) -> _t.Template:
    return template_from_wire(_rt.from_dict(_pb.Template, _j))


def list_templates_response_from_wire(_w: _pb.ListTemplatesResponse) -> _t.ListTemplatesResponse:
    return _t.ListTemplatesResponse(
        templates=tuple(template_from_wire(_x) for _x in _w.templates),
        next_page_token=_w.next_page_token,
    )


def list_templates_response_to_wire(_v: _t.ListTemplatesResponse) -> _pb.ListTemplatesResponse:
    return _pb.ListTemplatesResponse(
        templates=[template_to_wire(_x) for _x in _v.templates],
        next_page_token=_v.next_page_token or None,
    )


def list_templates_response_to_dict(_v: _t.ListTemplatesResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_templates_response_to_wire(_v))


def list_templates_response_from_dict(_j: dict[str, _Any]) -> _t.ListTemplatesResponse:
    return list_templates_response_from_wire(_rt.from_dict(_pb.ListTemplatesResponse, _j))


def list_usage_response_from_wire(_w: _pb.ListUsageResponse) -> _t.ListUsageResponse:
    return _t.ListUsageResponse(
        rows=tuple(usage_row_from_wire(_x) for _x in _w.rows),
        next_page_token=_w.next_page_token,
    )


def list_usage_response_to_wire(_v: _t.ListUsageResponse) -> _pb.ListUsageResponse:
    return _pb.ListUsageResponse(
        rows=[usage_row_to_wire(_x) for _x in _v.rows],
        next_page_token=_v.next_page_token or None,
    )


def list_usage_response_to_dict(_v: _t.ListUsageResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_usage_response_to_wire(_v))


def list_usage_response_from_dict(_j: dict[str, _Any]) -> _t.ListUsageResponse:
    return list_usage_response_from_wire(_rt.from_dict(_pb.ListUsageResponse, _j))


def usage_row_from_wire(_w: _pb.UsageRow) -> _t.UsageRow:
    return _t.UsageRow(
        day=_rt.time_from_wire(_w.day) if _w.day is not None else None,
        meter=meter_from_wire(_w.meter),
        unit_hours=_w.unit_hours,
        size=size_from_wire(_w.size),
        cost_micros=_w.cost_micros,
    )


def usage_row_to_wire(_v: _t.UsageRow) -> _pb.UsageRow:
    return _pb.UsageRow(
        day=_rt.time_to_wire(_v.day) if _v.day is not None else None,
        meter=meter_to_wire(_v.meter) if _v.meter.value else None,
        unit_hours=_v.unit_hours or None,
        size=size_to_wire(_v.size) if _v.size.value else None,
        cost_micros=_v.cost_micros or None,
    )


def usage_row_to_dict(_v: _t.UsageRow) -> dict[str, _Any]:
    return _rt.to_dict(usage_row_to_wire(_v))


def usage_row_from_dict(_j: dict[str, _Any]) -> _t.UsageRow:
    return usage_row_from_wire(_rt.from_dict(_pb.UsageRow, _j))


def command_from_wire(_w: _pb.Command) -> _t.Command:
    return _t.Command(
        command_id=_w.command_id,
        command=_w.command,
        state=command_state_from_wire(_w.state),
        exit_code=_w.exit_code if _w.has_field("exit_code") else None,
        stdout=_w.stdout,
        stderr=_w.stderr,
        stdout_bytes=_w.stdout_bytes,
        stderr_bytes=_w.stderr_bytes,
        output_truncated=_w.output_truncated,
        started_by=started_by_from_wire(_w.started_by),
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        end_time=_rt.time_from_wire(_w.end_time) if _w.end_time is not None else None,
    )


def command_to_wire(_v: _t.Command) -> _pb.Command:
    return _pb.Command(
        command_id=_v.command_id or None,
        command=_v.command or None,
        state=command_state_to_wire(_v.state) if _v.state.value else None,
        exit_code=_v.exit_code,
        stdout=_v.stdout or None,
        stderr=_v.stderr or None,
        stdout_bytes=_v.stdout_bytes or None,
        stderr_bytes=_v.stderr_bytes or None,
        output_truncated=_v.output_truncated or None,
        started_by=started_by_to_wire(_v.started_by) if _v.started_by.value else None,
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        end_time=_rt.time_to_wire(_v.end_time) if _v.end_time is not None else None,
    )


def command_to_dict(_v: _t.Command) -> dict[str, _Any]:
    return _rt.to_dict(command_to_wire(_v))


def command_from_dict(_j: dict[str, _Any]) -> _t.Command:
    return command_from_wire(_rt.from_dict(_pb.Command, _j))


def list_commands_response_from_wire(_w: _pb.ListCommandsResponse) -> _t.ListCommandsResponse:
    return _t.ListCommandsResponse(
        commands=tuple(command_from_wire(_x) for _x in _w.commands),
    )


def list_commands_response_to_wire(_v: _t.ListCommandsResponse) -> _pb.ListCommandsResponse:
    return _pb.ListCommandsResponse(
        commands=[command_to_wire(_x) for _x in _v.commands],
    )


def list_commands_response_to_dict(_v: _t.ListCommandsResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_commands_response_to_wire(_v))


def list_commands_response_from_dict(_j: dict[str, _Any]) -> _t.ListCommandsResponse:
    return list_commands_response_from_wire(_rt.from_dict(_pb.ListCommandsResponse, _j))


def command_output_from_wire(_w: _pb.CommandOutput) -> _t.CommandOutput:
    _k = _w.output
    if _k is None:
        return _t.CommandOutput()
    if _k.field == "stdout":
        return _t.CommandOutput(
            stdout=_k.value,
        )
    if _k.field == "stderr":
        return _t.CommandOutput(
            stderr=_k.value,
        )
    if _k.field == "ended":
        return _t.CommandOutput(
            ended=command_from_wire(_k.value),
        )
    _rt.never(_k)


def command_output_to_wire(_v: _t.CommandOutput) -> _pb.CommandOutput:
    _w = _pb.CommandOutput()
    if _v.stdout is not None:
        _w.output = _Oneof[_Literal["stdout"], bytes]("stdout", _v.stdout)
    elif _v.stderr is not None:
        _w.output = _Oneof[_Literal["stderr"], bytes]("stderr", _v.stderr)
    elif _v.ended is not None:
        _w.output = _Oneof[_Literal["ended"], _pb.Command]("ended", command_to_wire(_v.ended))
    return _w


def command_output_to_dict(_v: _t.CommandOutput) -> dict[str, _Any]:
    return _rt.to_dict(command_output_to_wire(_v))


def command_output_from_dict(_j: dict[str, _Any]) -> _t.CommandOutput:
    return command_output_from_wire(_rt.from_dict(_pb.CommandOutput, _j))


def file_from_wire(_w: _pb.File) -> _t.File:
    _k = _w.content
    if _k is None:
        return _t.File(
            path=_w.path,
            size_bytes=_w.size_bytes,
        )
    if _k.field == "text":
        return _t.File(
            path=_w.path,
            size_bytes=_w.size_bytes,
            text=_k.value,
        )
    if _k.field == "data":
        return _t.File(
            path=_w.path,
            size_bytes=_w.size_bytes,
            data=_k.value,
        )
    _rt.never(_k)


def file_to_wire(_v: _t.File) -> _pb.File:
    _w = _pb.File(
        path=_v.path or None,
        size_bytes=_v.size_bytes or None,
    )
    if _v.text is not None:
        _w.content = _Oneof[_Literal["text"], str]("text", _v.text)
    elif _v.data is not None:
        _w.content = _Oneof[_Literal["data"], bytes]("data", _v.data)
    return _w


def file_to_dict(_v: _t.File) -> dict[str, _Any]:
    return _rt.to_dict(file_to_wire(_v))


def file_from_dict(_j: dict[str, _Any]) -> _t.File:
    return file_from_wire(_rt.from_dict(_pb.File, _j))


def list_files_response_from_wire(_w: _pb.ListFilesResponse) -> _t.ListFilesResponse:
    return _t.ListFilesResponse(
        files=tuple(file_info_from_wire(_x) for _x in _w.files),
        next_page_token=_w.next_page_token,
    )


def list_files_response_to_wire(_v: _t.ListFilesResponse) -> _pb.ListFilesResponse:
    return _pb.ListFilesResponse(
        files=[file_info_to_wire(_x) for _x in _v.files],
        next_page_token=_v.next_page_token or None,
    )


def list_files_response_to_dict(_v: _t.ListFilesResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_files_response_to_wire(_v))


def list_files_response_from_dict(_j: dict[str, _Any]) -> _t.ListFilesResponse:
    return list_files_response_from_wire(_rt.from_dict(_pb.ListFilesResponse, _j))


def file_info_from_wire(_w: _pb.FileInfo) -> _t.FileInfo:
    return _t.FileInfo(
        path=_w.path,
        kind=file_kind_from_wire(_w.kind),
        size_bytes=_w.size_bytes,
        mode=_w.mode,
        owner=_w.owner,
        modify_time=_rt.time_from_wire(_w.modify_time) if _w.modify_time is not None else None,
        symlink_target=_w.symlink_target,
    )


def file_info_to_wire(_v: _t.FileInfo) -> _pb.FileInfo:
    return _pb.FileInfo(
        path=_v.path or None,
        kind=file_kind_to_wire(_v.kind) if _v.kind.value else None,
        size_bytes=_v.size_bytes or None,
        mode=_v.mode or None,
        owner=_v.owner or None,
        modify_time=_rt.time_to_wire(_v.modify_time) if _v.modify_time is not None else None,
        symlink_target=_v.symlink_target or None,
    )


def file_info_to_dict(_v: _t.FileInfo) -> dict[str, _Any]:
    return _rt.to_dict(file_info_to_wire(_v))


def file_info_from_dict(_j: dict[str, _Any]) -> _t.FileInfo:
    return file_info_from_wire(_rt.from_dict(_pb.FileInfo, _j))


def file_change_from_wire(_w: _pb.FileChange) -> _t.FileChange:
    _k = _w.change
    if _k is None:
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
        )
    if _k.field == "text":
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
            text=_k.value,
        )
    if _k.field == "data":
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
            data=_k.value,
        )
    if _k.field == "edit":
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
            edit=text_edit_from_wire(_k.value),
        )
    if _k.field == "move_to":
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
            move_to=_k.value,
        )
    if _k.field == "delete":
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
            delete=delete_from_wire(_k.value),
        )
    if _k.field == "make_directory":
        return _t.FileChange(
            path=_w.path,
            mode=_w.mode,
            make_directory=make_directory_from_wire(_k.value),
        )
    _rt.never(_k)


def file_change_to_wire(_v: _t.FileChange) -> _pb.FileChange:
    _w = _pb.FileChange(
        path=_v.path or None,
        mode=_v.mode or None,
    )
    if _v.text is not None:
        _w.change = _Oneof[_Literal["text"], str]("text", _v.text)
    elif _v.data is not None:
        _w.change = _Oneof[_Literal["data"], bytes]("data", _v.data)
    elif _v.edit is not None:
        _w.change = _Oneof[_Literal["edit"], _pb.TextEdit]("edit", text_edit_to_wire(_v.edit))
    elif _v.move_to is not None:
        _w.change = _Oneof[_Literal["move_to"], str]("move_to", _v.move_to)
    elif _v.delete is not None:
        _w.change = _Oneof[_Literal["delete"], _pb.Delete]("delete", delete_to_wire(_v.delete))
    elif _v.make_directory is not None:
        _w.change = _Oneof[_Literal["make_directory"], _pb.MakeDirectory]("make_directory", make_directory_to_wire(_v.make_directory))
    return _w


def file_change_to_dict(_v: _t.FileChange) -> dict[str, _Any]:
    return _rt.to_dict(file_change_to_wire(_v))


def file_change_from_dict(_j: dict[str, _Any]) -> _t.FileChange:
    return file_change_from_wire(_rt.from_dict(_pb.FileChange, _j))


def delete_from_wire(_w: _pb.Delete) -> _t.Delete:
    return _t.Delete()


def delete_to_wire(_v: _t.Delete) -> _pb.Delete:
    return _pb.Delete()


def delete_to_dict(_v: _t.Delete) -> dict[str, _Any]:
    return _rt.to_dict(delete_to_wire(_v))


def delete_from_dict(_j: dict[str, _Any]) -> _t.Delete:
    return delete_from_wire(_rt.from_dict(_pb.Delete, _j))


def make_directory_from_wire(_w: _pb.MakeDirectory) -> _t.MakeDirectory:
    return _t.MakeDirectory()


def make_directory_to_wire(_v: _t.MakeDirectory) -> _pb.MakeDirectory:
    return _pb.MakeDirectory()


def make_directory_to_dict(_v: _t.MakeDirectory) -> dict[str, _Any]:
    return _rt.to_dict(make_directory_to_wire(_v))


def make_directory_from_dict(_j: dict[str, _Any]) -> _t.MakeDirectory:
    return make_directory_from_wire(_rt.from_dict(_pb.MakeDirectory, _j))


def text_edit_from_wire(_w: _pb.TextEdit) -> _t.TextEdit:
    return _t.TextEdit(
        old_text=_w.old_text,
        new_text=_w.new_text,
    )


def text_edit_to_wire(_v: _t.TextEdit) -> _pb.TextEdit:
    return _pb.TextEdit(
        old_text=_v.old_text or None,
        new_text=_v.new_text or None,
    )


def text_edit_to_dict(_v: _t.TextEdit) -> dict[str, _Any]:
    return _rt.to_dict(text_edit_to_wire(_v))


def text_edit_from_dict(_j: dict[str, _Any]) -> _t.TextEdit:
    return text_edit_from_wire(_rt.from_dict(_pb.TextEdit, _j))


def write_files_response_from_wire(_w: _pb.WriteFilesResponse) -> _t.WriteFilesResponse:
    return _t.WriteFilesResponse(
        done_count=_w.done_count,
        failure_message=_w.failure_message,
        failure=file_failure_from_wire(_w.failure),
    )


def write_files_response_to_wire(_v: _t.WriteFilesResponse) -> _pb.WriteFilesResponse:
    return _pb.WriteFilesResponse(
        done_count=_v.done_count or None,
        failure_message=_v.failure_message or None,
        failure=file_failure_to_wire(_v.failure) if _v.failure.value else None,
    )


def write_files_response_to_dict(_v: _t.WriteFilesResponse) -> dict[str, _Any]:
    return _rt.to_dict(write_files_response_to_wire(_v))


def write_files_response_from_dict(_j: dict[str, _Any]) -> _t.WriteFilesResponse:
    return write_files_response_from_wire(_rt.from_dict(_pb.WriteFilesResponse, _j))


def file_event_from_wire(_w: _pb.FileEvent) -> _t.FileEvent:
    return _t.FileEvent(
        path=_w.path,
        kind=file_event_kind_from_wire(_w.kind),
        to_path=_w.to_path,
    )


def file_event_to_wire(_v: _t.FileEvent) -> _pb.FileEvent:
    return _pb.FileEvent(
        path=_v.path or None,
        kind=file_event_kind_to_wire(_v.kind) if _v.kind.value else None,
        to_path=_v.to_path or None,
    )


def file_event_to_dict(_v: _t.FileEvent) -> dict[str, _Any]:
    return _rt.to_dict(file_event_to_wire(_v))


def file_event_from_dict(_j: dict[str, _Any]) -> _t.FileEvent:
    return file_event_from_wire(_rt.from_dict(_pb.FileEvent, _j))


def control_desktop_response_from_wire(_w: _pb.ControlDesktopResponse) -> _t.ControlDesktopResponse:
    return _t.ControlDesktopResponse(
        done_count=_w.done_count,
        failure_message=_w.failure_message,
        screenshot=screenshot_from_wire(_w.screenshot) if _w.screenshot is not None else None,
        failure=desktop_failure_from_wire(_w.failure),
    )


def control_desktop_response_to_wire(_v: _t.ControlDesktopResponse) -> _pb.ControlDesktopResponse:
    return _pb.ControlDesktopResponse(
        done_count=_v.done_count or None,
        failure_message=_v.failure_message or None,
        screenshot=screenshot_to_wire(_v.screenshot) if _v.screenshot is not None else None,
        failure=desktop_failure_to_wire(_v.failure) if _v.failure.value else None,
    )


def control_desktop_response_to_dict(_v: _t.ControlDesktopResponse) -> dict[str, _Any]:
    return _rt.to_dict(control_desktop_response_to_wire(_v))


def control_desktop_response_from_dict(_j: dict[str, _Any]) -> _t.ControlDesktopResponse:
    return control_desktop_response_from_wire(_rt.from_dict(_pb.ControlDesktopResponse, _j))


def screenshot_from_wire(_w: _pb.Screenshot) -> _t.Screenshot:
    return _t.Screenshot(
        image=_w.image,
        mime_type=_w.mime_type,
        width=_w.width,
        height=_w.height,
        cursor_x=_w.cursor_x,
        cursor_y=_w.cursor_y,
    )


def screenshot_to_wire(_v: _t.Screenshot) -> _pb.Screenshot:
    return _pb.Screenshot(
        image=_v.image or None,
        mime_type=_v.mime_type or None,
        width=_v.width or None,
        height=_v.height or None,
        cursor_x=_v.cursor_x or None,
        cursor_y=_v.cursor_y or None,
    )


def screenshot_to_dict(_v: _t.Screenshot) -> dict[str, _Any]:
    return _rt.to_dict(screenshot_to_wire(_v))


def screenshot_from_dict(_j: dict[str, _Any]) -> _t.Screenshot:
    return screenshot_from_wire(_rt.from_dict(_pb.Screenshot, _j))


def desktop_action_from_wire(_w: _pb.DesktopAction) -> _t.DesktopAction:
    _k = _w.action
    if _k is None:
        return _t.DesktopAction()
    if _k.field == "click":
        return _t.DesktopAction(
            click=click_from_wire(_k.value),
        )
    if _k.field == "move_mouse":
        return _t.DesktopAction(
            move_mouse=point_from_wire(_k.value),
        )
    if _k.field == "drag":
        return _t.DesktopAction(
            drag=drag_from_wire(_k.value),
        )
    if _k.field == "scroll":
        return _t.DesktopAction(
            scroll=scroll_from_wire(_k.value),
        )
    if _k.field == "type_text":
        return _t.DesktopAction(
            type_text=_k.value,
        )
    if _k.field == "press_keys":
        return _t.DesktopAction(
            press_keys=_k.value,
        )
    if _k.field == "wait_ms":
        return _t.DesktopAction(
            wait_ms=_k.value,
        )
    _rt.never(_k)


def desktop_action_to_wire(_v: _t.DesktopAction) -> _pb.DesktopAction:
    _w = _pb.DesktopAction()
    if _v.click is not None:
        _w.action = _Oneof[_Literal["click"], _pb.Click]("click", click_to_wire(_v.click))
    elif _v.move_mouse is not None:
        _w.action = _Oneof[_Literal["move_mouse"], _pb.Point]("move_mouse", point_to_wire(_v.move_mouse))
    elif _v.drag is not None:
        _w.action = _Oneof[_Literal["drag"], _pb.Drag]("drag", drag_to_wire(_v.drag))
    elif _v.scroll is not None:
        _w.action = _Oneof[_Literal["scroll"], _pb.Scroll]("scroll", scroll_to_wire(_v.scroll))
    elif _v.type_text is not None:
        _w.action = _Oneof[_Literal["type_text"], str]("type_text", _v.type_text)
    elif _v.press_keys is not None:
        _w.action = _Oneof[_Literal["press_keys"], str]("press_keys", _v.press_keys)
    elif _v.wait_ms is not None:
        _w.action = _Oneof[_Literal["wait_ms"], int]("wait_ms", _v.wait_ms)
    return _w


def desktop_action_to_dict(_v: _t.DesktopAction) -> dict[str, _Any]:
    return _rt.to_dict(desktop_action_to_wire(_v))


def desktop_action_from_dict(_j: dict[str, _Any]) -> _t.DesktopAction:
    return desktop_action_from_wire(_rt.from_dict(_pb.DesktopAction, _j))


def point_from_wire(_w: _pb.Point) -> _t.Point:
    return _t.Point(
        x=_w.x,
        y=_w.y,
    )


def point_to_wire(_v: _t.Point) -> _pb.Point:
    return _pb.Point(
        x=_v.x or None,
        y=_v.y or None,
    )


def point_to_dict(_v: _t.Point) -> dict[str, _Any]:
    return _rt.to_dict(point_to_wire(_v))


def point_from_dict(_j: dict[str, _Any]) -> _t.Point:
    return point_from_wire(_rt.from_dict(_pb.Point, _j))


def click_from_wire(_w: _pb.Click) -> _t.Click:
    return _t.Click(
        x=_w.x,
        y=_w.y,
        button=mouse_button_from_wire(_w.button),
        count=_w.count,
        hold_keys=_w.hold_keys,
    )


def click_to_wire(_v: _t.Click) -> _pb.Click:
    return _pb.Click(
        x=_v.x or None,
        y=_v.y or None,
        button=mouse_button_to_wire(_v.button) if _v.button.value else None,
        count=_v.count or None,
        hold_keys=_v.hold_keys or None,
    )


def click_to_dict(_v: _t.Click) -> dict[str, _Any]:
    return _rt.to_dict(click_to_wire(_v))


def click_from_dict(_j: dict[str, _Any]) -> _t.Click:
    return click_from_wire(_rt.from_dict(_pb.Click, _j))


def drag_from_wire(_w: _pb.Drag) -> _t.Drag:
    return _t.Drag(
        path=tuple(point_from_wire(_x) for _x in _w.path),
    )


def drag_to_wire(_v: _t.Drag) -> _pb.Drag:
    return _pb.Drag(
        path=[point_to_wire(_x) for _x in _v.path],
    )


def drag_to_dict(_v: _t.Drag) -> dict[str, _Any]:
    return _rt.to_dict(drag_to_wire(_v))


def drag_from_dict(_j: dict[str, _Any]) -> _t.Drag:
    return drag_from_wire(_rt.from_dict(_pb.Drag, _j))


def scroll_from_wire(_w: _pb.Scroll) -> _t.Scroll:
    return _t.Scroll(
        x=_w.x,
        y=_w.y,
        down=_w.down,
        right=_w.right,
    )


def scroll_to_wire(_v: _t.Scroll) -> _pb.Scroll:
    return _pb.Scroll(
        x=_v.x or None,
        y=_v.y or None,
        down=_v.down or None,
        right=_v.right or None,
    )


def scroll_to_dict(_v: _t.Scroll) -> dict[str, _Any]:
    return _rt.to_dict(scroll_to_wire(_v))


def scroll_from_dict(_j: dict[str, _Any]) -> _t.Scroll:
    return scroll_from_wire(_rt.from_dict(_pb.Scroll, _j))


def desktop_from_wire(_w: _pb.Desktop) -> _t.Desktop:
    return _t.Desktop(
        width=_w.width,
        height=_w.height,
    )


def desktop_to_wire(_v: _t.Desktop) -> _pb.Desktop:
    return _pb.Desktop(
        width=_v.width or None,
        height=_v.height or None,
    )


def desktop_to_dict(_v: _t.Desktop) -> dict[str, _Any]:
    return _rt.to_dict(desktop_to_wire(_v))


def desktop_from_dict(_j: dict[str, _Any]) -> _t.Desktop:
    return desktop_from_wire(_rt.from_dict(_pb.Desktop, _j))


def terminal_link_from_wire(_w: _pb.TerminalLink) -> _t.TerminalLink:
    return _t.TerminalLink(
        command=_w.command,
    )


def terminal_link_to_wire(_v: _t.TerminalLink) -> _pb.TerminalLink:
    return _pb.TerminalLink(
        command=_v.command or None,
    )


def terminal_link_to_dict(_v: _t.TerminalLink) -> dict[str, _Any]:
    return _rt.to_dict(terminal_link_to_wire(_v))


def terminal_link_from_dict(_j: dict[str, _Any]) -> _t.TerminalLink:
    return terminal_link_from_wire(_rt.from_dict(_pb.TerminalLink, _j))


def desktop_link_from_wire(_w: _pb.DesktopLink) -> _t.DesktopLink:
    return _t.DesktopLink(
        view_only=_w.view_only,
    )


def desktop_link_to_wire(_v: _t.DesktopLink) -> _pb.DesktopLink:
    return _pb.DesktopLink(
        view_only=_v.view_only or None,
    )


def desktop_link_to_dict(_v: _t.DesktopLink) -> dict[str, _Any]:
    return _rt.to_dict(desktop_link_to_wire(_v))


def desktop_link_from_dict(_j: dict[str, _Any]) -> _t.DesktopLink:
    return desktop_link_from_wire(_rt.from_dict(_pb.DesktopLink, _j))


def link_from_wire(_w: _pb.Link) -> _t.Link:
    return _t.Link(
        url=_w.url,
        expire_time=_rt.time_from_wire(_w.expire_time) if _w.expire_time is not None else None,
        token=_w.token,
    )


def link_to_wire(_v: _t.Link) -> _pb.Link:
    return _pb.Link(
        url=_v.url or None,
        expire_time=_rt.time_to_wire(_v.expire_time) if _v.expire_time is not None else None,
        token=_v.token or None,
    )


def link_to_dict(_v: _t.Link) -> dict[str, _Any]:
    return _rt.to_dict(link_to_wire(_v))


def link_from_dict(_j: dict[str, _Any]) -> _t.Link:
    return link_from_wire(_rt.from_dict(_pb.Link, _j))


def agent_turn_from_wire(_w: _pb.AgentTurn) -> _t.AgentTurn:
    return _t.AgentTurn(
        turn_id=_w.turn_id,
        conversation_id=_w.conversation_id,
        agent=agent_from_wire(_w.agent),
        model=_w.model,
        state=agent_turn_state_from_wire(_w.state),
        reply=_w.reply,
        failure_message=_w.failure_message,
        input_tokens=_w.input_tokens,
        output_tokens=_w.output_tokens,
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        end_time=_rt.time_from_wire(_w.end_time) if _w.end_time is not None else None,
    )


def agent_turn_to_wire(_v: _t.AgentTurn) -> _pb.AgentTurn:
    return _pb.AgentTurn(
        turn_id=_v.turn_id or None,
        conversation_id=_v.conversation_id or None,
        agent=agent_to_wire(_v.agent) if _v.agent.value else None,
        model=_v.model or None,
        state=agent_turn_state_to_wire(_v.state) if _v.state.value else None,
        reply=_v.reply or None,
        failure_message=_v.failure_message or None,
        input_tokens=_v.input_tokens or None,
        output_tokens=_v.output_tokens or None,
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        end_time=_rt.time_to_wire(_v.end_time) if _v.end_time is not None else None,
    )


def agent_turn_to_dict(_v: _t.AgentTurn) -> dict[str, _Any]:
    return _rt.to_dict(agent_turn_to_wire(_v))


def agent_turn_from_dict(_j: dict[str, _Any]) -> _t.AgentTurn:
    return agent_turn_from_wire(_rt.from_dict(_pb.AgentTurn, _j))


def list_conversations_response_from_wire(_w: _pb.ListConversationsResponse) -> _t.ListConversationsResponse:
    return _t.ListConversationsResponse(
        conversations=tuple(conversation_from_wire(_x) for _x in _w.conversations),
        next_page_token=_w.next_page_token,
    )


def list_conversations_response_to_wire(_v: _t.ListConversationsResponse) -> _pb.ListConversationsResponse:
    return _pb.ListConversationsResponse(
        conversations=[conversation_to_wire(_x) for _x in _v.conversations],
        next_page_token=_v.next_page_token or None,
    )


def list_conversations_response_to_dict(_v: _t.ListConversationsResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_conversations_response_to_wire(_v))


def list_conversations_response_from_dict(_j: dict[str, _Any]) -> _t.ListConversationsResponse:
    return list_conversations_response_from_wire(_rt.from_dict(_pb.ListConversationsResponse, _j))


def conversation_from_wire(_w: _pb.Conversation) -> _t.Conversation:
    return _t.Conversation(
        conversation_id=_w.conversation_id,
        agent=agent_from_wire(_w.agent),
        model=_w.model,
        cwd=_w.cwd,
        running_turn_id=_w.running_turn_id,
        input_tokens=_w.input_tokens,
        output_tokens=_w.output_tokens,
        create_time=_rt.time_from_wire(_w.create_time) if _w.create_time is not None else None,
    )


def conversation_to_wire(_v: _t.Conversation) -> _pb.Conversation:
    return _pb.Conversation(
        conversation_id=_v.conversation_id or None,
        agent=agent_to_wire(_v.agent) if _v.agent.value else None,
        model=_v.model or None,
        cwd=_v.cwd or None,
        running_turn_id=_v.running_turn_id or None,
        input_tokens=_v.input_tokens or None,
        output_tokens=_v.output_tokens or None,
        create_time=_rt.time_to_wire(_v.create_time) if _v.create_time is not None else None,
    )


def conversation_to_dict(_v: _t.Conversation) -> dict[str, _Any]:
    return _rt.to_dict(conversation_to_wire(_v))


def conversation_from_dict(_j: dict[str, _Any]) -> _t.Conversation:
    return conversation_from_wire(_rt.from_dict(_pb.Conversation, _j))


def agent_event_from_wire(_w: _pb.AgentEvent) -> _t.AgentEvent:
    _k = _w.event
    if _k is None:
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
        )
    if _k.field == "prompt":
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
            prompt=_k.value,
        )
    if _k.field == "message":
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
            message=_k.value,
        )
    if _k.field == "tool_call":
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
            tool_call=tool_call_from_wire(_k.value),
        )
    if _k.field == "tool_result":
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
            tool_result=tool_result_from_wire(_k.value),
        )
    if _k.field == "turn_end":
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
            turn_end=agent_turn_from_wire(_k.value),
        )
    if _k.field == "caught_up":
        return _t.AgentEvent(
            seq=_w.seq,
            time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
            turn_id=_w.turn_id,
            caught_up=caught_up_from_wire(_k.value),
        )
    _rt.never(_k)


def agent_event_to_wire(_v: _t.AgentEvent) -> _pb.AgentEvent:
    _w = _pb.AgentEvent(
        seq=_v.seq or None,
        time=_rt.time_to_wire(_v.time) if _v.time is not None else None,
        turn_id=_v.turn_id or None,
    )
    if _v.prompt is not None:
        _w.event = _Oneof[_Literal["prompt"], str]("prompt", _v.prompt)
    elif _v.message is not None:
        _w.event = _Oneof[_Literal["message"], str]("message", _v.message)
    elif _v.tool_call is not None:
        _w.event = _Oneof[_Literal["tool_call"], _pb.ToolCall]("tool_call", tool_call_to_wire(_v.tool_call))
    elif _v.tool_result is not None:
        _w.event = _Oneof[_Literal["tool_result"], _pb.ToolResult]("tool_result", tool_result_to_wire(_v.tool_result))
    elif _v.turn_end is not None:
        _w.event = _Oneof[_Literal["turn_end"], _pb.AgentTurn]("turn_end", agent_turn_to_wire(_v.turn_end))
    elif _v.caught_up is not None:
        _w.event = _Oneof[_Literal["caught_up"], _pb.CaughtUp]("caught_up", caught_up_to_wire(_v.caught_up))
    return _w


def agent_event_to_dict(_v: _t.AgentEvent) -> dict[str, _Any]:
    return _rt.to_dict(agent_event_to_wire(_v))


def agent_event_from_dict(_j: dict[str, _Any]) -> _t.AgentEvent:
    return agent_event_from_wire(_rt.from_dict(_pb.AgentEvent, _j))


def caught_up_from_wire(_w: _pb.CaughtUp) -> _t.CaughtUp:
    return _t.CaughtUp()


def caught_up_to_wire(_v: _t.CaughtUp) -> _pb.CaughtUp:
    return _pb.CaughtUp()


def caught_up_to_dict(_v: _t.CaughtUp) -> dict[str, _Any]:
    return _rt.to_dict(caught_up_to_wire(_v))


def caught_up_from_dict(_j: dict[str, _Any]) -> _t.CaughtUp:
    return caught_up_from_wire(_rt.from_dict(_pb.CaughtUp, _j))


def tool_call_from_wire(_w: _pb.ToolCall) -> _t.ToolCall:
    return _t.ToolCall(
        tool_call_id=_w.tool_call_id,
        name=_w.name,
        input=_w.input,
    )


def tool_call_to_wire(_v: _t.ToolCall) -> _pb.ToolCall:
    return _pb.ToolCall(
        tool_call_id=_v.tool_call_id or None,
        name=_v.name or None,
        input=_v.input or None,
    )


def tool_call_to_dict(_v: _t.ToolCall) -> dict[str, _Any]:
    return _rt.to_dict(tool_call_to_wire(_v))


def tool_call_from_dict(_j: dict[str, _Any]) -> _t.ToolCall:
    return tool_call_from_wire(_rt.from_dict(_pb.ToolCall, _j))


def tool_result_from_wire(_w: _pb.ToolResult) -> _t.ToolResult:
    return _t.ToolResult(
        tool_call_id=_w.tool_call_id,
        output=_w.output,
        failed=_w.failed,
    )


def tool_result_to_wire(_v: _t.ToolResult) -> _pb.ToolResult:
    return _pb.ToolResult(
        tool_call_id=_v.tool_call_id or None,
        output=_v.output or None,
        failed=_v.failed or None,
    )


def tool_result_to_dict(_v: _t.ToolResult) -> dict[str, _Any]:
    return _rt.to_dict(tool_result_to_wire(_v))


def tool_result_from_dict(_j: dict[str, _Any]) -> _t.ToolResult:
    return tool_result_from_wire(_rt.from_dict(_pb.ToolResult, _j))


def limit_reached_from_wire(_w: _pb.LimitReached) -> _t.LimitReached:
    return _t.LimitReached(
        limit=_w.limit,
        max=_w.max,
        retry_time=_rt.time_from_wire(_w.retry_time) if _w.retry_time is not None else None,
    )


def limit_reached_to_wire(_v: _t.LimitReached) -> _pb.LimitReached:
    return _pb.LimitReached(
        limit=_v.limit or None,
        max=_v.max or None,
        retry_time=_rt.time_to_wire(_v.retry_time) if _v.retry_time is not None else None,
    )


def limit_reached_to_dict(_v: _t.LimitReached) -> dict[str, _Any]:
    return _rt.to_dict(limit_reached_to_wire(_v))


def limit_reached_from_dict(_j: dict[str, _Any]) -> _t.LimitReached:
    return limit_reached_from_wire(_rt.from_dict(_pb.LimitReached, _j))


def stopped_from_wire(_w: _pb.Stopped) -> _t.Stopped:
    return _t.Stopped()


def stopped_to_wire(_v: _t.Stopped) -> _pb.Stopped:
    return _pb.Stopped()


def stopped_to_dict(_v: _t.Stopped) -> dict[str, _Any]:
    return _rt.to_dict(stopped_to_wire(_v))


def stopped_from_dict(_j: dict[str, _Any]) -> _t.Stopped:
    return stopped_from_wire(_rt.from_dict(_pb.Stopped, _j))


def usage_unpaid_from_wire(_w: _pb.UsageUnpaid) -> _t.UsageUnpaid:
    return _t.UsageUnpaid()


def usage_unpaid_to_wire(_v: _t.UsageUnpaid) -> _pb.UsageUnpaid:
    return _pb.UsageUnpaid()


def usage_unpaid_to_dict(_v: _t.UsageUnpaid) -> dict[str, _Any]:
    return _rt.to_dict(usage_unpaid_to_wire(_v))


def usage_unpaid_from_dict(_j: dict[str, _Any]) -> _t.UsageUnpaid:
    return usage_unpaid_from_wire(_rt.from_dict(_pb.UsageUnpaid, _j))


def restoring_from_wire(_w: _pb.Restoring) -> _t.Restoring:
    return _t.Restoring(
        fetched_bytes=_w.fetched_bytes,
        total_bytes=_w.total_bytes,
    )


def restoring_to_wire(_v: _t.Restoring) -> _pb.Restoring:
    return _pb.Restoring(
        fetched_bytes=_v.fetched_bytes or None,
        total_bytes=_v.total_bytes or None,
    )


def restoring_to_dict(_v: _t.Restoring) -> dict[str, _Any]:
    return _rt.to_dict(restoring_to_wire(_v))


def restoring_from_dict(_j: dict[str, _Any]) -> _t.Restoring:
    return restoring_from_wire(_rt.from_dict(_pb.Restoring, _j))


def no_capacity_from_wire(_w: _pb.NoCapacity) -> _t.NoCapacity:
    return _t.NoCapacity(
        bound=room_bound_from_wire(_w.bound),
    )


def no_capacity_to_wire(_v: _t.NoCapacity) -> _pb.NoCapacity:
    return _pb.NoCapacity(
        bound=room_bound_to_wire(_v.bound) if _v.bound.value else None,
    )


def no_capacity_to_dict(_v: _t.NoCapacity) -> dict[str, _Any]:
    return _rt.to_dict(no_capacity_to_wire(_v))


def no_capacity_from_dict(_j: dict[str, _Any]) -> _t.NoCapacity:
    return no_capacity_from_wire(_rt.from_dict(_pb.NoCapacity, _j))


def name_taken_from_wire(_w: _pb.NameTaken) -> _t.NameTaken:
    return _t.NameTaken(
        sandbox_id=_w.sandbox_id,
    )


def name_taken_to_wire(_v: _t.NameTaken) -> _pb.NameTaken:
    return _pb.NameTaken(
        sandbox_id=_v.sandbox_id or None,
    )


def name_taken_to_dict(_v: _t.NameTaken) -> dict[str, _Any]:
    return _rt.to_dict(name_taken_to_wire(_v))


def name_taken_from_dict(_j: dict[str, _Any]) -> _t.NameTaken:
    return name_taken_from_wire(_rt.from_dict(_pb.NameTaken, _j))


def workspace_choice_from_wire(_w: _pb.WorkspaceChoice) -> _t.WorkspaceChoice:
    return _t.WorkspaceChoice(
        workspaces=tuple(workspace_from_wire(_x) for _x in _w.workspaces),
        total=_w.total,
    )


def workspace_choice_to_wire(_v: _t.WorkspaceChoice) -> _pb.WorkspaceChoice:
    return _pb.WorkspaceChoice(
        workspaces=[workspace_to_wire(_x) for _x in _v.workspaces],
        total=_v.total or None,
    )


def workspace_choice_to_dict(_v: _t.WorkspaceChoice) -> dict[str, _Any]:
    return _rt.to_dict(workspace_choice_to_wire(_v))


def workspace_choice_from_dict(_j: dict[str, _Any]) -> _t.WorkspaceChoice:
    return workspace_choice_from_wire(_rt.from_dict(_pb.WorkspaceChoice, _j))


def agent_sign_in_from_wire(_w: _pb.AgentSignIn) -> _t.AgentSignIn:
    return _t.AgentSignIn(
        variable=_w.variable,
        sign_in_command=_w.sign_in_command,
    )


def agent_sign_in_to_wire(_v: _t.AgentSignIn) -> _pb.AgentSignIn:
    return _pb.AgentSignIn(
        variable=_v.variable or None,
        sign_in_command=_v.sign_in_command or None,
    )


def agent_sign_in_to_dict(_v: _t.AgentSignIn) -> dict[str, _Any]:
    return _rt.to_dict(agent_sign_in_to_wire(_v))


def agent_sign_in_from_dict(_j: dict[str, _Any]) -> _t.AgentSignIn:
    return agent_sign_in_from_wire(_rt.from_dict(_pb.AgentSignIn, _j))


def get_workspace_request(
    *,
    workspace: str,
) -> _pb.GetWorkspaceRequest:
    _w = _pb.GetWorkspaceRequest(
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def set_ssh_keys_request(
    *,
    ssh_keys: Sequence[str],
    workspace: str,
) -> _pb.SetSshKeysRequest:
    _w = _pb.SetSshKeysRequest(
        ssh_keys=_rt.strings("set_ssh_keys(ssh_keys=)", ssh_keys),
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def set_secret_request(
    *,
    name: str,
    value: str,
    hosts: Sequence[str],
    workspace: str,
) -> _pb.SetSecretRequest:
    _w = _pb.SetSecretRequest(
        name=name or None,
        value=value or None,
        hosts=_rt.strings("set_secret(hosts=)", hosts),
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def delete_secret_request(
    *,
    name: str,
    workspace: str,
) -> _pb.DeleteSecretRequest:
    _w = _pb.DeleteSecretRequest(
        name=name or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def create_sandbox_request(
    *,
    template: str,
    settings: _t.SandboxSettings | None,
    labels: Sequence[_t.Label],
    name: str,
    request_id: str,
    workspace: str,
) -> _pb.CreateSandboxRequest:
    _w = _pb.CreateSandboxRequest(
        template=template or None,
        settings=sandbox_settings_to_wire(settings) if settings is not None else None,
        labels=[label_to_wire(_x) for _x in labels],
        name=name or None,
        request_id=request_id or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def get_sandbox_request(
    *,
    sandbox_id: str,
) -> _pb.GetSandboxRequest:
    _w = _pb.GetSandboxRequest(
        sandbox_id=sandbox_id or None,
    )
    return _rt.checked(_w)


def list_sandboxes_request(
    *,
    states: Sequence[_t.SandboxState],
    labels: Sequence[_t.Label],
    page_size: int,
    page_token: str,
    name: str,
    workspace: str,
) -> _pb.ListSandboxesRequest:
    _w = _pb.ListSandboxesRequest(
        states=[sandbox_state_to_wire(_x) for _x in states],
        labels=[label_to_wire(_x) for _x in labels],
        page_size=page_size or None,
        page_token=page_token or None,
        name=name or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def update_sandbox_request(
    *,
    sandbox_id: str,
    settings: _t.SandboxSettings | None,
    if_revision: int,
    revoke_tokens: bool,
    grow_disk: bool,
    name: str | None,
) -> _pb.UpdateSandboxRequest:
    _w = _pb.UpdateSandboxRequest(
        sandbox_id=sandbox_id or None,
        settings=sandbox_settings_to_wire(settings) if settings is not None else None,
        if_revision=if_revision or None,
        revoke_tokens=revoke_tokens or None,
        grow_disk=grow_disk or None,
        name=name,
    )
    return _rt.checked(_w)


def pause_sandbox_request(
    *,
    sandbox_id: str,
) -> _pb.PauseSandboxRequest:
    _w = _pb.PauseSandboxRequest(
        sandbox_id=sandbox_id or None,
    )
    return _rt.checked(_w)


def stop_sandbox_request(
    *,
    sandbox_id: str,
) -> _pb.StopSandboxRequest:
    _w = _pb.StopSandboxRequest(
        sandbox_id=sandbox_id or None,
    )
    return _rt.checked(_w)


def resume_sandbox_request(
    *,
    sandbox_id: str,
) -> _pb.ResumeSandboxRequest:
    _w = _pb.ResumeSandboxRequest(
        sandbox_id=sandbox_id or None,
    )
    return _rt.checked(_w)


def delete_sandbox_request(
    *,
    sandbox_id: str,
) -> _pb.DeleteSandboxRequest:
    _w = _pb.DeleteSandboxRequest(
        sandbox_id=sandbox_id or None,
    )
    return _rt.checked(_w)


def connect_sandbox_request(
    *,
    sandbox_id: str,
    ttl_seconds: int,
) -> _pb.ConnectSandboxRequest:
    _w = _pb.ConnectSandboxRequest(
        sandbox_id=sandbox_id or None,
        ttl_seconds=ttl_seconds or None,
    )
    return _rt.checked(_w)


def get_sandbox_metrics_request(
    *,
    sandbox_id: str,
    since: datetime | None,
    until: datetime | None,
    step_seconds: int,
) -> _pb.GetSandboxMetricsRequest:
    _w = _pb.GetSandboxMetricsRequest(
        sandbox_id=sandbox_id or None,
        since=_rt.time_to_wire(since) if since is not None else None,
        until=_rt.time_to_wire(until) if until is not None else None,
        step_seconds=step_seconds or None,
    )
    return _rt.checked(_w)


def list_sandbox_events_request(
    *,
    sandbox_id: str,
    kinds: Sequence[_t.SandboxEventKind],
    after: str,
    newest_first: bool,
    limit: int,
) -> _pb.ListSandboxEventsRequest:
    _w = _pb.ListSandboxEventsRequest(
        sandbox_id=sandbox_id or None,
        kinds=[sandbox_event_kind_to_wire(_x) for _x in kinds],
        after=after or None,
        newest_first=newest_first or None,
        limit=limit or None,
    )
    return _rt.checked(_w)


def watch_sandbox_events_request(
    *,
    sandbox_id: str,
    kinds: Sequence[_t.SandboxEventKind],
    after: str,
) -> _pb.WatchSandboxEventsRequest:
    _w = _pb.WatchSandboxEventsRequest(
        sandbox_id=sandbox_id or None,
        kinds=[sandbox_event_kind_to_wire(_x) for _x in kinds],
        after=after or None,
    )
    return _rt.checked(_w)


def create_template_request(
    *,
    name: str,
    sandbox_id: str,
    description: str,
    request_id: str,
) -> _pb.CreateTemplateRequest:
    _w = _pb.CreateTemplateRequest(
        name=name or None,
        sandbox_id=sandbox_id or None,
        description=description or None,
        request_id=request_id or None,
    )
    return _rt.checked(_w)


def get_template_request(
    *,
    template: str,
    workspace: str,
) -> _pb.GetTemplateRequest:
    _w = _pb.GetTemplateRequest(
        template=template or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def list_templates_request(
    *,
    name: str,
    page_size: int,
    page_token: str,
    workspace: str,
) -> _pb.ListTemplatesRequest:
    _w = _pb.ListTemplatesRequest(
        name=name or None,
        page_size=page_size or None,
        page_token=page_token or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def delete_template_request(
    *,
    name: str,
    workspace: str,
) -> _pb.DeleteTemplateRequest:
    _w = _pb.DeleteTemplateRequest(
        name=name or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def list_usage_request(
    *,
    since: datetime | None,
    until: datetime | None,
    page_size: int,
    page_token: str,
    workspace: str,
) -> _pb.ListUsageRequest:
    _w = _pb.ListUsageRequest(
        since=_rt.time_to_wire(since) if since is not None else None,
        until=_rt.time_to_wire(until) if until is not None else None,
        page_size=page_size or None,
        page_token=page_token or None,
        workspace=workspace or None,
    )
    return _rt.checked(_w)


def run_command_request(
    *,
    sandbox_id: str,
    command: str,
    cwd: str,
    user: str,
    stdin: str,
    wait_seconds: int | None,
    wait_for_port: int,
    timeout_seconds: int,
    keep_awake: bool,
    request_id: str,
) -> _pb.RunCommandRequest:
    _w = _pb.RunCommandRequest(
        sandbox_id=sandbox_id or None,
        command=command or None,
        cwd=cwd or None,
        user=user or None,
        stdin=stdin or None,
        wait_seconds=wait_seconds,
        wait_for_port=wait_for_port or None,
        timeout_seconds=timeout_seconds or None,
        keep_awake=keep_awake or None,
        request_id=request_id or None,
    )
    return _rt.checked(_w)


def get_command_request(
    *,
    sandbox_id: str,
    command_id: str,
    wait_seconds: int | None,
    stdout_after_bytes: int,
    stderr_after_bytes: int,
) -> _pb.GetCommandRequest:
    _w = _pb.GetCommandRequest(
        sandbox_id=sandbox_id or None,
        command_id=command_id or None,
        wait_seconds=wait_seconds,
        stdout_after_bytes=stdout_after_bytes or None,
        stderr_after_bytes=stderr_after_bytes or None,
    )
    return _rt.checked(_w)


def stop_command_request(
    *,
    sandbox_id: str,
    command_id: str,
) -> _pb.StopCommandRequest:
    _w = _pb.StopCommandRequest(
        sandbox_id=sandbox_id or None,
        command_id=command_id or None,
    )
    return _rt.checked(_w)


def list_commands_request(
    *,
    sandbox_id: str,
) -> _pb.ListCommandsRequest:
    _w = _pb.ListCommandsRequest(
        sandbox_id=sandbox_id or None,
    )
    return _rt.checked(_w)


def watch_command_request(
    *,
    sandbox_id: str,
    command_id: str,
) -> _pb.WatchCommandRequest:
    _w = _pb.WatchCommandRequest(
        sandbox_id=sandbox_id or None,
        command_id=command_id or None,
    )
    return _rt.checked(_w)


def read_file_request(
    *,
    sandbox_id: str,
    path: str,
    offset_bytes: int,
    length_bytes: int,
) -> _pb.ReadFileRequest:
    _w = _pb.ReadFileRequest(
        sandbox_id=sandbox_id or None,
        path=path or None,
        offset_bytes=offset_bytes or None,
        length_bytes=length_bytes or None,
    )
    return _rt.checked(_w)


def list_files_request(
    *,
    sandbox_id: str,
    path: str,
    depth: int,
    page_token: str,
) -> _pb.ListFilesRequest:
    _w = _pb.ListFilesRequest(
        sandbox_id=sandbox_id or None,
        path=path or None,
        depth=depth or None,
        page_token=page_token or None,
    )
    return _rt.checked(_w)


def write_files_request(
    *,
    sandbox_id: str,
    changes: Sequence[_t.FileChange],
) -> _pb.WriteFilesRequest:
    _w = _pb.WriteFilesRequest(
        sandbox_id=sandbox_id or None,
        changes=[file_change_to_wire(_x) for _x in changes],
    )
    return _rt.checked(_w)


def watch_files_request(
    *,
    sandbox_id: str,
    path: str,
    recursive: bool,
) -> _pb.WatchFilesRequest:
    _w = _pb.WatchFilesRequest(
        sandbox_id=sandbox_id or None,
        path=path or None,
        recursive=recursive or None,
    )
    return _rt.checked(_w)


def control_desktop_request(
    *,
    sandbox_id: str,
    actions: Sequence[_t.DesktopAction],
) -> _pb.ControlDesktopRequest:
    _w = _pb.ControlDesktopRequest(
        sandbox_id=sandbox_id or None,
        actions=[desktop_action_to_wire(_x) for _x in actions],
    )
    return _rt.checked(_w)


def create_link_request(
    *,
    sandbox_id: str,
    port: int | None,
    terminal: _t.TerminalLink | None,
    desktop: _t.DesktopLink | None,
    download_path: str | None,
    upload_path: str | None,
    ttl_seconds: int,
) -> _pb.CreateLinkRequest:
    _rt.one_of("create_link", port=port, terminal=terminal, desktop=desktop, download_path=download_path, upload_path=upload_path)
    _w = _pb.CreateLinkRequest(
        sandbox_id=sandbox_id or None,
        ttl_seconds=ttl_seconds or None,
    )
    if port is not None:
        _w.target = _Oneof[_Literal["port"], int]("port", port)
    elif terminal is not None:
        _w.target = _Oneof[_Literal["terminal"], _pb.TerminalLink]("terminal", terminal_link_to_wire(terminal))
    elif desktop is not None:
        _w.target = _Oneof[_Literal["desktop"], _pb.DesktopLink]("desktop", desktop_link_to_wire(desktop))
    elif download_path is not None:
        _w.target = _Oneof[_Literal["download_path"], str]("download_path", download_path)
    elif upload_path is not None:
        _w.target = _Oneof[_Literal["upload_path"], str]("upload_path", upload_path)
    return _rt.checked(_w)


def prompt_agent_request(
    *,
    sandbox_id: str,
    prompt: str,
    agent: _t.Agent,
    conversation_id: str,
    model: str,
    cwd: str,
    wait_seconds: int | None,
    request_id: str,
) -> _pb.PromptAgentRequest:
    _w = _pb.PromptAgentRequest(
        sandbox_id=sandbox_id or None,
        prompt=prompt or None,
        agent=agent_to_wire(agent) if agent.value else None,
        conversation_id=conversation_id or None,
        model=model or None,
        cwd=cwd or None,
        wait_seconds=wait_seconds,
        request_id=request_id or None,
    )
    return _rt.checked(_w)


def get_agent_turn_request(
    *,
    sandbox_id: str,
    turn_id: str,
    wait_seconds: int | None,
) -> _pb.GetAgentTurnRequest:
    _w = _pb.GetAgentTurnRequest(
        sandbox_id=sandbox_id or None,
        turn_id=turn_id or None,
        wait_seconds=wait_seconds,
    )
    return _rt.checked(_w)


def stop_agent_turn_request(
    *,
    sandbox_id: str,
    turn_id: str,
) -> _pb.StopAgentTurnRequest:
    _w = _pb.StopAgentTurnRequest(
        sandbox_id=sandbox_id or None,
        turn_id=turn_id or None,
    )
    return _rt.checked(_w)


def list_conversations_request(
    *,
    sandbox_id: str,
    page_size: int,
    page_token: str,
) -> _pb.ListConversationsRequest:
    _w = _pb.ListConversationsRequest(
        sandbox_id=sandbox_id or None,
        page_size=page_size or None,
        page_token=page_token or None,
    )
    return _rt.checked(_w)


def watch_conversation_request(
    *,
    sandbox_id: str,
    conversation_id: str,
    after_seq: int,
) -> _pb.WatchConversationRequest:
    _w = _pb.WatchConversationRequest(
        sandbox_id=sandbox_id or None,
        conversation_id=conversation_id or None,
        after_seq=after_seq or None,
    )
    return _rt.checked(_w)


def connect_request(_key: str) -> _pb.ConnectSandboxRequest:
    """The request for a key's connection: its other fields absent."""
    return _pb.ConnectSandboxRequest(sandbox_id=_key)


def kept(_w: _pb.Connection) -> _connections.Kept:
    """A connection as the client keeps it. One whose expiry is not said is good for its own call alone."""
    _expire = _rt.time_from_wire(_w.expire_time) if _w.expire_time is not None else None
    return _connections.Kept(url=_w.url, token=_w.token, expire=_expire)


def sandbox_seeds(_w: _pb.Sandbox) -> Iterator[tuple[str, _connections.Kept]]:
    if _w.connection is not None:
        yield _w.sandbox_id, kept(_w.connection)


def list_sandboxes_response_seeds(_w: _pb.ListSandboxesResponse) -> Iterator[tuple[str, _connections.Kept]]:
    for _s0 in _w.sandboxes:
        if _s0.connection is not None:
            yield _s0.sandbox_id, kept(_s0.connection)


_ERRORS: dict[_Code, type[_errors.SandboxesError]] = {
    _Code.CANCELED: _errors.CanceledError,
    _Code.UNKNOWN: _errors.UnknownError,
    _Code.INVALID_ARGUMENT: _errors.InvalidArgumentError,
    _Code.DEADLINE_EXCEEDED: _errors.DeadlineExceededError,
    _Code.NOT_FOUND: _errors.NotFoundError,
    _Code.ALREADY_EXISTS: _errors.AlreadyExistsError,
    _Code.PERMISSION_DENIED: _errors.PermissionDeniedError,
    _Code.RESOURCE_EXHAUSTED: _errors.ResourceExhaustedError,
    _Code.FAILED_PRECONDITION: _errors.FailedPreconditionError,
    _Code.ABORTED: _errors.AbortedError,
    _Code.OUT_OF_RANGE: _errors.OutOfRangeError,
    _Code.UNIMPLEMENTED: _errors.UnimplementedError,
    _Code.INTERNAL: _errors.InternalError,
    _Code.UNAVAILABLE: _errors.UnavailableError,
    _Code.DATA_LOSS: _errors.DataLossError,
    _Code.UNAUTHENTICATED: _errors.UnauthenticatedError,
}


def _detail(_e: _ConnectError) -> _errors.ErrorDetail | None:
    """The first detail this version knows. One it does not know is passed over, and so is one
    whose bytes are not its message."""
    for _d in _e.details:
        try:
            if _d.type_name == "pethost.sandboxes.v1.LimitReached":
                _wLimitReached = _d.value(_pb.LimitReached)
                if _wLimitReached is not None:
                    return limit_reached_from_wire(_wLimitReached)
            if _d.type_name == "pethost.sandboxes.v1.Stopped":
                _wStopped = _d.value(_pb.Stopped)
                if _wStopped is not None:
                    return stopped_from_wire(_wStopped)
            if _d.type_name == "pethost.sandboxes.v1.UsageUnpaid":
                _wUsageUnpaid = _d.value(_pb.UsageUnpaid)
                if _wUsageUnpaid is not None:
                    return usage_unpaid_from_wire(_wUsageUnpaid)
            if _d.type_name == "pethost.sandboxes.v1.Restoring":
                _wRestoring = _d.value(_pb.Restoring)
                if _wRestoring is not None:
                    return restoring_from_wire(_wRestoring)
            if _d.type_name == "pethost.sandboxes.v1.NoCapacity":
                _wNoCapacity = _d.value(_pb.NoCapacity)
                if _wNoCapacity is not None:
                    return no_capacity_from_wire(_wNoCapacity)
            if _d.type_name == "pethost.sandboxes.v1.NameTaken":
                _wNameTaken = _d.value(_pb.NameTaken)
                if _wNameTaken is not None:
                    return name_taken_from_wire(_wNameTaken)
            if _d.type_name == "pethost.sandboxes.v1.WorkspaceChoice":
                _wWorkspaceChoice = _d.value(_pb.WorkspaceChoice)
                if _wWorkspaceChoice is not None:
                    return workspace_choice_from_wire(_wWorkspaceChoice)
            if _d.type_name == "pethost.sandboxes.v1.AgentSignIn":
                _wAgentSignIn = _d.value(_pb.AgentSignIn)
                if _wAgentSignIn is not None:
                    return agent_sign_in_from_wire(_wAgentSignIn)
        except ValueError:
            continue
    return None


def error_from_wire(_e: _ConnectError) -> _errors.SandboxesError:
    return _ERRORS.get(_e.code, _errors.UnknownError)(_e.message, _detail(_e))
