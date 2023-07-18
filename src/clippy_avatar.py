class ClippyAvatar:
    def __init__(self):
        self.name = 'Clippy'
        self.mood = 'Neutral'
        self.location = 'Desktop'

    def greet(self):
        print(f'Hello! I am {self.name}, your friendly Clippy avatar.')

    def set_mood(self, mood):
        self.mood = mood
        print(f'My mood is now {self.mood}.')

    def set_location(self, location):
        self.location = location
        print(f'I am now located at {self.location}.')

    def interact(self):
        self.greet()
        print(f'I am currently in a {self.mood} mood.')
        print(f'I am located at {self.location}.')

    def wave(self):
        print(f'{self.name} waves hello!')

    def dance(self):
        print(f'{self.name} does a little dance.')

    def perform_action(self, action):
        print(f'{self.name} performs {action}.')