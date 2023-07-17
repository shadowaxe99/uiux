class ProjectDashboard:
    def __init__(self):
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def display(self):
        for project in self.projects:
            print(project)