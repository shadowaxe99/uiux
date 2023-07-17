import unittest
from src import mobile_support

class TestMobileSupport(unittest.TestCase):

    def setUp(self):
        self.mobile_support = mobile_support.MobileSupport()

    def test_responsive_ui(self):
        self.assertTrue(self.mobile_support.check_responsive_ui())

    def test_navigation(self):
        self.assertTrue(self.mobile_support.check_navigation())

    def test_unified_interface(self):
        self.assertTrue(self.mobile_support.check_unified_interface())

    def test_visual_cues(self):
        self.assertTrue(self.mobile_support.check_visual_cues())

if __name__ == '__main__':
    unittest.main()