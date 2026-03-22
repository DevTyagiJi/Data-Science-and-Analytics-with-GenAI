#----------------------------------- logic building ------------------------------------

# 1. Compare Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("First number is greater")
elif b > a:
    print("Second number is greater")
else:
    print("Both numbers are equal")

# 2. Greet by Gender (m/f)
gender = input("\nEnter gender (m/f): ")

if gender == 'm':
    print("Hello Sir")
elif gender == 'f':
    print("Hello Ma'am")
else:
    print("Invalid input")

# 3. Gender with Case Handling
gender = input("\nEnter gender (m/f): ")

if gender.lower() == 'm':
    print("Hello Sir")
elif gender.lower() == 'f':
    print("Hello Ma'am")
else:
    print("Wrong input")

# 4. Even or Odd Checker
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 5. Voting Eligibility
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name, "is eligible to vote")
else:
    print(name, "is not eligible. Wait", 18 - age, "years")

# 6. Day Number to Day Name (1-7)
day = int(input("\nEnter day number (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")
else:
    print("Invalid input")

# 7. Greatest of Three Numbers
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a == b == c:
    print("All numbers are equal")
elif a == b or b == c or a == c:
    print("Two numbers are equal")
else:
    if a > b and a > c:
        print("Greatest is:", a)
    elif b > c:
        print("Greatest is:", b)
    else:
        print("Greatest is:", c)

# 8. Leap Year Checker
year = int(input("\nEnter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 9. Shop Discount Calculator
amount = float(input("\nEnter purchase amount: "))

if amount > 5000:
    discount = amount * 0.20
elif amount > 1000:
    discount = amount * 0.10
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Bill:", final_amount)

# 10. Vowel or Consonant
ch = input("Enter a character: ")

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")