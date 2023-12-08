import game_logic
import computer_player

def main():
    # Create an instance of ComputerPlayer
    computer = computer_player.ComputerPlayer()

    # Game loop
    while True:
        # Get the player's choice
        player_choice = input("Enter rock, paper, or scissors: ")

        # Get the computer's choice
        computer_choice = computer.get_choice()

        # Determine the winner
        winner = game_logic.GameLogic.determine_winner(player_choice, computer_choice)

        # Print the result
        print(f"You chose {player_choice}, computer chose {computer_choice}. {winner} wins!")

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()