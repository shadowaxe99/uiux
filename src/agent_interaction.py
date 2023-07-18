import json


class NoteTakerAgent:
    def __init__(self):
        self.name = 'Note Taker Agent'
        self.notes = []

    def take_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def clear_notes(self):
        self.notes = []



import json


class NoteTakerAgent:
    def __init__(self):
        self.name = 'Note Taker Agent'
        self.notes = []

    def take_note(self, note):
        self.notes.append(note)

    def get_notes(self):
        return self.notes

    def clear_notes(self):
        self.notes = []


class AgentInteraction: