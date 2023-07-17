import unittest
from src import agent_management

class TestAgentManagement(unittest.TestCase):

    def setUp(self):
        self.agent_management = agent_management.AgentManagement()

    def test_configure_agents(self):
        self.agent_management.configure_agents("Agent1", "Project1")
        self.assertEqual(self.agent_management.agentConfig["Agent1"], "Project1")

    def test_pause_agent(self):
        self.agent_management.pause_agent("Agent1")
        self.assertEqual(self.agent_management.agentConfig["Agent1"], "Paused")

    def test_resume_agent(self):
        self.agent_management.resume_agent("Agent1")
        self.assertEqual(self.agent_management.agentConfig["Agent1"], "Active")

if __name__ == '__main__':
    unittest.main()