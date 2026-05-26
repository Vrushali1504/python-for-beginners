# Nested Function

"""
Nested Function means a function inside another function.

The inner function can access variables
from the outer function.
"""

# ---------------------------------------------------
# Simple Nested Function
# ---------------------------------------------------

def outer():

    message = "Hello"

    def inner():
        print(message)

    inner()

outer()

# ---------------------------------------------------
# Accessing Outer Function Variable
# ---------------------------------------------------

def parent():

    name = "Python"

    def child():
        print("Inside Child Function:", name)

    child()

parent()

# ---------------------------------------------------
# Inner Function with Its Own Variable
# ---------------------------------------------------

def outer_function():

    x = 10

    def inner_function():

        y = 20

        print("Outer Variable:", x)
        print("Inner Variable:", y)

    inner_function()

outer_function()

# ---------------------------------------------------
# nonlocal Keyword
# ---------------------------------------------------

# nonlocal -> Modifies variable from outer function

def main():

    value = 5

    def change():
        nonlocal value
        value = 10

    change()

    print(value)

main()

# ---------------------------------------------------
# Returning Inner Function
# ---------------------------------------------------

def greet(message):

    def display():
        print(message)

    return display

result = greet("Welcome")

result()

# ---------------------------------------------------
# Nested Function Example
# ---------------------------------------------------

def calculation(a, b):

    def add():
        print("Addition:", a + b)

    def subtract():
        print("Subtraction:", a - b)

    add()
    subtract()

calculation(10, 5)