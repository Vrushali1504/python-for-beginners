# Modules

"""
A module is a file containing Python code (functions, variables, classes).
It helps in organizing code and reusing it.
"""

# ---------------------------------------------------
# 1. math module
# ---------------------------------------------------

import math

print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)

# ---------------------------------------------------
# 2. Import specific functions
# ---------------------------------------------------

from math import sqrt, pi

print(sqrt(16))
print(pi)

# ---------------------------------------------------
# 3. Import with alias
# ---------------------------------------------------

import math as m

print(m.pow(2, 3))
print(m.floor(4.7))

# ---------------------------------------------------
# 4. random module
# ---------------------------------------------------

import random

print(random.randint(1, 10))
print(random.choice(["A", "B", "C"]))

# ---------------------------------------------------
# 5. datetime module
# ---------------------------------------------------

import datetime

print(datetime.datetime.now())

# ---------------------------------------------------
# 6. os module
# ---------------------------------------------------

import os

print(os.getcwd())

# ---------------------------------------------------
# 7. sys module
# ---------------------------------------------------

import sys

print(sys.version)
