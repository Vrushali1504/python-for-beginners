# Recursion

"""
Recursion is a process where a function calls itself.

A recursive function must have:
1. Base Case
   - Condition that stops recursion.

2. Recursive Case
   - Function calls itself again.
"""

# ---------------------------------------------------
# 1. Simple Recursion Example
# ---------------------------------------------------

def show_numbers(n):

    # Base Case
    if n == 0:
        return

    print(n)

    # Recursive Call
    show_numbers(n - 1)

show_numbers(5)

# ---------------------------------------------------
# 2. Factorial Using Recursion
# ---------------------------------------------------

"""
Factorial Formula
"""

def factorial(n):

    # Base Case
    if n == 1:
        return 1

    # Recursive Case
    return n * factorial(n - 1)

print(factorial(5))  # 120

# ---------------------------------------------------
# 3. Sum of Natural Numbers
# ---------------------------------------------------

def sum_numbers(n):

    # Base Case
    if n == 0:
        return 0

    # Recursive Case
    return n + sum_numbers(n - 1)

print(sum_numbers(5))  # 15

# ---------------------------------------------------
# 4. Fibonacci Series Using Recursion
# ---------------------------------------------------

"""
Fibonacci Series:
0 1 1 2 3 5 8 ...
"""

def fibonacci(n):

    # Base Cases
    if n == 0:
        return 0

    if n == 1:
        return 1

    # Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 8

# ---------------------------------------------------
# 5. Reverse a String Using Recursion
# ---------------------------------------------------

def reverse_string(text):

    # Base Case
    if len(text) == 0:
        return text

    # Recursive Case
    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))  # nohtyP

# ---------------------------------------------------
# 6. Power of a Number Using Recursion
# ---------------------------------------------------

def power(base, exponent):

    # Base Case
    if exponent == 0:
        return 1

    # Recursive Case
    return base * power(base, exponent - 1)

print(power(2, 4))  # 16

# ---------------------------------------------------
# 7. Count Down Using Recursion
# ---------------------------------------------------

def countdown(n):

    # Base Case
    if n == 0:
        print("Finished")
        return

    print(n)

    # Recursive Call
    countdown(n - 1)

countdown(5)