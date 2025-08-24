# What is an iteration?

num = [1,2,3]
for i in num:
    print(i) # 1,2,3

###################################################################

# What is an iterator?
import sys
L = [x for x in range(1,10000)]

for i in L:
    print(i * 2)
    
print(sys.getsizeof(L))  # Size of list in bytes - 85176

x = range(1,10000)
print(sys.getsizeof(x))  # Size of range object in bytes - 48

###################################################################

# What is Iterable?
L = [1,2,3,4]
type(L)  # list

# L is an iterable
iter(L)  # <list_iterator at 0x7f8e8c2d1d90>

###################################################################

# To check if an object is iterable or not
from collections.abc import Iterable

L = [1,2,3,4]
isinstance(L, Iterable)  # True

num = 1234
isinstance(num, Iterable)  # False

s = "hello"
isinstance(s, Iterable)  # True

d = {'a':1, 'b':2}
isinstance(d, Iterable)  # True

t = (1,2,3)
isinstance(t, Iterable)  # True

s = {1,2,3}
isinstance(s, Iterable)  # True

# Or you can use dir() function
dir(L)  # '__iter__' is present in the list of attributes and methods

###################################################################

# # To check if an object is iterator or not
from collections.abc import Iterator
L = [1,2,3,4]
isinstance(L, Iterator)  # False

it = iter(L)
isinstance(it, Iterator)  # True

# Or you can use dir() function
dir(it)  # '__next__' is present in the list of attributes and methods

###################################################################

# Understanding how for loop works in Python
L = [1,2,3,4]

for i in L:
    print(i)

# Step 1: fetch the iterator object from the iterable
it = iter(L)

# Step 2: keep calling next() to fetch the next element
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 4
print(next(it))  # StopIteration Error

# This is exactly how for loop works in Python internally

###################################################################

# Making our own for loop
def my_for_loop(iterable):
    iterator = iter(iterable)

    while True:
        try:
            element = next(iterator)
            print(element)
        except StopIteration:
            break

a = [1,2,3,4]
b = range(1,11)
c = (1,2,3,4)
d = { 1,2,3,4 }
e = { 0: 1, 1: 2, 2: 3 }

my_for_loop(a) # 1 2 3 4
my_for_loop(b) # 1 2 3 4 5 6 7 8 9 10
my_for_loop(c) # 1 2 3 4
my_for_loop(d) # 1 2 3 4 (order may vary)
my_for_loop(e) # 0 1 2 (order may vary)

###################################################################

# A confusing point

num = [1,2,3]
iter_obj = iter(num)
iter_obj2 = iter(iter_obj) # Confusion: iter() called on an iterator returns the same iterator

iter_obj is iter_obj2  # True
print(id(iter_obj), id(iter_obj2))  # Same id

next(iter_obj)  # 1
next(iter_obj2) # 1

###################################################################

# Let's create our own range() function

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self)

class MyRangeIterator:
    def __init__(self, iterable_obj):
        self.iterable = iterable_obj

    def __iter__(self):
       return self

    def __next__(self):
       if self.iterable.start >= self.iterable.end:
           raise StopIteration
       else:
           current = self.iterable.start
           self.iterable.start += 1
           return current
       
r = MyRange(1,11)
for i in r:
    print(i)  # 1 2 3 4 5 6 7 8 9 10
type(r)  # __main__.MyRange
isinstance(r, Iterable)  # True
isinstance(r, Iterator)  # False