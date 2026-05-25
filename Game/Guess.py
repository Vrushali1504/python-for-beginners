# Guessing game

import random

def get_difficulty():
    print("\nChoose difficulty level:")
    print("1. Easy (1–50)")
    print("2. Medium (1–100)")
    print("3. Hard (1–500)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        return 50
    elif choice == "2":
        return 100
    elif choice == "3":
        return 500
    else:
        print("Invalid choice. Defaulting to Medium.")
        return 100


def generate_number(max_range):
    return random.randint(1, max_range)


def get_guess():
    while True:
        try:
            return int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number!")


def play_game():
    print("Welcome to Guess the Number Game!")

    max_range = get_difficulty()
    number = generate_number(max_range)

    attempts = 0
    guessed = False

    print(f"\nI'm thinking of a number between 1 and {max_range}!")

    while not guessed:
        guess = get_guess()
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! The number was {number}")
            print(f"You got it in {attempts} attempts.")
            guessed = True


def main():
    while True:
        play_game()

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


main()
