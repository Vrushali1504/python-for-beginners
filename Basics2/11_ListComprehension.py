# List Comprehension

"""
List comprehension is a concise way to create lists
using a single line of code instead of loops.

WHY USE IT?
-----------
1. Shorter code
2. Faster execution (in many cases)
3. More readable for simple operations
========================================================
"""


# -------------------------------------------------------
# 1. BASIC LIST COMPREHENSION
# -------------------------------------------------------

# Normal way using loop
squares = []
for i in range(1, 6):
    squares.append(i * i)

print("Using loop:", squares)

# Using list comprehension
squares_comp = [i * i for i in range(1, 6)]
print("Using list comprehension:", squares_comp)


# -------------------------------------------------------
# 2. WITH CONDITION (IF FILTER)
# -------------------------------------------------------

# Get even numbers using loop
evens = []
for i in range(1, 11):
    if i % 2 == 0:
        evens.append(i)

print("\nEven numbers (loop):", evens)

# Using list comprehension with condition
evens_comp = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers (comprehension):", evens_comp)


# -------------------------------------------------------
# 3. IF-ELSE INSIDE LIST COMPREHENSION
# -------------------------------------------------------

# Mark even or odd
labels = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]

print("\nEven/Odd labels:", labels)


# -------------------------------------------------------
# 4. STRING MANIPULATION
# -------------------------------------------------------

words = ["python", "java", "c++"]

# Convert each word to uppercase
upper_words = [word.upper() for word in words]

print("\nUppercase words:", upper_words)


# -------------------------------------------------------
# 5. NESTED LIST COMPREHENSION
# -------------------------------------------------------

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

# Flatten the matrix into a single list
flat = [num for row in matrix for num in row]

print("\nFlattened list:", flat)


# -------------------------------------------------------
# 6. PRACTICAL EXAMPLE
# -------------------------------------------------------

# Get square of only even numbers
result = [i * i for i in range(1, 11) if i % 2 == 0]

print("\nSquares of even numbers:", result)
