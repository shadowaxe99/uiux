import unittest
from src.agent_interaction import interactWithAvatar

class TestAgentInteraction(unittest.TestCase):

    def setUp(self):
        self.projectChat = []
        self.clippyAvatar = {}

    def test_interactWithAvatar(self):
        message = "Initialize new project"
        interactWithAvatar(self.projectChat, self.clippyAvatar, message)
        self.assertEqual(self.projectChat[-1], message)

    def test_emptyMessage(self):
        message = ""
        interactWithAvatar(self.projectChat, self.clippyAvatar, message)
        self.assertEqual(self.projectChat[-1], message)

    def test_avatarSettings(self):
        self.clippyAvatar['voice'] = 'male'
        message = "Change avatar voice to female"
        interactWithAvatar(self.projectChat, self.clippyAvatar, message)
        self.assertEqual(self.clippyAvatar['voice'], 'female')

if __name__ == '__main__':
    unittest.main()