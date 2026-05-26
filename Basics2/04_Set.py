# Set

"""
Set is a data structure in Python.
It is used to store multiple unique items in one variable.
Set is unordered and mutable.
Duplicate values are not allowed.
It is created using {} brackets.
"""

# Creating Set
animals = {"dog", "cat", "lion"}

# print() -> Displays the set
print(animals)

# in operator -> Checks item exists or not
print("dog" in animals)
print("tiger" in animals)

# ---------------------------------------------------
# Adding Items
# ---------------------------------------------------

# add() -> Adds single item
animals.add("tiger")
print(animals)

# update() -> Adds multiple items
animals.update(["elephant", "zebra"])
print(animals)

# ---------------------------------------------------
# Removing Items
# ---------------------------------------------------

# remove() -> Removes item
animals.remove("cat")
print(animals)

# discard() -> Removes item safely
animals.discard("horse")
print(animals)

# pop() -> Removes random item
animals.pop()
print(animals)

# clear() -> Removes all items
temp = {"a", "b", "c"}
temp.clear()
print(temp)

# ---------------------------------------------------
# Copying Set
# ---------------------------------------------------

# copy() -> Creates copy of set
numbers = {1, 2, 3}
new_numbers = numbers.copy()
print(new_numbers)

# ---------------------------------------------------
# Set Operations
# ---------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union() -> Combines both sets
print(A.union(B))

# intersection() -> Common elements
print(A.intersection(B))

# difference() -> Elements present in A only
print(A.difference(B))

# symmetric_difference() -> Non-common elements
print(A.symmetric_difference(B))

# ---------------------------------------------------
# Update Set Operations
# ---------------------------------------------------

# intersection_update() -> Updates with common elements
C = {1, 2, 3}
D = {2, 3, 4}

C.intersection_update(D)
print(C)

# difference_update() -> Removes common elements
E = {1, 2, 3, 4}
F = {3, 4, 5}

E.difference_update(F)
print(E)

# symmetric_difference_update() -> Updates with non-common elements
G = {1, 2, 3}
H = {3, 4, 5}

G.symmetric_difference_update(H)
print(G)

# ---------------------------------------------------
# Checking Relations
# ---------------------------------------------------

X = {1, 2}
Y = {1, 2, 3, 4}

# issubset() -> Checks if set is subset
print(X.issubset(Y))

# issuperset() -> Checks if set is superset
print(Y.issuperset(X))

# isdisjoint() -> Checks no common elements
print(X.isdisjoint({5, 6}))

# ---------------------------------------------------
# Built-in Functions
# ---------------------------------------------------

values = {5, 2, 8, 1}

# len() -> Returns number of items
print(len(values))

# max() -> Returns maximum value
print(max(values))

# min() -> Returns minimum value
print(min(values))

# sum() -> Returns sum of values
print(sum(values))

# sorted() -> Returns sorted list
print(sorted(values))

# ---------------------------------------------------
# Duplicate Values
# ---------------------------------------------------

# Duplicate values are automatically removed
nums = {1, 2, 2, 3, 3, 4}
print(nums)

# ---------------------------------------------------
# Frozen Set
# ---------------------------------------------------

# frozenset() -> Immutable set
frozen = frozenset([1, 2, 3])

print(frozen)