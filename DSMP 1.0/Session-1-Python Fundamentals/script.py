# python is a case sensitive language

print("Hello World") # Hello World
print("Hello", 1, 1.5, True) # Hello 1 1.5 True
print("Hello", 2, 4.5, True, sep="/") # Hello/2/4.5/True

print("Hello") # Hello
print("World") # World


print("Hello", end="-")
print("World")

# Output: Hello-World

# -----------------------------------------------------

# Data Types

# 1. Integer
print(8) # 8
print(1e308) # 1e+308
print(1e309) # infinite

# 2. Decimal/Float
print(8.55) # 8.55

# 3. Boolean
print(True) # True
print(False) # False

# 4. Text/String
print("Hello World") # Hello World

# 5. Complex Number
print(5+6j) # (5+6j)

# 6. List/Array
print([1,2,3,4,5]) # [1,2,3,4,5]

# 7. Tuple
print((1,2,3,4,5)) # (1,2,3,4,5)

# 8. Sets
print({1,2,3,4,5}) # {1,2,3,4,5}

# 9. Dictonary
print({ "name": "Nitish", "gender": "Male", "weight": 60}) # { name: "Nitish", gender: "Male", weight: 60}

# 10. type()
type(8) # int
type("Abhishek") # str

# ------------------------------------------------------------------------------------

# Variables
# It is a container to store some value or you can say future use.

name = "Abhishek Thakur"
print(name) # Abhishek Thakur

a = 5;
b = 6;
print(a + b) # 6

# Dynamic Typing: Where you do not tell the data type of any variable
name = "Sachin"

# Static Typing: Where you declare variable with types like other language
# int a = 10

# Dynamic Binding: You can use multiple date types for a single variable
a = 5
print(a) # 5
a = "Sachin"
print(a) # Sachin

# Static Binding: It means once you declare a variable with a data type then you can't change that data type like other programming language

# You can declare the variables like this:

a,b,c = 10, 20, 30
print(a,b,c)

x=y=z=50
print(x,y,z)

# --------------------------------------------------------------------

# Keywords

# 1. try/catch
# 2. switch
# 3. if
# and many more...

# Identifier

# 1. Whenever you create any variables or functions, you can't start with a digit

# 1name = "Abhishek" # Error

# 2. You can only use underscore (_) special character

# first-name = "Nitin" # Error
first_name = "Nitin"

# 3. Identifiers can not be keywords

# --------------------------------------------------------------------

# User Input

input("Enter your name") # Take user input

# Add two number

fnum = input("Enter first number")
snum = input("Enter second number")

result = int(fnum) + int(snum)
print(result)

# --------------------------------------------------------------------

# Type Conversion

# Implicit: Automatically converted by interpreture
# Ex:
print(5 + 5.6) # 10.6

# pring(5 + 'hello') TypeError

# Explicit: Programmer do type conversion

int('4') # 4
int(4.5) # 4

# int(4 + 5j) # Error

str(5) # '5'

float(4) # 4.0

# --------------------------------------------------------------------

# Literals: Suppose you assign some value in a variable, that value is called literals

a = 0b1010 # Binary Literal
b = 100 # Decimal Literal
c = 0o310 # Octal Literal
d = 0x12c # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2
float_3 = 1.5e-3

# Complex Literal
x = 3.14j

print(a,b,c,d)
print(float_1, float_2, float_3)
print(x, x.imag, x.real)

string = 'This is Python'
string2 = "This is Python"
multiple_line = """This is multi line string"""
unicode = u"\U001f600\U001f600\U001f600"
raw_str = r"raw \n string"

print(string, string2, multiple_line)
print(unicode, raw_str)


print(True + 1) # 2
print(False + 2) # 1

# To use for future
a = None
print(a) # None


