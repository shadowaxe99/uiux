```python
import unittest
from src.clippy_avatar import ClippyAvatar

class TestClippyAvatar(unittest.TestCase):

    def setUp(self):
        self.clippy_avatar = ClippyAvatar()

    def test_avatar_settings(self):
        self.clippy_avatar.set_avatar("happy")
        self.assertEqual(self.clippy_avatar.get_avatar(), "happy")

    def test_avatar_interaction(self):
        response = self.clippy_avatar.interact("Hello Clippy!")
        self.assertIsNotNone(response)

    def test_avatar_update(self):
        self.clippy_avatar.update_avatar("sad")
        self.assertEqual(self.clippy_avatar.get_avatar(), "sad")

if __name__ == '__main__':
    unittest.main()
```