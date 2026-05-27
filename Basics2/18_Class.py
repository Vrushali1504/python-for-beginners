#Class

"""
Class is a blueprint for creating objects.

It defines:
1. Attributes (data/variables)
2. Methods (functions)

Object is an instance of a class.
"""

# ---------------------------------------------------
# Creating a Class
# ---------------------------------------------------

class Student:

    def set_data(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

s1 = Student()
s2 = Student()

s1.set_data("Bob", 21)
s2.set_data("Alice", 22)

s1.show()
s2.show()

# ---------------------------------------------------
# Accessing Attributes
# ---------------------------------------------------

print(s1.name)
print(s2.age)

# ---------------------------------------------------
# Modifying Attributes
# ---------------------------------------------------

s1.age = 25
print(s1.age)

# ---------------------------------------------------
# Adding New Attribute
# ---------------------------------------------------

s1.city = "Pune"
print(s1.city)

# ---------------------------------------------------
# Constructor (__init__)
# ---------------------------------------------------

"""
__init__ is a constructor method.
It runs automatically when object is created.
"""

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Innova")

print(car1.brand, car1.model)

# ---------------------------------------------------
# self Keyword
# ---------------------------------------------------

"""
self refers to current object.
It is used to access attributes and methods.
"""

class Employee:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

e1 = Employee("David")
e1.display()

# ---------------------------------------------------
# Multiple Methods in Class
# ---------------------------------------------------

class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

calc = Calculator()

print(calc.add(10, 5))
print(calc.sub(10, 5))

# ---------------------------------------------------
# Deleting Object Attribute
# ---------------------------------------------------

del s1.city
# print(s1.city)  # Error