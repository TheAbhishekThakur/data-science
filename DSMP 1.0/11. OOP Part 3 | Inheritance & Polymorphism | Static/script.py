# OOP Part 3 | Inheritance & Polymorphism | Static

## Class Relationship

# 1. Aggregation  (Has-A relationship)

class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def print_address(self):
        print(self.address.city, self.address.pin, self.address.state, self.address.get_country())

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.edit_address(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pin, state, country):
        self.city = city
        self.pin = pin
        self.state = state
        self._country = country

    # To get private property (getter)
    def get_country(self):
        return self._country
    
    # To set private property (setter)
    def set_country(self, country):
        self._country = country

    def edit_address(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pin = new_pin
        self.state = new_state

address = Address("Sarita Vihar", 110076, "Delhi", "India")

## Aggregation Example: To pass an object inside the another class object
customer = Customer("Abhishek", "Male", address)

customer.print_address() # Sarita Vihar 110076 Delhi India
customer.edit_profile("Ankit", "Mumbai", 111111, "Maharastra")
customer.print_address() #



##############################################################################

# 2. Inheritance

# Parent Class
class User:
    def __init__(self):
        self.name = "Abhishek"

    def login(self):
        print("Login")

# Child Class
class Student(User):
    # def __init__(self):
    #     self.rollno = 100

    def enroll(self):
        print("Enroll into the course")

user = User()
student = Student()
print(student.name) # It will throw the error if you defined the constructir without super because parent class constructor will never called.
# print(student.rollno)
student.login()
student.enroll()


## Constructor Example 1:
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass

smartPhone = SmartPhone(20000, "Apple", 13)
smartPhone.buy() # Buying a phone


## Constructor Example 2:
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")
       
s = SmartPhone("Android", 2) # Inside smartphone constructor

# Note: If child have constructor then parent's constructor will not call


## Constructor Example 3: Child can't access private members of the parent class
class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)

        
class SmartPhone(Phone):
    def check(self):
        print(self.__price) # 'SmartPhone' object has no attribute '_SmartPhone__price'.

s = SmartPhone(2000, "Abble", 13)
s.show()
s.check()


## Constructor Example 4: get access of private member using getter
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):
    def show(self):
        print("This is in child class")

son = Child(100)
print(son.get_num()) # 100
son.show() # This is in child class


## Constructor Example 4:
class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num
    
class Child(Parent):
    def __init__(self, val, num):
        self.__val = val
        
    def get_val(self):
        return self.__val

son = Child(100, 10)
print("Parent Num:", son.get_num()) # Error: because parent constructor never call
print("Child val:", son.get_val()) # 10



## Constructor Example 5: Method Overriding, Child method will always call if there is same name method in parent and child class both.
class Phone:
    def _init_(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy (self):
        print("Buying a phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")

s=SmartPhone(20000, "Apple", 13)
s.buy() # Buying a smartphone



## Constructor Example 6: super keyword
class Phone:
    def _init_(self, price, brand, camera):
        print("Inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy (self):
        print("Buying a phone")

class SmartPhone(Phone):
    
    def buy(self):
        print("Buying a smartphone")
        super().buy()

s=SmartPhone(20000, "Apple", 13)
s.buy() 
# Output:
# Inside phone constructor
# Buying a smartphone
# Buying a phone



## Constructor Example 7: super -> constructor

class Phone:
    def _init_(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        price("Inside smartphone constructor")

s=SmartPhone(20000, "Samsung", 12, "Android", 2)
print(s.os) # Android
print(s.brand) # Samsung

# Output: 
# Inside phone constructor
# Inside smartphone constructor
# Android
# Samsung