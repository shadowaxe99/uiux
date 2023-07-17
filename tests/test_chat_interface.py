import unittest
from src import chat_interface

class TestChatInterface(unittest.TestCase):

    def setUp(self):
        self.chat_interface = chat_interface.ChatInterface()

    def test_initialize_project(self):
        project_name = "Test Project"
        objectives = "Create a simple web app"
        self.chat_interface.initialize_project(project_name, objectives)
        self.assertIn(project_name, chat_interface.activeProjects)

    def test_provide_objectives(self):
        project_name = "Test Project"
        objectives = "Create a simple web app"
        self.chat_interface.provide_objectives(project_name, objectives)
        self.assertEqual(chat_interface.projectChat[project_name], objectives)

    def test_provide_guidance(self):
        project_name = "Test Project"
        guidance = "Use Python and Flask for the backend"
        self.chat_interface.provide_guidance(project_name, guidance)
        self.assertIn(guidance, chat_interface.projectChat[project_name])

    def test_chat_update(self):
        project_name = "Test Project"
        chat_update = "Added a new feature"
        self.chat_interface.chat_update(project_name, chat_update)
        self.assertIn(chat_update, chat_interface.projectChat[project_name])

if __name__ == '__main__':
    unittest.main()