# Boolean

"""
A Boolean is a data type that has only two values: True or False.
It is commonly used in conditions and comparisons. Booleans help control program flow.
"""

is_student = True
is_adult = False

print(is_student)  # True
print(is_adult)  # False


# =================================
# Boolean from comparisons
# =================================

print(5 > 3)  # True
print(2 == 10)  # False
print(7 < 1)  # False
print(10 >= 10)  # True
print(4 != 5)  # True


# =======================
# Boolean in conditions
# =======================

age = 18

if age >= 18:
    print("Allowed")  # True condition
else:
    print("Not Allowed")


# ===================
# Boolean operations
# ====================

print(True and False)  # False
print(True or False)  # True
print(not True)  # False


# ============================
# String-based Boolean checks
# ============================

text = "Python Programming"

print("Py" in text)  # True
print("Java" in text)  # False
print(text.startswith("Py"))  # True
print(text.endswith("ing"))  # True


# ======================
# Empty value → Boolean
# ======================

empty_string = ""
non_empty = "Hello"

print(bool(empty_string))  # False
print(bool(non_empty))  # True


# =========================
# Numeric values → Boolean
# =========================

print(bool(0))  # False
print(bool(10))  # True
print(bool(-5))  # True
print(bool(0.0))  # False
print(bool(3.14))  # True


# ================
# any() and all()
# ================

print("\nany() and all() examples:")

# any() → True if at least one value is True
print(any([False, False, True]))  # True
print(any([0, 0, 0]))  # False
print(any([0, 1, 0]))  # True

# all() → True only if all values are True
print(all([True, True, True]))  # True
print(all([True, False, True]))  # False
print(all([1, 2, 3]))  # True (all non-zero values are True)

# using conditions
numbers = [2, 4, 6, 8]

print(any(n > 5 for n in numbers))  # True (6, 8 > 5)
print(all(n % 2 == 0 for n in numbers))  # True (all even)
