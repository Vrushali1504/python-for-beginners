# Variable scope

"""
Variable Scope defines where a variable can be used.
Python mainly has:
1. Local Scope
2. Global Scope
"""

# ---------------------------------------------------
# Local Variable
# ---------------------------------------------------

# Variable created inside function
# Can be used only inside that function

def demo():
    x = 100
    print("Local Variable:", x)

demo()

# print(x)   # Error -> x not accessible outside function

# ---------------------------------------------------
# Global Variable
# ---------------------------------------------------

# Variable created outside function
# Can be used anywhere in program

y = 50

def show():
    print("Global Variable:", y)

show()

print(y)

# ---------------------------------------------------
# Local and Global Variable Together
# ---------------------------------------------------

a = 10

def test():
    a = 20     # Local variable
    print("Inside Function:", a)

test()

print("Outside Function:", a)

# ---------------------------------------------------
# global Keyword
# ---------------------------------------------------

# global -> Used to modify global variable inside function

count = 0

def update():
    global count
    count = count + 1
    print("Inside Function:", count)

update()

print("Outside Function:", count)

# ---------------------------------------------------
# LEGB Rule
# ---------------------------------------------------

"""
Python searches variables in this order:

L -> Local
E -> Enclosing
G -> Global
B -> Built-in
"""

name = "Global"

def outer_function():
    
    name = "Enclosing"

    def inner_function():
        
        name = "Local"
        print(name)

    inner_function()

outer_function()