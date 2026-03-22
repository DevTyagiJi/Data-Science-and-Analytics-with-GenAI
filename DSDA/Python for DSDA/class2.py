# ----------------------------- Arithmetic Operators -----------------------------------------------
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333... (always gives float)
print(a // b)  # 3 (gives integer quotient)
print(a ** b)  # 1000 (exponent)
print(a % b)   # 1 (remainder)

# ----------------------------- BODMAS / Operator Precedence ---------------------------------------

"""
B - Brackets
O - Orders (power)
D - Division
M - Multiplication
A - Addition
S - Subtraction
"""

result1 = 10 + 2 * 3        # 10 + (2*3) = 16
result2 = (10 + 2) * 3      # (12)*3 = 36
result3 = 2 ** 3 * 4        # (2^3)*4 = 32

# ----------------------------- Assignment Operators -----------------------------------------------

"""
=    simple assignment
+=   add and assign
-=   subtract and assign
*=   multiply and assign
/=   divide and assign
//=  floor divide and assign
%=   modulus and assign
"""

x = 10

x += 5 # 15
x -= 3 # 12
x *= 2 # 24
x /= 4 # 6.0
x //= 2 # 3.0
x %= 2 # 1.0

# ----------------------------- String Concatenation -----------------------------------------------
first_name = "Dev"
last_name = "Tyagi"

full_name = first_name + " " + last_name
print(full_name)  # Dev Tyagi


# ----------------------------- String Multiplication ----------------------------------------------
text = "Hi "
print(text * 3)   # Hi Hi Hi 

line = "-" * 20
print(line)       # --------------------

# ----------------------------- Comparison Operators -----------------------------------------------

"""
==   Equal to
!=   Not equal to
>    Greater than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
"""

a = 10
b = 20

print(a == b)   # False
print(a != b)   # True
print(a > b)    # False
print(a < b)    # True
print(a >= b)   # False
print(a <= b)   # True

# ----------------------------- Trivial Examples ----------------------------------------------------

print(136 < 120)     # False
print(50 == 50)      # True
print(99 != 100)     # True
print(45 >= 45)      # True
print(10 <= 5)       # False

# ----------------------------- Logical Operators ---------------------------------------------------

"""
and - True if both conditions are True
or  - True if at least one condition is True
not - Reverse the result (True becomes False, False becomes True)
"""

x = 15
y = 5

print(x > 10 and y < 10)   # True
print(x > 20 and y < 10)   # False

print(x > 20 or y < 10)    # True
print(x > 20 or y > 10)    # False

print(not(x > 10))         # False
print(not(x < 10))         # True

"""
bool(0) - False
bool(1) - True
"""

print(bool(0))   # False
print(bool(1))   # True

print(bool(0) and bool(1))   # False
print(bool(1) and bool(1))   # True

print(bool(0) or bool(1))    # True
print(bool(0) or bool(0))    # False

print(not(bool(0)))          # True
print(not(bool(1)))          # False

# ----------------------------- Combined Examples ---------------------------------------------------

age = 18
has_id = True

print(age >= 18 and has_id)     # True
print(age < 18 or has_id)       # True
print(not(has_id))              # False

# ----------------------------- if, else -----------------------------------------------
age = 18

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")

# pass - used as a placeholder (does nothing)

x = 10
if x > 5:
    pass   # we will write logic later
else:
    print("x is small")

# ----------------------------- Ternary Operator -----------------------------------------------
num = 7

result = "Even" if num % 2 == 0 else "Odd"
print(result)

# ----------------------------- elif Statement --------------------------------------------------
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")


# ----------------------------- elif vs multiple if ---------------------------------------------

# multiple if (all conditions are checked)
num = 80

if num > 50:
    print("Greater than 50") 

if num > 70:
    print("Greater than 70")
# both will run

# elif (stops after first true condition)
num = 80

if num > 50:
    print("Greater than 50")
elif num > 70:
    print("Greater than 70")   # this will NOT run

# ----------------------------- Greatest of 3 numbers (using logical operators) -----------------
a = 10
b = 25
c = 15

if a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")