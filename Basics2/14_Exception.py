# Exception

"""
An exception is an error that occurs during execution
which disrupts normal program flow.

WHY USE EXCEPTIONS?
-------------------
1. Prevent program crash
2. Handle errors gracefully
3. Improve user experience

KEY BLOCKS:
-----------
try     → code that may cause error
except  → handles error
else    → runs if no error occurs
finally → always runs (error or not)
========================================================
"""


# -------------------------------------------------------
# 1. BASIC EXCEPTION HANDLING
# -------------------------------------------------------

try:
    # Code that may cause error
    a = 10
    b = 0

    result = a / b   # ❌ division by zero error
    print(result)

except ZeroDivisionError:
    # Runs when division by zero happens
    print("Error: Cannot divide by zero!")


# -------------------------------------------------------
# 2. MULTIPLE EXCEPT BLOCKS
# -------------------------------------------------------

try:
    num = int("abc")   # ❌ invalid conversion
    print(num)

except ValueError:
    # Handles invalid type conversion
    print("Error: Invalid number format!")

except Exception as e:
    # Generic exception handler
    print("Some other error occurred:", e)


# -------------------------------------------------------
# 3. TRY-EXCEPT-ELSE
# -------------------------------------------------------

try:
    x = 10
    y = 2
    result = x / y

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    # Runs only if NO error occurs
    print("Division successful:", result)


# -------------------------------------------------------
# 4. FINALLY BLOCK
# -------------------------------------------------------

try:
    file = open("demo.txt", "r")
    content = file.read()

except FileNotFoundError:
    print("File not found!")

finally:
    # Always executes (cleanup code)
    print("Execution completed (finally block runs always)")


# -------------------------------------------------------
# 5. CUSTOM EXCEPTION (USER DEFINED)
# -------------------------------------------------------

class AgeError(Exception):
    # Custom exception class
    pass

def check_age(age):
    if age < 18:
        raise AgeError("Age must be 18 or above")
    else:
        print("Access granted")

try:
    check_age(15)

except AgeError as e:
    print("Custom Exception:", e)


# -------------------------------------------------------
# 6. COMMON BUILT-IN EXCEPTIONS
# -------------------------------------------------------

# ZeroDivisionError → divide by zero
# ValueError        → wrong value type
# TypeError         → wrong data type operation
# IndexError        → invalid list index
# KeyError          → missing dictionary key

print("\nCommon exceptions explained in comments above")