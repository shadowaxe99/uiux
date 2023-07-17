import unittest
from src import integrations

class TestIntegrations(unittest.TestCase):

    def setUp(self):
        self.ideIntegrations = integrations.ideIntegrations

    def test_ide_integration_exists(self):
        self.assertIsNotNone(self.ideIntegrations)

    def test_vscode_integration(self):
        self.assertIn('VSCode', self.ideIntegrations)

    def test_integration_update(self):
        old_integrations = self.ideIntegrations.copy()
        integrations.integrateIDE('PyCharm')
        self.assertNotEqual(old_integrations, self.ideIntegrations)

    def test_integration_removal(self):
        integrations.integrateIDE('PyCharm')
        old_integrations = self.ideIntegrations.copy()
        integrations.removeIDE('PyCharm')
        self.assertNotEqual(old_integrations, self.ideIntegrations)

if __name__ == '__main__':
    unittest.main()