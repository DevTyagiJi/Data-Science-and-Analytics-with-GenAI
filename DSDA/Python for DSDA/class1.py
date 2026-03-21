# ----------------------------- Comments -----------------------------------------------
# # single line comments
# i am Dev Tyagi

# multi line comments

'''i learn poython for data sience and data analytics
which is important for placements'''

# ------------------------------- Variables ------------------------------------------------
x = 23
age = 18
name =  "Dev"

# --------------------- Naming Conventions of variable ---------------------------------------------

# camel case - rahulAge
# pascal case - RahulAge
# snake case - rahul_age

# you can not start a variable with number 
# you can not use space in variable name
# you can not use any special character in variable name but only underscore (_)

# ---------------------------- Data Types --------------------
a = 45
b = 1.66
c = 2+3j
name = "Dev"
valid = True

print(type(a)) # itn
print(type(b)) # float
print(type(c)) # complex
print(type(name)) # str
print(type(valid)) # bool

# ----------------------- String Indexing --------------------
# strings are both +ve indexed and -ve indexed
# space in a string is also indexed
# strings are immutable , name[1] = O gives error

name =  "DEV TYAGI"

#  0  1  2  3  4  5  6  7  8  (+ve indexing)
#  D  E  V     T  Y  A  G  I
# -9 -8 -7 -6 -5 -4 -3 -2 -1  (-ve indexing)

print(name[4]) # T
print(name[-8]) # E

# ----------------------- String Slicing --------------------
# [start : stop+1 : steps]
# default value [0 : upto last indexing : 1]

name =  "DEV TYAGI"

print(name[4:9:1]) # TYAGI
print(name[-5::1]) # TYAGI
print(name[:6:]) # DEV TY
print(name[::2]) # DVTAI
print(name[1:6:2]) # E Y

# -------------------- Escape Sequences -----------------------
"""
\n  -> New Line (moves text to next line)
\t  -> Tab Space (adds horizontal space)
\b  -> Backspace (removes last character)
f-string -> used to insert variables inside string
raw string -> ignores escape sequences
"""

print("Hello\nWorld")
# Hello
# World

print("Hello\tWorld")
# Hello    World

print("Helloo\b")
# Hello 

name = "Dev"
age = 20

print(f"My name is {name} and I am {age} years old")
# My name is Dev and I am 20 years old

print("C:\newfolder\test")
# \n and \t will act as escape sequences (wrong output)

print(r"C:\newfolder\test")
# Output: C:\newfolder\test

# ------------------- Type Conversion ------------------------
"""Type Conversion means converting one data type into another.

Types:
1. Implicit Type Conversion (automatic by Python)
2. Explicit Type Conversion (manual by user)
"""

# Implicit Type Conversion (Python automatically converts smaller type to larger type)

a = 5       # int
b = 2.5     # float

c = a + b   # int -> float automatically
print(c)    
print(type(c))  
# Output: 7.5 <class 'float'>

# Explicit Type Conversion (User manually converts data type using functions)

# int() -> convert to integer
x = "10"
print(int(x))        # Output: 10

# float() -> convert to float
y = "5.5"
print(float(y))      # Output: 5.5

# str() -> convert to string
z = 100
print(str(z))        # Output: "100"

# int to float
print(float(5))      # 5.0

# float to int
print(int(5.9))      # 5 (decimal removed)

# number to string
print(str(123))      # "123"

# Invalid conversion gives error
# print(int("abc"))  -> ValueError

# Falsey Values
"""Falsy values → treated as False in Python:
0, 0.0, False, None, "", [], {}
"""
print(bool(0))        # False
print(bool(0.0))      # False
print(bool(False))    # False
print(bool(None))     # False
print(bool(""))       # False (empty string)
print(bool([]))       # False (empty list)
print(bool({}))       # False (empty dictionary)

# ----------------------Input Statements ------------------
"""input() is used to take user input.
By default, input is always taken as string.
"""

name = input("Enter your name: ")
print(name)

# Type conversion with input
age = int(input("Enter age: "))
print(age)

# Multiple inputs
a, b = input("Enter two values: ").split()
print(a, b)