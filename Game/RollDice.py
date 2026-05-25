# Roll dice game

import random

def roll_dice():
    return random.randint(1, 6)

def play_round():
    input("Press Enter to roll the dice...")

    user = roll_dice()
    computer = roll_dice()

    print(f"You rolled: {user}")
    print(f"Computer rolled: {computer}")

    if user > computer:
        print("You win this round!")
        return "user"
    elif user < computer:
        print("Computer wins this round!")
        return "computer"
    else:
        print("Round draw!")
        return "draw"

def main():
    print("Dice Game (Best of 5)")

    user_score = 0
    computer_score = 0

    for round_no in range(1, 6):
        print(f"\n--- Round {round_no} ---")

        result = play_round()

        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")

    print("\nFinal Result")

    if user_score > computer_score:
        print("You win the game!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It's a draw overall!")

main()