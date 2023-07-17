```python
import os
from git import Repo

class CodeEditor:
    def __init__(self):
        self.generatedCode = {}

    def display_code(self, project_name):
        if project_name in self.generatedCode:
            return self.generatedCode[project_name]
        else:
            return "No code generated for this project yet."

    def commit_changes(self, project_name, commit_message):
        if project_name in self.generatedCode:
            repo = Repo(os.getcwd())
            repo.git.add(update=True)
            repo.index.commit(commit_message)
            return "Changes committed successfully."
        else:
            return "No code generated for this project yet."

    def update_code(self, project_name, new_code):
        self.generatedCode[project_name] = new_code
        return "Code updated successfully."

code_editor = CodeEditor()
```