# Enum

"""
Enum is used to define a set of named constant values.
It makes code more readable and organized. Enums are useful when values should not change.
"""
from enum import Enum


class Status(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3


print(Status.SUCCESS)  # Success
print(Status(1))  # Pending
print(list(Status))  # list
