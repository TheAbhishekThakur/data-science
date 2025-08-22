# Types of Syntax Error

print 'hello world'

# 1. IndexError
L = [1,2,3]
L[5]

# 2. ModuleNotFoundError
import mathi
math.floor(5, 3)

# 3. KeyError
d = { "name": "Abhishek" }
print(d.age)

# 4. TypeError
1 + 'a'

# 5. ValueError
int('a')

# 6. NameError
print(name)

# AttributeError
L = [1,2,3]
L.upper()


############################################################################

# Exceptions

## using try/except block

with open("sample.txt", "w") as f:
    f.write("Hello world")

try:
    with open("sample.txt", "r") as f:
        print(f.read())
except:
    print("Sorry, file not found!")

## catching specific exception
try:
    f = open("sample1.txt", "r")
    print(f.read())
    print(m)
except FileNotFoundError:
        print("File not found!")
except NameError:
        print("Variable not defined!")
except Exception as e:
    print("Some error occured!", e)

### Note: If you generic exception on top then it will go inside always there.


## else : you can do your work after try block successfully run inside the else block.
try:
    f = open("sample1.txt", "r")
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("Some error occured!", e)
else:
    print(f.read())
    print("Everything is working fine.")


## finally: It will always execute.
try:
    f = open("sample1.txt", "r")
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("Some error occured!", e)
else:
    print(f.read())
finally:
    print("It will always run.")


########################################################################################################

# Raise Exception
# In Python programming, exceptions are raised when errors occur at runtime.
# We can also manually raise exceptions using the raise keyword

raise NameError("Error")

class Bank:
    def __init__(self, balance):
        self.balane = balance;

    def withdraw(self,amount):
        if amount < 0:
            raise Exception("Amount can't be -ve")
        if self.balance < amout:
            raise Exception("Amount not available")
        self.balance = self.balance - amout

obj = Bank(1000)
try:
    obj.withdraw(5000)
except Exception as e:
    print(e)
else:
    print(obj.balance)
finally:
    print("Transaction successful.")

### Creating custom exception

class MyException(Exception):
    def __init__(self, message):
        print(message)

class Bank:
    def __init__(self, balance):
        self.balane = balance;

    def withdraw(self,amount):
        if amount < 0:
            raise MyException("Amount can't be -ve")
        if self.balance < amout:
            raise MyException("Amount not available")
        self.balance = self.balance - amout

obj = Bank(1000)
try:
    obj.withdraw(5000)
except MyException as e:
    pass
else:
    print(obj.balance)
finally:
    print("Transaction successful.")


### Simple Example

class SecurityError(Exception):
    def __init__(self, message):
        print(message)

    def logout(Self):
        print("Logout")

class Google:
    def __init__(self, name, email, password, device):
        self.name = name
        self.email = email
        self.password = password
        self.device = device

    def login(self, email, password, device):
        if device != self.device:
            raise SecurityError("Device not matched!")
        if email == self.email and password == self.password:
            print("Welcome")
        else:
            print("Login error")

obj = Google("abhishek", "abhishek@gmail.com", "1234", "iphone")

try:
    obj.login("abhishek@gmail.com", "1234")
except SecurityError as e:
     e.logout()
else:
    print(obj.name)
finally:
    print("Database connection closed")