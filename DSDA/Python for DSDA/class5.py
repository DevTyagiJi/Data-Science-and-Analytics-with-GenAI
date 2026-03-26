# ------------------------------ while loop logic building---------------------------------

# 1. Print Each Digit (Reverse Order)
num = int(input("Enter a number: "))
while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num = num // 10

# 2. Sum of Digits
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10
print("Sum of digits:", sum_digits)

# 3. Reverse a Number
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)

# 4. Palindrome Number Check
num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")

# 5. Automorphic Number
num = int(input("Enter a number: "))
square = num * num
temp = num
is_automorphic = True
while temp > 0:
    if temp % 10 != square % 10:
        is_automorphic = False
        break
    temp = temp // 10
    square = square // 10
if is_automorphic:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")

# -------------------- number guessing game ----------------------------
import random 
num = random.randint(1,100)

tries = 0
guess = int(input("Enter your guess : "))

while guess!=num :
    if guess > num:
        print("wrong one , try some lower number")
        guess = int(input("Enter your guess : "))
        tries += 1
    else:
        print("wrong one , try some upper number")
        guess = int(input("Enter your guess : "))
        tries += 1
print(f'you guessed it right man number was {num} you took {tries} tries to guess.')