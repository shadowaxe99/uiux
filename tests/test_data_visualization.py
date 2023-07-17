import unittest
from src import data_visualization

class TestDataVisualization(unittest.TestCase):

    def setUp(self):
        self.data_visualization = data_visualization.DataVisualization()

    def test_visualize_data(self):
        agent_usage_data = {
            "agent1": {"usage": 100, "performance": 95},
            "agent2": {"usage": 80, "performance": 90},
            "agent3": {"usage": 120, "performance": 85},
        }
        self.data_visualization.visualize_data(agent_usage_data)
        self.assertTrue(self.data_visualization.data_visualized)

    def test_update_agent_usage_data(self):
        new_data = {"agent4": {"usage": 60, "performance": 92}}
        self.data_visualization.update_agent_usage_data(new_data)
        self.assertIn("agent4", self.data_visualization.agent_usage_data)

    def test_get_agent_usage_data(self):
        agent_usage_data = self.data_visualization.get_agent_usage_data()
        self.assertIsInstance(agent_usage_data, dict)

if __name__ == '__main__':
    unittest.main()