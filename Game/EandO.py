# Even odd game

import random

print("Welcome to Even or Odd Game!")

while True:
    number = random.randint(1, 100)

    guess = input("\nGuess (even/odd) or type 'quit' to exit: ").lower()

    if guess == "quit":
        print("Thanks for playing!")
        break

    if guess not in ["even", "odd"]:
        print("Please type 'even' or 'odd'")
        continue

    if number % 2 == 0:
        result = "even"
    else:
        result = "odd"

    print("Number was:", number)

    if guess == result:
        print("Correct!")
    else:
        print("Wrong!")
