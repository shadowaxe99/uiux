class ClippyAvatar:
    def __init__(self):
        self.settings = clippyAvatar

    def interactWithAvatar(self, interaction):
        if interaction == "greet":
            return "Hello, how can I assist you today?"
        elif interaction == "goodbye":
            return "Goodbye, have a great day!"
        else:
            return "I'm sorry, I didn't understand that. Can you please repeat?"

    def updateAvatarSettings(self, newSettings):
        self.settings = newSettings
        return "Avatar settings updated successfully."

    def getAvatarSettings(self):
        return self.settings