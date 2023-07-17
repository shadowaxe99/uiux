import unittest
from src.visual_cues import VisualCues

class TestVisualCues(unittest.TestCase):

    def setUp(self):
        self.visual_cues = VisualCues()

    def test_visual_cues_for_agent_activity(self):
        agent_activity = {"agent": "Clippy", "activity": "code generation", "timestamp": "2022-01-01T00:00:00Z"}
        self.visual_cues.update_agent_activity(agent_activity)
        self.assertEqual(self.visual_cues.agent_activities[-1], agent_activity)

    def test_visual_cues_for_project_status(self):
        project_status = {"project": "Project 1", "status": "In Progress"}
        self.visual_cues.update_project_status(project_status)
        self.assertEqual(self.visual_cues.project_statuses[-1], project_status)

    def test_visual_cues_for_code_output(self):
        code_output = {"project": "Project 1", "code": "print('Hello, World!')", "timestamp": "2022-01-01T00:00:00Z"}
        self.visual_cues.update_code_output(code_output)
        self.assertEqual(self.visual_cues.code_outputs[-1], code_output)

if __name__ == '__main__':
    unittest.main()