#Tuple

"""
Tuple is a data structure in Python.
It is used to store multiple items in one variable.
Tuple is ordered and immutable (cannot be changed).
It is created using () brackets.
"""

# Creating Tuple
animals = ("dog", "cat", "lion")

# print() -> Displays the tuple
print(animals)

# Indexing -> Access element using index number
print(animals[1])

# in operator -> Checks item exists or not
print("cat" in animals)
print("tiger" in animals)

# Slicing -> Get elements from range
print(animals[0:2])

# Length of tuple
print(len(animals))

# ---------------------------------------------------
# Tuple Methods
# ---------------------------------------------------

numbers = (10, 20, 30, 20, 40, 20)

# count() -> Counts repeated items
print(numbers.count(20))

# index() -> Returns index of first occurrence
print(numbers.index(30))

# ---------------------------------------------------
# Tuple Packing and Unpacking
# ---------------------------------------------------

# Packing -> Storing multiple values in tuple
person = ("John", 25, "India")
print(person)

# Unpacking -> Extracting values from tuple
name, age, country = person
print(name)
print(age)
print(country)

# ---------------------------------------------------
# Nested Tuple
# ---------------------------------------------------

nested = ((1, 2), (3, 4), (5, 6))

# Access nested tuple value
print(nested[1][0])

# ---------------------------------------------------
# Converting Tuple
# ---------------------------------------------------

# Tuple to List
list_data = list(numbers)
print(list_data)

# List to Tuple
tuple_data = tuple(list_data)
print(tuple_data)

# ---------------------------------------------------
# Built-in Functions with Tuple
# ---------------------------------------------------

values = (5, 2, 8, 1)

# max() -> Returns maximum value
print(max(values))

# min() -> Returns minimum value
print(min(values))

# sum() -> Returns sum of values
print(sum(values))

# sorted() -> Returns sorted list
print(sorted(values))

# ---------------------------------------------------
# Single Item Tuple
# ---------------------------------------------------

# Important: comma is required
single = (10,)
print(single)
print(type(single))