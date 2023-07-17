import unittest
from src import main

class TestMain(unittest.TestCase):

    def setUp(self):
        self.main = main.Main()

    def test_initialize_project(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.assertIn("Test Project", self.main.activeProjects)

    def test_monitor_agent_activity(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.monitor_agent_activity("Test Project")
        self.assertIsNotNone(self.main.agentActivities["Test Project"])

    def test_provide_feedback(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.provide_feedback("Test Project", "Great job!")
        self.assertIn("Great job!", self.main.projectFeedback["Test Project"])

    def test_review_code(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.review_code("Test Project")
        self.assertIsNotNone(self.main.generatedCode["Test Project"])

    def test_manage_agents(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.manage_agents("Test Project", "Pause")
        self.assertEqual(self.main.agentConfig["Test Project"], "Pause")

    def test_initiate_chat(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.initiate_chat("Test Project", "Hello Clippy!")
        self.assertIn("Hello Clippy!", self.main.projectChat["Test Project"])

    def test_run_test(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.run_test("Test Project")
        self.assertIsNotNone(self.main.testOutputs["Test Project"])

    def test_search_feedback(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.provide_feedback("Test Project", "Great job!")
        self.main.search_feedback("Great job!")
        self.assertIn("Test Project", self.main.searchResults)

    def test_visualize_data(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.visualize_data("Test Project")
        self.assertIsNotNone(self.main.agentUsageData["Test Project"])

    def test_integrate_ide(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.integrate_ide("Test Project", "VSCode")
        self.assertIn("VSCode", self.main.ideIntegrations["Test Project"])

    def test_interact_with_avatar(self):
        self.main.initialize_project("Test Project", "High-level objectives")
        self.main.interact_with_avatar("Test Project", "Hello Clippy!")
        self.assertIn("Hello Clippy!", self.main.clippyAvatar["Test Project"])

if __name__ == '__main__':
    unittest.main()