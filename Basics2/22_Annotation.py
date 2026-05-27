# Annotation

"""
Annotations in Python are used to provide extra information
about variables, function parameters, and return types.

They are mainly used for:
1. Type hints (int, str, float, etc.)
2. Better readability
3. IDE support (autocomplete, warnings)
4. Static type checking tools (like mypy)

IMPORTANT:
----------
- Python does NOT enforce annotations at runtime
- They are only hints for developers and tools
========================================================
"""

# -------------------------------------------------------
# 1. FUNCTION ANNOTATIONS
# -------------------------------------------------------

def add(a: int, b: int) -> int:
    # a: int  → first parameter should be integer
    # b: int  → second parameter should be integer
    # -> int  → function returns integer
    return a + b

print("Addition:", add(10, 5))


# -------------------------------------------------------
# 2. VARIABLE ANNOTATIONS
# -------------------------------------------------------

name: str = "Rutu"      # name should be string
age: int = 23           # age should be integer
height: float = 5.6     # height should be float

print("\nVariable Annotations:")
print(name, age, height)


# -------------------------------------------------------
# 3. FUNCTION WITH NO RETURN (None TYPE)
# -------------------------------------------------------

def greet(user: str) -> None:
    # user: str → input must be string
    # -> None → function returns nothing
    print("\nHello", user)

greet("Rutu")


# -------------------------------------------------------
# 4. LIST AND DICTIONARY ANNOTATIONS
# -------------------------------------------------------

numbers: list[int] = [1, 2, 3, 4, 5]  # only integers allowed
marks: dict[str, int] = {
    "Math": 90,
    "Science": 85
}

print("\nList and Dict Annotations:")
print(numbers)
print(marks)


# -------------------------------------------------------
# 5. OPTIONAL TYPE (MAY RETURN VALUE OR NONE)
# -------------------------------------------------------

from typing import Optional

def find_student(student_id: int) -> Optional[str]:
    # Optional[str] → returns str OR None
    if student_id == 1:
        return "Rutu"
    return None

print("\nOptional Return Type:")
print(find_student(1))
print(find_student(2))


# -------------------------------------------------------
# 6. CLASS WITH ANNOTATIONS
# -------------------------------------------------------

class Student:
    """
    Represents a student.

    Attributes:
        name (str): Student name
        age (int): Student age
    """

    name: str   # class variable annotation
    age: int

    def __init__(self, name: str, age: int) -> None:
        # Constructor parameters are annotated
        self.name = name
        self.age = age

    def display(self) -> None:
        # Method returns nothing
        print("\nStudent Details:")
        print("Name:", self.name)
        print("Age:", self.age)


s1 = Student("Rutu", 23)
s1.display()


# -------------------------------------------------------
# 7. VIEW FUNCTION ANNOTATIONS
# -------------------------------------------------------

def multiply(a: int, b: int) -> int:
    return a * b

print("\nAnnotations of multiply function:")
print(multiply.__annotations__)