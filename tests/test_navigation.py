import unittest
from src import navigation

class TestNavigation(unittest.TestCase):

    def setUp(self):
        self.navigation = navigation.Navigation()

    def test_initializeProject(self):
        result = self.navigation.initializeProject("Test Project", "High-level objectives")
        self.assertEqual(result, "Project initialized")

    def test_monitorAgentActivity(self):
        result = self.navigation.monitorAgentActivity("Test Project")
        self.assertEqual(result, "Monitoring agent activity")

    def test_provideFeedback(self):
        result = self.navigation.provideFeedback("Test Project", "Feedback")
        self.assertEqual(result, "Feedback provided")

    def test_reviewCode(self):
        result = self.navigation.reviewCode("Test Project")
        self.assertEqual(result, "Code reviewed")

    def test_manageAgents(self):
        result = self.navigation.manageAgents("Test Project")
        self.assertEqual(result, "Agents managed")

    def test_initiateChat(self):
        result = self.navigation.initiateChat("Test Project")
        self.assertEqual(result, "Chat initiated")

    def test_runTest(self):
        result = self.navigation.runTest("Test Project")
        self.assertEqual(result, "Test run")

    def test_searchFeedback(self):
        result = self.navigation.searchFeedback("Test Project")
        self.assertEqual(result, "Feedback searched")

    def test_visualizeData(self):
        result = self.navigation.visualizeData("Test Project")
        self.assertEqual(result, "Data visualized")

    def test_integrateIDE(self):
        result = self.navigation.integrateIDE("Test Project")
        self.assertEqual(result, "IDE integrated")

    def test_interactWithAvatar(self):
        result = self.navigation.interactWithAvatar("Test Project")
        self.assertEqual(result, "Interacted with avatar")

if __name__ == '__main__':
    unittest.main()