import unittest
from src.testing_interface import TestingInterface

class TestTestingInterface(unittest.TestCase):

    def setUp(self):
        self.testing_interface = TestingInterface()

    def test_run_test(self):
        code = "print('Hello, World!')"
        expected_output = "Hello, World!\n"
        self.assertEqual(self.testing_interface.run_test(code), expected_output)

    def test_update_test_outputs(self):
        test_output = "Test passed"
        self.testing_interface.update_test_outputs(test_output)
        self.assertEqual(self.testing_interface.testOutputs[-1], test_output)

    def test_get_test_outputs(self):
        test_output = "Test failed"
        self.testing_interface.update_test_outputs(test_output)
        self.assertEqual(self.testing_interface.get_test_outputs()[-1], test_output)

if __name__ == '__main__':
    unittest.main()