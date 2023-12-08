import unittest
from src.game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game_logic = GameLogic()

    def test_rock_beats_scissors(self):
        result = self.game_logic.determine_winner('rock', 'scissors')
        self.assertEqual(result, 'rock')

    def test_scissors_beats_paper(self):
        result = self.game_logic.determine_winner('scissors', 'paper')
        self.assertEqual(result, 'scissors')

    def test_paper_beats_rock(self):
        result = self.game_logic.determine_winner('paper', 'rock')
        self.assertEqual(result, 'paper')

    def test_tie(self):
        result = self.game_logic.determine_winner('rock', 'rock')
        self.assertEqual(result, 'tie')

if __name__ == '__main__':
    unittest.main()