"""Between the public types and the wire layer: the type checker holds every line here against
both. Generated from v1/panel.proto: do not edit."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
from typing import Any as _Any
from typing import Literal as _Literal

from connectrpc.code import Code as _Code
from connectrpc.errors import ConnectError as _ConnectError
from protobuf import Oneof as _Oneof

import pethost._errors as _errors
import pethost._runtime as _rt
import pethost._types as _t
import pethost._wire.v1.panel_pb as _pb


def machine_session_kind_from_wire(_w: _pb.MachineSessionKind) -> _t.MachineSessionKind:
    return _t.MachineSessionKind(_w.value)


def machine_session_kind_to_wire(_v: _t.MachineSessionKind) -> _pb.MachineSessionKind:
    return _pb.MachineSessionKind(_v.value)


def project_problem_kind_from_wire(_w: _pb.ProjectProblemKind) -> _t.ProjectProblemKind:
    return _t.ProjectProblemKind(_w.value)


def project_problem_kind_to_wire(_v: _t.ProjectProblemKind) -> _pb.ProjectProblemKind:
    return _pb.ProjectProblemKind(_v.value)


def services_action_kind_from_wire(_w: _pb.ServicesActionKind) -> _t.ServicesActionKind:
    return _t.ServicesActionKind(_w.value)


def services_action_kind_to_wire(_v: _t.ServicesActionKind) -> _pb.ServicesActionKind:
    return _pb.ServicesActionKind(_v.value)


def service_state_from_wire(_w: _pb.ServiceState) -> _t.ServiceState:
    return _t.ServiceState(_w.value)


def service_state_to_wire(_v: _t.ServiceState) -> _pb.ServiceState:
    return _pb.ServiceState(_v.value)


def restart_policy_from_wire(_w: _pb.RestartPolicy) -> _t.RestartPolicy:
    return _t.RestartPolicy(_w.value)


def restart_policy_to_wire(_v: _t.RestartPolicy) -> _pb.RestartPolicy:
    return _pb.RestartPolicy(_v.value)


def health_status_from_wire(_w: _pb.HealthStatus) -> _t.HealthStatus:
    return _t.HealthStatus(_w.value)


def health_status_to_wire(_v: _t.HealthStatus) -> _pb.HealthStatus:
    return _pb.HealthStatus(_v.value)


def certificate_source_from_wire(_w: _pb.CertificateSource) -> _t.CertificateSource:
    return _t.CertificateSource(_w.value)


def certificate_source_to_wire(_v: _t.CertificateSource) -> _pb.CertificateSource:
    return _pb.CertificateSource(_v.value)


def operation_kind_from_wire(_w: _pb.OperationKind) -> _t.OperationKind:
    return _t.OperationKind(_w.value)


def operation_kind_to_wire(_v: _t.OperationKind) -> _pb.OperationKind:
    return _pb.OperationKind(_v.value)


def operation_status_from_wire(_w: _pb.OperationStatus) -> _t.OperationStatus:
    return _t.OperationStatus(_w.value)


def operation_status_to_wire(_v: _t.OperationStatus) -> _pb.OperationStatus:
    return _pb.OperationStatus(_v.value)


def deploy_failure_reason_from_wire(_w: _pb.DeployFailureReason) -> _t.DeployFailureReason:
    return _t.DeployFailureReason(_w.value)


def deploy_failure_reason_to_wire(_v: _t.DeployFailureReason) -> _pb.DeployFailureReason:
    return _pb.DeployFailureReason(_v.value)


def output_stream_from_wire(_w: _pb.OutputStream) -> _t.OutputStream:
    return _t.OutputStream(_w.value)


def output_stream_to_wire(_v: _t.OutputStream) -> _pb.OutputStream:
    return _pb.OutputStream(_v.value)


def file_type_from_wire(_w: _pb.FileType) -> _t.FileType:
    return _t.FileType(_w.value)


def file_type_to_wire(_v: _t.FileType) -> _pb.FileType:
    return _pb.FileType(_v.value)


def file_location_from_wire(_w: _pb.FileLocation) -> _t.FileLocation:
    return _t.FileLocation(_w.value)


def file_location_to_wire(_v: _t.FileLocation) -> _pb.FileLocation:
    return _pb.FileLocation(_v.value)


def no_machine_reason_from_wire(_w: _pb.NoMachineReason) -> _t.NoMachineReason:
    return _t.NoMachineReason(_w.value)


def no_machine_reason_to_wire(_v: _t.NoMachineReason) -> _pb.NoMachineReason:
    return _pb.NoMachineReason(_v.value)


def get_machine_response_from_wire(_w: _pb.GetMachineResponse) -> _t.GetMachineResponse:
    return _t.GetMachineResponse(
        machine=machine_from_wire(_w.machine) if _w.machine is not None else None,
        projects=tuple(project_summary_from_wire(_x) for _x in _w.projects),
        deleted_projects=tuple(deleted_project_from_wire(_x) for _x in _w.deleted_projects),
        github=github_connection_from_wire(_w.github) if _w.github is not None else None,
    )


def get_machine_response_to_wire(_v: _t.GetMachineResponse) -> _pb.GetMachineResponse:
    return _pb.GetMachineResponse(
        machine=machine_to_wire(_v.machine) if _v.machine is not None else None,
        projects=[project_summary_to_wire(_x) for _x in _v.projects],
        deleted_projects=[deleted_project_to_wire(_x) for _x in _v.deleted_projects],
        github=github_connection_to_wire(_v.github) if _v.github is not None else None,
    )


def get_machine_response_to_dict(_v: _t.GetMachineResponse) -> dict[str, _Any]:
    return _rt.to_dict(get_machine_response_to_wire(_v))


def get_machine_response_from_dict(_j: dict[str, _Any]) -> _t.GetMachineResponse:
    return get_machine_response_from_wire(_rt.from_dict(_pb.GetMachineResponse, _j))


def machine_from_wire(_w: _pb.Machine) -> _t.Machine:
    return _t.Machine(
        name=_w.name,
        location=_w.location,
        sample_time=_rt.time_from_wire(_w.sample_time) if _w.sample_time is not None else None,
        cpu_used_cores=_w.cpu_used_cores,
        cpu_total_cores=_w.cpu_total_cores,
        memory_used_bytes=_w.memory_used_bytes,
        memory_total_bytes=_w.memory_total_bytes,
        disk_used_bytes=_w.disk_used_bytes,
        disk_total_bytes=_w.disk_total_bytes,
        disk_usage=disk_usage_from_wire(_w.disk_usage) if _w.disk_usage is not None else None,
        hostname=_w.hostname,
        ssh_host_key_fingerprint=_w.ssh_host_key_fingerprint,
        ssh_keys=tuple(ssh_key_from_wire(_x) for _x in _w.ssh_keys),
        backups_enabled=_w.backups_enabled,
        snapshot_list_time=_rt.time_from_wire(_w.snapshot_list_time) if _w.snapshot_list_time is not None else None,
        snapshot_list_failure_message=_w.snapshot_list_failure_message,
        backup_retention_hours=_w.backup_retention_hours,
        acme_enabled=_w.acme_enabled,
        apps_domain=_w.apps_domain,
        daemon_version=_w.daemon_version,
        docker_version=_w.docker_version,
        boot_time=_rt.time_from_wire(_w.boot_time) if _w.boot_time is not None else None,
        restart_required_time=_rt.time_from_wire(_w.restart_required_time) if _w.restart_required_time is not None else None,
        scheduled_restart_time=_rt.time_from_wire(_w.scheduled_restart_time) if _w.scheduled_restart_time is not None else None,
        sessions=tuple(machine_session_from_wire(_x) for _x in _w.sessions),
    )


def machine_to_wire(_v: _t.Machine) -> _pb.Machine:
    return _pb.Machine(
        name=_v.name or None,
        location=_v.location or None,
        sample_time=_rt.time_to_wire(_v.sample_time) if _v.sample_time is not None else None,
        cpu_used_cores=_v.cpu_used_cores or None,
        cpu_total_cores=_v.cpu_total_cores or None,
        memory_used_bytes=_v.memory_used_bytes or None,
        memory_total_bytes=_v.memory_total_bytes or None,
        disk_used_bytes=_v.disk_used_bytes or None,
        disk_total_bytes=_v.disk_total_bytes or None,
        disk_usage=disk_usage_to_wire(_v.disk_usage) if _v.disk_usage is not None else None,
        hostname=_v.hostname or None,
        ssh_host_key_fingerprint=_v.ssh_host_key_fingerprint or None,
        ssh_keys=[ssh_key_to_wire(_x) for _x in _v.ssh_keys],
        backups_enabled=_v.backups_enabled or None,
        snapshot_list_time=_rt.time_to_wire(_v.snapshot_list_time) if _v.snapshot_list_time is not None else None,
        snapshot_list_failure_message=_v.snapshot_list_failure_message or None,
        backup_retention_hours=_v.backup_retention_hours or None,
        acme_enabled=_v.acme_enabled or None,
        apps_domain=_v.apps_domain or None,
        daemon_version=_v.daemon_version or None,
        docker_version=_v.docker_version or None,
        boot_time=_rt.time_to_wire(_v.boot_time) if _v.boot_time is not None else None,
        restart_required_time=_rt.time_to_wire(_v.restart_required_time) if _v.restart_required_time is not None else None,
        scheduled_restart_time=_rt.time_to_wire(_v.scheduled_restart_time) if _v.scheduled_restart_time is not None else None,
        sessions=[machine_session_to_wire(_x) for _x in _v.sessions],
    )


def machine_to_dict(_v: _t.Machine) -> dict[str, _Any]:
    return _rt.to_dict(machine_to_wire(_v))


def machine_from_dict(_j: dict[str, _Any]) -> _t.Machine:
    return machine_from_wire(_rt.from_dict(_pb.Machine, _j))


def machine_session_from_wire(_w: _pb.MachineSession) -> _t.MachineSession:
    return _t.MachineSession(
        session_id=_w.session_id,
        kind=machine_session_kind_from_wire(_w.kind),
        project_id=_w.project_id,
        service=_w.service,
        port=_w.port,
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        client_address=_w.client_address,
        ssh_key_label=_w.ssh_key_label,
        ssh_key_fingerprint=_w.ssh_key_fingerprint,
    )


def machine_session_to_wire(_v: _t.MachineSession) -> _pb.MachineSession:
    return _pb.MachineSession(
        session_id=_v.session_id or None,
        kind=machine_session_kind_to_wire(_v.kind) if _v.kind.value else None,
        project_id=_v.project_id or None,
        service=_v.service or None,
        port=_v.port or None,
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        client_address=_v.client_address or None,
        ssh_key_label=_v.ssh_key_label or None,
        ssh_key_fingerprint=_v.ssh_key_fingerprint or None,
    )


def machine_session_to_dict(_v: _t.MachineSession) -> dict[str, _Any]:
    return _rt.to_dict(machine_session_to_wire(_v))


def machine_session_from_dict(_j: dict[str, _Any]) -> _t.MachineSession:
    return machine_session_from_wire(_rt.from_dict(_pb.MachineSession, _j))


def disk_usage_from_wire(_w: _pb.DiskUsage) -> _t.DiskUsage:
    return _t.DiskUsage(
        images_bytes=_w.images_bytes,
        build_cache_bytes=_w.build_cache_bytes if _w.has_field("build_cache_bytes") else None,
        volumes_bytes=_w.volumes_bytes,
        container_layers_bytes=_w.container_layers_bytes,
        project_files_bytes=_w.project_files_bytes,
        container_logs_bytes=_w.container_logs_bytes,
        http_traffic_bytes=_w.http_traffic_bytes,
    )


def disk_usage_to_wire(_v: _t.DiskUsage) -> _pb.DiskUsage:
    return _pb.DiskUsage(
        images_bytes=_v.images_bytes or None,
        build_cache_bytes=_v.build_cache_bytes,
        volumes_bytes=_v.volumes_bytes or None,
        container_layers_bytes=_v.container_layers_bytes or None,
        project_files_bytes=_v.project_files_bytes or None,
        container_logs_bytes=_v.container_logs_bytes or None,
        http_traffic_bytes=_v.http_traffic_bytes or None,
    )


def disk_usage_to_dict(_v: _t.DiskUsage) -> dict[str, _Any]:
    return _rt.to_dict(disk_usage_to_wire(_v))


def disk_usage_from_dict(_j: dict[str, _Any]) -> _t.DiskUsage:
    return disk_usage_from_wire(_rt.from_dict(_pb.DiskUsage, _j))


def ssh_key_from_wire(_w: _pb.SshKey) -> _t.SshKey:
    return _t.SshKey(
        public_key=_w.public_key,
        label=_w.label,
        fingerprint=_w.fingerprint,
    )


def ssh_key_to_wire(_v: _t.SshKey) -> _pb.SshKey:
    return _pb.SshKey(
        public_key=_v.public_key or None,
        label=_v.label or None,
        fingerprint=_v.fingerprint or None,
    )


def ssh_key_to_dict(_v: _t.SshKey) -> dict[str, _Any]:
    return _rt.to_dict(ssh_key_to_wire(_v))


def ssh_key_from_dict(_j: dict[str, _Any]) -> _t.SshKey:
    return ssh_key_from_wire(_rt.from_dict(_pb.SshKey, _j))


def github_connection_from_wire(_w: _pb.GithubConnection) -> _t.GithubConnection:
    return _t.GithubConnection(
        app_name=_w.app_name,
        install_url=_w.install_url,
        repositories=tuple(github_repository_from_wire(_x) for _x in _w.repositories),
        repository_count=_w.repository_count,
        webhooks_enabled=_w.webhooks_enabled,
    )


def github_connection_to_wire(_v: _t.GithubConnection) -> _pb.GithubConnection:
    return _pb.GithubConnection(
        app_name=_v.app_name or None,
        install_url=_v.install_url or None,
        repositories=[github_repository_to_wire(_x) for _x in _v.repositories],
        repository_count=_v.repository_count or None,
        webhooks_enabled=_v.webhooks_enabled or None,
    )


def github_connection_to_dict(_v: _t.GithubConnection) -> dict[str, _Any]:
    return _rt.to_dict(github_connection_to_wire(_v))


def github_connection_from_dict(_j: dict[str, _Any]) -> _t.GithubConnection:
    return github_connection_from_wire(_rt.from_dict(_pb.GithubConnection, _j))


def github_repository_from_wire(_w: _pb.GithubRepository) -> _t.GithubRepository:
    return _t.GithubRepository(
        repository=_w.repository,
        default_branch=_w.default_branch,
        private=_w.private,
        push_time=_rt.time_from_wire(_w.push_time) if _w.push_time is not None else None,
    )


def github_repository_to_wire(_v: _t.GithubRepository) -> _pb.GithubRepository:
    return _pb.GithubRepository(
        repository=_v.repository or None,
        default_branch=_v.default_branch or None,
        private=_v.private or None,
        push_time=_rt.time_to_wire(_v.push_time) if _v.push_time is not None else None,
    )


def github_repository_to_dict(_v: _t.GithubRepository) -> dict[str, _Any]:
    return _rt.to_dict(github_repository_to_wire(_v))


def github_repository_from_dict(_j: dict[str, _Any]) -> _t.GithubRepository:
    return github_repository_from_wire(_rt.from_dict(_pb.GithubRepository, _j))


def deleted_project_from_wire(_w: _pb.DeletedProject) -> _t.DeletedProject:
    return _t.DeletedProject(
        project_id=_w.project_id,
        newest_snapshot=snapshot_from_wire(_w.newest_snapshot) if _w.newest_snapshot is not None else None,
        snapshot_count=_w.snapshot_count,
    )


def deleted_project_to_wire(_v: _t.DeletedProject) -> _pb.DeletedProject:
    return _pb.DeletedProject(
        project_id=_v.project_id or None,
        newest_snapshot=snapshot_to_wire(_v.newest_snapshot) if _v.newest_snapshot is not None else None,
        snapshot_count=_v.snapshot_count or None,
    )


def deleted_project_to_dict(_v: _t.DeletedProject) -> dict[str, _Any]:
    return _rt.to_dict(deleted_project_to_wire(_v))


def deleted_project_from_dict(_j: dict[str, _Any]) -> _t.DeletedProject:
    return deleted_project_from_wire(_rt.from_dict(_pb.DeletedProject, _j))


def restart_machine_action_from_wire(_w: _pb.RestartMachineAction) -> _t.RestartMachineAction:
    return _t.RestartMachineAction(
        restart_time=_rt.time_from_wire(_w.restart_time) if _w.restart_time is not None else None,
        at_maintenance_window=_w.at_maintenance_window,
        interrupt_operations=_w.interrupt_operations,
    )


def restart_machine_action_to_wire(_v: _t.RestartMachineAction) -> _pb.RestartMachineAction:
    return _pb.RestartMachineAction(
        restart_time=_rt.time_to_wire(_v.restart_time) if _v.restart_time is not None else None,
        at_maintenance_window=_v.at_maintenance_window or None,
        interrupt_operations=_v.interrupt_operations or None,
    )


def restart_machine_action_to_dict(_v: _t.RestartMachineAction) -> dict[str, _Any]:
    return _rt.to_dict(restart_machine_action_to_wire(_v))


def restart_machine_action_from_dict(_j: dict[str, _Any]) -> _t.RestartMachineAction:
    return restart_machine_action_from_wire(_rt.from_dict(_pb.RestartMachineAction, _j))


def run_machine_action_response_from_wire(_w: _pb.RunMachineActionResponse) -> _t.RunMachineActionResponse:
    return _t.RunMachineActionResponse(
        machine=machine_from_wire(_w.machine) if _w.machine is not None else None,
    )


def run_machine_action_response_to_wire(_v: _t.RunMachineActionResponse) -> _pb.RunMachineActionResponse:
    return _pb.RunMachineActionResponse(
        machine=machine_to_wire(_v.machine) if _v.machine is not None else None,
    )


def run_machine_action_response_to_dict(_v: _t.RunMachineActionResponse) -> dict[str, _Any]:
    return _rt.to_dict(run_machine_action_response_to_wire(_v))


def run_machine_action_response_from_dict(_j: dict[str, _Any]) -> _t.RunMachineActionResponse:
    return run_machine_action_response_from_wire(_rt.from_dict(_pb.RunMachineActionResponse, _j))


def project_metadata_from_wire(_w: _pb.ProjectMetadata) -> _t.ProjectMetadata:
    return _t.ProjectMetadata(
        name=_w.name if _w.has_field("name") else None,
        emoji=_w.emoji if _w.has_field("emoji") else None,
        description=_w.description if _w.has_field("description") else None,
        notes=_w.notes if _w.has_field("notes") else None,
    )


def project_metadata_to_wire(_v: _t.ProjectMetadata) -> _pb.ProjectMetadata:
    return _pb.ProjectMetadata(
        name=_v.name,
        emoji=_v.emoji,
        description=_v.description,
        notes=_v.notes,
    )


def project_metadata_to_dict(_v: _t.ProjectMetadata) -> dict[str, _Any]:
    return _rt.to_dict(project_metadata_to_wire(_v))


def project_metadata_from_dict(_j: dict[str, _Any]) -> _t.ProjectMetadata:
    return project_metadata_from_wire(_rt.from_dict(_pb.ProjectMetadata, _j))


def project_summary_from_wire(_w: _pb.ProjectSummary) -> _t.ProjectSummary:
    return _t.ProjectSummary(
        project_id=_w.project_id,
        metadata=project_metadata_from_wire(_w.metadata) if _w.metadata is not None else None,
        problems=tuple(project_problem_from_wire(_x) for _x in _w.problems),
        services=tuple(service_summary_from_wire(_x) for _x in _w.services),
        url=_w.url,
        hosts=tuple(_w.hosts),
        http_traffic_last_day=http_traffic_summary_from_wire(_w.http_traffic_last_day) if _w.http_traffic_last_day is not None else None,
        cpu_used_cores=_w.cpu_used_cores,
        memory_used_bytes=_w.memory_used_bytes,
        deploy_time=_rt.time_from_wire(_w.deploy_time) if _w.deploy_time is not None else None,
        running_operations=tuple(operation_from_wire(_x) for _x in _w.running_operations),
        pinned=_w.pinned,
        disk_used_bytes=_w.disk_used_bytes,
    )


def project_summary_to_wire(_v: _t.ProjectSummary) -> _pb.ProjectSummary:
    return _pb.ProjectSummary(
        project_id=_v.project_id or None,
        metadata=project_metadata_to_wire(_v.metadata) if _v.metadata is not None else None,
        problems=[project_problem_to_wire(_x) for _x in _v.problems],
        services=[service_summary_to_wire(_x) for _x in _v.services],
        url=_v.url or None,
        hosts=_rt.strings("ProjectSummary.hosts", _v.hosts),
        http_traffic_last_day=http_traffic_summary_to_wire(_v.http_traffic_last_day) if _v.http_traffic_last_day is not None else None,
        cpu_used_cores=_v.cpu_used_cores or None,
        memory_used_bytes=_v.memory_used_bytes or None,
        deploy_time=_rt.time_to_wire(_v.deploy_time) if _v.deploy_time is not None else None,
        running_operations=[operation_to_wire(_x) for _x in _v.running_operations],
        pinned=_v.pinned or None,
        disk_used_bytes=_v.disk_used_bytes or None,
    )


def project_summary_to_dict(_v: _t.ProjectSummary) -> dict[str, _Any]:
    return _rt.to_dict(project_summary_to_wire(_v))


def project_summary_from_dict(_j: dict[str, _Any]) -> _t.ProjectSummary:
    return project_summary_from_wire(_rt.from_dict(_pb.ProjectSummary, _j))


def service_summary_from_wire(_w: _pb.ServiceSummary) -> _t.ServiceSummary:
    return _t.ServiceSummary(
        service=_w.service,
        state=service_state_from_wire(_w.state),
    )


def service_summary_to_wire(_v: _t.ServiceSummary) -> _pb.ServiceSummary:
    return _pb.ServiceSummary(
        service=_v.service or None,
        state=service_state_to_wire(_v.state) if _v.state.value else None,
    )


def service_summary_to_dict(_v: _t.ServiceSummary) -> dict[str, _Any]:
    return _rt.to_dict(service_summary_to_wire(_v))


def service_summary_from_dict(_j: dict[str, _Any]) -> _t.ServiceSummary:
    return service_summary_from_wire(_rt.from_dict(_pb.ServiceSummary, _j))


def project_problem_from_wire(_w: _pb.ProjectProblem) -> _t.ProjectProblem:
    return _t.ProjectProblem(
        kind=project_problem_kind_from_wire(_w.kind),
        service=_w.service,
        operation_id=_w.operation_id,
        since_time=_rt.time_from_wire(_w.since_time) if _w.since_time is not None else None,
        problem_message=_w.problem_message,
    )


def project_problem_to_wire(_v: _t.ProjectProblem) -> _pb.ProjectProblem:
    return _pb.ProjectProblem(
        kind=project_problem_kind_to_wire(_v.kind) if _v.kind.value else None,
        service=_v.service or None,
        operation_id=_v.operation_id or None,
        since_time=_rt.time_to_wire(_v.since_time) if _v.since_time is not None else None,
        problem_message=_v.problem_message or None,
    )


def project_problem_to_dict(_v: _t.ProjectProblem) -> dict[str, _Any]:
    return _rt.to_dict(project_problem_to_wire(_v))


def project_problem_from_dict(_j: dict[str, _Any]) -> _t.ProjectProblem:
    return project_problem_from_wire(_rt.from_dict(_pb.ProjectProblem, _j))


def get_project_response_from_wire(_w: _pb.GetProjectResponse) -> _t.GetProjectResponse:
    return _t.GetProjectResponse(
        project=project_from_wire(_w.project) if _w.project is not None else None,
    )


def get_project_response_to_wire(_v: _t.GetProjectResponse) -> _pb.GetProjectResponse:
    return _pb.GetProjectResponse(
        project=project_to_wire(_v.project) if _v.project is not None else None,
    )


def get_project_response_to_dict(_v: _t.GetProjectResponse) -> dict[str, _Any]:
    return _rt.to_dict(get_project_response_to_wire(_v))


def get_project_response_from_dict(_j: dict[str, _Any]) -> _t.GetProjectResponse:
    return get_project_response_from_wire(_rt.from_dict(_pb.GetProjectResponse, _j))


def project_from_wire(_w: _pb.Project) -> _t.Project:
    return _t.Project(
        project_id=_w.project_id,
        metadata=project_metadata_from_wire(_w.metadata) if _w.metadata is not None else None,
        problems=tuple(project_problem_from_wire(_x) for _x in _w.problems),
        url=_w.url,
        cpu_used_cores=_w.cpu_used_cores,
        memory_used_bytes=_w.memory_used_bytes,
        deploy_id=_w.deploy_id,
        deploy_status=operation_status_from_wire(_w.deploy_status),
        deploy_time=_rt.time_from_wire(_w.deploy_time) if _w.deploy_time is not None else None,
        x_pethost_applies_at_once=_w.x_pethost_applies_at_once,
        services=tuple(service_from_wire(_x) for _x in _w.services),
        volumes=tuple(volume_from_wire(_x) for _x in _w.volumes),
        routes=tuple(route_from_wire(_x) for _x in _w.routes),
        hosts=tuple(host_from_wire(_x) for _x in _w.hosts),
        password_protected=_w.password_protected,
        operations=tuple(operation_from_wire(_x) for _x in _w.operations),
        snapshots=tuple(snapshot_from_wire(_x) for _x in _w.snapshots),
        snapshot_count=_w.snapshot_count,
        snapshot_list_time=_rt.time_from_wire(_w.snapshot_list_time) if _w.snapshot_list_time is not None else None,
        http_traffic_last_day=http_traffic_summary_from_wire(_w.http_traffic_last_day) if _w.http_traffic_last_day is not None else None,
        source=project_source_from_wire(_w.source) if _w.source is not None else None,
        running_services_action=running_services_action_from_wire(_w.running_services_action) if _w.running_services_action is not None else None,
    )


def project_to_wire(_v: _t.Project) -> _pb.Project:
    return _pb.Project(
        project_id=_v.project_id or None,
        metadata=project_metadata_to_wire(_v.metadata) if _v.metadata is not None else None,
        problems=[project_problem_to_wire(_x) for _x in _v.problems],
        url=_v.url or None,
        cpu_used_cores=_v.cpu_used_cores or None,
        memory_used_bytes=_v.memory_used_bytes or None,
        deploy_id=_v.deploy_id or None,
        deploy_status=operation_status_to_wire(_v.deploy_status) if _v.deploy_status.value else None,
        deploy_time=_rt.time_to_wire(_v.deploy_time) if _v.deploy_time is not None else None,
        x_pethost_applies_at_once=_v.x_pethost_applies_at_once or None,
        services=[service_to_wire(_x) for _x in _v.services],
        volumes=[volume_to_wire(_x) for _x in _v.volumes],
        routes=[route_to_wire(_x) for _x in _v.routes],
        hosts=[host_to_wire(_x) for _x in _v.hosts],
        password_protected=_v.password_protected or None,
        operations=[operation_to_wire(_x) for _x in _v.operations],
        snapshots=[snapshot_to_wire(_x) for _x in _v.snapshots],
        snapshot_count=_v.snapshot_count or None,
        snapshot_list_time=_rt.time_to_wire(_v.snapshot_list_time) if _v.snapshot_list_time is not None else None,
        http_traffic_last_day=http_traffic_summary_to_wire(_v.http_traffic_last_day) if _v.http_traffic_last_day is not None else None,
        source=project_source_to_wire(_v.source) if _v.source is not None else None,
        running_services_action=running_services_action_to_wire(_v.running_services_action) if _v.running_services_action is not None else None,
    )


def project_to_dict(_v: _t.Project) -> dict[str, _Any]:
    return _rt.to_dict(project_to_wire(_v))


def project_from_dict(_j: dict[str, _Any]) -> _t.Project:
    return project_from_wire(_rt.from_dict(_pb.Project, _j))


def running_services_action_from_wire(_w: _pb.RunningServicesAction) -> _t.RunningServicesAction:
    return _t.RunningServicesAction(
        kind=services_action_kind_from_wire(_w.kind),
        services=tuple(_w.services),
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
    )


def running_services_action_to_wire(_v: _t.RunningServicesAction) -> _pb.RunningServicesAction:
    return _pb.RunningServicesAction(
        kind=services_action_kind_to_wire(_v.kind) if _v.kind.value else None,
        services=_rt.strings("RunningServicesAction.services", _v.services),
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
    )


def running_services_action_to_dict(_v: _t.RunningServicesAction) -> dict[str, _Any]:
    return _rt.to_dict(running_services_action_to_wire(_v))


def running_services_action_from_dict(_j: dict[str, _Any]) -> _t.RunningServicesAction:
    return running_services_action_from_wire(_rt.from_dict(_pb.RunningServicesAction, _j))


def project_source_from_wire(_w: _pb.ProjectSource) -> _t.ProjectSource:
    _k = _w.kind
    if _k is None:
        return _t.ProjectSource()
    if _k.field == "files":
        return _t.ProjectSource(
            files=_k.value,
        )
    if _k.field == "github":
        return _t.ProjectSource(
            github=github_source_from_wire(_k.value),
        )
    _rt.never(_k)


def project_source_to_wire(_v: _t.ProjectSource) -> _pb.ProjectSource:
    _w = _pb.ProjectSource()
    if _v.files is not None:
        _w.kind = _Oneof[_Literal["files"], bool]("files", _v.files)
    elif _v.github is not None:
        _w.kind = _Oneof[_Literal["github"], _pb.GithubSource]("github", github_source_to_wire(_v.github))
    return _w


def project_source_to_dict(_v: _t.ProjectSource) -> dict[str, _Any]:
    return _rt.to_dict(project_source_to_wire(_v))


def project_source_from_dict(_j: dict[str, _Any]) -> _t.ProjectSource:
    return project_source_from_wire(_rt.from_dict(_pb.ProjectSource, _j))


def github_source_from_wire(_w: _pb.GithubSource) -> _t.GithubSource:
    return _t.GithubSource(
        repository=_w.repository if _w.has_field("repository") else None,
        branch=_w.branch if _w.has_field("branch") else None,
        directory=_w.directory if _w.has_field("directory") else None,
        auto_deploy=_w.auto_deploy if _w.has_field("auto_deploy") else None,
        newest_commit=github_commit_from_wire(_w.newest_commit) if _w.newest_commit is not None else None,
        deployed_commit=github_commit_from_wire(_w.deployed_commit) if _w.deployed_commit is not None else None,
        pinned=_w.pinned,
        auto_deploy_pending=_w.auto_deploy_pending,
    )


def github_source_to_wire(_v: _t.GithubSource) -> _pb.GithubSource:
    return _pb.GithubSource(
        repository=_v.repository,
        branch=_v.branch,
        directory=_v.directory,
        auto_deploy=_v.auto_deploy,
        newest_commit=github_commit_to_wire(_v.newest_commit) if _v.newest_commit is not None else None,
        deployed_commit=github_commit_to_wire(_v.deployed_commit) if _v.deployed_commit is not None else None,
        pinned=_v.pinned or None,
        auto_deploy_pending=_v.auto_deploy_pending or None,
    )


def github_source_to_dict(_v: _t.GithubSource) -> dict[str, _Any]:
    return _rt.to_dict(github_source_to_wire(_v))


def github_source_from_dict(_j: dict[str, _Any]) -> _t.GithubSource:
    return github_source_from_wire(_rt.from_dict(_pb.GithubSource, _j))


def github_commit_from_wire(_w: _pb.GithubCommit) -> _t.GithubCommit:
    return _t.GithubCommit(
        sha=_w.sha,
        title=_w.title,
        url=_w.url,
    )


def github_commit_to_wire(_v: _t.GithubCommit) -> _pb.GithubCommit:
    return _pb.GithubCommit(
        sha=_v.sha or None,
        title=_v.title or None,
        url=_v.url or None,
    )


def github_commit_to_dict(_v: _t.GithubCommit) -> dict[str, _Any]:
    return _rt.to_dict(github_commit_to_wire(_v))


def github_commit_from_dict(_j: dict[str, _Any]) -> _t.GithubCommit:
    return github_commit_from_wire(_rt.from_dict(_pb.GithubCommit, _j))


def service_from_wire(_w: _pb.Service) -> _t.Service:
    return _t.Service(
        service=_w.service,
        state=service_state_from_wire(_w.state),
        container_running=_w.container_running,
        image=_w.image,
        builds_image=_w.builds_image,
        image_digest=_w.image_digest,
        image_size_bytes=_w.image_size_bytes,
        command=tuple(_w.command),
        run_as_user=_w.run_as_user,
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        finish_time=_rt.time_from_wire(_w.finish_time) if _w.finish_time is not None else None,
        exit_code=_w.exit_code if _w.has_field("exit_code") else None,
        out_of_memory=_w.out_of_memory,
        restart_count=_w.restart_count,
        cpu_used_cores=_w.cpu_used_cores,
        memory_used_bytes=_w.memory_used_bytes,
        memory_limit_bytes=_w.memory_limit_bytes,
        cpu_limit_cores=_w.cpu_limit_cores,
        writable_layer_bytes=_w.writable_layer_bytes,
        ports=tuple(_w.ports),
        listening_ports=tuple(_w.listening_ports),
        published_ports=tuple(published_port_from_wire(_x) for _x in _w.published_ports),
        volume_mounts=tuple(volume_mount_from_wire(_x) for _x in _w.volume_mounts),
        restart_policy=restart_policy_from_wire(_w.restart_policy),
        health_check=health_check_from_wire(_w.health_check) if _w.health_check is not None else None,
        environment=tuple(environment_variable_from_wire(_x) for _x in _w.environment),
        env_files=tuple(_w.env_files),
        ssh_command=_w.ssh_command,
    )


def service_to_wire(_v: _t.Service) -> _pb.Service:
    return _pb.Service(
        service=_v.service or None,
        state=service_state_to_wire(_v.state) if _v.state.value else None,
        container_running=_v.container_running or None,
        image=_v.image or None,
        builds_image=_v.builds_image or None,
        image_digest=_v.image_digest or None,
        image_size_bytes=_v.image_size_bytes or None,
        command=_rt.strings("Service.command", _v.command),
        run_as_user=_v.run_as_user or None,
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        finish_time=_rt.time_to_wire(_v.finish_time) if _v.finish_time is not None else None,
        exit_code=_v.exit_code,
        out_of_memory=_v.out_of_memory or None,
        restart_count=_v.restart_count or None,
        cpu_used_cores=_v.cpu_used_cores or None,
        memory_used_bytes=_v.memory_used_bytes or None,
        memory_limit_bytes=_v.memory_limit_bytes or None,
        cpu_limit_cores=_v.cpu_limit_cores or None,
        writable_layer_bytes=_v.writable_layer_bytes or None,
        ports=[*_v.ports],
        listening_ports=[*_v.listening_ports],
        published_ports=[published_port_to_wire(_x) for _x in _v.published_ports],
        volume_mounts=[volume_mount_to_wire(_x) for _x in _v.volume_mounts],
        restart_policy=restart_policy_to_wire(_v.restart_policy) if _v.restart_policy.value else None,
        health_check=health_check_to_wire(_v.health_check) if _v.health_check is not None else None,
        environment=[environment_variable_to_wire(_x) for _x in _v.environment],
        env_files=_rt.strings("Service.env_files", _v.env_files),
        ssh_command=_v.ssh_command or None,
    )


def service_to_dict(_v: _t.Service) -> dict[str, _Any]:
    return _rt.to_dict(service_to_wire(_v))


def service_from_dict(_j: dict[str, _Any]) -> _t.Service:
    return service_from_wire(_rt.from_dict(_pb.Service, _j))


def published_port_from_wire(_w: _pb.PublishedPort) -> _t.PublishedPort:
    return _t.PublishedPort(
        machine_port=_w.machine_port,
        container_port=_w.container_port,
        protocol=_w.protocol,
        machine_only=_w.machine_only,
    )


def published_port_to_wire(_v: _t.PublishedPort) -> _pb.PublishedPort:
    return _pb.PublishedPort(
        machine_port=_v.machine_port or None,
        container_port=_v.container_port or None,
        protocol=_v.protocol or None,
        machine_only=_v.machine_only or None,
    )


def published_port_to_dict(_v: _t.PublishedPort) -> dict[str, _Any]:
    return _rt.to_dict(published_port_to_wire(_v))


def published_port_from_dict(_j: dict[str, _Any]) -> _t.PublishedPort:
    return published_port_from_wire(_rt.from_dict(_pb.PublishedPort, _j))


def volume_mount_from_wire(_w: _pb.VolumeMount) -> _t.VolumeMount:
    return _t.VolumeMount(
        volume=_w.volume,
        container_path=_w.container_path,
    )


def volume_mount_to_wire(_v: _t.VolumeMount) -> _pb.VolumeMount:
    return _pb.VolumeMount(
        volume=_v.volume or None,
        container_path=_v.container_path or None,
    )


def volume_mount_to_dict(_v: _t.VolumeMount) -> dict[str, _Any]:
    return _rt.to_dict(volume_mount_to_wire(_v))


def volume_mount_from_dict(_j: dict[str, _Any]) -> _t.VolumeMount:
    return volume_mount_from_wire(_rt.from_dict(_pb.VolumeMount, _j))


def health_check_from_wire(_w: _pb.HealthCheck) -> _t.HealthCheck:
    return _t.HealthCheck(
        command=tuple(_w.command),
        interval_seconds=_w.interval_seconds,
        status=health_status_from_wire(_w.status),
        consecutive_failure_count=_w.consecutive_failure_count,
        recent_results_passed=tuple(_w.recent_results_passed),
        last_failure_output=_w.last_failure_output,
    )


def health_check_to_wire(_v: _t.HealthCheck) -> _pb.HealthCheck:
    return _pb.HealthCheck(
        command=_rt.strings("HealthCheck.command", _v.command),
        interval_seconds=_v.interval_seconds or None,
        status=health_status_to_wire(_v.status) if _v.status.value else None,
        consecutive_failure_count=_v.consecutive_failure_count or None,
        recent_results_passed=[*_v.recent_results_passed],
        last_failure_output=_v.last_failure_output or None,
    )


def health_check_to_dict(_v: _t.HealthCheck) -> dict[str, _Any]:
    return _rt.to_dict(health_check_to_wire(_v))


def health_check_from_dict(_j: dict[str, _Any]) -> _t.HealthCheck:
    return health_check_from_wire(_rt.from_dict(_pb.HealthCheck, _j))


def environment_variable_from_wire(_w: _pb.EnvironmentVariable) -> _t.EnvironmentVariable:
    return _t.EnvironmentVariable(
        name=_w.name,
        value=_w.value,
        secret=_w.secret,
        source_file=_w.source_file,
        from_env_file_variables=tuple(_w.from_env_file_variables),
        value_left_out=_w.value_left_out,
    )


def environment_variable_to_wire(_v: _t.EnvironmentVariable) -> _pb.EnvironmentVariable:
    return _pb.EnvironmentVariable(
        name=_v.name or None,
        value=_v.value or None,
        secret=_v.secret or None,
        source_file=_v.source_file or None,
        from_env_file_variables=_rt.strings("EnvironmentVariable.from_env_file_variables", _v.from_env_file_variables),
        value_left_out=_v.value_left_out or None,
    )


def environment_variable_to_dict(_v: _t.EnvironmentVariable) -> dict[str, _Any]:
    return _rt.to_dict(environment_variable_to_wire(_v))


def environment_variable_from_dict(_j: dict[str, _Any]) -> _t.EnvironmentVariable:
    return environment_variable_from_wire(_rt.from_dict(_pb.EnvironmentVariable, _j))


def volume_from_wire(_w: _pb.Volume) -> _t.Volume:
    return _t.Volume(
        volume=_w.volume,
        size_bytes=_w.size_bytes,
        mounted_by=tuple(volume_mounted_by_from_wire(_x) for _x in _w.mounted_by),
        last_backup_time=_rt.time_from_wire(_w.last_backup_time) if _w.last_backup_time is not None else None,
        snapshot_count=_w.snapshot_count,
        declared=_w.declared,
    )


def volume_to_wire(_v: _t.Volume) -> _pb.Volume:
    return _pb.Volume(
        volume=_v.volume or None,
        size_bytes=_v.size_bytes or None,
        mounted_by=[volume_mounted_by_to_wire(_x) for _x in _v.mounted_by],
        last_backup_time=_rt.time_to_wire(_v.last_backup_time) if _v.last_backup_time is not None else None,
        snapshot_count=_v.snapshot_count or None,
        declared=_v.declared or None,
    )


def volume_to_dict(_v: _t.Volume) -> dict[str, _Any]:
    return _rt.to_dict(volume_to_wire(_v))


def volume_from_dict(_j: dict[str, _Any]) -> _t.Volume:
    return volume_from_wire(_rt.from_dict(_pb.Volume, _j))


def volume_mounted_by_from_wire(_w: _pb.VolumeMountedBy) -> _t.VolumeMountedBy:
    return _t.VolumeMountedBy(
        service=_w.service,
        container_path=_w.container_path,
    )


def volume_mounted_by_to_wire(_v: _t.VolumeMountedBy) -> _pb.VolumeMountedBy:
    return _pb.VolumeMountedBy(
        service=_v.service or None,
        container_path=_v.container_path or None,
    )


def volume_mounted_by_to_dict(_v: _t.VolumeMountedBy) -> dict[str, _Any]:
    return _rt.to_dict(volume_mounted_by_to_wire(_v))


def volume_mounted_by_from_dict(_j: dict[str, _Any]) -> _t.VolumeMountedBy:
    return volume_mounted_by_from_wire(_rt.from_dict(_pb.VolumeMountedBy, _j))


def host_from_wire(_w: _pb.Host) -> _t.Host:
    return _t.Host(
        host=_w.host,
        url=_w.url,
        certificate_source=certificate_source_from_wire(_w.certificate_source),
        certificate_expire_time=_rt.time_from_wire(_w.certificate_expire_time) if _w.certificate_expire_time is not None else None,
        unavailable_message=_w.unavailable_message,
    )


def host_to_wire(_v: _t.Host) -> _pb.Host:
    return _pb.Host(
        host=_v.host or None,
        url=_v.url or None,
        certificate_source=certificate_source_to_wire(_v.certificate_source) if _v.certificate_source.value else None,
        certificate_expire_time=_rt.time_to_wire(_v.certificate_expire_time) if _v.certificate_expire_time is not None else None,
        unavailable_message=_v.unavailable_message or None,
    )


def host_to_dict(_v: _t.Host) -> dict[str, _Any]:
    return _rt.to_dict(host_to_wire(_v))


def host_from_dict(_j: dict[str, _Any]) -> _t.Host:
    return host_from_wire(_rt.from_dict(_pb.Host, _j))


def route_from_wire(_w: _pb.Route) -> _t.Route:
    return _t.Route(
        host=_w.host,
        path=_w.path,
        service=_w.service,
        port=_w.port,
        strip_path=_w.strip_path,
    )


def route_to_wire(_v: _t.Route) -> _pb.Route:
    return _pb.Route(
        host=_v.host or None,
        path=_v.path or None,
        service=_v.service or None,
        port=_v.port or None,
        strip_path=_v.strip_path or None,
    )


def route_to_dict(_v: _t.Route) -> dict[str, _Any]:
    return _rt.to_dict(route_to_wire(_v))


def route_from_dict(_j: dict[str, _Any]) -> _t.Route:
    return route_from_wire(_rt.from_dict(_pb.Route, _j))


def operation_from_wire(_w: _pb.Operation) -> _t.Operation:
    return _t.Operation(
        operation_id=_w.operation_id,
        kind=operation_kind_from_wire(_w.kind),
        status=operation_status_from_wire(_w.status),
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        finish_time=_rt.time_from_wire(_w.finish_time) if _w.finish_time is not None else None,
        failure_message=_w.failure_message,
        deploy_failure_reason=deploy_failure_reason_from_wire(_w.deploy_failure_reason),
        made_current=_w.made_current,
        service=_w.service,
        failed_exit_code=_w.failed_exit_code,
        snapshot_id=_w.snapshot_id,
        restored_volumes=tuple(_w.restored_volumes),
        undo_snapshot_id=_w.undo_snapshot_id,
        github_commit=github_commit_from_wire(_w.github_commit) if _w.github_commit is not None else None,
        archive_name=_w.archive_name,
        adjustments=tuple(_w.adjustments),
        changed_paths=tuple(_w.changed_paths),
        changed_path_count=_w.changed_path_count,
        files_kept=_w.files_kept,
    )


def operation_to_wire(_v: _t.Operation) -> _pb.Operation:
    return _pb.Operation(
        operation_id=_v.operation_id or None,
        kind=operation_kind_to_wire(_v.kind) if _v.kind.value else None,
        status=operation_status_to_wire(_v.status) if _v.status.value else None,
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        finish_time=_rt.time_to_wire(_v.finish_time) if _v.finish_time is not None else None,
        failure_message=_v.failure_message or None,
        deploy_failure_reason=deploy_failure_reason_to_wire(_v.deploy_failure_reason) if _v.deploy_failure_reason.value else None,
        made_current=_v.made_current or None,
        service=_v.service or None,
        failed_exit_code=_v.failed_exit_code or None,
        snapshot_id=_v.snapshot_id or None,
        restored_volumes=_rt.strings("Operation.restored_volumes", _v.restored_volumes),
        undo_snapshot_id=_v.undo_snapshot_id or None,
        github_commit=github_commit_to_wire(_v.github_commit) if _v.github_commit is not None else None,
        archive_name=_v.archive_name or None,
        adjustments=_rt.strings("Operation.adjustments", _v.adjustments),
        changed_paths=_rt.strings("Operation.changed_paths", _v.changed_paths),
        changed_path_count=_v.changed_path_count or None,
        files_kept=_v.files_kept or None,
    )


def operation_to_dict(_v: _t.Operation) -> dict[str, _Any]:
    return _rt.to_dict(operation_to_wire(_v))


def operation_from_dict(_j: dict[str, _Any]) -> _t.Operation:
    return operation_from_wire(_rt.from_dict(_pb.Operation, _j))


def snapshot_from_wire(_w: _pb.Snapshot) -> _t.Snapshot:
    return _t.Snapshot(
        snapshot_id=_w.snapshot_id,
        create_time=_rt.time_from_wire(_w.create_time) if _w.create_time is not None else None,
        size_bytes=_w.size_bytes,
        volumes=tuple(_w.volumes),
    )


def snapshot_to_wire(_v: _t.Snapshot) -> _pb.Snapshot:
    return _pb.Snapshot(
        snapshot_id=_v.snapshot_id or None,
        create_time=_rt.time_to_wire(_v.create_time) if _v.create_time is not None else None,
        size_bytes=_v.size_bytes or None,
        volumes=_rt.strings("Snapshot.volumes", _v.volumes),
    )


def snapshot_to_dict(_v: _t.Snapshot) -> dict[str, _Any]:
    return _rt.to_dict(snapshot_to_wire(_v))


def snapshot_from_dict(_j: dict[str, _Any]) -> _t.Snapshot:
    return snapshot_from_wire(_rt.from_dict(_pb.Snapshot, _j))


def http_traffic_summary_from_wire(_w: _pb.HttpTrafficSummary) -> _t.HttpTrafficSummary:
    return _t.HttpTrafficSummary(
        request_count=_w.request_count,
        server_error_count=_w.server_error_count,
        latency_p50_ms=_w.latency_p50_ms,
        latency_p95_ms=_w.latency_p95_ms,
    )


def http_traffic_summary_to_wire(_v: _t.HttpTrafficSummary) -> _pb.HttpTrafficSummary:
    return _pb.HttpTrafficSummary(
        request_count=_v.request_count or None,
        server_error_count=_v.server_error_count or None,
        latency_p50_ms=_v.latency_p50_ms or None,
        latency_p95_ms=_v.latency_p95_ms or None,
    )


def http_traffic_summary_to_dict(_v: _t.HttpTrafficSummary) -> dict[str, _Any]:
    return _rt.to_dict(http_traffic_summary_to_wire(_v))


def http_traffic_summary_from_dict(_j: dict[str, _Any]) -> _t.HttpTrafficSummary:
    return http_traffic_summary_from_wire(_rt.from_dict(_pb.HttpTrafficSummary, _j))


def create_project_response_from_wire(_w: _pb.CreateProjectResponse) -> _t.CreateProjectResponse:
    return _t.CreateProjectResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        violations=tuple(spec_violation_from_wire(_x) for _x in _w.violations),
        adjustments=tuple(_w.adjustments),
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
    )


def create_project_response_to_wire(_v: _t.CreateProjectResponse) -> _pb.CreateProjectResponse:
    return _pb.CreateProjectResponse(
        operation=operation_to_wire(_v.operation) if _v.operation is not None else None,
        violations=[spec_violation_to_wire(_x) for _x in _v.violations],
        adjustments=_rt.strings("CreateProjectResponse.adjustments", _v.adjustments),
        project=project_to_wire(_v.project) if _v.project is not None else None,
        log=[operation_log_line_to_wire(_x) for _x in _v.log],
    )


def create_project_response_to_dict(_v: _t.CreateProjectResponse) -> dict[str, _Any]:
    return _rt.to_dict(create_project_response_to_wire(_v))


def create_project_response_from_dict(_j: dict[str, _Any]) -> _t.CreateProjectResponse:
    return create_project_response_from_wire(_rt.from_dict(_pb.CreateProjectResponse, _j))


def mount_volume_from_wire(_w: _pb.MountVolume) -> _t.MountVolume:
    return _t.MountVolume(
        service=_w.service,
        volume=_w.volume,
        container_path=_w.container_path,
    )


def mount_volume_to_wire(_v: _t.MountVolume) -> _pb.MountVolume:
    return _pb.MountVolume(
        service=_v.service or None,
        volume=_v.volume or None,
        container_path=_v.container_path or None,
    )


def mount_volume_to_dict(_v: _t.MountVolume) -> dict[str, _Any]:
    return _rt.to_dict(mount_volume_to_wire(_v))


def mount_volume_from_dict(_j: dict[str, _Any]) -> _t.MountVolume:
    return mount_volume_from_wire(_rt.from_dict(_pb.MountVolume, _j))


def project_extension_from_wire(_w: _pb.ProjectExtension) -> _t.ProjectExtension:
    return _t.ProjectExtension(
        metadata=project_metadata_from_wire(_w.metadata) if _w.metadata is not None else None,
        routes=tuple(route_from_wire(_x) for _x in _w.routes),
        remove_routes=_w.remove_routes,
        password=_w.password,
        remove_password=_w.remove_password,
    )


def project_extension_to_wire(_v: _t.ProjectExtension) -> _pb.ProjectExtension:
    return _pb.ProjectExtension(
        metadata=project_metadata_to_wire(_v.metadata) if _v.metadata is not None else None,
        routes=[route_to_wire(_x) for _x in _v.routes],
        remove_routes=_v.remove_routes or None,
        password=_v.password or None,
        remove_password=_v.remove_password or None,
    )


def project_extension_to_dict(_v: _t.ProjectExtension) -> dict[str, _Any]:
    return _rt.to_dict(project_extension_to_wire(_v))


def project_extension_from_dict(_j: dict[str, _Any]) -> _t.ProjectExtension:
    return project_extension_from_wire(_rt.from_dict(_pb.ProjectExtension, _j))


def file_change_from_wire(_w: _pb.FileChange) -> _t.FileChange:
    _k = _w.change
    if _k is None:
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
        )
    if _k.field == "text":
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
            text=_k.value,
        )
    if _k.field == "data":
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
            data=_k.value,
        )
    if _k.field == "make_directory":
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
            make_directory=_k.value,
        )
    if _k.field == "delete":
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
            delete=_k.value,
        )
    if _k.field == "delete_tree":
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
            delete_tree=_k.value,
        )
    if _k.field == "rename_to":
        return _t.FileChange(
            path=_w.path,
            executable=_w.executable,
            rename_to=_k.value,
        )
    _rt.never(_k)


def file_change_to_wire(_v: _t.FileChange) -> _pb.FileChange:
    _w = _pb.FileChange(
        path=_v.path or None,
        executable=_v.executable or None,
    )
    if _v.text is not None:
        _w.change = _Oneof[_Literal["text"], str]("text", _v.text)
    elif _v.data is not None:
        _w.change = _Oneof[_Literal["data"], bytes]("data", _v.data)
    elif _v.make_directory is not None:
        _w.change = _Oneof[_Literal["make_directory"], bool]("make_directory", _v.make_directory)
    elif _v.delete is not None:
        _w.change = _Oneof[_Literal["delete"], bool]("delete", _v.delete)
    elif _v.delete_tree is not None:
        _w.change = _Oneof[_Literal["delete_tree"], bool]("delete_tree", _v.delete_tree)
    elif _v.rename_to is not None:
        _w.change = _Oneof[_Literal["rename_to"], str]("rename_to", _v.rename_to)
    return _w


def file_change_to_dict(_v: _t.FileChange) -> dict[str, _Any]:
    return _rt.to_dict(file_change_to_wire(_v))


def file_change_from_dict(_j: dict[str, _Any]) -> _t.FileChange:
    return file_change_from_wire(_rt.from_dict(_pb.FileChange, _j))


def deploy_project_response_from_wire(_w: _pb.DeployProjectResponse) -> _t.DeployProjectResponse:
    return _t.DeployProjectResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        violations=tuple(spec_violation_from_wire(_x) for _x in _w.violations),
        adjustments=tuple(_w.adjustments),
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
    )


def deploy_project_response_to_wire(_v: _t.DeployProjectResponse) -> _pb.DeployProjectResponse:
    return _pb.DeployProjectResponse(
        operation=operation_to_wire(_v.operation) if _v.operation is not None else None,
        violations=[spec_violation_to_wire(_x) for _x in _v.violations],
        adjustments=_rt.strings("DeployProjectResponse.adjustments", _v.adjustments),
        project=project_to_wire(_v.project) if _v.project is not None else None,
        log=[operation_log_line_to_wire(_x) for _x in _v.log],
    )


def deploy_project_response_to_dict(_v: _t.DeployProjectResponse) -> dict[str, _Any]:
    return _rt.to_dict(deploy_project_response_to_wire(_v))


def deploy_project_response_from_dict(_j: dict[str, _Any]) -> _t.DeployProjectResponse:
    return deploy_project_response_from_wire(_rt.from_dict(_pb.DeployProjectResponse, _j))


def spec_violation_from_wire(_w: _pb.SpecViolation) -> _t.SpecViolation:
    return _t.SpecViolation(
        service=_w.service,
        location=_w.location,
        violation_message=_w.violation_message,
    )


def spec_violation_to_wire(_v: _t.SpecViolation) -> _pb.SpecViolation:
    return _pb.SpecViolation(
        service=_v.service or None,
        location=_v.location or None,
        violation_message=_v.violation_message or None,
    )


def spec_violation_to_dict(_v: _t.SpecViolation) -> dict[str, _Any]:
    return _rt.to_dict(spec_violation_to_wire(_v))


def spec_violation_from_dict(_j: dict[str, _Any]) -> _t.SpecViolation:
    return spec_violation_from_wire(_rt.from_dict(_pb.SpecViolation, _j))


def list_commits_response_from_wire(_w: _pb.ListCommitsResponse) -> _t.ListCommitsResponse:
    return _t.ListCommitsResponse(
        commits=tuple(branch_commit_from_wire(_x) for _x in _w.commits),
        more=_w.more,
    )


def list_commits_response_to_wire(_v: _t.ListCommitsResponse) -> _pb.ListCommitsResponse:
    return _pb.ListCommitsResponse(
        commits=[branch_commit_to_wire(_x) for _x in _v.commits],
        more=_v.more or None,
    )


def list_commits_response_to_dict(_v: _t.ListCommitsResponse) -> dict[str, _Any]:
    return _rt.to_dict(list_commits_response_to_wire(_v))


def list_commits_response_from_dict(_j: dict[str, _Any]) -> _t.ListCommitsResponse:
    return list_commits_response_from_wire(_rt.from_dict(_pb.ListCommitsResponse, _j))


def branch_commit_from_wire(_w: _pb.BranchCommit) -> _t.BranchCommit:
    return _t.BranchCommit(
        commit=github_commit_from_wire(_w.commit) if _w.commit is not None else None,
        author=_w.author,
        commit_time=_rt.time_from_wire(_w.commit_time) if _w.commit_time is not None else None,
        deployed=_w.deployed,
        last_deploy=operation_from_wire(_w.last_deploy) if _w.last_deploy is not None else None,
        newest=_w.newest,
    )


def branch_commit_to_wire(_v: _t.BranchCommit) -> _pb.BranchCommit:
    return _pb.BranchCommit(
        commit=github_commit_to_wire(_v.commit) if _v.commit is not None else None,
        author=_v.author or None,
        commit_time=_rt.time_to_wire(_v.commit_time) if _v.commit_time is not None else None,
        deployed=_v.deployed or None,
        last_deploy=operation_to_wire(_v.last_deploy) if _v.last_deploy is not None else None,
        newest=_v.newest or None,
    )


def branch_commit_to_dict(_v: _t.BranchCommit) -> dict[str, _Any]:
    return _rt.to_dict(branch_commit_to_wire(_v))


def branch_commit_from_dict(_j: dict[str, _Any]) -> _t.BranchCommit:
    return branch_commit_from_wire(_rt.from_dict(_pb.BranchCommit, _j))


def services_action_from_wire(_w: _pb.ServicesAction) -> _t.ServicesAction:
    return _t.ServicesAction(
        services=tuple(_w.services),
    )


def services_action_to_wire(_v: _t.ServicesAction) -> _pb.ServicesAction:
    return _pb.ServicesAction(
        services=_rt.strings("ServicesAction.services", _v.services),
    )


def services_action_to_dict(_v: _t.ServicesAction) -> dict[str, _Any]:
    return _rt.to_dict(services_action_to_wire(_v))


def services_action_from_dict(_j: dict[str, _Any]) -> _t.ServicesAction:
    return services_action_from_wire(_rt.from_dict(_pb.ServicesAction, _j))


def recreate_service_action_from_wire(_w: _pb.RecreateServiceAction) -> _t.RecreateServiceAction:
    return _t.RecreateServiceAction(
        service=_w.service,
        pull_latest_image=_w.pull_latest_image,
    )


def recreate_service_action_to_wire(_v: _t.RecreateServiceAction) -> _pb.RecreateServiceAction:
    return _pb.RecreateServiceAction(
        service=_v.service or None,
        pull_latest_image=_v.pull_latest_image or None,
    )


def recreate_service_action_to_dict(_v: _t.RecreateServiceAction) -> dict[str, _Any]:
    return _rt.to_dict(recreate_service_action_to_wire(_v))


def recreate_service_action_from_dict(_j: dict[str, _Any]) -> _t.RecreateServiceAction:
    return recreate_service_action_from_wire(_rt.from_dict(_pb.RecreateServiceAction, _j))


def back_up_action_from_wire(_w: _pb.BackUpAction) -> _t.BackUpAction:
    return _t.BackUpAction()


def back_up_action_to_wire(_v: _t.BackUpAction) -> _pb.BackUpAction:
    return _pb.BackUpAction()


def back_up_action_to_dict(_v: _t.BackUpAction) -> dict[str, _Any]:
    return _rt.to_dict(back_up_action_to_wire(_v))


def back_up_action_from_dict(_j: dict[str, _Any]) -> _t.BackUpAction:
    return back_up_action_from_wire(_rt.from_dict(_pb.BackUpAction, _j))


def restore_snapshot_action_from_wire(_w: _pb.RestoreSnapshotAction) -> _t.RestoreSnapshotAction:
    return _t.RestoreSnapshotAction(
        snapshot_id=_w.snapshot_id,
        volumes=tuple(_w.volumes),
    )


def restore_snapshot_action_to_wire(_v: _t.RestoreSnapshotAction) -> _pb.RestoreSnapshotAction:
    return _pb.RestoreSnapshotAction(
        snapshot_id=_v.snapshot_id or None,
        volumes=_rt.strings("RestoreSnapshotAction.volumes", _v.volumes),
    )


def restore_snapshot_action_to_dict(_v: _t.RestoreSnapshotAction) -> dict[str, _Any]:
    return _rt.to_dict(restore_snapshot_action_to_wire(_v))


def restore_snapshot_action_from_dict(_j: dict[str, _Any]) -> _t.RestoreSnapshotAction:
    return restore_snapshot_action_from_wire(_rt.from_dict(_pb.RestoreSnapshotAction, _j))


def cancel_operation_action_from_wire(_w: _pb.CancelOperationAction) -> _t.CancelOperationAction:
    return _t.CancelOperationAction(
        operation_id=_w.operation_id,
    )


def cancel_operation_action_to_wire(_v: _t.CancelOperationAction) -> _pb.CancelOperationAction:
    return _pb.CancelOperationAction(
        operation_id=_v.operation_id or None,
    )


def cancel_operation_action_to_dict(_v: _t.CancelOperationAction) -> dict[str, _Any]:
    return _rt.to_dict(cancel_operation_action_to_wire(_v))


def cancel_operation_action_from_dict(_j: dict[str, _Any]) -> _t.CancelOperationAction:
    return cancel_operation_action_from_wire(_rt.from_dict(_pb.CancelOperationAction, _j))


def delete_project_action_from_wire(_w: _pb.DeleteProjectAction) -> _t.DeleteProjectAction:
    return _t.DeleteProjectAction(
        skip_final_backup=_w.skip_final_backup,
    )


def delete_project_action_to_wire(_v: _t.DeleteProjectAction) -> _pb.DeleteProjectAction:
    return _pb.DeleteProjectAction(
        skip_final_backup=_v.skip_final_backup or None,
    )


def delete_project_action_to_dict(_v: _t.DeleteProjectAction) -> dict[str, _Any]:
    return _rt.to_dict(delete_project_action_to_wire(_v))


def delete_project_action_from_dict(_j: dict[str, _Any]) -> _t.DeleteProjectAction:
    return delete_project_action_from_wire(_rt.from_dict(_pb.DeleteProjectAction, _j))


def run_project_action_response_from_wire(_w: _pb.RunProjectActionResponse) -> _t.RunProjectActionResponse:
    return _t.RunProjectActionResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
    )


def run_project_action_response_to_wire(_v: _t.RunProjectActionResponse) -> _pb.RunProjectActionResponse:
    return _pb.RunProjectActionResponse(
        operation=operation_to_wire(_v.operation) if _v.operation is not None else None,
        project=project_to_wire(_v.project) if _v.project is not None else None,
        log=[operation_log_line_to_wire(_x) for _x in _v.log],
    )


def run_project_action_response_to_dict(_v: _t.RunProjectActionResponse) -> dict[str, _Any]:
    return _rt.to_dict(run_project_action_response_to_wire(_v))


def run_project_action_response_from_dict(_j: dict[str, _Any]) -> _t.RunProjectActionResponse:
    return run_project_action_response_from_wire(_rt.from_dict(_pb.RunProjectActionResponse, _j))


def get_operation_response_from_wire(_w: _pb.GetOperationResponse) -> _t.GetOperationResponse:
    return _t.GetOperationResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
        log_line_count=_w.log_line_count,
        next_after_log_line=_w.next_after_log_line,
    )


def get_operation_response_to_wire(_v: _t.GetOperationResponse) -> _pb.GetOperationResponse:
    return _pb.GetOperationResponse(
        operation=operation_to_wire(_v.operation) if _v.operation is not None else None,
        project=project_to_wire(_v.project) if _v.project is not None else None,
        log=[operation_log_line_to_wire(_x) for _x in _v.log],
        log_line_count=_v.log_line_count or None,
        next_after_log_line=_v.next_after_log_line or None,
    )


def get_operation_response_to_dict(_v: _t.GetOperationResponse) -> dict[str, _Any]:
    return _rt.to_dict(get_operation_response_to_wire(_v))


def get_operation_response_from_dict(_j: dict[str, _Any]) -> _t.GetOperationResponse:
    return get_operation_response_from_wire(_rt.from_dict(_pb.GetOperationResponse, _j))


def operation_log_line_from_wire(_w: _pb.OperationLogLine) -> _t.OperationLogLine:
    return _t.OperationLogLine(
        time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
        text=_w.text,
    )


def operation_log_line_to_wire(_v: _t.OperationLogLine) -> _pb.OperationLogLine:
    return _pb.OperationLogLine(
        time=_rt.time_to_wire(_v.time) if _v.time is not None else None,
        text=_v.text or None,
    )


def operation_log_line_to_dict(_v: _t.OperationLogLine) -> dict[str, _Any]:
    return _rt.to_dict(operation_log_line_to_wire(_v))


def operation_log_line_from_dict(_j: dict[str, _Any]) -> _t.OperationLogLine:
    return operation_log_line_from_wire(_rt.from_dict(_pb.OperationLogLine, _j))


def http_traffic_filter_from_wire(_w: _pb.HttpTrafficFilter) -> _t.HttpTrafficFilter:
    return _t.HttpTrafficFilter(
        host=_w.host,
        method=_w.method,
        path_contains=_w.path_contains,
        path_pattern=_w.path_pattern,
        status_class=_w.status_class,
    )


def http_traffic_filter_to_wire(_v: _t.HttpTrafficFilter) -> _pb.HttpTrafficFilter:
    return _pb.HttpTrafficFilter(
        host=_v.host or None,
        method=_v.method or None,
        path_contains=_v.path_contains or None,
        path_pattern=_v.path_pattern or None,
        status_class=_v.status_class or None,
    )


def http_traffic_filter_to_dict(_v: _t.HttpTrafficFilter) -> dict[str, _Any]:
    return _rt.to_dict(http_traffic_filter_to_wire(_v))


def http_traffic_filter_from_dict(_j: dict[str, _Any]) -> _t.HttpTrafficFilter:
    return http_traffic_filter_from_wire(_rt.from_dict(_pb.HttpTrafficFilter, _j))


def query_http_traffic_response_from_wire(_w: _pb.QueryHttpTrafficResponse) -> _t.QueryHttpTrafficResponse:
    return _t.QueryHttpTrafficResponse(
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        end_time=_rt.time_from_wire(_w.end_time) if _w.end_time is not None else None,
        oldest_kept_time=_rt.time_from_wire(_w.oldest_kept_time) if _w.oldest_kept_time is not None else None,
        summary=http_traffic_summary_from_wire(_w.summary) if _w.summary is not None else None,
        buckets=tuple(http_traffic_bucket_from_wire(_x) for _x in _w.buckets),
        top_paths=tuple(http_path_traffic_from_wire(_x) for _x in _w.top_paths),
        newest_sequence=_w.newest_sequence,
        requests=tuple(http_request_from_wire(_x) for _x in _w.requests),
        next_page_token=_w.next_page_token,
        tail_sequence=_w.tail_sequence,
    )


def query_http_traffic_response_to_wire(_v: _t.QueryHttpTrafficResponse) -> _pb.QueryHttpTrafficResponse:
    return _pb.QueryHttpTrafficResponse(
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        end_time=_rt.time_to_wire(_v.end_time) if _v.end_time is not None else None,
        oldest_kept_time=_rt.time_to_wire(_v.oldest_kept_time) if _v.oldest_kept_time is not None else None,
        summary=http_traffic_summary_to_wire(_v.summary) if _v.summary is not None else None,
        buckets=[http_traffic_bucket_to_wire(_x) for _x in _v.buckets],
        top_paths=[http_path_traffic_to_wire(_x) for _x in _v.top_paths],
        newest_sequence=_v.newest_sequence or None,
        requests=[http_request_to_wire(_x) for _x in _v.requests],
        next_page_token=_v.next_page_token or None,
        tail_sequence=_v.tail_sequence or None,
    )


def query_http_traffic_response_to_dict(_v: _t.QueryHttpTrafficResponse) -> dict[str, _Any]:
    return _rt.to_dict(query_http_traffic_response_to_wire(_v))


def query_http_traffic_response_from_dict(_j: dict[str, _Any]) -> _t.QueryHttpTrafficResponse:
    return query_http_traffic_response_from_wire(_rt.from_dict(_pb.QueryHttpTrafficResponse, _j))


def http_traffic_bucket_from_wire(_w: _pb.HttpTrafficBucket) -> _t.HttpTrafficBucket:
    return _t.HttpTrafficBucket(
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        summary=http_traffic_summary_from_wire(_w.summary) if _w.summary is not None else None,
    )


def http_traffic_bucket_to_wire(_v: _t.HttpTrafficBucket) -> _pb.HttpTrafficBucket:
    return _pb.HttpTrafficBucket(
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        summary=http_traffic_summary_to_wire(_v.summary) if _v.summary is not None else None,
    )


def http_traffic_bucket_to_dict(_v: _t.HttpTrafficBucket) -> dict[str, _Any]:
    return _rt.to_dict(http_traffic_bucket_to_wire(_v))


def http_traffic_bucket_from_dict(_j: dict[str, _Any]) -> _t.HttpTrafficBucket:
    return http_traffic_bucket_from_wire(_rt.from_dict(_pb.HttpTrafficBucket, _j))


def http_path_traffic_from_wire(_w: _pb.HttpPathTraffic) -> _t.HttpPathTraffic:
    return _t.HttpPathTraffic(
        method=_w.method,
        path_pattern=_w.path_pattern,
        summary=http_traffic_summary_from_wire(_w.summary) if _w.summary is not None else None,
    )


def http_path_traffic_to_wire(_v: _t.HttpPathTraffic) -> _pb.HttpPathTraffic:
    return _pb.HttpPathTraffic(
        method=_v.method or None,
        path_pattern=_v.path_pattern or None,
        summary=http_traffic_summary_to_wire(_v.summary) if _v.summary is not None else None,
    )


def http_path_traffic_to_dict(_v: _t.HttpPathTraffic) -> dict[str, _Any]:
    return _rt.to_dict(http_path_traffic_to_wire(_v))


def http_path_traffic_from_dict(_j: dict[str, _Any]) -> _t.HttpPathTraffic:
    return http_path_traffic_from_wire(_rt.from_dict(_pb.HttpPathTraffic, _j))


def http_request_from_wire(_w: _pb.HttpRequest) -> _t.HttpRequest:
    return _t.HttpRequest(
        sequence=_w.sequence,
        finish_time=_rt.time_from_wire(_w.finish_time) if _w.finish_time is not None else None,
        host=_w.host,
        method=_w.method,
        path=_w.path,
        path_pattern=_w.path_pattern,
        route_path=_w.route_path,
        service=_w.service,
        port=_w.port,
        status_code=_w.status_code,
        response_size_bytes=_w.response_size_bytes,
        duration_ms=_w.duration_ms,
        service_duration_ms=_w.service_duration_ms,
        client_ip_address=_w.client_ip_address,
        user_agent=_w.user_agent,
    )


def http_request_to_wire(_v: _t.HttpRequest) -> _pb.HttpRequest:
    return _pb.HttpRequest(
        sequence=_v.sequence or None,
        finish_time=_rt.time_to_wire(_v.finish_time) if _v.finish_time is not None else None,
        host=_v.host or None,
        method=_v.method or None,
        path=_v.path or None,
        path_pattern=_v.path_pattern or None,
        route_path=_v.route_path or None,
        service=_v.service or None,
        port=_v.port or None,
        status_code=_v.status_code or None,
        response_size_bytes=_v.response_size_bytes or None,
        duration_ms=_v.duration_ms or None,
        service_duration_ms=_v.service_duration_ms or None,
        client_ip_address=_v.client_ip_address or None,
        user_agent=_v.user_agent or None,
    )


def http_request_to_dict(_v: _t.HttpRequest) -> dict[str, _Any]:
    return _rt.to_dict(http_request_to_wire(_v))


def http_request_from_dict(_j: dict[str, _Any]) -> _t.HttpRequest:
    return http_request_from_wire(_rt.from_dict(_pb.HttpRequest, _j))


def container_log_filter_from_wire(_w: _pb.ContainerLogFilter) -> _t.ContainerLogFilter:
    return _t.ContainerLogFilter(
        service=_w.service,
        stream=output_stream_from_wire(_w.stream),
        text_contains=_w.text_contains,
    )


def container_log_filter_to_wire(_v: _t.ContainerLogFilter) -> _pb.ContainerLogFilter:
    return _pb.ContainerLogFilter(
        service=_v.service or None,
        stream=output_stream_to_wire(_v.stream) if _v.stream.value else None,
        text_contains=_v.text_contains or None,
    )


def container_log_filter_to_dict(_v: _t.ContainerLogFilter) -> dict[str, _Any]:
    return _rt.to_dict(container_log_filter_to_wire(_v))


def container_log_filter_from_dict(_j: dict[str, _Any]) -> _t.ContainerLogFilter:
    return container_log_filter_from_wire(_rt.from_dict(_pb.ContainerLogFilter, _j))


def query_container_logs_response_from_wire(_w: _pb.QueryContainerLogsResponse) -> _t.QueryContainerLogsResponse:
    return _t.QueryContainerLogsResponse(
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        end_time=_rt.time_from_wire(_w.end_time) if _w.end_time is not None else None,
        oldest_kept_time=_rt.time_from_wire(_w.oldest_kept_time) if _w.oldest_kept_time is not None else None,
        lines=tuple(log_line_from_wire(_x) for _x in _w.lines),
        next_page_token=_w.next_page_token,
        tail_cursor=_w.tail_cursor,
    )


def query_container_logs_response_to_wire(_v: _t.QueryContainerLogsResponse) -> _pb.QueryContainerLogsResponse:
    return _pb.QueryContainerLogsResponse(
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
        end_time=_rt.time_to_wire(_v.end_time) if _v.end_time is not None else None,
        oldest_kept_time=_rt.time_to_wire(_v.oldest_kept_time) if _v.oldest_kept_time is not None else None,
        lines=[log_line_to_wire(_x) for _x in _v.lines],
        next_page_token=_v.next_page_token or None,
        tail_cursor=_v.tail_cursor or None,
    )


def query_container_logs_response_to_dict(_v: _t.QueryContainerLogsResponse) -> dict[str, _Any]:
    return _rt.to_dict(query_container_logs_response_to_wire(_v))


def query_container_logs_response_from_dict(_j: dict[str, _Any]) -> _t.QueryContainerLogsResponse:
    return query_container_logs_response_from_wire(_rt.from_dict(_pb.QueryContainerLogsResponse, _j))


def log_line_from_wire(_w: _pb.LogLine) -> _t.LogLine:
    return _t.LogLine(
        time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
        service=_w.service,
        stream=output_stream_from_wire(_w.stream),
        text=_w.text,
    )


def log_line_to_wire(_v: _t.LogLine) -> _pb.LogLine:
    return _pb.LogLine(
        time=_rt.time_to_wire(_v.time) if _v.time is not None else None,
        service=_v.service or None,
        stream=output_stream_to_wire(_v.stream) if _v.stream.value else None,
        text=_v.text or None,
    )


def log_line_to_dict(_v: _t.LogLine) -> dict[str, _Any]:
    return _rt.to_dict(log_line_to_wire(_v))


def log_line_from_dict(_j: dict[str, _Any]) -> _t.LogLine:
    return log_line_from_wire(_rt.from_dict(_pb.LogLine, _j))


def run_service_command_response_from_wire(_w: _pb.RunServiceCommandResponse) -> _t.RunServiceCommandResponse:
    return _t.RunServiceCommandResponse(
        exit_code=_w.exit_code,
        timed_out=_w.timed_out,
        stdout=_w.stdout,
        stderr=_w.stderr,
        output_truncated=_w.output_truncated,
    )


def run_service_command_response_to_wire(_v: _t.RunServiceCommandResponse) -> _pb.RunServiceCommandResponse:
    return _pb.RunServiceCommandResponse(
        exit_code=_v.exit_code or None,
        timed_out=_v.timed_out or None,
        stdout=_v.stdout or None,
        stderr=_v.stderr or None,
        output_truncated=_v.output_truncated or None,
    )


def run_service_command_response_to_dict(_v: _t.RunServiceCommandResponse) -> dict[str, _Any]:
    return _rt.to_dict(run_service_command_response_to_wire(_v))


def run_service_command_response_from_dict(_j: dict[str, _Any]) -> _t.RunServiceCommandResponse:
    return run_service_command_response_from_wire(_rt.from_dict(_pb.RunServiceCommandResponse, _j))


def file_entry_from_wire(_w: _pb.FileEntry) -> _t.FileEntry:
    return _t.FileEntry(
        name=_w.name,
        type=file_type_from_wire(_w.type),
        size_bytes=_w.size_bytes,
        modify_time=_rt.time_from_wire(_w.modify_time) if _w.modify_time is not None else None,
        mode=_w.mode,
        owner_uid=_w.owner_uid,
        owner_gid=_w.owner_gid,
        symlink_target=_w.symlink_target,
    )


def file_entry_to_wire(_v: _t.FileEntry) -> _pb.FileEntry:
    return _pb.FileEntry(
        name=_v.name or None,
        type=file_type_to_wire(_v.type) if _v.type.value else None,
        size_bytes=_v.size_bytes or None,
        modify_time=_rt.time_to_wire(_v.modify_time) if _v.modify_time is not None else None,
        mode=_v.mode or None,
        owner_uid=_v.owner_uid or None,
        owner_gid=_v.owner_gid or None,
        symlink_target=_v.symlink_target or None,
    )


def file_entry_to_dict(_v: _t.FileEntry) -> dict[str, _Any]:
    return _rt.to_dict(file_entry_to_wire(_v))


def file_entry_from_dict(_j: dict[str, _Any]) -> _t.FileEntry:
    return file_entry_from_wire(_rt.from_dict(_pb.FileEntry, _j))


def read_path_response_from_wire(_w: _pb.ReadPathResponse) -> _t.ReadPathResponse:
    return _t.ReadPathResponse(
        entry=file_entry_from_wire(_w.entry) if _w.entry is not None else None,
        location=file_location_from_wire(_w.location),
        volume=_w.volume,
        entries=tuple(file_entry_from_wire(_x) for _x in _w.entries),
        entry_count=_w.entry_count,
        next_entry_page_token=_w.next_entry_page_token,
        text=_w.text,
        binary=_w.binary,
        next_offset_bytes=_w.next_offset_bytes,
        deploy_id=_w.deploy_id,
    )


def read_path_response_to_wire(_v: _t.ReadPathResponse) -> _pb.ReadPathResponse:
    return _pb.ReadPathResponse(
        entry=file_entry_to_wire(_v.entry) if _v.entry is not None else None,
        location=file_location_to_wire(_v.location) if _v.location.value else None,
        volume=_v.volume or None,
        entries=[file_entry_to_wire(_x) for _x in _v.entries],
        entry_count=_v.entry_count or None,
        next_entry_page_token=_v.next_entry_page_token or None,
        text=_v.text or None,
        binary=_v.binary or None,
        next_offset_bytes=_v.next_offset_bytes or None,
        deploy_id=_v.deploy_id or None,
    )


def read_path_response_to_dict(_v: _t.ReadPathResponse) -> dict[str, _Any]:
    return _rt.to_dict(read_path_response_to_wire(_v))


def read_path_response_from_dict(_j: dict[str, _Any]) -> _t.ReadPathResponse:
    return read_path_response_from_wire(_rt.from_dict(_pb.ReadPathResponse, _j))


def archive_upload_from_wire(_w: _pb.ArchiveUpload) -> _t.ArchiveUpload:
    return _t.ArchiveUpload(
        file_name=_w.file_name,
    )


def archive_upload_to_wire(_v: _t.ArchiveUpload) -> _pb.ArchiveUpload:
    return _pb.ArchiveUpload(
        file_name=_v.file_name or None,
    )


def archive_upload_to_dict(_v: _t.ArchiveUpload) -> dict[str, _Any]:
    return _rt.to_dict(archive_upload_to_wire(_v))


def archive_upload_from_dict(_j: dict[str, _Any]) -> _t.ArchiveUpload:
    return archive_upload_from_wire(_rt.from_dict(_pb.ArchiveUpload, _j))


def file_upload_from_wire(_w: _pb.FileUpload) -> _t.FileUpload:
    _k = _w.root
    if _k is None:
        return _t.FileUpload(
            project_id=_w.project_id,
            path=_w.path,
        )
    if _k.field == "service":
        return _t.FileUpload(
            project_id=_w.project_id,
            path=_w.path,
            service=_k.value,
        )
    if _k.field == "volume":
        return _t.FileUpload(
            project_id=_w.project_id,
            path=_w.path,
            volume=_k.value,
        )
    _rt.never(_k)


def file_upload_to_wire(_v: _t.FileUpload) -> _pb.FileUpload:
    _w = _pb.FileUpload(
        project_id=_v.project_id or None,
        path=_v.path or None,
    )
    if _v.service is not None:
        _w.root = _Oneof[_Literal["service"], str]("service", _v.service)
    elif _v.volume is not None:
        _w.root = _Oneof[_Literal["volume"], str]("volume", _v.volume)
    return _w


def file_upload_to_dict(_v: _t.FileUpload) -> dict[str, _Any]:
    return _rt.to_dict(file_upload_to_wire(_v))


def file_upload_from_dict(_j: dict[str, _Any]) -> _t.FileUpload:
    return file_upload_from_wire(_rt.from_dict(_pb.FileUpload, _j))


def path_download_from_wire(_w: _pb.PathDownload) -> _t.PathDownload:
    _k = _w.root
    if _k is None:
        return _t.PathDownload(
            project_id=_w.project_id,
            path=_w.path,
        )
    if _k.field == "service":
        return _t.PathDownload(
            project_id=_w.project_id,
            path=_w.path,
            service=_k.value,
        )
    if _k.field == "volume":
        return _t.PathDownload(
            project_id=_w.project_id,
            path=_w.path,
            volume=_k.value,
        )
    _rt.never(_k)


def path_download_to_wire(_v: _t.PathDownload) -> _pb.PathDownload:
    _w = _pb.PathDownload(
        project_id=_v.project_id or None,
        path=_v.path or None,
    )
    if _v.service is not None:
        _w.root = _Oneof[_Literal["service"], str]("service", _v.service)
    elif _v.volume is not None:
        _w.root = _Oneof[_Literal["volume"], str]("volume", _v.volume)
    return _w


def path_download_to_dict(_v: _t.PathDownload) -> dict[str, _Any]:
    return _rt.to_dict(path_download_to_wire(_v))


def path_download_from_dict(_j: dict[str, _Any]) -> _t.PathDownload:
    return path_download_from_wire(_rt.from_dict(_pb.PathDownload, _j))


def create_transfer_response_from_wire(_w: _pb.CreateTransferResponse) -> _t.CreateTransferResponse:
    return _t.CreateTransferResponse(
        url=_w.url,
        http_method=_w.http_method,
        expire_time=_rt.time_from_wire(_w.expire_time) if _w.expire_time is not None else None,
        command=_w.command,
        upload_id=_w.upload_id,
        replaces=_w.replaces,
        file_name=_w.file_name,
        exclude_names=tuple(_w.exclude_names),
    )


def create_transfer_response_to_wire(_v: _t.CreateTransferResponse) -> _pb.CreateTransferResponse:
    return _pb.CreateTransferResponse(
        url=_v.url or None,
        http_method=_v.http_method or None,
        expire_time=_rt.time_to_wire(_v.expire_time) if _v.expire_time is not None else None,
        command=_v.command or None,
        upload_id=_v.upload_id or None,
        replaces=_v.replaces or None,
        file_name=_v.file_name or None,
        exclude_names=_rt.strings("CreateTransferResponse.exclude_names", _v.exclude_names),
    )


def create_transfer_response_to_dict(_v: _t.CreateTransferResponse) -> dict[str, _Any]:
    return _rt.to_dict(create_transfer_response_to_wire(_v))


def create_transfer_response_from_dict(_j: dict[str, _Any]) -> _t.CreateTransferResponse:
    return create_transfer_response_from_wire(_rt.from_dict(_pb.CreateTransferResponse, _j))


def project_busy_from_wire(_w: _pb.ProjectBusy) -> _t.ProjectBusy:
    return _t.ProjectBusy(
        operation_id=_w.operation_id,
        kind=operation_kind_from_wire(_w.kind),
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
    )


def project_busy_to_wire(_v: _t.ProjectBusy) -> _pb.ProjectBusy:
    return _pb.ProjectBusy(
        operation_id=_v.operation_id or None,
        kind=operation_kind_to_wire(_v.kind) if _v.kind.value else None,
        start_time=_rt.time_to_wire(_v.start_time) if _v.start_time is not None else None,
    )


def project_busy_to_dict(_v: _t.ProjectBusy) -> dict[str, _Any]:
    return _rt.to_dict(project_busy_to_wire(_v))


def project_busy_from_dict(_j: dict[str, _Any]) -> _t.ProjectBusy:
    return project_busy_from_wire(_rt.from_dict(_pb.ProjectBusy, _j))


def project_changed_from_wire(_w: _pb.ProjectChanged) -> _t.ProjectChanged:
    return _t.ProjectChanged()


def project_changed_to_wire(_v: _t.ProjectChanged) -> _pb.ProjectChanged:
    return _pb.ProjectChanged()


def project_changed_to_dict(_v: _t.ProjectChanged) -> dict[str, _Any]:
    return _rt.to_dict(project_changed_to_wire(_v))


def project_changed_from_dict(_j: dict[str, _Any]) -> _t.ProjectChanged:
    return project_changed_from_wire(_rt.from_dict(_pb.ProjectChanged, _j))


def machine_unreachable_from_wire(_w: _pb.MachineUnreachable) -> _t.MachineUnreachable:
    return _t.MachineUnreachable()


def machine_unreachable_to_wire(_v: _t.MachineUnreachable) -> _pb.MachineUnreachable:
    return _pb.MachineUnreachable()


def machine_unreachable_to_dict(_v: _t.MachineUnreachable) -> dict[str, _Any]:
    return _rt.to_dict(machine_unreachable_to_wire(_v))


def machine_unreachable_from_dict(_j: dict[str, _Any]) -> _t.MachineUnreachable:
    return machine_unreachable_from_wire(_rt.from_dict(_pb.MachineUnreachable, _j))


def no_machine_from_wire(_w: _pb.NoMachine) -> _t.NoMachine:
    return _t.NoMachine(
        reason=no_machine_reason_from_wire(_w.reason),
        url=_w.url,
    )


def no_machine_to_wire(_v: _t.NoMachine) -> _pb.NoMachine:
    return _pb.NoMachine(
        reason=no_machine_reason_to_wire(_v.reason) if _v.reason.value else None,
        url=_v.url or None,
    )


def no_machine_to_dict(_v: _t.NoMachine) -> dict[str, _Any]:
    return _rt.to_dict(no_machine_to_wire(_v))


def no_machine_from_dict(_j: dict[str, _Any]) -> _t.NoMachine:
    return no_machine_from_wire(_rt.from_dict(_pb.NoMachine, _j))


def watch_operation_response_from_wire(_w: _pb.WatchOperationResponse) -> _t.WatchOperationResponse:
    _k = _w.message
    if _k is None:
        return _t.WatchOperationResponse()
    if _k.field == "log":
        return _t.WatchOperationResponse(
            log=operation_log_line_from_wire(_k.value),
        )
    if _k.field == "finished_operation":
        return _t.WatchOperationResponse(
            finished_operation=operation_from_wire(_k.value),
        )
    _rt.never(_k)


def watch_operation_response_to_wire(_v: _t.WatchOperationResponse) -> _pb.WatchOperationResponse:
    _w = _pb.WatchOperationResponse()
    if _v.log is not None:
        _w.message = _Oneof[_Literal["log"], _pb.OperationLogLine]("log", operation_log_line_to_wire(_v.log))
    elif _v.finished_operation is not None:
        _w.message = _Oneof[_Literal["finished_operation"], _pb.Operation]("finished_operation", operation_to_wire(_v.finished_operation))
    return _w


def watch_operation_response_to_dict(_v: _t.WatchOperationResponse) -> dict[str, _Any]:
    return _rt.to_dict(watch_operation_response_to_wire(_v))


def watch_operation_response_from_dict(_j: dict[str, _Any]) -> _t.WatchOperationResponse:
    return watch_operation_response_from_wire(_rt.from_dict(_pb.WatchOperationResponse, _j))


def tail_container_logs_response_from_wire(_w: _pb.TailContainerLogsResponse) -> _t.TailContainerLogsResponse:
    return _t.TailContainerLogsResponse(
        line=log_line_from_wire(_w.line) if _w.line is not None else None,
        cursor=_w.cursor,
    )


def tail_container_logs_response_to_wire(_v: _t.TailContainerLogsResponse) -> _pb.TailContainerLogsResponse:
    return _pb.TailContainerLogsResponse(
        line=log_line_to_wire(_v.line) if _v.line is not None else None,
        cursor=_v.cursor or None,
    )


def tail_container_logs_response_to_dict(_v: _t.TailContainerLogsResponse) -> dict[str, _Any]:
    return _rt.to_dict(tail_container_logs_response_to_wire(_v))


def tail_container_logs_response_from_dict(_j: dict[str, _Any]) -> _t.TailContainerLogsResponse:
    return tail_container_logs_response_from_wire(_rt.from_dict(_pb.TailContainerLogsResponse, _j))


def tail_http_traffic_response_from_wire(_w: _pb.TailHttpTrafficResponse) -> _t.TailHttpTrafficResponse:
    return _t.TailHttpTrafficResponse(
        request=http_request_from_wire(_w.request) if _w.request is not None else None,
    )


def tail_http_traffic_response_to_wire(_v: _t.TailHttpTrafficResponse) -> _pb.TailHttpTrafficResponse:
    return _pb.TailHttpTrafficResponse(
        request=http_request_to_wire(_v.request) if _v.request is not None else None,
    )


def tail_http_traffic_response_to_dict(_v: _t.TailHttpTrafficResponse) -> dict[str, _Any]:
    return _rt.to_dict(tail_http_traffic_response_to_wire(_v))


def tail_http_traffic_response_from_dict(_j: dict[str, _Any]) -> _t.TailHttpTrafficResponse:
    return tail_http_traffic_response_from_wire(_rt.from_dict(_pb.TailHttpTrafficResponse, _j))


def get_machine_request(
) -> _pb.GetMachineRequest:
    _w = _pb.GetMachineRequest()
    return _rt.checked(_w)


def run_machine_action_request(
    *,
    add_ssh_key: _t.SshKey | None,
    remove_ssh_key_fingerprint: str | None,
    restart_machine: _t.RestartMachineAction | None,
    cancel_restart: bool | None,
    end_session_id: str | None,
) -> _pb.RunMachineActionRequest:
    _rt.one_of("run_machine_action", add_ssh_key=add_ssh_key, remove_ssh_key_fingerprint=remove_ssh_key_fingerprint, restart_machine=restart_machine, cancel_restart=cancel_restart, end_session_id=end_session_id)
    _w = _pb.RunMachineActionRequest()
    if add_ssh_key is not None:
        _w.action = _Oneof[_Literal["add_ssh_key"], _pb.SshKey]("add_ssh_key", ssh_key_to_wire(add_ssh_key))
    elif remove_ssh_key_fingerprint is not None:
        _w.action = _Oneof[_Literal["remove_ssh_key_fingerprint"], str]("remove_ssh_key_fingerprint", remove_ssh_key_fingerprint)
    elif restart_machine is not None:
        _w.action = _Oneof[_Literal["restart_machine"], _pb.RestartMachineAction]("restart_machine", restart_machine_action_to_wire(restart_machine))
    elif cancel_restart is not None:
        _w.action = _Oneof[_Literal["cancel_restart"], bool]("cancel_restart", cancel_restart)
    elif end_session_id is not None:
        _w.action = _Oneof[_Literal["end_session_id"], str]("end_session_id", end_session_id)
    return _rt.checked(_w)


def get_project_request(
    *,
    project_id: str,
    include_secret_values: bool,
    snapshots_before: datetime | None,
    snapshots_volume: str,
) -> _pb.GetProjectRequest:
    _w = _pb.GetProjectRequest(
        project_id=project_id or None,
        include_secret_values=include_secret_values or None,
        snapshots_before=_rt.time_to_wire(snapshots_before) if snapshots_before is not None else None,
        snapshots_volume=snapshots_volume or None,
    )
    return _rt.checked(_w)


def create_project_request(
    *,
    project_id: str,
    source: _t.ProjectSource | None,
    upload_id: str,
    files: Sequence[_t.FileChange],
    x_pethost: _t.ProjectExtension | None,
    timeout_seconds: int,
    operation_id: str,
    wait_seconds: int | None,
) -> _pb.CreateProjectRequest:
    _w = _pb.CreateProjectRequest(
        project_id=project_id or None,
        source=project_source_to_wire(source) if source is not None else None,
        upload_id=upload_id or None,
        files=[file_change_to_wire(_x) for _x in files],
        x_pethost=project_extension_to_wire(x_pethost) if x_pethost is not None else None,
        timeout_seconds=timeout_seconds or None,
        operation_id=operation_id or None,
        wait_seconds=wait_seconds,
    )
    return _rt.checked(_w)


def deploy_project_request(
    *,
    project_id: str,
    base_deploy_id: str,
    files: Sequence[_t.FileChange],
    x_pethost: _t.ProjectExtension | None,
    mount_volume: _t.MountVolume | None,
    timeout_seconds: int,
    operation_id: str,
    upload_id: str | None,
    commit: str | None,
    newest_commit: bool | None,
    rollback_deploy_id: str | None,
    wait_seconds: int | None,
) -> _pb.DeployProjectRequest:
    _rt.one_of("deploy_project", upload_id=upload_id, commit=commit, newest_commit=newest_commit, rollback_deploy_id=rollback_deploy_id)
    _w = _pb.DeployProjectRequest(
        project_id=project_id or None,
        base_deploy_id=base_deploy_id or None,
        files=[file_change_to_wire(_x) for _x in files],
        x_pethost=project_extension_to_wire(x_pethost) if x_pethost is not None else None,
        mount_volume=mount_volume_to_wire(mount_volume) if mount_volume is not None else None,
        timeout_seconds=timeout_seconds or None,
        operation_id=operation_id or None,
        wait_seconds=wait_seconds,
    )
    if upload_id is not None:
        _w.version = _Oneof[_Literal["upload_id"], str]("upload_id", upload_id)
    elif commit is not None:
        _w.version = _Oneof[_Literal["commit"], str]("commit", commit)
    elif newest_commit is not None:
        _w.version = _Oneof[_Literal["newest_commit"], bool]("newest_commit", newest_commit)
    elif rollback_deploy_id is not None:
        _w.version = _Oneof[_Literal["rollback_deploy_id"], str]("rollback_deploy_id", rollback_deploy_id)
    return _rt.checked(_w)


def list_commits_request(
    *,
    project_id: str,
    before_commit: str,
) -> _pb.ListCommitsRequest:
    _w = _pb.ListCommitsRequest(
        project_id=project_id or None,
        before_commit=before_commit or None,
    )
    return _rt.checked(_w)


def run_project_action_request(
    *,
    project_id: str,
    start_services: _t.ServicesAction | None,
    stop_services: _t.ServicesAction | None,
    restart_services: _t.ServicesAction | None,
    recreate_service: _t.RecreateServiceAction | None,
    back_up: _t.BackUpAction | None,
    restore_snapshot: _t.RestoreSnapshotAction | None,
    cancel_operation: _t.CancelOperationAction | None,
    delete_project: _t.DeleteProjectAction | None,
    set_source: _t.ProjectSource | None,
    delete_volume: str | None,
    operation_id: str,
    wait_seconds: int | None,
) -> _pb.RunProjectActionRequest:
    _rt.one_of("run_project_action", start_services=start_services, stop_services=stop_services, restart_services=restart_services, recreate_service=recreate_service, back_up=back_up, restore_snapshot=restore_snapshot, cancel_operation=cancel_operation, delete_project=delete_project, set_source=set_source, delete_volume=delete_volume)
    _w = _pb.RunProjectActionRequest(
        project_id=project_id or None,
        operation_id=operation_id or None,
        wait_seconds=wait_seconds,
    )
    if start_services is not None:
        _w.action = _Oneof[_Literal["start_services"], _pb.ServicesAction]("start_services", services_action_to_wire(start_services))
    elif stop_services is not None:
        _w.action = _Oneof[_Literal["stop_services"], _pb.ServicesAction]("stop_services", services_action_to_wire(stop_services))
    elif restart_services is not None:
        _w.action = _Oneof[_Literal["restart_services"], _pb.ServicesAction]("restart_services", services_action_to_wire(restart_services))
    elif recreate_service is not None:
        _w.action = _Oneof[_Literal["recreate_service"], _pb.RecreateServiceAction]("recreate_service", recreate_service_action_to_wire(recreate_service))
    elif back_up is not None:
        _w.action = _Oneof[_Literal["back_up"], _pb.BackUpAction]("back_up", back_up_action_to_wire(back_up))
    elif restore_snapshot is not None:
        _w.action = _Oneof[_Literal["restore_snapshot"], _pb.RestoreSnapshotAction]("restore_snapshot", restore_snapshot_action_to_wire(restore_snapshot))
    elif cancel_operation is not None:
        _w.action = _Oneof[_Literal["cancel_operation"], _pb.CancelOperationAction]("cancel_operation", cancel_operation_action_to_wire(cancel_operation))
    elif delete_project is not None:
        _w.action = _Oneof[_Literal["delete_project"], _pb.DeleteProjectAction]("delete_project", delete_project_action_to_wire(delete_project))
    elif set_source is not None:
        _w.action = _Oneof[_Literal["set_source"], _pb.ProjectSource]("set_source", project_source_to_wire(set_source))
    elif delete_volume is not None:
        _w.action = _Oneof[_Literal["delete_volume"], str]("delete_volume", delete_volume)
    return _rt.checked(_w)


def get_operation_request(
    *,
    project_id: str,
    operation_id: str,
    wait_seconds: int | None,
    after_log_line: int | None,
    log_line_limit: int | None,
) -> _pb.GetOperationRequest:
    _w = _pb.GetOperationRequest(
        project_id=project_id or None,
        operation_id=operation_id or None,
        wait_seconds=wait_seconds,
        after_log_line=after_log_line,
        log_line_limit=log_line_limit,
    )
    return _rt.checked(_w)


def query_http_traffic_request(
    *,
    project_id: str,
    filter: _t.HttpTrafficFilter | None,
    start_time: datetime | None,
    end_time: datetime | None,
    last_seconds: int,
    bucket_width_seconds: int,
    request_limit: int,
    page_token: str,
) -> _pb.QueryHttpTrafficRequest:
    _w = _pb.QueryHttpTrafficRequest(
        project_id=project_id or None,
        filter=http_traffic_filter_to_wire(filter) if filter is not None else None,
        start_time=_rt.time_to_wire(start_time) if start_time is not None else None,
        end_time=_rt.time_to_wire(end_time) if end_time is not None else None,
        last_seconds=last_seconds or None,
        bucket_width_seconds=bucket_width_seconds or None,
        request_limit=request_limit or None,
        page_token=page_token or None,
    )
    return _rt.checked(_w)


def query_container_logs_request(
    *,
    project_id: str,
    filter: _t.ContainerLogFilter | None,
    start_time: datetime | None,
    end_time: datetime | None,
    last_seconds: int,
    limit: int,
    from_start: bool,
    page_token: str,
) -> _pb.QueryContainerLogsRequest:
    _w = _pb.QueryContainerLogsRequest(
        project_id=project_id or None,
        filter=container_log_filter_to_wire(filter) if filter is not None else None,
        start_time=_rt.time_to_wire(start_time) if start_time is not None else None,
        end_time=_rt.time_to_wire(end_time) if end_time is not None else None,
        last_seconds=last_seconds or None,
        limit=limit or None,
        from_start=from_start or None,
        page_token=page_token or None,
    )
    return _rt.checked(_w)


def run_service_command_request(
    *,
    project_id: str,
    service: str,
    command: Sequence[str],
    stdin: str,
    run_as_user: str,
    working_directory: str,
    timeout_seconds: int,
) -> _pb.RunServiceCommandRequest:
    _w = _pb.RunServiceCommandRequest(
        project_id=project_id or None,
        service=service or None,
        command=_rt.strings("run_service_command(command=)", command),
        stdin=stdin or None,
        run_as_user=run_as_user or None,
        working_directory=working_directory or None,
        timeout_seconds=timeout_seconds or None,
    )
    return _rt.checked(_w)


def read_path_request(
    *,
    project_id: str,
    service: str | None,
    volume: str | None,
    path: str,
    entry_limit: int,
    offset_bytes: int,
    length_bytes: int,
    entry_page_token: str,
) -> _pb.ReadPathRequest:
    _rt.one_of("read_path", service=service, volume=volume)
    _w = _pb.ReadPathRequest(
        project_id=project_id or None,
        path=path or None,
        entry_limit=entry_limit or None,
        offset_bytes=offset_bytes or None,
        length_bytes=length_bytes or None,
        entry_page_token=entry_page_token or None,
    )
    if service is not None:
        _w.root = _Oneof[_Literal["service"], str]("service", service)
    elif volume is not None:
        _w.root = _Oneof[_Literal["volume"], str]("volume", volume)
    return _rt.checked(_w)


def create_transfer_request(
    *,
    upload_archive: _t.ArchiveUpload | None,
    upload_file: _t.FileUpload | None,
    download: _t.PathDownload | None,
) -> _pb.CreateTransferRequest:
    _rt.one_of("create_transfer", upload_archive=upload_archive, upload_file=upload_file, download=download)
    _w = _pb.CreateTransferRequest()
    if upload_archive is not None:
        _w.transfer = _Oneof[_Literal["upload_archive"], _pb.ArchiveUpload]("upload_archive", archive_upload_to_wire(upload_archive))
    elif upload_file is not None:
        _w.transfer = _Oneof[_Literal["upload_file"], _pb.FileUpload]("upload_file", file_upload_to_wire(upload_file))
    elif download is not None:
        _w.transfer = _Oneof[_Literal["download"], _pb.PathDownload]("download", path_download_to_wire(download))
    return _rt.checked(_w)


def watch_operation_request(
    *,
    project_id: str,
    operation_id: str,
) -> _pb.WatchOperationRequest:
    _w = _pb.WatchOperationRequest(
        project_id=project_id or None,
        operation_id=operation_id or None,
    )
    return _rt.checked(_w)


def tail_container_logs_request(
    *,
    project_id: str,
    filter: _t.ContainerLogFilter | None,
    after_cursor: str,
) -> _pb.TailContainerLogsRequest:
    _w = _pb.TailContainerLogsRequest(
        project_id=project_id or None,
        filter=container_log_filter_to_wire(filter) if filter is not None else None,
        after_cursor=after_cursor or None,
    )
    return _rt.checked(_w)


def tail_http_traffic_request(
    *,
    project_id: str,
    filter: _t.HttpTrafficFilter | None,
    after_sequence: int,
) -> _pb.TailHttpTrafficRequest:
    _w = _pb.TailHttpTrafficRequest(
        project_id=project_id or None,
        filter=http_traffic_filter_to_wire(filter) if filter is not None else None,
        after_sequence=after_sequence or None,
    )
    return _rt.checked(_w)


_ERRORS: dict[_Code, type[_errors.PethostError]] = {
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
            if _d.type_name == "pethost.panel.v1.ProjectBusy":
                _wProjectBusy = _d.value(_pb.ProjectBusy)
                if _wProjectBusy is not None:
                    return project_busy_from_wire(_wProjectBusy)
            if _d.type_name == "pethost.panel.v1.ProjectChanged":
                _wProjectChanged = _d.value(_pb.ProjectChanged)
                if _wProjectChanged is not None:
                    return project_changed_from_wire(_wProjectChanged)
            if _d.type_name == "pethost.panel.v1.MachineUnreachable":
                _wMachineUnreachable = _d.value(_pb.MachineUnreachable)
                if _wMachineUnreachable is not None:
                    return machine_unreachable_from_wire(_wMachineUnreachable)
            if _d.type_name == "pethost.panel.v1.NoMachine":
                _wNoMachine = _d.value(_pb.NoMachine)
                if _wNoMachine is not None:
                    return no_machine_from_wire(_wNoMachine)
        except ValueError:
            continue
    return None


def error_from_wire(_e: _ConnectError) -> _errors.PethostError:
    return _ERRORS.get(_e.code, _errors.UnknownError)(_e.message, _detail(_e))
