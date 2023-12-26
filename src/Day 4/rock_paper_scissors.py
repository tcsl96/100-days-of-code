"""Rock, paper, scissors game."""

from random import randint

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

WIN_MESSAGE = "You win!"
DRAW_MESSAGE = "It's a draw."
LOSE_MESSAGE = "You lose."

choices_list = [ROCK, PAPER, SCISSORS]

def check_winner(player_c: int, computer_c: int) -> None:
    """
    Summary:
        Checks who won the game, the player o the computer.

    Args:
        __player_choice (int): The player choice: 0 - Rock, 1 - Paper, 2 - Scissors.
        __computer_choice (int): The computer choice: 0 - Rock, 1 - Paper, 2 - Scissors
    """
    if (player_c == 0 and computer_c == 2):
        print(WIN_MESSAGE)
        return None
    if (player_c == 2 and computer_c == 0):
        print(LOSE_MESSAGE)
        return None
    if player_c > computer_c:
        print(WIN_MESSAGE)
    elif player_c == computer_c:
        print(DRAW_MESSAGE)
    else:
        print(LOSE_MESSAGE)
    return None

if __name__ == "__main__":
    while True:
        try:
            player_choice = int(input("What do you choose? Type 0 for Rock, \
                                      1 for Paper or 2 for Scissors: ").strip())
        except ValueError:
            print("Please, select a valid choice.")
            continue
        if player_choice not in (0, 1, 2):
            print("Please, select a valid choice.")
            continue
        break

    computer_choice = randint(0, 2)

    print(f"Your choice:{choices_list[player_choice]}")
    print(f"Computer choice:{choices_list[computer_choice]}")

    check_winner(player_choice, computer_choice)
