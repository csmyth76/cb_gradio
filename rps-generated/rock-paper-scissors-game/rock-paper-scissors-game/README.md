# Rock Paper Scissors Game

This is a simple text-based Rock, Paper, Scissors game played against the computer.

## How to Run the Game

1. Navigate to the `src` directory.
2. Run the `main.py` file using Python.

```bash
cd src
python main.py
```

## Game Rules

The game rules are as follows:

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock

The player and the computer both choose one of Rock, Paper, or Scissors. The winner is determined based on the rules above.

## Project Structure

- `src/main.py`: The entry point of the game.
- `src/game_logic.py`: Contains the `GameLogic` class with methods for determining the winner.
- `src/computer_player.py`: Contains the `ComputerPlayer` class with a method for generating a random choice.
- `tests/test_game_logic.py`: Contains unit tests for the `GameLogic` class.
- `tests/test_computer_player.py`: Contains unit tests for the `ComputerPlayer` class.

## Testing

To run the tests, navigate to the `tests` directory and run the test files using Python.

```bash
cd tests
python test_game_logic.py
python test_computer_player.py
```

Enjoy the game!