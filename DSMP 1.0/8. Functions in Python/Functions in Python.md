# Functions in Python
Function is a block of code which takes some input and return some output. But it's not mendatory. You can also call a function without any input parameters.

You can define a function single time and use it multiple times.

## There are two types of functions:

1. Built-In function
2. User-defined function

## Function uses two types of principles:

1. `Abstraction`: Abstraction means hiding the internal details and showing only the necessary features of an object or function. You don’t need to know how a function works internally to use it—just what it does and how to call it.

**Example:**
```
def calculate_area(radius):
    return 3.14 * radius * radius

# You can use this function without knowing its internal implementation.
area = calculate_area(5)
print(area)
```

2. `Decomposition`: Decomposition means breaking a complex problem into smaller, more manageable parts (functions, classes, or modules). Each part handles a specific task, making your code easier to understand, maintain, and reuse.


**Example:**
```
def get_user_input():
    return float(input("Enter radius: "))

def calculate_area(radius):
    return 3.14 * radius * radius

def display_area(area):
    print(f"The area is {area}")

# Decompose the program into smaller functions
radius = get_user_input()
area = calculate_area(radius)
display_area(area)
```

Here, the problem “calculate and display the area of a circle” is decomposed into three simpler functions.


## Benifits of using a Function
1. Code Modularity
2. Code Readibility
3. Code Reusability

## Lambda Function

- A lambda function is a small anonymous function.
- A lambda function can take any number of arguments, but can only have one expression.

```
res = lambda a: a * 2
```

## Differences between lambda function vs normal function

1. No Name
2. lambda has no return value (infacts, returns a function)
3. lambda is written in 1 line
4. lambda function not reusable


## Then why use lambda function
They are used with Higher Order Function