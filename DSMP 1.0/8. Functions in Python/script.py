# Functions in Python

# Create a function (with docstring)
def isEven(num):
    """
    This function returns if a given number is odd or even
    input - Any valid integer
    output - odd/even
    create on - 07th Aug 2025
    created by - Abhishek Thakur
    """

    if type(num) != int:
        return "Invalid input type"

    if num % 2 == 0:
        return "even"
    else:
        return "odd"

value = isEven("5") # "Invalid input type"
value = isEven(5) # "Invalid input type"
print(value) # odd

# To view the documentation
print(isEven.__doc__)
# Output
# This function returns if a given number is odd or even
#    input - Any valid integer
#    output - odd/even
#    create on - 07th Aug 2025
#    created by - Abhishek Thakur


# Types of Arguments

# 1. Default Argument
def power(a = 1, b = 1):
    return a**b
print(power(10,2)) # 100

# 2. Positional Argument
def power(a = 1, b = 1): # Order will be the sequentional of arguments and parameters
    return a**b
print(power(10,2)) # 100

# 3. Keyword Argument
def power(a = 1, b = 1):
    return a**b
print(power(b=3,a=2)) # 8


# *args and **kwargs
# *args and **kwargs are special python keyword that are used to pass the variable length of arguments to a function

# *args
# Allows us to pass a variable number of non-keyword arguments to a function.
def multiply(*args): # args converts all the parameters into the tuple, also you can use any name instead of args it's optional
    product = 1
    for i in args:
        product = product * i
    return product

print(multiply(1,2,3,4,5,6,7,8,9,10)) # 3628800



# **kwargs
# Allows us to pass a variable number of keyword arguments to a function.
def display(**kwargs): # args converts all the parameters into the tuple, also you can use any name instead of args it's optional
    for (key, value) in kwargs.items():
        print(key, '->', value)

display(india="delhi",srilanka="colombo", nepal="kathmandu")

# Output
# india -> delhi
# srilanka -> colombo
# nepal -> kathmandu


# Points to remember while using *args and **kwargs
# 1. Order of the arguments matter (normal -> *args -> **args)
# 2. The words "args" and "kwargs" are only a convention, you can use any name of your choice


# How Functions are executed in memory?

# What does it return?
# If a function has no return statement, or just return without a value, it automatically returns:
# None
# For ex: L = [1,2,3]
# print(L.append(4)) # None
# pring(L) # [1,2,3,4]


# Variable Scope
# Example 1:
def g(y): # y local variable
    print(x) # 5
    print(x+1) # 6

x = 5 # Global Variable
g(x)
print(x) # 5


# Example 2:
def f(y): # y local variable
    x = 1
    x += 1
    print(x) # 2
x = 5 # Global Variable
f(x)
print(x) # 5


# Example 3:
def h(y): # y local variable
    x += 1 # Error: You can use global variable but you can't change it.
x = 5 # Global Variable
h(x)
print(x) 


# Example 4:
def h(y): # y local variable
    global x
    x += 1
x = 5 # Global Variable
h(x)
print(x) # 6


# Example 5:
def f(x):
    x = x + 1
    print('in f(x): x =', x) # 4
    return x
x = 3
z = f(x)
print('in main program scope: z=', z) # 4
print('in main program scope: x=', x) # 3


# Nested Functions
# Example 1:
def f():
    print('inside f function')
    def g():
        print('inside g function')
    g()
f()

# Example 2:
def g(x):
    def h(x):
        x = x + 1
        print("in h(x):x=", x) # 4
    x = x + 1
    print("in g(x):x=", x) # 5
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x) # 3
print('in main program scope: z = ', z) # 4


# Functions are 1st class citizens
# It means being passed as an argument, returned from a function, and assigned to a variable.

# type and id
def square(num):
    return num * 2

print(type(square)) # function
print(id(square)) # 111276776868768 (Address)

# reassign
x = square
print(x) # print whole function code

# deleting a function
del square # It will delete the function square

# storing
L = [1,2,3,square]
print(L) # [1,2,3,print square function whole code]

# returning a function
def f():
    def x(a, b):
        return a + b
    return x
val = f()(3,4)
print(val) # 7

# function as argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_b')
    return z()

print(func_b(func_a))


# Benifits of using a Function
# 1. Code Modularity
# 2. Code Readibility
# 3. Code Reusability

# Lambda Function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

res = lambda x : x ** 2
print(res(2)) # 4

sum = lambda x,y: x+y
print(sum(5, 2)) # 7

# Example 1: Check if string has 'a'
checkString = lambda str: 'a' in str
print(checkString('hello')) # False

# Example 2: odd or even
num = lambda n : 'even' if n % 2 == 0 else 'odd'
print(num(5)) # odd


# Higher Order Function

def square(x):
    return x ** 2

# HOF
def transform(fun, listData):
    output = []
    for i in listData:
        output.append(fun(i))
    print(output) # [1,4,9,16,25]

transform(square, [1,2,3,4,5])


# Map function
data = list(map(lambda x:x**2, [1,2,3,4,5]))
print(data) # [1,4,9,16,25]

# Filter function
data = list(filter(lambda x : x > 2, [1,2,3,4,5]))
print(data) # [3,4,5]

# Reduce function

# Example 1: sum of all items
import functools
data = functools.reduce(lambda x,y : x + y, [1,2,3,4,5])
print(data) # 15

# Example 2: find min
import functools
min = functools.reduce(lambda x,y : x if x < y else y, [1,2,3,4,5])
print(min) # 1