# Sets

# empty
s1 = {}
print(s1) # {}
print(type(s1)) # <class 'dict'>

# To create proper set
s2 = set()
print(s2) # set()
print(type(s2)) # <class 'set'>

# 1D and 2D set
s3 = { 1,2,4 }
print(s3) # {1,2,3}

s4 = {1,2,3, {4,5,6}}
# print(s4) # TypeError: unhashable type: 'set'

# Homo and Hetro
s5 = {1,2,3}
s6 = {1, "Abhishek", True, (10, 20, 30)}
print(s5) # {1,2,3}
print(s6) # {1, "Abhishek", (10, 20, 30)} (True will not show because True means 1 and 1 is duplicate, but set contains only unique value)


# Using type conversion
s1 = set([1, 2, 3])
print(s1) # { 1, 2, 3 }

# Set can't have mutable items
s2 = {1,2,[3,4]}
print(s2) # TypeError: unhashable type: 'list'


# Accessing items
s1 = {1,2,3,4}
print(s1[3]) # TypeError: 'set' object is not subscriptable

# Editing items
s1 = {1,2,3,4}
s1[0] = 100 # # TypeError: 'set' object is not item assignment

# Adding items
s1 = {1,2,3,4}
s1.add(100) # It can add only one item
print(s1) # {1,2,3,4,100}

# Updating items
s1 = {1,2,3,4}
s1.update([10,20,30]) # It can update multiple items
print(s1) # {1,2,3,4,10,20,30}

# Deleting items

# del
s1 = {1,2,3,4}
del s1 # Delete whole s1 set

# discard
s1 = {1,2,3,4}
s1.discard(4) # It will not throw error if element not found
print(s1) # {1,2,3}

# remove
s1 = {1,2,3,4}
s1.remove(3) # It will throw error if element not found
print(s1) # {1,2,4}

# pop
s1 = {1,2,3,4}
s1.pop()
print(s1) # Delete random item

# clear
s1 = {1,2,3,4}
s1.clear()
print(s1) # Delete whole set



# Set Operation

# Union (|)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1 | s2) # {1,2,3,4,5,6,7,8}

# Intersection (&)
print(s1 & s2) # {4,5}

# Difference (-)
print(s1 - s2) # {1,2,3} (Items, which is not preset in s2)
print(s2 - s1) # {6,7,8} (Items, which is not preset in s1)

# Symmetric Difference (^)
print(s1 ^ s2) # {1,2,3,6,7,8}

# Membership Test
print(1 in s1) # True
print(1 not in s1) # False

# Iteration
for i in s1:
    print(i) # 1,2,3,4,5



# Set Functions

# len
s1 = {3, 4, 5, 1, 7}
print(len(s1)) # 5

# sum
print(sum(s1)) # 20

# min
print(min(s1)) # 1

# max
print(max(s1)) # 7

# sorted
print(sorted(s1)) # [3,4,5,1,7]

# union
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2)) # {1,2,3,4,5,6,7,8}

# update
s1.update(s2)
print(s1) # {1,2,3,4,5,6,7,8}
print(s2) # {4,5,6,7,8}

# intersection
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.intersection(s2)) # {4,5}

# intersection_update
s1.intersection_update(s2)
print(s1) # {4,5}
print(s2) # {4,5,6,7,8}

# difference
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.difference(s2)) # {1,2,3}

# difference_update
s1.difference_update(s2)
print(s1) # {1,2,3}
print(s2) # {4,5,6,7,8}

# symmetric_difference
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.symmetric_difference(s2)) # {1,2,3,6,7,8}

# symmetric_difference_update
s1.symmetric_difference_update(s2)
print(s1) # {1,2,3,6,7,8}
print(s2) # {4,5,6,7,8}

# isdisjoint
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1.isdisjoint(s2)) # False (3,4 is common)

# issubset
s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issubset(s2)) # True (because {3,4,5} inside s1)

# issuperset
s1 = {1,2,3,4,5}
s2 = {3,4,5}
print(s1.issuperset(s2)) # True (because {3,4,5} inside s1)

# copy
s1 = {1,2,3,4,5}
s2 = s1.copy()
print(s1) # {1,2,3,4,5}
print(s2) # {1,2,3,4,5}



# Frozenset
# Frozen set is just an immutable version of a python set object
# It is immutable, also you can do anything like add,remove...

fs = frozenset([1,2,3])
print(fs) # {1,2,3}
fs.add(10) # Error: You can add.

# What works and what does not
# work - all read functions
# does't work - write operations

fs1 = frozenset({1,2,3})
fs2 = frozenset({3,4,5})
print(fs1 | fs2) # {1,2,3,4,5}

# Note :- All the operations will work, only addition, deletion, and modification will not work.


# When to use
# - For read only

# 2D frozenset
fs = frozenset([1,2, frozenset([3,4])])
print(fs) # frozenset({1,2, frozenset({3,4})})


# Set Comprehension
{i for i in range(1,11)} # {1,2,3,4,5,6,7,8,9,10}
{i for i in range(1,11) if i > 5} # {6,7,8,9,10}
