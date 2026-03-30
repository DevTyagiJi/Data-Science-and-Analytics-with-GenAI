# ------------------------ functions ---------------------

# Basic Function Syntax
def greet():
    print("Hello, welcome!")
greet()   # function calling

# Function with Parameters
def greet_user(name):
    print("Hello", name)
greet_user("Dev")

# Multiple Parameters
def add(a, b):
    print("Sum:", a + b)
add(5, 7)

# ------------------------ Return vs Print ------------------------------------------

def using_print(a, b):
    print(a + b)
def using_return(a, b):
    return a + b

using_print(2, 3)          # only prints
result = using_return(2, 3)
print("Returned:", result) # stores + prints

# Default Parameters
def power(base, exp=2):
    return base ** exp
print(power(5))     # default exp = 2
print(power(5, 3))  # custom exp

# Keyword Arguments
def student(name, age):
    print(name, age)
student(age=20, name="Dev")  # order doesn't matter

# --------------------- args and kwargs ---------------------------

# *args = multiple values (tuple)
# **kwargs = key-value pairs (dict)

# Arbitrary Arguments (*args)
def total_sum(*args):
    s = 0
    for i in args:
        s += i
    print("Sum:", s)

total_sum(1, 2, 3, 4, 5)


# Arbitrary Keyword Arguments (**kwargs)
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

user_info(name="Dev", age=20, city="Delhi")


# Function Returning Multiple Values
def calc(a, b):
    return a+b, a-b, a*b

x, y, z = calc(10, 5)
print("Add:", x, "Sub:", y, "Mul:", z)


# Nested Function
def outer():
    def inner():
        print("Inside inner function")
    inner()

outer()


# -------------------------- Lambda Function -------------------
# one line function
square = lambda x: x*x
print("Square:", square(4))


# Recursion Example (Factorial)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print("Factorial:", fact(5))


# Function with List
def even_count(lst):
    count = 0
    for i in lst:
        if i % 2 == 0:
            count += 1
    return count

print("Even numbers:", even_count([1,2,3,4,5,6]))


# Passing Function as Argument
def multiply(x):
    return x * 2
def square(x):
    return x * x
def apply_operation(func, value):
    result = func(value)
    print("Result:", result)

apply_operation(multiply, 5)   # 5 * 2 = 10
apply_operation(square, 5)     # 5 * 5 = 25