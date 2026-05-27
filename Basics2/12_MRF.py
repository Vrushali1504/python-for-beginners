# map(), filter(), and reduce()

"""
map(), filter(), and reduce() are built-in functions in Python.

1. map()
   - Applies a function to every item in a list.

2. filter()
   - Selects items based on a condition.

3. reduce()
   - Combines all values into one single value.
"""

from functools import reduce

# ---------------------------------------------------
# 1. map() Function
# ---------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Function to square a number
def square(num):
    return num * num

# Apply square() to every element
squared = list(map(square, numbers))

print(squared)  # [1, 4, 9, 16, 25]

# ---------------------------------------------------
# 2. map() with Multiple Lists
# ---------------------------------------------------

a = [1, 2, 3]
b = [4, 5, 6]

# Function to add two numbers
def add(x, y):
    return x + y

# Add elements from both lists
added = list(map(add, a, b))

print(added)  # [5, 7, 9]

# ---------------------------------------------------
# 3. filter() Function
# ---------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]

# Function to check even number
def is_even(num):
    return num % 2 == 0

# Keep only even numbers
even = list(filter(is_even, nums))

print(even)  # [2, 4, 6]

# ---------------------------------------------------
# 4. filter() with Positive Numbers
# ---------------------------------------------------

values = [-5, -2, 0, 3, 7]

# Function to check positive numbers
def is_positive(num):
    return num > 0

# Keep only positive numbers
positive = list(filter(is_positive, values))

print(positive)  # [3, 7]

# ---------------------------------------------------
# 5. reduce() Function
# ---------------------------------------------------

numbers = [1, 2, 3, 4, 5]

# Function to add two numbers
def addition(x, y):
    return x + y

# Add all numbers
total = reduce(addition, numbers)

print(total)  # 15

# ---------------------------------------------------
# 6. reduce() for Multiplication
# ---------------------------------------------------

numbers = [1, 2, 3, 4]

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Multiply all numbers
product = reduce(multiply, numbers)

print(product)  # 24

# ---------------------------------------------------
# 7. Using map(), filter(), reduce() Together
# ---------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6]

# Step 1: Filter even numbers
even_numbers = filter(is_even, numbers)

# Step 2: Square even numbers
squared_even = map(square, even_numbers)

# Step 3: Add all squared numbers
result = reduce(addition, squared_even)

print(result)  # 56