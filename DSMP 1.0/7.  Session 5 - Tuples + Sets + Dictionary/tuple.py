# Tuples
# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.
# In short, a tuple is an immutable list. A tuple can not be changed in any way once it is created.


# Characterstics
# 1. Ordered
# 2. Unchangeble
# 3. Allows duplicate

# Plan of Attack
# 1. Creating a Tupple
t1 = ()
print(t1) # ()

t2 = (2)
print(t2) # 2 (It's not tuple, it's integer)

# To make it singal tuple use comma (,)
t3 = (2,)
print(t3) # (2,)

# Homo
t4 = (1,2,3,4,5)
print(t4) # (1,2,3,4,5)

# Hetro
t5 = (1, True, "Abhishek", (10, 20))
print(t5) # (1, True, "Abhishek", (10, 20))

# Using type conversion
t6 = tuple("hello") 
print(t6) # ("h", "e", "l", "l", "o")


# 2. Accessing items
# Indexing
tuple1 = (1,2,3,4,5)
print(tuple1[1]) # 2
print(tuple1[-1]) # 5

# Slicing
tuple2 = (1,2,3,4,5)
print(tuple2[0:3]) # (1,2,3,4)

# 3. Editing items
tuple3 = (1,2,3,4,5)
tuple3[0] = 10 # Error: Because it's immutable just like string

# 4. Adding items
# You can not add new item in tuple, because it's immutable just like string

# 5. Deleting items
tuple3 = (1,2,3,4,5)
del tuple3 # You can delete whole tuple3
del tuple3[0] # Error: Because it's immutable just like string


# 6. Operations on Tuples

# + Operation
t1 = (1,2,3,4,5)
t2 = (6,7,8,9,10)
t3 = t1 + t2
print(t3) # (1,2,3,4,5,6,7,8,9,10)

# * Operation
t1 = (1,2,3,4,5)
print(t1 * 3) # (1,2,3,4,5,1,2,3,4,5,1,2,3,4,5)

# Membership
t1 = (1,2,3,4,5)
print(1 in t1) # True
print(6 not in t1) # True

# Iteration
t1 = (1,2,3,4,5)
for i in t1:
    print(i) # 1,2,3,4,5


# 7. Tuple Functions

# len
t1 = (1,2,3,4,5) 
print(len(t1)) # 5

# sum
t1 = (1,2,3,4,5) 
print(sum(t1)) # 15

# min
t1 = (1,2,3,4,5) 
print(min(t1)) # 1

# max
t1 = (1,2,3,4,5) 
print(max(t1)) # 5

# sorted
t2 = (1,2,30,41,5) 
print(sorted(t2)) # (1,2,5,30,41) 
print(sorted(t2, reverse=True)) # (5,41,30,2,1) 

# count
t3 = (1,2,30,41,5, 1)
print(t3.count(1)) # 2

# index
t4 = (1,2,30,41,5, 1)
print(t3.index(41)) # 3



# To check Tuples are faster than Lists
import time
L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
    i * 5
print('List time', time.time() - start) # 9.85....

start = time.time()
for i in T:
    i * 5
print('Tuple time', time.time() - start) # 8.43....

# To check Tuple takes less memory than list
import sys
L = list(range(1000))
T = tuple(range(1000))

print('List size', sys.getsizeof(L)) # 9120
print('Tuple size', sys.getsizeof(T)) # 8056


# Special Syntax

# Tuple Unpacking
a,b,c = (1,2,3)
print(a, b, c) # 1, 2, 3

a, b = (1,2,3) # Error :- Extra value

a = 10
b = 20
a,b = b,a
print(a, b) # 20, 10

# Ignore extra values
a, b, *others = (1,2,3,4,5)
print(a, b) # 1, 2
print(others) # [3,4,5]

# Zipping Tuples
t1 = (1,2,3)
t2 = (4,5,6)
list_data = list(zip(t1, t2))
tuple_data = tuple(zip(t1, t2))

print(list_data) # [(1,4), (2,5), (3,6)]
print(tuple_data) # ((1,4), (2,5), (3,6))