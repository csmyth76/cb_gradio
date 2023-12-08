import unittest
from src.computer_player import ComputerPlayer

class TestComputerPlayer(unittest.TestCase):
    def setUp(self):
        self.computer = ComputerPlayer()

    def test_random_choice(self):
        # Test that the computer's choice is always one of 'rock', 'paper', or 'scissors'
        for _ in range(100):
            self.assertIn(self.computer.make_choice(), ['rock', 'paper', 'scissors'])

if __name__ == '__main__':
    unittest.main()