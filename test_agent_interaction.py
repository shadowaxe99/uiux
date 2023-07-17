import unittest
from src.agent_interaction import AgentInteraction

class TestAgentInteraction(unittest.TestCase):

    def setUp(self):
        self.agent_interaction = AgentInteraction()

    def test_initialize_project(self):
        self.agent_interaction.initialize_project('Test Project', 'Objectives')

    def test_monitor_agent_activity(self):
        self.agent_interaction.monitor_agent_activity('Test Project')

    def test_provide_feedback(self):
        self.agent_interaction.provide_feedback('Test Project', 'Feedback')

    def test_review_code(self):
        self.agent_interaction.review_code('Test Project')

    def test_manage_agents(self):
        self.agent_interaction.manage_agents('Test Project', 'pause')
        self.agent_interaction.manage_agents('Test Project', 'resume')

    def test_initiate_chat(self):
        self.agent_interaction.initiate_chat('Test Project')

    def test_run_test(self):
        self.agent_interaction.run_test('Test Project')

    def test_search_feedback(self):
        self.agent_interaction.search_feedback('Feedback')

    def test_visualize_data(self):
        self.agent_interaction.visualize_data()

    def test_integrate_ide(self):
        self.agent_interaction.integrate_ide('VSCode')

    def test_interact_with_avatar(self):
        self.agent_interaction.interact_with_avatar('wave')

if __name__ == '__main__':
    unittest.main()