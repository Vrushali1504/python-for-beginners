"""
Operator overloading allows us to define how operators
(+ - * / etc.) work with user-defined objects (classes).

WHY USE IT?
-----------
- Makes code more natural and readable
- Lets objects behave like built-in types
========================================================
"""


# -------------------------------------------------------
# 1. BASIC OPERATOR OVERLOADING (+)
# -------------------------------------------------------

print("\n--- Operator Overloading: + ---")

class Number:
    def __init__(self, value):
        self.value = value

    # Overloading '+' operator
    def __add__(self, other):
        return Number(self.value + other.value)

    def show(self):
        print(self.value)


n1 = Number(10)
n2 = Number(20)

result = n1 + n2   # internally calls n1.__add__(n2)

result.show()      # Output: 30


# -------------------------------------------------------
# 2. SUBTRACTION OVERLOADING (-)
# -------------------------------------------------------

print("\n--- Operator Overloading: - ---")

class Number2:
    def __init__(self, value):
        self.value = value

    def __sub__(self, other):
        return Number2(self.value - other.value)

    def show(self):
        print(self.value)


a = Number2(50)
b = Number2(20)

result2 = a - b   # calls __sub__

result2.show()    # Output: 30


# -------------------------------------------------------
# 3. MULTIPLICATION OVERLOADING (*)
# -------------------------------------------------------

print("\n--- Operator Overloading: * ---")

class Number3:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return Number3(self.value * other.value)

    def show(self):
        print(self.value)


x = Number3(5)
y = Number3(4)

result3 = x * y

result3.show()    # Output: 20


# -------------------------------------------------------
# 4. STRING-LIKE OBJECT CONCATENATION
# -------------------------------------------------------

print("\n--- Custom String Concatenation ---")

class Text:
    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        return Text(self.text + " " + other.text)

    def show(self):
        print(self.text)


t1 = Text("Hello")
t2 = Text("World")

t3 = t1 + t2

t3.show()   # Output: Hello World