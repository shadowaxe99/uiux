import unittest
from src import timeline

class TestTimeline(unittest.TestCase):

    def setUp(self):
        self.timeline = timeline.Timeline()
        self.project_id = "test_project"
        self.agent_id = "test_agent"
        self.timestamp = "2022-01-01 00:00:00"

    def test_add_activity(self):
        self.timeline.add_activity(self.project_id, self.agent_id, self.timestamp)
        self.assertIn(self.project_id, self.timeline.agentActivities)
        self.assertIn(self.agent_id, self.timeline.agentActivities[self.project_id])
        self.assertIn(self.timestamp, self.timeline.agentActivities[self.project_id][self.agent_id])

    def test_get_project_activities(self):
        self.timeline.add_activity(self.project_id, self.agent_id, self.timestamp)
        activities = self.timeline.get_project_activities(self.project_id)
        self.assertEqual(len(activities), 1)
        self.assertEqual(activities[0]['agent_id'], self.agent_id)
        self.assertEqual(activities[0]['timestamp'], self.timestamp)

    def test_get_agent_activities(self):
        self.timeline.add_activity(self.project_id, self.agent_id, self.timestamp)
        activities = self.timeline.get_agent_activities(self.agent_id)
        self.assertEqual(len(activities), 1)
        self.assertEqual(activities[0]['project_id'], self.project_id)
        self.assertEqual(activities[0]['timestamp'], self.timestamp)

if __name__ == '__main__':
    unittest.main()