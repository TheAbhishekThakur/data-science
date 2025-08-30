# 1. Find the length of a given string without using the len() function.

s = input("Enter a string: ")
length = 0
for char in s:
    length += 1
print("Length of the string is:", length)


# 2. Extract username from a given email.
# Eg: If the email is "abhishek84411@gmail.com"
# Then the username should be "abhishek84411"

email = input("Enter an email address: ")
username = email.split('@')[0]
print("Username extracted from the email is:", username)

# Or
index = email.index('@')
username = email[0:index]
print("Username extracted from the email is:", username)


# 3. Count the frequency of a particular character in a provided string.
# Eg: "Hello how are you" is the string, the frequency of 'h' in this string is 2.

s = input("Enter a string: ")
search = input("Enter the character to search for: ")
frequency = 0
for char in s:
    if char.lower() == search.lower():
        frequency += 1
print(f"The frequency of '{search}' in the string is:", frequency)


# 4. Write a program which can remove a particular character from a string.
s = input("Enter a string: ")
remove_char = input("Enter the character to remove: ")
new_string = ''
for char in s:
    if char != remove_char:
        new_string += char
print("String after removing the character is:", new_string)


# 5. Write a program that can check weather a given string is palindrome or not.
# Eg: abba -> abba is a palindrome
# Eg: abcd -> abcd is not a palindrome
s = input("Enter a string: ")

for i in range(0, len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print(f"{s} is not a palindrome")
        break
else:
    print(f"{s} is a palindrome")


# 6. Write a program to count the number of words in a string without split().

s = input("Enter a string: ")
L = []
temp = ''
for i in range(len(s)):
    if s[i] != ' ':
        temp = temp + s[i]
    else:
        L.append(temp)
L.append(temp)  # Append the last word
print("Number of words in the string is:", len(L))

    
# 7. Write a python program to convert string to title case without using title() function.
# Eg: "hello world" -> "Hello World"

s = input("Enter a string: ")
L = []

for i in s.split():
    L.append([i][0].upper() + i[1:].lower())
print("Title case of the string is:", " ".join(L))


# 8. Write a program that can convert an integer to string.
number = int(input("Enter an integer: "))
digits = "0123456789"
result = ""

while number != str:
    result = digits[number % 10] + result
    number //= 10

print("The integer as a string is:", result)