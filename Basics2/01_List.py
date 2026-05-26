# List

"""
List is a data structure in Python.
It is used to store different types of data items in one variable.
It is created using [] brackets.
"""

# Creating List
animals = ["dog", "cat", "lion"]

# print() -> Displays the list
print(animals)

# Indexing -> Access element using index number
print(animals[2])

# in operator -> Checks item exists or not
print("dog" in animals)
print("tiger" in animals)

# Updating List -> Change value using index
animals[2] = "tiger"
print(animals)

# Checking updated value
print("tiger" in animals)

# Slicing -> Get elements from range
print(animals[1:6])


# ---------------------------------------------------
# List Methods
# ---------------------------------------------------

numbers = [10, 20, 30]

# append() -> Adds item at the end
numbers.append(40)
print(numbers)

# insert() -> Adds item at specific position
numbers.insert(1, 15)
print(numbers)

# extend() -> Adds multiple items
numbers.extend([50, 60])
print(numbers)

# remove() -> Removes specific item
numbers.remove(20)
print(numbers)

# pop() -> Removes item using index
numbers.pop(2)
print(numbers)

# clear() -> Removes all items
temp = [1, 2, 3]
temp.clear()
print(temp)

# index() -> Returns index of item
print(numbers.index(40))

# count() -> Counts repeated items
values = [1, 2, 2, 3, 2]
print(values.count(2))

# sort() -> Sorts list in ascending order
values.sort()
print(values)

# reverse() -> Reverses the list
values.reverse()
print(values)

# copy() -> Creates copy of list
new_values = values.copy()
print(new_values)

# len() -> Returns total number of items
print(len(values))

# max() -> Returns maximum value
print(max(values))

# min() -> Returns minimum value
print(min(values))

# sum() -> Returns sum of all items
print(sum(values))

# ---------------------------------------------------
# Sorting Strings in List
# ---------------------------------------------------

fruits = ["banana", "apple", "mango", "cherry"]

# sort() -> Sorts strings in alphabetical order
fruits.sort()
print(fruits)

# sort(reverse=True) -> Sorts in descending order
fruits.sort(reverse=True)
print(fruits)

# sorted() -> Returns new sorted list without changing original list
names = ["zebra", "dog", "cat", "elephant"]

sorted_names = sorted(names)
print(sorted_names)

# Original list remains unchanged
print(names)

# Sorting strings by length using key=len
words = ["python", "java", "c", "javascript"]

words.sort(key=len)
print(words)

# Sorting ignoring uppercase/lowercase
languages = ["Python", "java", "C", "ruby"]

languages.sort(key=str.lower)
print(languages)
