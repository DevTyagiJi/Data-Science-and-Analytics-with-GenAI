# --------------------------- Set ---------------------------
# set = unordered, mutable collection, no duplicates

s1 = {1, 2, 3}
s2 = set([4, 5, 6])   # using constructor

# empty set is NOT {}
d = {}        # this is dict
empty_set = set()

homo = {1, 2, 3}
hetero = {1, "dev", 3.14, True}

# mutable (can modify)
s1.add(10)

# duplicates NOT allowed
dup = {1, 2, 2, 3, 3}
print(dup)   # {1, 2, 3}

# only hashable values allowed
# hashable = immutable types like int, str, tuple
valid = {1, "a", (1, 2)}

# invalid (unhashable)
# s = {[1, 2], {3, 4}}   # error (list, set not allowed)

# unordered → no indexing / slicing
# s1[0] error

# --------------------------- Set Constructor ---------------------------
a = set([1, 2, 2, 3])      # removes duplicates → {1,2,3}
b = set("hello")           # {'h','e','l','o'}
c = set((10, 20, 30))      # from tuple

# --------------------------- Traversing ---------------------------
data = {100, 200, 300}

for val in data:   # order is random
    print(val)

# --------------------------- Methods ---------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.add(10)
print(A)        # {1, 2, 3, 4, 10}

temp = {1, 2}
temp.clear()
print(temp)     # set()

C = A.copy()
print(C)        # {1, 2, 3, 4, 10}

print(A.difference(B))   # {1, 2, 10}
print(A - B)             # {1, 2, 10}

print(A.intersection(B)) # {3, 4}
print(A & B)             # {3, 4}

print(A.union(B))        # {1, 2, 3, 4, 5, 6, 10}
print(A | B)             # {1, 2, 3, 4, 5, 6, 10}

A.discard(100)
print(A)                 # {1, 2, 3, 4, 10}

print(A.isdisjoint({7, 8}))   # True

print({1, 2}.issubset(A))     # True
print(A.issuperset({1, 2}))   # True

x = A.pop()
print(x)   # any one element (random)
print(A)   # remaining elements (order random)

print(A.symmetric_difference(B))  # elements not common
print(A ^ B)                      # same result