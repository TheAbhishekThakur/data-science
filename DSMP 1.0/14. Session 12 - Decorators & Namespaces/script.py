# local and global

## Example 1
a = 2

def temp():
    b = 3
    print(b) # local variable - 3

print(a) # global variable - 2
temp()

##########################################################################

## Example 2
a = 2

def temp():
    a = 3
    print(a) # local variable - 3

print(a) # global variable - 2
temp()

##########################################################################

# local and global -> local does not have but global has
a = 2

def temp():
    print(a) # global variable - 2

print(a) # global variable - 2
temp()


##########################################################################

# local and global -> local does not have but global has
a = 2

def temp():
    print(a) # global variable - 2

print(a) # global variable - 2
temp()


##########################################################################

# local and global -> editing global (Problem)
a = 2

def temp():
    a += 1 # UnboundLocalError: local variable 'a' referenced before assignment
    print(a)

print(a) # global variable - 2
temp()


# local and global -> editing global (Solution)
a = 2

def temp():
    global a
    a += 1 # 3

print(a) # 3
temp()


##########################################################################

# local and global -> global created inside local
def temp():
    global a
    a = 1
    print(a) # 1

temp()
print(a) # 1

##########################################################################

# local and global -> function parameter is local
def temp(z):
    print(z) # 5

a = 5
temp(5)
print(a) # 5


##########################################################################

# built-in scope
print("Hello World") # Hello World
input() # waits for user input
len("Hello") # 5
list() # []
# etc.

##########################################################################

# How to see all the built-in
import builtins
print(dir(builtins))
# Output: ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',  ...]

##########################################################################

# renaming built-ins
L = [1, 2, 3]
max(L) # 3

def max():
    return "Hello"

max(L) # TypeError: max() takes 0 positional arguments but 1 was given
max() # "Hello"

##########################################################################

# Enclosing scope -> nested functions
def outer():
    a = 1
    def inner():
        print(a) # 1
    inner()

outer()

##########################################################################

# nonlocal keyword

## Problem
def outer():
    a = 1
    def inner():
        a += 1 # UnboundLocalError: local variable 'a' referenced before assignment
        print(a)
    inner()

outer()

## Solution
def outer():
    a = 1
    def inner():
        nonlocal a
        a += 1 # 2
        print(a)
    inner()

outer()

############################### Decorators ###########################################

## Python are first class functions
def func(value):
    print(value)

a = func # assign the function to a variable
# del func # delete the name func
a(10) # 10

def modify(func, num): # you can pass function as parameter
    return func(num)

modify(func, 20) # 20

##########################################################################

## simple example
def my_decorator(func):
    def wrapper():
        print("***************")
        func()
        print("***************")
    return wrapper

def say_hello():
    print("Hello World")

a = my_decorator(say_hello) # decorate the function
a() # call the decorated function

### Better Syntax using @ 

def my_decorator(func):
    def wrapper():
        print("***************")
        func()
        print("***************")
    return wrapper

@my_decorator
def say_hello():
    print("Hello World")
    
say_hello()

# Output:
# ***************
# Hello World
# ***************


##########################################################################

## anything meaningful?
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print("Time taken by", func.__name__, time.time() - start, "seconds")
    return wrapper


@timer
def hello():
    print("Hello World")
    time.sleep(2)

hello() # Time taken by hello 2.002345323562622 seconds

##########################################################################

## decorator with parameters
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print("Time taken by", func.__name__, time.time() - start, "seconds")
    return wrapper

@timer
def add(a, b):
    print(a + b)
    time.sleep(2)

add(2, 3) # 5 \n Time taken by add 2.002345323562622 seconds


##########################################################################

# A big problem with decorators
def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
           if type(args[0]) == data_type:
               func(*args)
           else:
               raise TypeError("Invalid Input")
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(n):
    print(n * n)

@sanity_check(str)
def greet(name):
    print("Hello", name)

square(5) # 25
square("5") # Invalid Input

greet("John") # Hello John
greet(5) # Invalid Input