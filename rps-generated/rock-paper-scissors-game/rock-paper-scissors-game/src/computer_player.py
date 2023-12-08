import random

class ComputerPlayer:
    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']

    def make_choice(self):
        return random.choice(self.choices)