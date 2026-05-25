# Control Statement

# Control statements in Python are used to control the flow of a program based on conditions.

# ==============
# IF STATEMENT
# ==============

age = 18

if age >= 18:
    print("You are eligible to vote")

# ==================
# IF-ELSE STATEMENT
# ==================

num = 10

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# =======================
# IF-ELIF-ELSE STATEMENT
# =======================

marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# =====================
# MATCH-CASE STATEMENT
# =====================

day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")
