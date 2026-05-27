# Polymorphism

"""
Polymorphism means "many forms".

It allows the same function/method name to work differently
depending on the object or data type.

TYPES OF POLYMORPHISM:
----------------------
1. Function Polymorphism
2. Method Overriding (OOP)
3. Operator Overloading
========================================================
"""


# -------------------------------------------------------
# 1. FUNCTION POLYMORPHISM
# -------------------------------------------------------

# Same function name behaves differently based on input type

print("\n--- Function Polymorphism ---")

print(len("Python"))      # string → counts characters
print(len([1, 2, 3, 4]))  # list → counts elements


# -------------------------------------------------------
# 2. METHOD POLYMORPHISM (METHOD OVERRIDING)
# -------------------------------------------------------

print("\n--- Method Overriding ---")

class Animal:
    def sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


# Same method name, different behavior
a1 = Animal()
a2 = Dog()
a3 = Cat()

a1.sound()
a2.sound()
a3.sound()


# -------------------------------------------------------
# 3. POLYMORPHISM USING LOOP
# -------------------------------------------------------

print("\n--- Polymorphism in Loop ---")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()   # same method, different output


# -------------------------------------------------------
# 4. OPERATOR POLYMORPHISM (OVERLOADING)
# -------------------------------------------------------

print("\n--- Operator Polymorphism ---")

# '+' works differently based on type

print(10 + 20)            # integer addition
print("Hello " + "World") # string concatenation
print([1, 2] + [3, 4])    # list merging


# -------------------------------------------------------
# 5. CUSTOM POLYMORPHISM (REAL WORLD STYLE)
# -------------------------------------------------------

print("\n--- Custom Polymorphism Example ---")

class Shape:
    def area(self):
        print("Calculating area")


class Circle(Shape):
    def area(self):
        print("Area of Circle = πr²")


class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle = l × b")


shapes = [Circle(), Rectangle()]

for shape in shapes:
    shape.area()
