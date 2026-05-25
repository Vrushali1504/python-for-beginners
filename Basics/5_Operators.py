# Operators

# Operators are symbols used to perform operations

a = 10
b = 3

# =================================
# Arithmetic Operators
# =================================

print(a + b)  # Addition -> 13
print(a - b)  # Subtraction -> 7
print(a * b)  # Multiplication -> 30
print(a / b)  # Division -> 3.3333333333333335
print(a // b)  # Floor Division -> 3
print(a % b)  # Modulus -> 1
print(a**b)  # Exponent -> 1000

# =================================
# Assignment Operators
# =================================

x = 5

x += 2
print(x)  # 7

x -= 1
print(x)  # 6

x *= 3
print(x)  # 18

x /= 2
print(x)  # 9.0

x //= 2
print(x)  # 4.0

x %= 3
print(x)  # 1.0

x **= 4
print(x)  # 1.0

# =================================
# Comparison Operators
# =================================

print(a == b)  # Equal to -> False
print(a != b)  # Not equal to -> True
print(a > b)  # Greater than -> True
print(a < b)  # Less than -> False
print(a >= b)  # Greater than or equal -> True
print(a <= b)  # Less than or equal -> False

# =================================
# Logical Operators
# =================================

print(True and False)  # AND -> False
print(True or False)  # OR -> True
print(not True)  # NOT -> False

# =================================
# Bitwise Operators
# =================================

print(a & b)  # Bitwise AND -> 2
print(a | b)  # Bitwise OR -> 11
print(a ^ b)  # Bitwise XOR -> 9
print(~a)  # Bitwise NOT -> -11
print(a << 1)  # Left Shift -> 20
print(a >> 1)  # Right Shift -> 5

# =================================
# Identity Operators
# =================================

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True
print(x is z)  # False
print(x is not z)  # True

# =================================
# Membership Operators
# =================================

numbers = [1, 2, 3, 4, 5]

print(3 in numbers)  # True
print(10 in numbers)  # False
print(10 not in numbers)  # True

# =================================
# Ternary Operator
# =================================

age = 18

result = "Adult" if age >= 18 else "Minor"

print(result)  # Adult
