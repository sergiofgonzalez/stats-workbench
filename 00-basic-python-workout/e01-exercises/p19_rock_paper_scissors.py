import random
import time


def play_rock_paper_scissors():

    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    all_choices = (rock, paper, scissors)

    user_choice = input(f"Enter your choice ({rock!r}, {paper!r}, {scissors!r}): ")

    if user_choice not in all_choices:
        print("Invalid choice!\n")

    computer_choice = random.choice(all_choices)

    print("Jan...")
    time.sleep(1)

    print("Ken...")
    time.sleep(1)

    print("Pon...")
    time.sleep(1)

    print(f"\nYou chose {user_choice!r}, the opponent chose {computer_choice!r}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == rock and computer_choice == scissors) or
        (user_choice == paper and computer_choice == rock) or
        (user_choice == scissors and computer_choice == paper)
    ):
        print("You win!")
    else:
        print("You lose!")


print("== Rock, Paper, Scissors ==\n")
play_rock_paper_scissors()
