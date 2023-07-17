import unittest
from src import design_guidelines

class TestDesignGuidelines(unittest.TestCase):

    def setUp(self):
        self.design_guidelines = design_guidelines.DesignGuidelines()

    def test_simple_intuitive_ui(self):
        result = self.design_guidelines.is_ui_simple_and_intuitive()
        self.assertTrue(result, "UI is not simple and intuitive")

    def test_responsive_ui(self):
        result = self.design_guidelines.is_ui_responsive()
        self.assertTrue(result, "UI is not responsive")

    def test_easy_navigation(self):
        result = self.design_guidelines.is_navigation_easy()
        self.assertTrue(result, "Navigation is not easy")

    def test_unified_interface(self):
        result = self.design_guidelines.is_interface_unified()
        self.assertTrue(result, "Interface is not unified")

    def test_visual_cues(self):
        result = self.design_guidelines.are_visual_cues_present()
        self.assertTrue(result, "Visual cues are not present")

if __name__ == '__main__':
    unittest.main()