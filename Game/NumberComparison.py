# Number Comparison game

import random

def generate_number():
    computer_choice = random.randint(1, 100)
    return computer_choice

def get_user_number():
    while True:
        try:
            user_num = int(input("Enter your number: "))
            if 1 <= user_num <= 100:
                return user_num
            else:
                print("Number must be between 1 and 100!")

        except ValueError:
            print("Please enter a valid number!")

def compare(myChoice, computerChoice):
    print("Your number:", myChoice)
    print("Computer number:", computerChoice)

    if myChoice > computerChoice:
        print("You win!")
    elif myChoice < computerChoice:
        print("Computer Win!")
    else:
        print("Same number, Its a draw!")

def main():
    myChoice = get_user_number()
    computerChoice = generate_number()

    compare(myChoice, computerChoice)

main()
