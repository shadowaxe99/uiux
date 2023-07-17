class VisualCues:
    def __init__(self):
        self.agent_activities = []
        self.project_statuses = []
        self.code_outputs = []

    def update_agent_activity(self, agent_activity):
        self.agent_activities.append(agent_activity)

    def update_project_status(self, project_status):
        self.project_statuses.append(project_status)

    def update_code_output(self, code_output):
        self.code_outputs.append(code_output)