# Docstring

"""
A docstring is a special string used to describe a function, class, or module.

It is written inside triple quotes (""" """).

Docstrings explain:
1. What the function does
2. What parameters it takes
3. What it returns
"""

# ---------------------------------------------------
# 1. Simple Function with Docstring
# ---------------------------------------------------


def greet():
    """
    This function prints a greeting message.
    """
    print("Hello, Welcome!")


greet()

# Accessing docstring
print(greet.__doc__)

# ---------------------------------------------------
# 2. Function with Parameters Docstring
# ---------------------------------------------------


def add(a, b):
    """
    This function takes two numbers and returns their sum.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: Sum of a and b
    """
    return a + b


print(add(5, 3))

# Access docstring
print(add.__doc__)

# ---------------------------------------------------
# 3. Class Docstring
# ---------------------------------------------------


class Student:
    """
    This class represents a student.

    Attributes:
    name (str): Name of the student
    age (int): Age of the student
    """

    def __init__(self, name, age):
        """
        Constructor to initialize student object.
        """
        self.name = name
        self.age = age

    def display(self):
        """
        This method displays student details.
        """
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rutu", 23)
s1.display()

# ---------------------------------------------------
# 4. Module Docstring (Example at top of file)
# ---------------------------------------------------

"""
This module demonstrates the use of docstrings in Python.
It includes functions and classes with proper documentation.
"""

# ---------------------------------------------------
# 5. Multi-line Docstring Style (Google Style)
# ---------------------------------------------------


def multiply(a, b):
    """
    Multiply two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Product of a and b
    """
    return a * b


print(multiply(4, 5))
