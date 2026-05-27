# With

"""
The 'with' statement is used to manage resources properly.

It automatically handles:
1. Opening resource
2. Using resource
3. Closing resource (even if error occurs)

WHY USE IT?
-----------
- Prevents resource leaks
- Cleaner code
- Better error handling
========================================================
"""


# -------------------------------------------------------
# 1. FILE HANDLING USING WITH
# -------------------------------------------------------

# Without "with" → you must manually close file
file = open("demo.txt", "w")
file.write("Hello World")
file.close()  # ❌ manual close needed


# Using "with" → automatic file closing
with open("demo.txt", "w") as file:
    # File is automatically opened
    file.write("Hello using WITH statement")

# File is automatically closed here (no need to call close())


# -------------------------------------------------------
# 2. READING FILE USING WITH
# -------------------------------------------------------

with open("demo.txt", "r") as file:
    content = file.read()
    print("\nFile Content:")
    print(content)


# -------------------------------------------------------
# 3. WHY WITH IS IMPORTANT (ERROR SAFETY)
# -------------------------------------------------------

try:
    with open("demo2.txt", "r") as file:
        data = file.read()
        print(data)

except FileNotFoundError:
    print("\nError: File not found!")

# Even if error happens → file is safely closed


# -------------------------------------------------------
# 4. WITH WORKS WITH CONTEXT MANAGERS
# -------------------------------------------------------

# Built-in examples:
# - open() for files
# - threading.Lock()
# - database connections


import threading

lock = threading.Lock()

with lock:
    # Only one thread can execute this block at a time
    print("\nLock acquired safely using WITH")


# -------------------------------------------------------
# 5. CUSTOM CONTEXT MANAGER (ADVANCED)
# -------------------------------------------------------

class MyContext:
    def __enter__(self):
        print("\nEntering context (setup)")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context (cleanup)")
        if exc_type:
            print("Error occurred:", exc_val)
        return True  # suppress exception


with MyContext() as obj:
    print("Inside with block")
    # raise ValueError("Something went wrong")  # try uncomment
