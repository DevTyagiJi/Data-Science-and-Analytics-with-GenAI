# ------------------------------ FOR LOOP ------------------------------
'''
for variable in range(start, end+1, step):      # step is +ve   
    do something

for variable in range(start, end-1, step):      # step is -ve
    do something
'''

# dafault value of start is 0 and step is 1

for i in range(1, 6):
    print(i)
# 1
# 2
# 3
# 4
# 5

for i in range(2, 11, 2):
    print(i)
# 2
# 4
# 6
# 8
# 10

for ch in "Dev":
    print(ch)
# D
# e
# v

# ------------------------------ WHILE LOOP ------------------------------

'''
while (condition):
    do something
    updation
'''

# updation is important otherwise infinite loop runs and ultimately crash the code 

i = 1
while i <= 5:
    print(i)
    i += 1
# 1
# 2
# 3
# 4
# 5

i = 5
while i >= 1:
    print(i)
    i -= 1
# 5
# 4
# 3
# 2
# 1

i = 1
s = 0
while i <= 5:
    s += i
    i += 1

print(s) # 15

# ----------------------- for logic building ------------------------------------------

# 1. print HELLO WORLD n times
n = int(input("Enter the number : "))
for i in range(1,n+1):
    print("HELLO WORLD")

# 2. print numbers 1 to n
n = int(input("Enter the number : "))
for i in range(1,n+1):
    print(i)

# 3. print numbers from n to 1
n = int(input("Enter the number : "))
for i in range(n,0,-1):
    print(i)

# 4. sum of natural numbers 1 to n
n = int(input("Enter the number : "))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)

# 5. factorial of a number
n = int(input("Enter the number : "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

# 6. sum of even and odd numbers upto n
n = int(input("Enter the number : "))
even_sum = 0
odd_sum = 0
for i in range(1,n+1):
    if i%2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of even integers : ",even_sum)
print("Sum of odd integers : ",odd_sum)

# 7. print all factors of a number
n = int(input("Enter the number : "))
for i in range(1,n+1):
    if n%i == 0:
        print(i)

# 8. sum of all factors of a number
n = int(input("Enter the number : "))
sum_of_factors = 0
for i in range(1,n+1):
    if n%i == 0:
        sum_of_factors += i
print("sum of all factors = ",sum_of_factors)

# 9. power calculator (a^b)
a = int(input("Enter the base : "))
b = int(input("Enter the exponent : "))
ans = 1
for i in range(1,b+1):
    ans *= a
print("base^exponent = ",ans)

# 10. prime factor or not
n = int(input("Enter the number : "))
status = 0 # 0 for not a prime, 1 for prime number
if n==0 :
    print("0 is not a prime number")
elif n==1 :
    print("1 is not a prime number")
else :
    for i in range(2,n):
        if n%i == 0:
            status = 0
            break 
        else:
            status = 1
    if status == 0:
        print(n,"is not a prime")
    else:
        print(n,"is a prime")    
    
