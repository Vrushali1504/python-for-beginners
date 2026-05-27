# Lambda

"""
Lambda function is a small anonymous function in Python.
It is used for simple operations in one line.
It can take any number of arguments but only one expression.
"""

# lambda arguments: expression

# ---------------------------------------------------
# 1. Simple Lambda Function
# ---------------------------------------------------

square = lambda x: x * x

print(square(5))  # 25

# ---------------------------------------------------
# 2. Multiple Arguments
# ---------------------------------------------------

add = lambda a, b: a + b

print(add(10, 20))  # 30

# ---------------------------------------------------
# 3. Lambda in print directly
# ---------------------------------------------------

print((lambda x: x + 10)(5))

# ---------------------------------------------------
# 4. Lambda with if condition
# ---------------------------------------------------

max_value = lambda a, b: a if a > b else b

print(max_value(10, 20))

# ---------------------------------------------------
# 5. Lambda with map()
# ---------------------------------------------------

numbers = [1, 2, 3, 4]

squared = list(map(lambda x: x * x, numbers))

print(squared)

# ---------------------------------------------------
# 6. Lambda with filter()
# ---------------------------------------------------

nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))

print(even)

# ---------------------------------------------------
# 7. Lambda with sorted()
# ---------------------------------------------------

pairs = [(1, 3), (2, 1), (4, 2)]

sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)
