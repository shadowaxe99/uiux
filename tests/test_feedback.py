import unittest
from src.feedback import Feedback

class TestFeedback(unittest.TestCase):

    def setUp(self):
        self.feedback = Feedback()

    def test_provide_feedback(self):
        self.feedback.provide_feedback("Project1", "Agent1", "Good job!")
        self.assertIn("Project1", self.feedback.projectFeedback)
        self.assertIn("Agent1", self.feedback.projectFeedback["Project1"])
        self.assertEqual("Good job!", self.feedback.projectFeedback["Project1"]["Agent1"])

    def test_tag_feedback(self):
        self.feedback.tag_feedback("Project1", "Agent1", "10:00 AM")
        self.assertIn("10:00 AM", self.feedback.projectFeedback["Project1"]["Agent1"])
        
    def test_search_feedback(self):
        self.feedback.provide_feedback("Project1", "Agent1", "Good job!")
        results = self.feedback.search_feedback("Good job!")
        self.assertIn("Project1", results)
        self.assertIn("Agent1", results["Project1"])

if __name__ == '__main__':
    unittest.main()