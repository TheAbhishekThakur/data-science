# ------------- Operators in Python ------------- #

# 1. Arithmetic Operators

print(5 + 3)  # 8 - Addition
print(10 - 2)  # 8 - Subtraction
print(4 * 2)  # 8 - Multiplication
print(16 / 2)  # 8 - Division
print(10 // 2)  # 2 - Integer Division
print(10 % 3)  # 1 - Modulus
print(2 ** 3)  # 8 - Powerof

# 2. Relationals Operators

print(5 > 3)  # True - Greater than
print(5 < 3)  # False - Less than
print(5 == 3)  # False - Equal to
print(5 != 3)  # True - Not equal to
print(5 >= 3)  # True - Greater than or equal to
print(5 <= 3)  # False - Less than or equal to


# 3. Logical Operators

print(True and False)  # False - Logical AND
print(True or False)   # True - Logical OR
print(not True)        # False - Logical NOT


# 4. Bitwise Operators

print(5 & 3)  # 1 - Bitwise AND
print(5 | 3)  # 7 - Bitwise OR
print(5 ^ 3)  # 6 - Bitwise XOR
print(~5)     # -6 - Bitwise NOT
print(5 << 1)  # 10 - Bitwise left shift
print(5 >> 1)  # 2 - Bitwise right shift


# 5. Assignment Operators

print(5)  # Initial value
x = 5
x += 3  # x = x + 3
print(x)  # 8 - Add and assign
x -= 2  # x = x - 2
print(x)  # 6 - Subtract and assign
x *= 2  # x = x * 2
print(x)  # 12 - Multiply and assign
x /= 3  # x = x / 3
print(x)  # 4.0 - Divide and assign
x //= 2  # x = x // 2
print(x)  # 2.0 - Integer divide and assign
x %= 2  # x = x % 2
print(x)  # 0.0 - Modulus and assign
x **= 3  # x = x ** 3
print(x)  # 0.0 - Power and assign

# 6. Membership Operators

my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # True - Check if 3 is in the list
print(6 not in my_list)  # True - Check if 6 is not in the list
print('a' in 'apple')  # True - Check if 'a' is in the string
print('b' not in 'apple')  # True - Check if 'b' is not in the string


# 7. Identity Operators
print(5 is 5)  # True - Check if both are the same object
print(5 is not 3)  # True - Check if they are not the same
a = [1, 2, 3]
b = a
print(a is b)  # True - Both refer to the same list object
print(a is not b)  # False - They are the same object
c = a[:]
print(a is c)  # False - c is a different object (copy of a)
print(a == c)  # True - But they are equal in value
print(a is not c)  # True - c is not the same object as a


# Find the sum of a 3 digits number entered by the user
number = int(input("Enter a 3-digit number: "))

a = number % 10
number = number // 10 
b = number % 10
number = number // 10
c = number % 10
print("The sum of the digits is:", a + b + c)
   

# ------------------- If-Else Statements -------------------

email = "abhishek@gmail.com"
password = "12345"

input_email = input("Enter your email: ")
input_password = input("Enter your password: ")

if input_email == email and input_password == password:
    print("Login successful!")
elif input_email != email:
    print("Email not found! Please check your email.")
elif input_password != password:
    print("Incorrect password! Please try again.")
else:
    print("Login failed! Please check your email and password.")


# Find the min of 3 numbers entered by the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 < num2 and num1 < num3:
    print("The minimum number is:", num1)
elif num2 < num3:
    print("The minimum number is:", num2)
else:
    print("The minimum number is:", num3)


# Menu driven calculator
fnum = int(input("Enter first number: "))
snum = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print(fnum + snum)
elif operation == '-':
    print(fnum - snum)
elif operation == '*':
    print(fnum * snum)
elif operation == '/':
    if snum != 0:
        print(fnum / snum)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation! Please enter +, -, *, or /.") 


# ------------------- Modules in Python -------------------

# 1. math
import math
math.factorial(5)  # 120 - Factorial of 5
math.floor(5.7)  # 5 - Floor value of 5.7
math.sqrt(196)  # 14.0 - Square root of 196

# 2. keyword
import keyword
print(keyword.kwlist)  # List of all keywords in Python
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# 3. random
import random
print(random.randint(1, 10))  # Random integer between 1 and 10

# 4. datetime
import datetime
now = datetime.datetime.now()
print(now)  # Current date and time

# List all available modules in Python
help('modules') # This will display a list of all available modules in Python


# ------------------- Loops in Python -------------------
# Loops are used to execute a block of code repeatedly based on a condition or a sequence.

# 1. While Loop
number = int(input("Enter the number"))
i = 1
while  i < 11:
    print(number * i)
    i += 1  # Increment count by 1

# while loop with else
i = 1
while i < 11:
    print(number * i)
    i += 1  # Increment count by 1
else:
    print("Multiplication table completed!")

# Guessing game
import random
number_to_guess = random.randint(1, 100)
guess = None
count = 0

while guess != number_to_guess:
    
    if(guess < number_to_guess):
        print("Too low! Try again.")
    elif(guess > number_to_guess):
        print("Too high! Try again.")

    guess = int(input("Guess a number between 1 and 100: "))
    count += 1

else:
    print("Congratulations! You've guessed the number correctly.")
    print(f"Attempt {count}: You guessed {guess}.")



# 2. For Loop

for i in range(1, 11):
    print(i)

# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 - Print numbers from 1 to 10

for i in range(1, 11, 2): # Third argument is step
    print(i) # 1, 3, 5, 7, 9 - Print odd numbers from 1 to 10

for i in range(10, 0, -1): # Third argument is step
    print(i) # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 - Print numbers from 10 to 1 in reverse order

for i in "Delhi":
    print(i)  # D, e, l, h, i - Print each character in the string "Delhi"

for i in [1, 2, 3, 4, 5]:
    print(i)  # 1, 2, 3, 4, 5 - Print each element in the list

for i in (1, 2, 3, 4, 5):
    print(i)  # 1, 2, 3, 4, 5 - Print each element in the tuple

for i in {1, 2, 3, 4, 5}:
    print(i)  # 1, 2, 3, 4, 5 - Print each element in the set

for i in {1: 'one', 2: 'two', 3: 'three'}:
    print(i)  # 1, 2, 3 - Print each key in the dictionary

# Program - The current population of a town is 10000. The population increases by 10% every year. Calculate the population after 10 years.
population = 10000
for year in range(10, 0, -1):  # Loop from 10 to 1
    print(f"Population after year {year}: {int(population)}")  # Print population after each year
    population = population -  0.10 * population # Decrease population by 10% each year
