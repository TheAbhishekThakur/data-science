## With OOP classes to handle the following scenarious:
# 1. A user can create and view 2D coordinates
# 2. A user can find out the distance between 2 coordinates
# 3. A user can find out the distance of a coordinate from origin
# 4. A user can check if a point lies on a given line
# 5. A user can find the distance between a given 2D point and a given line

class Point:
    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    def __str__(self):
        return "<{}, {}>".format(self.x_cod, self.y_cod)
    
    def euclidean_distance(self, other):
        return (((self.x_cod - other.x_cod) ** 2) + ((self.y_cod - other.y_cod) ** 2)) ** 0.5
    
    def distance_from_origin(self):
        return ((self.x_cod ** 2) + (self.y_cod ** 2) ** 0.5)
    

class Line:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self):
        return "{}x + {}y + {} = 0".format(self.a,self.b,self.c)
    
    def point_on_line(line, point):
        if((line.a * point.x_cod) + (line.b * point.y_cod + line.c) == 0):
            return "Lies on the line"
        return "Does not lies on the line"

    def shortest_distance(line, point):
        return abs(line.a * point.x_cod + line.b * point.y_cod + line.c) / ((line.a ** 2 + line.b ** 2) ** 0.5
)
p1 = Point(0,0)
p2 = Point(1,1)

l1 = Line(3,4,5)
print(l1) # 3x + 4y + 5 = 0

print(p1.euclidean_distance(p2)) # 1.4142135623730951
print(p1.distance_from_origin()) # 0.0


l2 = Line(1,1,-2)
p3 = Point(1,1)
print(l2.point_on_line(p3)) # Lies on the line
print(l2.shortest_distance(p3)) # 0.0

##########################################################################

## Attribute creation from outside of the class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return {
            "name": self.name,
            "age": self.age
        }

person = Person("Abhishek", 27)
print(person.greet()) # { name: "Abhishek", age: 27 }

# print(person.gender) # Error
person.gender = "Male" # Create attribute from outside of the class
print(person.gender) # Male


##########################################################################


## Reference Variables
# 1. Reference variables holds the objects
# 2. We can create objects without reference variable as well
# 3. An object can have multiple reference variables
# 4. Assigning a new reference variable to an existing object does not create a new object

## Object without a reference
class OtherPerson:
    def __init__(self):
        self.name = "Abhishek"
        self.gender = "Male"

# p2 is not the object, It holds the reference of OtherPerson class object.
p2 = OtherPerson()


## Pass by reference
class AnotherPerson:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(person):
    print("Hi, My name is", person.name , 'and I am a', person.gender)
    return AnotherPerson("Ankit", "Male")

p3 = AnotherPerson("Abhishek", "Male")
p4 = greet(p3) # Hi, My name is Abhishek and I am a Male
print(p4.name) # Ankit
print(p4.gender) # Male


##########################################################################

## Object Mutability
class APerson:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(person):
    person.name = "Sachin"
    return person

p = APerson("Nitish", "Male")
print(id(p)) # Memory Address: 140655555218960
p1 = greet(p)
print(id(p1)) # Memory Address: 140655555218960


##########################################################################

# Encapsulation
class Atm:
    # constructor
    def __init__(self):
        self.pin = ''
        self.__balance = 0 # provate variable
        self.__menu()

    # getter
    def getBalance(self):
        return self.__balance
    
    # setter
    def setBalance(self, new_balance):
        if type(new_balance) == int:
            self.__balance = new_balance
        else:
            print("Invalid balance")
    
    ## private method
    def __menu(self):
        user_input = input("""
            Hi, How can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Enything else to exit
        """)

        if user_input == '1':
            # create pin
            self.create_pin_and_balance()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw_balance()
        else:
            exit()

    def create_pin_and_balance(self):
        user_pin = input("Enter your pin")
        self.pin = user_pin 

        user_balance = input("Enter your balance")
        self.__balance = user_balance  

        print("Pin created successfully...")


    def change_pin(self):
        user_old_pin = input("Enter your existing pin")

        if user_old_pin == self.pin:
            # change the pin
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("You pin updated successfully...")
        else:
            print("You can't change pin.")
            self.menu()


    def check_balance(self):
        pin = input("Enter your pin")
        if pin == self.pin:
            print("Your pin:", self.__balance)
        else:
            print("Invalid pin:")


    def withdraw_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount"))
            if amount > self.__balance:
                print("Incifient Balance")
            else:
                self.__balance = self.__balance - amount
                print("Withdral successfully, now your current balance is:", self.__balance)
        else:
            print("Invalid pin:")
        
        self.menu()
        
# To create an object of the class    
atmObj = Atm()
print(type(atmObj)) # <class '__main__.atm'>
print(atmObj.balance) # 0


##########################################################################


## Collection of objects

# list of objects
class ThePerson:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

p1 = ThePerson("Abhishek", "Male")
p2 = ThePerson("Kajal", "Female")
p3 = ThePerson("Sachin", "Male")

L = [p1,p2, p3]
for i in L:
    print(i.name)
    print(i.gender)


# dict of objects
class ThePerson2:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

p1 = ThePerson2("Abhishek", "Male")
p2 = ThePerson2("Kajal", "Female")
p3 = ThePerson2("Sachin", "Male")

d = { "p1": p1, "p2": p2, "p3": p3 }
for i in d:
    print(d[i].name)
    print(d[i].gender)


##########################################################################


# Static Variables vs Instance Variables

# need for a static variables
class Atm:

    # Static Variable - Class Variable
    counter = 1

    # Private static variable
    __counter2 = 10


    # constructor
    def __init__(self):
        self.pin = ''
        self.__balance = 0 # provate variable

        # Instance Variable - Represent Object
        # self.cid = 0
        # self.cid += 1   

        self.cid = Atm.counter
        Atm.counter += 1 

        self.__menu()

    @staticmethod
    def getCounter():
        return Atm.__counter2

    # getter
    def getBalance(self):
        return self.__balance
    
    # setter
    def setBalance(self, new_balance):
        if type(new_balance) == int:
            self.__balance = new_balance
        else:
            print("Invalid balance")
    
    ## private method
    def __menu(self):
        user_input = input("""
            Hi, How can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Enything else to exit
        """)

        if user_input == '1':
            # create pin
            self.create_pin_and_balance()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw_balance()
        else:
            exit()

    def create_pin_and_balance(self):
        user_pin = input("Enter your pin")
        self.pin = user_pin 

        user_balance = input("Enter your balance")
        self.__balance = user_balance  

        print("Pin created successfully...")


    def change_pin(self):
        user_old_pin = input("Enter your existing pin")

        if user_old_pin == self.pin:
            # change the pin
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("You pin updated successfully...")
        else:
            print("You can't change pin.")
            self.menu()


    def check_balance(self):
        pin = input("Enter your pin")
        if pin == self.pin:
            print("Your pin:", self.__balance)
        else:
            print("Invalid pin:")


    def withdraw_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount"))
            if amount > self.__balance:
                print("Incifient Balance")
            else:
                self.__balance = self.__balance - amount
                print("Withdral successfully, now your current balance is:", self.__balance)
        else:
            print("Invalid pin:")
        
        self.menu()
        
  
atmObj1 = Atm()
atmObj2 = Atm()
atmObj3 = Atm()

# Using Instance Variable
print(atmObj1.cid) # 1
print(atmObj2.cid) # 1
print(atmObj3.cid) # 1

# Using Static Variable
print(Atm.counter) # 4

print(Atm.getCounter()) # 0