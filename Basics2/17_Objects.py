# Objects

"""
Object is an instance of a class.

Class -> Blueprint
Object -> Real implementation of class

Objects contain:
1. Attributes (variables)
2. Methods (functions)
"""

# ---------------------------------------------------
# Creating Class and Object
# ---------------------------------------------------

class Student:

    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating Object
s1 = Student("rutu", 21)

# Accessing Object Method
s1.display()

# ---------------------------------------------------
# Accessing Object Attributes
# ---------------------------------------------------

print(s1.name)
print(s1.age)

# ---------------------------------------------------
# Creating Multiple Objects
# ---------------------------------------------------

s2 = Student("Alice", 22)

s1.display()
s2.display()

# ---------------------------------------------------
# Modifying Object Attributes
# ---------------------------------------------------

s1.age = 25

print(s1.age)

# ---------------------------------------------------
# Deleting Object Attributes
# ---------------------------------------------------

del s1.age

# print(s1.age)   # Error -> Attribute deleted

# ---------------------------------------------------
# Deleting Object
# ---------------------------------------------------

temp = Student("John", 20)

del temp

# print(temp)   # Error -> Object deleted

# ---------------------------------------------------
# Object Methods
# ---------------------------------------------------

class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(self.brand, "Car Started")

car1 = Car("BMW", "Black")

car1.start()

# ---------------------------------------------------
# self Keyword
# ---------------------------------------------------

"""
self refers to current object.

It is used to access object attributes
and methods inside class.
"""

class Employee:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

e1 = Employee("David")

e1.show()

# ---------------------------------------------------
# isinstance()
# ---------------------------------------------------

# Checks object belongs to class or not

print(isinstance(s1, Student))

# ---------------------------------------------------
# type()
# ---------------------------------------------------

# Returns object type

print(type(s1))