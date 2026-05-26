# Dictionary

"""
Dictionary is a data structure in Python.
It is used to store data in key-value pairs.
Dictionary is mutable (can be changed).
It is created using {} brackets.
"""

# Creating Dictionary
student = {"name": "John", "age": 21, "course": "Python"}

# print() -> Displays dictionary
print(student)

# Access value using key
print(student["name"])

# get() -> Access value safely
print(student.get("age"))

# in operator -> Checks key exists or not
print("name" in student)
print("city" in student)

# ---------------------------------------------------
# Updating Dictionary
# ---------------------------------------------------

# Changing value
student["age"] = 22
print(student)

# Adding new key-value pair
student["city"] = "Pune"
print(student)

# ---------------------------------------------------
# Dictionary Methods
# ---------------------------------------------------

# keys() -> Returns all keys
print(student.keys())

# values() -> Returns all values
print(student.values())

# items() -> Returns all key-value pairs
print(student.items())

# update() -> Updates dictionary with new values
student.update({"course": "Django", "marks": 90})
print(student)

# pop() -> Removes item using key
student.pop("marks")
print(student)

# popitem() -> Removes last inserted item
student.popitem()
print(student)

# clear() -> Removes all items
temp = {"a": 1, "b": 2}
temp.clear()
print(temp)

# copy() -> Creates copy of dictionary
new_student = student.copy()
print(new_student)

# setdefault() -> Returns value of key
# If key does not exist, adds key with default value
print(student.setdefault("country", "India"))
print(student)

# fromkeys() -> Creates dictionary with default value
keys = ("a", "b", "c")
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# ---------------------------------------------------
# Looping Through Dictionary
# ---------------------------------------------------

# Loop through keys
for key in student:
    print(key)

# Loop through values
for value in student.values():
    print(value)

# Loop through key-value pairs
for key, value in student.items():
    print(key, value)

# ---------------------------------------------------
# Nested Dictionary
# ---------------------------------------------------

employees = {"emp1": {"name": "Amit", "age": 25}, "emp2": {"name": "rutu", "age": 30}}

# Access nested dictionary value
print(employees["emp1"]["name"])

# ---------------------------------------------------
# Built-in Functions
# ---------------------------------------------------

data = {"x": 10, "y": 20, "z": 30}

# len() -> Returns number of items
print(len(data))

# max() -> Returns maximum key
print(max(data))

# min() -> Returns minimum key
print(min(data))

# sum() -> Sum of keys if numeric
numbers = {1: "one", 2: "two", 3: "three"}
print(sum(numbers))
