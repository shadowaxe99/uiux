class Agent:
    def __init__(self, name):
        self.name = name

    def work_on_project(self, project):
        print(f'{self.name} is working on {project.name}')