import unittest
from src import dashboard

class TestDashboard(unittest.TestCase):

    def setUp(self):
        self.dashboard = dashboard.Dashboard()

    def test_active_projects(self):
        self.assertIsInstance(self.dashboard.activeProjects, list)

    def test_project_status(self):
        for project in self.dashboard.activeProjects:
            self.assertIn(project.status, ["in progress", "completed"])

    def test_project_dashboard(self):
        dashboard_content = self.dashboard.display_dashboard()
        self.assertIsInstance(dashboard_content, str)

    def test_project_name_in_dashboard(self):
        dashboard_content = self.dashboard.display_dashboard()
        for project in self.dashboard.activeProjects:
            self.assertIn(project.name, dashboard_content)

    def test_project_objectives_in_dashboard(self):
        dashboard_content = self.dashboard.display_dashboard()
        for project in self.dashboard.activeProjects:
            self.assertIn(project.objectives, dashboard_content)

    def test_project_status_in_dashboard(self):
        dashboard_content = self.dashboard.display_dashboard()
        for project in self.dashboard.activeProjects:
            self.assertIn(project.status, dashboard_content)

if __name__ == '__main__':
    unittest.main()