# Function

"""
Function is a block of reusable code.
It is used to perform a specific task.
Functions help avoid repeating code.
A function is created using the def keyword.
"""

# ---------------------------------------------------
# Creating Function
# ---------------------------------------------------

# Simple function
def greet():
    print("Hello World")

# Calling function
greet()

# ---------------------------------------------------
# Function with Parameters
# ---------------------------------------------------

# Parameters -> Values passed into function
def welcome(name):
    print("Welcome", name)

welcome("Alice")
welcome("Bob")

# ---------------------------------------------------
# Function with Multiple Parameters
# ---------------------------------------------------

def add(a, b):
    print(a + b)

add(10, 20)

# ---------------------------------------------------
# Return Statement
# ---------------------------------------------------

# return -> Sends value back from function
def multiply(x, y):
    return x * y

result = multiply(5, 4)
print(result)

# ---------------------------------------------------
# Default Parameters
# ---------------------------------------------------

# Default value is used if argument not given
def country(name="India"):
    print("Country:", name)

country()
country("USA")

# ---------------------------------------------------
# Keyword Arguments
# ---------------------------------------------------

def student(name, age):
    print(name, age)

student(age=21, name="rutu")

# ---------------------------------------------------
# Arbitrary Arguments (*args)
# ---------------------------------------------------

# *args -> Multiple values stored as tuple
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)
total(10, 20, 30, 40)

# ---------------------------------------------------
# Arbitrary Keyword Arguments (**kwargs)
# ---------------------------------------------------

# **kwargs -> Multiple keyword values stored as dictionary
def details(**data):
    print(data)

details(name="John", age=25)

# ---------------------------------------------------
# Recursive Function
# ---------------------------------------------------

# Function calling itself
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# ---------------------------------------------------
# Function Returning Multiple Values
# ---------------------------------------------------

def calculation(a, b):
    return a + b, a - b

sum_value, sub_value = calculation(10, 5)

print(sum_value)
print(sub_value)

# ---------------------------------------------------
# Docstring
# ---------------------------------------------------

def info():
    """This is a docstring"""
    print("Python Function")

print(info.__doc__)

# ---------------------------------------------------
# pass Statement
# ---------------------------------------------------

# pass -> Empty function placeholder
def future_function():
    pass