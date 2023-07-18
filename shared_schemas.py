from typing import NamedTuple


class AgentActivitySchema(NamedTuple):
    project_id: str
    agent_name: str
    activity: str
    timestamp: str