"""What the checks need of v1/panel.proto that neither layer says: which RPC a method calls,
which fields are marked (optional), which messages an error carries, and what a request names its
workspace by, which a client made with one fills. Generated with the package:
do not edit."""

import pethost._wire.v1.panel_pb as wire

METHODS = {
    "list_workspaces": "ListWorkspaces",
    "get_machine": "GetMachine",
    "run_machine_action": "RunMachineAction",
    "get_project": "GetProject",
    "create_project": "CreateProject",
    "deploy_project": "DeployProject",
    "move_project": "MoveProject",
    "list_commits": "ListCommits",
    "run_project_action": "RunProjectAction",
    "set_project_alerts": "SetProjectAlerts",
    "get_operation": "GetOperation",
    "query_http_traffic": "QueryHttpTraffic",
    "query_container_logs": "QueryContainerLogs",
    "create_database": "CreateDatabase",
    "link_database": "LinkDatabase",
    "run_service_command": "RunServiceCommand",
    "read_path": "ReadPath",
    "create_transfer": "CreateTransfer",
    "watch_operation": "WatchOperation",
    "tail_container_logs": "TailContainerLogs",
    "tail_http_traffic": "TailHttpTraffic",
}

OPTIONAL = frozenset({
    "Workspace.memory_free_bytes",
    "Workspace.disk_free_bytes",
    "Workspace.project_count",
    "DiskUsage.build_cache_bytes",
    "ProjectMetadata.name",
    "ProjectMetadata.emoji",
    "ProjectMetadata.description",
    "ProjectMetadata.notes",
    "GithubSource.repository",
    "GithubSource.branch",
    "GithubSource.directory",
    "GithubSource.auto_deploy",
    "Service.exit_code",
    "CreateProjectRequest.wait_seconds",
    "DeployProjectRequest.wait_seconds",
    "MoveProjectRequest.wait_seconds",
    "RunProjectActionRequest.wait_seconds",
    "CreateDatabaseRequest.wait_seconds",
    "SetProjectAlertsRequest.off",
    "SetProjectAlertsRequest.mute_minutes",
    "ProjectAlerts.uptime_percent",
    "UptimeDay.uptime_percent",
    "GetOperationRequest.wait_seconds",
    "GetOperationRequest.after_log_line",
    "GetOperationRequest.log_line_limit",
})

DETAILS = (
    "ProjectBusy",
    "ProjectChanged",
    "MachineUnreachable",
    "DatabaseLinkRefusal",
    "DatabaseSizeRefusal",
    "NoMachine",
    "PaymentOverdue",
    "WorkspaceChoice",
    "WorkspaceNotGranted",
    "ProjectMoved",
)

WORKSPACE = "workspace"

__all__ = ["DETAILS", "METHODS", "OPTIONAL", "WORKSPACE", "wire"]
