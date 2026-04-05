# ----------------------------- Data Structures Intro -------------------------------------------

# inbuilt DS (list, set, dict) - ready-made, easy to use
lst = [1, 2, 3]; st = {1, 2, 3}; d = {"a": 1}

# customized DS - user defines (like stack using list)
stack = []; stack.append(10); stack.pop()   # simple stack example

# ----------------------------- List -------------------------------------------

# list = ordered collection, can store anything (int, str, bool etc)
marks = [90, 85, 78, 90]
print(marks)   # [90, 85, 78, 90]

# heterogeneous (mix types allowed)
mix = [10, "dev", 3.14, True]

# duplicate allowed
dup = [1, 2, 2, 3, 3]

# mutable (can change values)
marks[0] = 95
print(marks)   # [95, 85, 78, 90]

# syntax
lst = [1, 2, 3]

# type check
print(type(lst))   # <class 'list'>

# ----------------------------- Indexing & Slicing ----------------------------------------------
nums = [10, 20, 30, 40, 50]

print(nums[0])     # 10
print(nums[2])     # 30
print(nums[-1])    # 50

print(nums[1:4])   # [20, 30, 40]
print(nums[:3])    # [10, 20, 30]
print(nums[::2])   # [10, 30, 50]

# ----------------------------- Copy Types ------------------------------------------------------

# reference copy (same memory, both change)
a = [1, 2, 3]
b = a
b[0] = 100
print(a)   # [100, 2, 3]
print(b)   # [100, 2, 3]

# shallow copy (new list, safe for simple list)
c = [1, 2, 3]
d = c.copy()
d[0] = 200
print(c)   # [1, 2, 3]
print(d)   # [200, 2, 3]

# shallow copy issue (nested case)
x = [[1, 2], [3, 4]]
y = x.copy()
y[0][0] = 999
print(x)   # [[999, 2], [3, 4]]

# deep copy (nested safe)
import copy
p = [[1, 2], [3, 4]]
q = copy.deepcopy(p)
q[0][0] = 777
print(p)   # [[1, 2], [3, 4]]
print(q)   # [[777, 2], [3, 4]]

# ----------------------------- Traversing List -------------------------------------------------
nums = [10, 20, 30]

# direct item access
for i in nums:
    print(i) # 10 20 30

# using index
for i in range(len(nums)):
    print(nums[i]) # 10 20 30

# ----------------------------- List Methods ----------------------------------------------------
lst = [10, 20, 30]

print(lst.index(20))   # 1

lst.append(40)
print(lst)   # [10, 20, 30, 40]

lst.insert(1, 15)
print(lst)   # [10, 15, 20, 30, 40]

lst.pop()
print(lst)   # [10, 15, 20, 30]

lst.pop(1)
print(lst)   # [10, 20, 30]

lst.reverse()
print(lst)   # [30, 20, 10]

# more methods practice
lst2 = [5, 2, 9, 1]

lst2.sort()
print(lst2)   # [1, 2, 5, 9]

lst2.sort(reverse=True)
print(lst2)   # [9, 5, 2, 1]

lst2.extend([100, 200])
print(lst2)   # [9, 5, 2, 1, 100, 200]

lst2.remove(2)
print(lst2)   # [9, 5, 1, 100, 200]

print(lst2.count(9))   # 1

# clear list
lst2.clear()
print(lst2)   # []

# ----------------------------- Extra Practice --------------------------------------------------
a = [1, 2, 3]
b = a + [4, 5]
print(b)   # [1, 2, 3, 4, 5]

print(3 in b)   # True
print(len(b))   # 5

b[0:2] = [100, 200]
print(b)   # [100, 200, 3, 4, 5]

# --------------------------------- List Logic Building --------------------------------------

# 1. Sum and Average of list

marks = [86, 88, 95, 83, 86]
sum = 0
for i in marks:
    sum += i
avg = sum/(len(marks))
print("Marks : ",marks)
print("Sum of marks : ",sum)
print("Average of marks: ",avg)

# 2. Maximum Element with index

import copy
prices = [18, 36, 11, 87, 55, 87, 50, 36]
n = len(prices)
idx = 0
dup = copy.deepcopy(prices)
dup.sort()
max = dup[-1]
for i in range(n):
    if prices[i] == dup[-1]:
        idx = i
print("Max elements in the prices : ",max," with index : ",idx)

# 3. Second greatest element without sorting

list = [548, 596, 272, 475, 814, 325, 551, 365, 258, 662, 957, 120, 458, 222, 789, 911]
max_ele = list[0]
max_ele_2nd = list[0]
for i in list:
    if i > max_ele:
        max_ele = i
for i in list:
    if i != max_ele and (max_ele - i) < (max_ele - max_ele_2nd):
        max_ele_2nd = i
print("Second maximum element in the list is", max_ele_2nd)

# 4. checking list is sorted or not

import copy
l1 = [18, 36, 11, 69, 55, 37, 50, 36]
l2 = [13, 25, 27, 29, 33, 48, 59, 62]
def duplicate(list):
    dup = copy.deepcopy(list)
    dup.sort()
    return dup
def is_sorted(list):
    list_dup = duplicate(list)
    if list == list_dup:
        print("list is sorted")
    else:
        print("list is not sorted")
is_sorted(l1)
is_sorted(l2)

# 5. Left rotation by 1 

import copy
num = [11, 59, 49, 58, 86, 72, 70, 89]
l = len(num)
num_rotated = copy.deepcopy(num)
for i in range(l):
    num_rotated[i-1] = num[i]
print("actual list : ",num)
print("list that is left rotated by 1 : ",num_rotated)

# 6. Left rotation by k

k = int(input("Enter the value of k : "))
import copy
num = [11, 59, 49, 58, 86, 72, 70, 89]
l = len(num)
num_rotated = copy.deepcopy(num)
for i in range(l):
    num_rotated[i-k] = num[i]
print("actual list : ",num)
print(f"list that is left rotated by {k} : ",num_rotated)

# 7. Reversing the list

import copy
num = [48, 35, 14, 99, 75, 65, 47, 43]
l = len(num)
num_reversed = copy.deepcopy(num)
for i in range(1,l+1):
    num_reversed[-i] = num[i-1]
print("actual list : ",num)
print("Reversed List : ",num_reversed)

# 8. Linear Search

list = [74, 57, 79, 95, 9, 73, 1, 49]
ele = int(input("Enter the element you wanna search : "))
is_present = 0
for i in list:
    if i == ele:
        is_present = 1
        break
if is_present == 1:
    print(f"{ele} is in the list")
else:
    print(f"{ele} is not in the list")

# 9. Binary Search

list = [76, 79, 27, 18, 46, 37, 12, 35]
list.sort()
ele = int(input("Enter element: "))
left = 0
right = len(list) - 1
found = -1
while left <= right:
    mid = (left + right) // 2

    if list[mid] == ele:
        found = mid
        break
    elif list[mid] < ele:
        left = mid + 1
    else:
        right = mid - 1
if found != -1:
    print(f"{ele} found at index {found}")
else:
    print(f"{ele} not found")

# 10. Bubble Sort

list = [76, 79, 27, 18, 46, 37, 12, 35]
n = len(list)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
            swapped = True
    if swapped == False:
        break
print("Bubble Sorted list:", list)

# 11. Selection Sort

list = [76, 79, 27, 18, 46, 37, 12, 35]
n = len(list)
for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if list[j] < list[min_index]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[i]
print("Selection Sorted list:", list)

# 12. Insertion Sort

list = [76, 79, 27, 18, 46, 37, 12, 35]
n = len(list)
for i in range(1, n):
    key = list[i]
    j = i - 1
    while j >= 0 and list[j] > key:
        list[j + 1] = list[j]
        j -= 1
    list[j + 1] = key
print("Insertion Sorted list:", list)