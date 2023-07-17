import unittest
from src import code_editor

class TestCodeEditor(unittest.TestCase):

    def setUp(self):
        self.code_editor = code_editor.CodeEditor()
        self.generatedCode = "print('Hello, World!')"

    def test_display_code(self):
        self.code_editor.display_code(self.generatedCode)
        self.assertEqual(self.code_editor.code, self.generatedCode)

    def test_commit_changes(self):
        new_code = "print('Hello, Clippy!')"
        self.code_editor.commit_changes(new_code)
        self.assertEqual(self.code_editor.code, new_code)

    def test_integrate_source_control(self):
        self.code_editor.integrate_source_control('git')
        self.assertEqual(self.code_editor.source_control, 'git')

if __name__ == '__main__':
    unittest.main()