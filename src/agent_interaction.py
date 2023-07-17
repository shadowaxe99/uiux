from src import agent_management
from src import chat_interface

class AgentInteraction:
    def __init__(self):
        self.agent_management = agent_management.AgentManagement()
        self.chat_interface = chat_interface.ChatInterface()

    def initialize_project(self, project_name, objectives):
        self.agent_management.create_project(project_name, objectives)
        self.chat_interface.start_chat(project_name)

    def monitor_agent_activity(self, project_name):
        return self.agent_management.get_agent_activities(project_name)

    def provide_feedback(self, project_name, feedback):
        self.chat_interface.add_feedback(project_name, feedback)

    def review_code(self, project_name):
        return self.agent_management.get_generated_code(project_name)

    def manage_agents(self, project_name, action):
        if action == 'pause':
            self.agent_management.pause_agents(project_name)
        elif action == 'resume':
            self.agent_management.resume_agents(project_name)

    def initiate_chat(self, project_name):
        self.chat_interface.start_chat(project_name)

    def run_test(self, project_name):
        return self.agent_management.run_tests(project_name)

    def search_feedback(self, search_query):
        return self.chat_interface.search_feedback(search_query)

    def visualize_data(self):
        return self.agent_management.get_agent_usage_data()

    def integrate_ide(self, ide_name):
        return self.agent_management.integrate_ide(ide_name)

    def interact_with_avatar(self, action):
        return self.agent_management.interact_with_avatar(action)