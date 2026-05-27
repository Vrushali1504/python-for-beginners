# Inheritance

"""
Inheritance means one class (child class)
can use properties and methods of another class (parent class).
"""

# ---------------------------------------------------
# Parent Class
# ---------------------------------------------------

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")

# ---------------------------------------------------
# Child Class (Inheritance)
# ---------------------------------------------------

class Dog(Animal):

    def bark(self):
        print(self.name, "is barking")

# ---------------------------------------------------
# Creating Object of Child Class
# ---------------------------------------------------

d1 = Dog("Pogo")

# Child class method
d1.bark()

# Parent class methods (inherited)
d1.eat()
d1.sleep()