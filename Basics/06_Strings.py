# Strings

# Strings are sequences of characters used to represent text in Python. They are written inside quotes like

# Creating Strings
name = "Ruturaj"
city = "Pune"

print(name)
print(city)

# =================================
# Multiline String
# =================================

message = """This is
a multiline
string"""

print(message)

# =================================
# String Indexing
# =================================

text = "Python"

print(text[0])  # First character -> P
print(text[1])  # Second character -> y
print(text[-1])  # Last character -> n

# =================================
# String Slicing
# =================================

print(text[0:3])  # Pyt
print(text[2:])  # thon
print(text[:4])  # Pyth
print(text[::-1])  # Reverse string -> nohtyP

# =================================
# String Concatenation
# =================================

first = "Hello"
second = "World"

print(first + " " + second)  # Hello World

# =================================
# String Repetition
# =================================

print("Hi " * 3)  # Hi Hi Hi

# =================================
# String Length
# =================================

print(len(text))  # 6

# =================================
# String Methods
# =================================

language = "python programming"

language = "python programming"

# Change case
print(language.upper())  # PYTHON PROGRAMMING
print(language.lower())  # python programming
print(language.title())  # Python Programming
print(language.capitalize())  # Python programming
print(language.swapcase())  # PYTHON PROGRAMMING

# Find and replace
print(language.find("python"))  # 0
print(language.index("programming"))  # 7
print(language.replace("python", "Java"))  # Java programming

# Check methods
print(language.startswith("python"))  # True
print(language.endswith("ing"))  # True

print("Python".isalpha())  # True
print("123".isdigit())  # True
print("abc123".isalnum())  # True
print("python".islower())  # True
print("PYTHON".isupper())  # True
print("Python Programming".istitle())  # True
print("   ".isspace())  # True

# Remove spaces
text = "   hello world   "

print(text.strip())  # Removes spaces from both sides
print(text.lstrip())  # Removes left spaces
print(text.rstrip())  # Removes right spaces

# Split and join
sentence = "Python is easy"

words = sentence.split()
print(words)  # ['Python', 'is', 'easy']

joined = "-".join(words)
print(joined)  # Python-is-easy

# Count occurrences
print(language.count("m"))  # 2

# =================================
# Find and Replace
# =================================

print(language.find("programming"))  # 7
print(language.replace("python", "Java"))

# =================================
# Checking Methods
# =================================

print("Python".isalpha())  # True
print("123".isdigit())  # True
print("abc123".isalnum())  # True

# =================================
# Remove Spaces
# =================================

data = "   hello   "

print(data.strip())  # Removes both-side spaces
print(data.lstrip())  # Removes left spaces
print(data.rstrip())  # Removes right spaces

# =================================
# Split and Join
# =================================

sentence = "Python is easy"

words = sentence.split()
print(words)  # ['Python', 'is', 'easy']

joined = "-".join(words)
print(joined)  # Python-is-easy

# =================================
# String Formatting
# =================================

name = "Ruturaj"
age = 23

print("My name is", name, "and age is", age)

# f-string
print(f"My name is {name} and age is {age}")

# format method
print("My name is {} and age is {}".format(name, age))

# =================================
# Escape Characters
# =================================

print("Hello\nWorld")  # New line
print("Hello\tWorld")  # Tab space
print('He said "Python is easy"')

# =================================
# Membership Operator with Strings
# =================================

print("Py" in text)  # True
print("Java" not in text)  # True

# =====================
# Escape Characters
# =====================

# \n -> New Line
print("Hello\nWorld")

# Output:
# Hello
# World


# \t -> Tab Space
print("Hello\tWorld")  # Hello    World


# \\ -> Backslash
print("C:\\Users\\Ruturaj")  # C:\Users\Ruturaj


# \' -> Single Quote
print("It's Python")  # It's Python


# \" -> Double Quote
print('He said "Python is easy"')  # He said "Python is easy"


# Raw String
print(r"C:\newfolder\test")  # C:\newfolder\test
