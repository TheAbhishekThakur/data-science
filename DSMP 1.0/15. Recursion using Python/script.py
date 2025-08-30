# Recursion using Python

## Example 1: Factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120

###########################################################################

# Example 2: Palindrome check using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return "Palindrome"
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return "Not a Palindrome"
        
print(is_palindrome("racecar")) # Output: Palindrome
print(is_palindrome("hello"))   # Output: Not a Palindrome


###########################################################################

# Example 3: Fibonacci sequence using recursion

def fibonacci(n):
    if n == 0 or n == 1:
        return 1;
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(12)) # Output: 233