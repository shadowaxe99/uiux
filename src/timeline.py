```python
import datetime
from typing import List, Dict

# Import shared schemas
from shared_schemas import AgentActivitySchema

# Import shared variables
from shared_variables import agentActivities

def get_project_timeline(project_id: str) -> List[Dict[str, str]]:
    """
    Function to get the timeline of agent activities for a specific project.
    """
    project_timeline = []
    for activity in agentActivities:
        if activity['project_id'] == project_id:
            project_timeline.append(activity)
    return project_timeline

def display_project_timeline(project_id: str):
    """
    Function to display the timeline of agent activities for a specific project.
    """
    project_timeline = get_project_timeline(project_id)
    for activity in project_timeline:
        print(f"Agent: {activity['agent_name']}, Activity: {activity['activity']}, Time: {activity['timestamp']}")

def add_agent_activity(project_id: str, agent_name: str, activity: str):
    """
    Function to add an agent activity to the timeline.
    """
    new_activity = AgentActivitySchema(project_id=project_id, agent_name=agent_name, activity=activity, timestamp=datetime.datetime.now())
    agentActivities.append(new_activity)
```
