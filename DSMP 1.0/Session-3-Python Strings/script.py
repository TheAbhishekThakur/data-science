# Strings in Python
# In python specifically, strings are a sequence of unicode characters enclosed in single quotes, double quotes, or triple quotes.

# Unicode : 16-bit encoding for characters, allowing for a wide range of characters from different languages and symbols.
# Unicode allows for a much larger set of characters compared to ASCII, which is limited to
# 128 characters (0-127) and primarily supports English characters and some control characters.
# Unicode supports characters from various languages, symbols, and emojis, making it more versatile for global
# applications.


# ASCII : 7-bit encoding for characters, primarily used for English characters and control characters.
# ASCII is limited to 128 characters, which includes English letters, digits, punctuation marks,
# and some control characters. It does not support characters from other languages or special symbols.
# In Python, strings are Unicode by default, allowing for a wide range of characters to be used without
# needing to specify encoding explicitly.

# Creating a string
my_string = 'Hello, World!' # Sometime you might need to use single quotes inside double quotes
# or
my_string = "Hello, World!"
# or using triple quotes for multi-line strings
my_string = """This is a multi-line string.""" # Triple quotes can be used for multi-line strings or strings with both single and double quotes.

print(my_string)

s = str('Hello, World!')  # Convert to string explicitly (not necessary in Python, but shown for clarity)
print(s)

# Accessing substrings from a string
s = 'Hello, World!'
print(s[0])  # H - First character
print(s[7])  # W - Eighth character
print(s[-1])  # ! - Last character
print(s[-2])  # d -  Second last character
print(s[0:5])  # Hello - First five characters (slicing)
print(s[7:])  # World! - From the eighth character to the end
print(s[:5])  # Hello - From the start to the fifth character
print(s[7:12])  # World - From the eighth to the twelfth character
print(s[0:12:3])  # Hlo ol - From the first to the twelfth character, stepping by 3

# Reversing a string
print(s[::-1])  # !dlroW olleH - Reverses the string

# Editing and deleting a string

# Editing a string
s = 'Hello, World!'
s[0] = 'h'  # This will raise an error because strings are immutable in Python
# Python strings are immutable, meaning you cannot change them in place.

# Deleting a string
s = 'Hello, World!'
del s  # This will delete the string variable 's'

s = 'Hello, World!'
del s[0]  # This will raise an error because you cannot delete individual characters from a string

# Operations on Strings

# 1. Arithmetic Operations
print('Hello' + ' ' + 'World!')  # Concatenation - Hello World!
print('Hello' * 3)  # Repetition - HelloHelloHello


# 2. Relational Operations
# Compare lexicographically based on ASCII values

print('Delhi' == 'Mumbai')  # False - Comparing two strings for equality
print('Delhi' != 'Mumbai')  # True - Comparing two strings for inequality
print('Delhi' < 'Mumbai')  # True - Lexicographical comparison (based on ASCII values)
print('Delhi' > 'Mumbai')  # False - Lexicographical comparison
print('Delhi' <= 'Mumbai')  # True - Less than or equal to
print('Delhi' >= 'Mumbai')  # False - Greater than or equal to
print('Pune' > 'pune')  # False - Case-sensitive comparison (uppercase letters have lower ASCII values than lowercase letters)


# 3. Logical Operations
print('Delhi' == 'Delhi' and 'Mumbai' == 'Mumbai')  # True - Logical AND
print('Delhi' == 'Delhi' or 'Mumbai' == 'Pune')  # True - Logical OR
print(not ('Delhi' == 'Mumbai'))  # True - Logical NOT  
print('Hello' and 'World')  # World - Returns the second operand if the first is truthy
print('hello' or 'world')  # hello - Returns the first truthy operand


# 4. Loops on String
for char in 'Hello, World!':
    print(char, end=' ')  # Prints each character in the string on the same line

# 5. Membership Operations
print('H' in 'Hello, World!')  # True - Checks if 'H' is in the string
print('h' in 'Hello, World!')  # False - Case-sensitive check
print('Hello' in 'Hello, World!')  # True - Checks if 'Hello' is a substring
print('World' not in 'Hello, World!')  # False - Checks if 'World' is not a substring


# String Common Functions
print(len('Hello, World!'))  # 13 - Length of the string
print(max('hello, world!'))  # w - Maximum character based on ASCII value
print(min('hello, world!'))  #  , - Minimum character based on ASCII value
print(sorted('hello, world!'))  # [' ', '!', 'd', 'e', 'h', 'l', 'l', 'o', 'o', 'r', 'w'] - Sorted list of characters in the string
print(sorted('hello, world!', reverse=True))  # ['w', 'r', 'o', 'o', 'l', 'l', 'h', 'e', 'd', ' ', '!'] - Sorted in reverse order

# String Functions
s = 'Hello, World!'
print(s.lower())  # hello, world! - Converts to lowercase
print(s.upper())  # HELLO, WORLD! - Converts to uppercase
print(s.title())  # Hello, World! - Converts to title case (first letter of each word capitalized)
print(s.capitalize())  # Hello, world! - Capitalizes the first letter of the string
print(s.swapcase())  # hELLO, wORLD! - Swaps case of each character

print(s.count('o'))  # 2 - Counts occurrences of 'o'
print(s.find('World'))  # 7 - Finds the index of 'World' in the string, if not found returns -1
print(s.index('World'))  # 7 - Finds the index of 'World' in the string, raises ValueError if not found

print(s.startswith('Hello'))  # True - Checks if the string starts with 'Hello'
print(s.endswith('!'))  # True - Checks if the string ends with '!'

name = "Abhishek"
gender = "male"
paragraph = "Hi my name is {} and I am a {}".format(name, gender)
paragraph2 = "Hi my name is {1} and I am a {0}".format(gender, name)
print(paragraph) # Hi my name is Abhishek and I am a male
print(paragraph2) # Hi my name is Abhishek and I am a male

s = "abhishek13"
print(s.isalnum())  # True - Checks if all characters are alphanumeric (letters and digits)
print(s.isalpha())  # False - Checks if all characters are alphabetic (letters only)
print(s.isdigit())  # False - Checks if all characters are digits
print(s.islower())  # True - Checks if all characters are lowercase

s = "abhishek_thakur"
print(s.isidentifier()) # True - Checks if the string is a valid identifier (variable name)

s = "Hello World!"
print(s.split(',')) # ['Hello', ' World!'] - Splits the string into a list at the comma
print(s.split())  # ['Hello, 'World!'] - Splits the string into a list at whitespace
print(s.join(['Hello', 'World!']))  # Hello World! - Joins the list into a string with a space
print("_".join(['Hello', 'World!']))  # Hello_World! - Joins the list into a string with an underscore

print(s.replace('World', 'Python'))  # Hello, Python! - Replaces 'World' with 'Python'

s = "   Hello, World!   "
print(s.strip()) # Hello, World! - Removes leading and trailing whitespace