# --------------------------- Tuple ---------------------------

# tuple = ordered, immutable collection
t = (1, 2, 3)
t1 = (10, 20, 30)
t2 = 10, 20, 30   # without brackets

# homogeneous / heterogeneous
homo = (1, 2, 3, 4)
hetero = (1, "dev", 3.14, True)

# immutable (cannot modify)
# t1[0] = 100   # error

dup = (1, 2, 2, 3, 3) # duplicates allowed

# single element tuple (comma important)
single = (5,)
not_tuple = (5)

print(type(single))      # tuple
print(type(not_tuple))   # int

# --------------------------- Indexing & Slicing ---------------------------
nums = (10, 20, 30, 40, 50)

print(nums[0])     # 10
print(nums[-1])    # 50
print(nums[1:4])   # (20, 30, 40)
print(nums[:3])    # (10, 20, 30)

# --------------------------- Tuple Unpacking ---------------------------
a, b, c = (1, 2, 3)
print(a, b, c)

x, *y = (10, 20, 30, 40)
print(x)   # 10
print(y)   # [20, 30, 40]

# --------------------------- Tuple Constructor ---------------------------
t3 = tuple([1, 2, 3])
t4 = tuple("dev")

# --------------------------- Traversing ---------------------------
data = (100, 200, 300)

# values
for val in data:
    print(val)

# indexes
for i in range(len(data)):
    print(i, data[i])

# --------------------------- Tuple Methods ---------------------------
t5 = (1, 2, 2, 3, 2)

print(t5.count(2))   # 3
print(t5.index(3))   # 3