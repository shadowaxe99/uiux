class Project:
    def __init__(self, name, objectives):
        self.name = name
        self.objectives = objectives

    def __str__(self):
        return f'Project: {self.name}, Objectives: {self.objectives}'