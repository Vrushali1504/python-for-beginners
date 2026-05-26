#Loops

"""
Loop is used to execute a block of code repeatedly.

Python has two main loops:
1. for loop
2. while loop
"""

# ---------------------------------------------------
# for Loop
# ---------------------------------------------------

# for -> Iterates over sequence

fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

# ---------------------------------------------------
# Looping Through String
# ---------------------------------------------------

for letter in "Python":
    print(letter)

# ---------------------------------------------------
# range() Function
# ---------------------------------------------------

# range(stop)

for i in range(5):
    print(i)

# range(start, stop)

for i in range(1, 6):
    print(i)

# range(start, stop, step)

for i in range(1, 10, 2):
    print(i)

# ---------------------------------------------------
# while Loop
# ---------------------------------------------------

# while -> Executes until condition becomes False

count = 1

while count <= 5:
    print(count)
    count += 1

# ---------------------------------------------------
# break Statement
# ---------------------------------------------------

# break -> Stops loop immediately

for i in range(1, 6):

    if i == 3:
        break

    print(i)

# ---------------------------------------------------
# continue Statement
# ---------------------------------------------------

# continue -> Skips current iteration

for i in range(1, 6):

    if i == 3:
        continue

    print(i)

# ---------------------------------------------------
# pass Statement
# ---------------------------------------------------

# pass -> Empty loop placeholder

for i in range(3):
    pass

# ---------------------------------------------------
# else with Loop
# ---------------------------------------------------

# else runs when loop finishes normally

for i in range(3):
    print(i)

else:
    print("Loop Finished")

# ---------------------------------------------------
# Nested Loop
# ---------------------------------------------------

for i in range(1, 4):

    for j in range(1, 3):
        print(i, j)

# ---------------------------------------------------
# Loop Through Dictionary
# ---------------------------------------------------

student = {
    "name": "rutu",
    "age": 23
}

for key in student:
    print(key, student[key])

# ---------------------------------------------------
# Loop Through Set
# ---------------------------------------------------

numbers = {1, 2, 3}

for value in numbers:
    print(value)

# ---------------------------------------------------
# Infinite Loop
# ---------------------------------------------------

# Uncomment to run

"""
while True:
    print("Infinite Loop")
"""

# ---------------------------------------------------
# List Comprehension
# ---------------------------------------------------

# Short way to create list using loop

squares = [x * x for x in range(5)]

print(squares)