# Data Types

"""
Data types define the kind of data a variable can store, such as integers, floats, or strings.
They help Python understand how to handle the data.
"""

# Integer (int)
age = 23


# Float (float)
price = 99.99


# String (str)
name = "Ruturaj"


# Boolean (bool)
is_student = True


# List (list)
marks = [85, 90, 78]


# Tuple (tuple)
colors = ("red", "green", "blue")


# Dictionary (dict)
student = {"name": "Ruturaj", "age": 23}


# Set (set)
numbers = {1, 2, 3, 4}


# Complex Number (complex)
complex_num = 3 + 4j


# Checking data type
print(type(age))  # <class 'int'>
print(type(price))  # <class 'float'>
print(type(name))  # <class 'str'>

print(type(name) == str)  # True
print(isinstance(name, str))  # True

print(type(colors))  # <class 'tuple'>
print(type(student))  # <class 'dict'>
print(type(numbers))  # <class 'set'>
print(type(complex_num))  # <class 'complex'>


# Type Conversion / Type Casting
# Changing one data type into another


# int to float
num = 10
print(float(num))  # 10.0


# float to int
value = 99.99
print(int(value))  # 99


# int to string
age = 23
print(str(age))  # "23"


# string to int
number = "100"
print(int(number))  # 100


# string to float
price = "45.5"
print(float(price))  # 45.5


# list to tuple
data = [1, 2, 3]
print(tuple(data))  # (1, 2, 3)


# tuple to list
colors = ("red", "blue")
print(list(colors))  # ['red', 'blue']


# int to complex
num = 5
print(complex(num))  # (5+0j)


# float to complex
value = 2.5
print(complex(value))  # (2.5+0j)
