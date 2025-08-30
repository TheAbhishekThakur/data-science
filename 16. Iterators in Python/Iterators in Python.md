# What is an iteration?
Iteration is a general term for taking each item of something, one after another.
Any time you use a loop, explicit or implicit, to go over a group of items, that is iteration.

Example:
```
num = [1,2,3]
for i in num:
    print(i) # 1,2,3
```

# What is Iterators?

An iterator is an object that allows the programmer to traverse through a sequence of data without having to store the entire data in the memory.

In Python, iterators are objects that allow you to traverse through all the elements of a collection (like lists, tuples, or dictionaries) one at a time, without needing to use indexing.

## Key Concepts
- `Iterable`: An object capable of returning its members one at a time. Examples include lists, tuples, strings, and dictionaries. Any object with an __iter__() method is iterable.

- `Iterator`: An object representing a stream of data; it returns the next value when you call next() on it. Iterators implement both the __iter__() and __next__() methods.

Note: When you use the loop internally `Iterators` works.



# What is Iterable?
Iterable is an object, which one can iterate over.
It generates an iterator when passed to iter() method.

```
L = [1,2,3,4]
type(L)  # list

# L is an iterable
iter(L)  # <list_iterator at 0x7f8e8c2d1d90>
```


## Point to remember
- Every Iterator is also and Iterable.
- Not all Iterables are Iterators.

## Trick
- Every Iterable has an `iter()` function.
- Every Iterator has both `iter()` function as well as a `next()` function.
