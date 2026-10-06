"""Between the public types and the wire layer: the type checker holds every line here against
both. Generated from v1/panel.proto: do not edit."""

from __future__ import annotations

from collections.abc import Sequence
from datetime import datetime
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


def project_problem_kind_from_wire(_w: _pb.ProjectProblemKind) -> _t.ProjectProblemKind:
    return _t.ProjectProblemKind(_w.value)


def services_action_kind_from_wire(_w: _pb.ServicesActionKind) -> _t.ServicesActionKind:
    return _t.ServicesActionKind(_w.value)


def service_state_from_wire(_w: _pb.ServiceState) -> _t.ServiceState:
    return _t.ServiceState(_w.value)


def restart_policy_from_wire(_w: _pb.RestartPolicy) -> _t.RestartPolicy:
    return _t.RestartPolicy(_w.value)


def health_status_from_wire(_w: _pb.HealthStatus) -> _t.HealthStatus:
    return _t.HealthStatus(_w.value)


def certificate_source_from_wire(_w: _pb.CertificateSource) -> _t.CertificateSource:
    return _t.CertificateSource(_w.value)


def operation_kind_from_wire(_w: _pb.OperationKind) -> _t.OperationKind:
    return _t.OperationKind(_w.value)


def operation_status_from_wire(_w: _pb.OperationStatus) -> _t.OperationStatus:
    return _t.OperationStatus(_w.value)


def deploy_failure_reason_from_wire(_w: _pb.DeployFailureReason) -> _t.DeployFailureReason:
    return _t.DeployFailureReason(_w.value)


def output_stream_from_wire(_w: _pb.OutputStream) -> _t.OutputStream:
    return _t.OutputStream(_w.value)


def output_stream_to_wire(_v: _t.OutputStream) -> _pb.OutputStream:
    return _pb.OutputStream(_v.value)


def file_type_from_wire(_w: _pb.FileType) -> _t.FileType:
    return _t.FileType(_w.value)


def file_location_from_wire(_w: _pb.FileLocation) -> _t.FileLocation:
    return _t.FileLocation(_w.value)


def no_machine_reason_from_wire(_w: _pb.NoMachineReason) -> _t.NoMachineReason:
    return _t.NoMachineReason(_w.value)


def get_machine_response_from_wire(_w: _pb.GetMachineResponse) -> _t.GetMachineResponse:
    return _t.GetMachineResponse(
        machine=machine_from_wire(_w.machine) if _w.machine is not None else None,
        projects=tuple(project_summary_from_wire(_x) for _x in _w.projects),
        deleted_projects=tuple(deleted_project_from_wire(_x) for _x in _w.deleted_projects),
        github=github_connection_from_wire(_w.github) if _w.github is not None else None,
    )


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


def github_connection_from_wire(_w: _pb.GithubConnection) -> _t.GithubConnection:
    return _t.GithubConnection(
        app_name=_w.app_name,
        install_url=_w.install_url,
        repositories=tuple(github_repository_from_wire(_x) for _x in _w.repositories),
        repository_count=_w.repository_count,
        webhooks_enabled=_w.webhooks_enabled,
    )


def github_repository_from_wire(_w: _pb.GithubRepository) -> _t.GithubRepository:
    return _t.GithubRepository(
        repository=_w.repository,
        default_branch=_w.default_branch,
        private=_w.private,
        push_time=_rt.time_from_wire(_w.push_time) if _w.push_time is not None else None,
    )


def deleted_project_from_wire(_w: _pb.DeletedProject) -> _t.DeletedProject:
    return _t.DeletedProject(
        project_id=_w.project_id,
        newest_snapshot=snapshot_from_wire(_w.newest_snapshot) if _w.newest_snapshot is not None else None,
        snapshot_count=_w.snapshot_count,
    )


def restart_machine_action_to_wire(_v: _t.RestartMachineAction) -> _pb.RestartMachineAction:
    return _pb.RestartMachineAction(
        restart_time=_rt.time_to_wire(_v.restart_time) if _v.restart_time is not None else None,
        at_maintenance_window=_v.at_maintenance_window or None,
        interrupt_operations=_v.interrupt_operations or None,
    )


def run_machine_action_response_from_wire(_w: _pb.RunMachineActionResponse) -> _t.RunMachineActionResponse:
    return _t.RunMachineActionResponse(
        machine=machine_from_wire(_w.machine) if _w.machine is not None else None,
    )


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


def service_summary_from_wire(_w: _pb.ServiceSummary) -> _t.ServiceSummary:
    return _t.ServiceSummary(
        service=_w.service,
        state=service_state_from_wire(_w.state),
    )


def project_problem_from_wire(_w: _pb.ProjectProblem) -> _t.ProjectProblem:
    return _t.ProjectProblem(
        kind=project_problem_kind_from_wire(_w.kind),
        service=_w.service,
        operation_id=_w.operation_id,
        since_time=_rt.time_from_wire(_w.since_time) if _w.since_time is not None else None,
        problem_message=_w.problem_message,
    )


def get_project_response_from_wire(_w: _pb.GetProjectResponse) -> _t.GetProjectResponse:
    return _t.GetProjectResponse(
        project=project_from_wire(_w.project) if _w.project is not None else None,
    )


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


def running_services_action_from_wire(_w: _pb.RunningServicesAction) -> _t.RunningServicesAction:
    return _t.RunningServicesAction(
        kind=services_action_kind_from_wire(_w.kind),
        services=tuple(_w.services),
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
    )


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


def published_port_from_wire(_w: _pb.PublishedPort) -> _t.PublishedPort:
    return _t.PublishedPort(
        machine_port=_w.machine_port,
        container_port=_w.container_port,
        protocol=_w.protocol,
        machine_only=_w.machine_only,
    )


def volume_mount_from_wire(_w: _pb.VolumeMount) -> _t.VolumeMount:
    return _t.VolumeMount(
        volume=_w.volume,
        container_path=_w.container_path,
    )


def health_check_from_wire(_w: _pb.HealthCheck) -> _t.HealthCheck:
    return _t.HealthCheck(
        command=tuple(_w.command),
        interval_seconds=_w.interval_seconds,
        status=health_status_from_wire(_w.status),
        consecutive_failure_count=_w.consecutive_failure_count,
        recent_results_passed=tuple(_w.recent_results_passed),
        last_failure_output=_w.last_failure_output,
    )


def environment_variable_from_wire(_w: _pb.EnvironmentVariable) -> _t.EnvironmentVariable:
    return _t.EnvironmentVariable(
        name=_w.name,
        value=_w.value,
        secret=_w.secret,
        source_file=_w.source_file,
        from_env_file_variables=tuple(_w.from_env_file_variables),
        value_left_out=_w.value_left_out,
    )


def volume_from_wire(_w: _pb.Volume) -> _t.Volume:
    return _t.Volume(
        volume=_w.volume,
        size_bytes=_w.size_bytes,
        mounted_by=tuple(volume_mounted_by_from_wire(_x) for _x in _w.mounted_by),
        last_backup_time=_rt.time_from_wire(_w.last_backup_time) if _w.last_backup_time is not None else None,
        snapshot_count=_w.snapshot_count,
        declared=_w.declared,
    )


def volume_mounted_by_from_wire(_w: _pb.VolumeMountedBy) -> _t.VolumeMountedBy:
    return _t.VolumeMountedBy(
        service=_w.service,
        container_path=_w.container_path,
    )


def host_from_wire(_w: _pb.Host) -> _t.Host:
    return _t.Host(
        host=_w.host,
        url=_w.url,
        certificate_source=certificate_source_from_wire(_w.certificate_source),
        certificate_expire_time=_rt.time_from_wire(_w.certificate_expire_time) if _w.certificate_expire_time is not None else None,
        unavailable_message=_w.unavailable_message,
    )


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


def snapshot_from_wire(_w: _pb.Snapshot) -> _t.Snapshot:
    return _t.Snapshot(
        snapshot_id=_w.snapshot_id,
        create_time=_rt.time_from_wire(_w.create_time) if _w.create_time is not None else None,
        size_bytes=_w.size_bytes,
        volumes=tuple(_w.volumes),
    )


def http_traffic_summary_from_wire(_w: _pb.HttpTrafficSummary) -> _t.HttpTrafficSummary:
    return _t.HttpTrafficSummary(
        request_count=_w.request_count,
        server_error_count=_w.server_error_count,
        latency_p50_ms=_w.latency_p50_ms,
        latency_p95_ms=_w.latency_p95_ms,
    )


def create_project_response_from_wire(_w: _pb.CreateProjectResponse) -> _t.CreateProjectResponse:
    return _t.CreateProjectResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        violations=tuple(spec_violation_from_wire(_x) for _x in _w.violations),
        adjustments=tuple(_w.adjustments),
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
    )


def mount_volume_to_wire(_v: _t.MountVolume) -> _pb.MountVolume:
    return _pb.MountVolume(
        service=_v.service or None,
        volume=_v.volume or None,
        container_path=_v.container_path or None,
    )


def project_extension_to_wire(_v: _t.ProjectExtension) -> _pb.ProjectExtension:
    return _pb.ProjectExtension(
        metadata=project_metadata_to_wire(_v.metadata) if _v.metadata is not None else None,
        routes=[route_to_wire(_x) for _x in _v.routes],
        remove_routes=_v.remove_routes or None,
        password=_v.password or None,
        remove_password=_v.remove_password or None,
    )


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


def deploy_project_response_from_wire(_w: _pb.DeployProjectResponse) -> _t.DeployProjectResponse:
    return _t.DeployProjectResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        violations=tuple(spec_violation_from_wire(_x) for _x in _w.violations),
        adjustments=tuple(_w.adjustments),
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
    )


def spec_violation_from_wire(_w: _pb.SpecViolation) -> _t.SpecViolation:
    return _t.SpecViolation(
        service=_w.service,
        location=_w.location,
        violation_message=_w.violation_message,
    )


def list_commits_response_from_wire(_w: _pb.ListCommitsResponse) -> _t.ListCommitsResponse:
    return _t.ListCommitsResponse(
        commits=tuple(branch_commit_from_wire(_x) for _x in _w.commits),
        more=_w.more,
    )


def branch_commit_from_wire(_w: _pb.BranchCommit) -> _t.BranchCommit:
    return _t.BranchCommit(
        commit=github_commit_from_wire(_w.commit) if _w.commit is not None else None,
        author=_w.author,
        commit_time=_rt.time_from_wire(_w.commit_time) if _w.commit_time is not None else None,
        deployed=_w.deployed,
        last_deploy=operation_from_wire(_w.last_deploy) if _w.last_deploy is not None else None,
        newest=_w.newest,
    )


def services_action_to_wire(_v: _t.ServicesAction) -> _pb.ServicesAction:
    return _pb.ServicesAction(
        services=_rt.strings("ServicesAction.services", _v.services),
    )


def recreate_service_action_to_wire(_v: _t.RecreateServiceAction) -> _pb.RecreateServiceAction:
    return _pb.RecreateServiceAction(
        service=_v.service or None,
        pull_latest_image=_v.pull_latest_image or None,
    )


def back_up_action_to_wire(_v: _t.BackUpAction) -> _pb.BackUpAction:
    return _pb.BackUpAction()


def restore_snapshot_action_to_wire(_v: _t.RestoreSnapshotAction) -> _pb.RestoreSnapshotAction:
    return _pb.RestoreSnapshotAction(
        snapshot_id=_v.snapshot_id or None,
        volumes=_rt.strings("RestoreSnapshotAction.volumes", _v.volumes),
    )


def cancel_operation_action_to_wire(_v: _t.CancelOperationAction) -> _pb.CancelOperationAction:
    return _pb.CancelOperationAction(
        operation_id=_v.operation_id or None,
    )


def delete_project_action_to_wire(_v: _t.DeleteProjectAction) -> _pb.DeleteProjectAction:
    return _pb.DeleteProjectAction(
        skip_final_backup=_v.skip_final_backup or None,
    )


def run_project_action_response_from_wire(_w: _pb.RunProjectActionResponse) -> _t.RunProjectActionResponse:
    return _t.RunProjectActionResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
    )


def get_operation_response_from_wire(_w: _pb.GetOperationResponse) -> _t.GetOperationResponse:
    return _t.GetOperationResponse(
        operation=operation_from_wire(_w.operation) if _w.operation is not None else None,
        project=project_from_wire(_w.project) if _w.project is not None else None,
        log=tuple(operation_log_line_from_wire(_x) for _x in _w.log),
        log_line_count=_w.log_line_count,
        next_after_log_line=_w.next_after_log_line,
    )


def operation_log_line_from_wire(_w: _pb.OperationLogLine) -> _t.OperationLogLine:
    return _t.OperationLogLine(
        time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
        text=_w.text,
    )


def http_traffic_filter_to_wire(_v: _t.HttpTrafficFilter) -> _pb.HttpTrafficFilter:
    return _pb.HttpTrafficFilter(
        host=_v.host or None,
        method=_v.method or None,
        path_contains=_v.path_contains or None,
        path_pattern=_v.path_pattern or None,
        status_class=_v.status_class or None,
    )


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


def http_traffic_bucket_from_wire(_w: _pb.HttpTrafficBucket) -> _t.HttpTrafficBucket:
    return _t.HttpTrafficBucket(
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        summary=http_traffic_summary_from_wire(_w.summary) if _w.summary is not None else None,
    )


def http_path_traffic_from_wire(_w: _pb.HttpPathTraffic) -> _t.HttpPathTraffic:
    return _t.HttpPathTraffic(
        method=_w.method,
        path_pattern=_w.path_pattern,
        summary=http_traffic_summary_from_wire(_w.summary) if _w.summary is not None else None,
    )


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


def container_log_filter_to_wire(_v: _t.ContainerLogFilter) -> _pb.ContainerLogFilter:
    return _pb.ContainerLogFilter(
        service=_v.service or None,
        stream=output_stream_to_wire(_v.stream) if _v.stream.value else None,
        text_contains=_v.text_contains or None,
    )


def query_container_logs_response_from_wire(_w: _pb.QueryContainerLogsResponse) -> _t.QueryContainerLogsResponse:
    return _t.QueryContainerLogsResponse(
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
        end_time=_rt.time_from_wire(_w.end_time) if _w.end_time is not None else None,
        oldest_kept_time=_rt.time_from_wire(_w.oldest_kept_time) if _w.oldest_kept_time is not None else None,
        lines=tuple(log_line_from_wire(_x) for _x in _w.lines),
        next_page_token=_w.next_page_token,
        tail_cursor=_w.tail_cursor,
    )


def log_line_from_wire(_w: _pb.LogLine) -> _t.LogLine:
    return _t.LogLine(
        time=_rt.time_from_wire(_w.time) if _w.time is not None else None,
        service=_w.service,
        stream=output_stream_from_wire(_w.stream),
        text=_w.text,
    )


def run_service_command_response_from_wire(_w: _pb.RunServiceCommandResponse) -> _t.RunServiceCommandResponse:
    return _t.RunServiceCommandResponse(
        exit_code=_w.exit_code,
        timed_out=_w.timed_out,
        stdout=_w.stdout,
        stderr=_w.stderr,
        output_truncated=_w.output_truncated,
    )


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


def archive_upload_to_wire(_v: _t.ArchiveUpload) -> _pb.ArchiveUpload:
    return _pb.ArchiveUpload(
        file_name=_v.file_name or None,
    )


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


def create_transfer_response_from_wire(_w: _pb.CreateTransferResponse) -> _t.CreateTransferResponse:
    return _t.CreateTransferResponse(
        url=_w.url,
        http_method=_w.http_method,
        expire_time=_rt.time_from_wire(_w.expire_time) if _w.expire_time is not None else None,
        command=_w.command,
        upload_id=_w.upload_id,
        replaces=_w.replaces,
        file_name=_w.file_name,
    )


def project_busy_from_wire(_w: _pb.ProjectBusy) -> _t.ProjectBusy:
    return _t.ProjectBusy(
        operation_id=_w.operation_id,
        kind=operation_kind_from_wire(_w.kind),
        start_time=_rt.time_from_wire(_w.start_time) if _w.start_time is not None else None,
    )


def project_changed_from_wire(_w: _pb.ProjectChanged) -> _t.ProjectChanged:
    return _t.ProjectChanged()


def machine_unreachable_from_wire(_w: _pb.MachineUnreachable) -> _t.MachineUnreachable:
    return _t.MachineUnreachable()


def no_machine_from_wire(_w: _pb.NoMachine) -> _t.NoMachine:
    return _t.NoMachine(
        reason=no_machine_reason_from_wire(_w.reason),
        url=_w.url,
    )


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
