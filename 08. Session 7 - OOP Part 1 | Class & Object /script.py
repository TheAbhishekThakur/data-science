# OOP Part 1 | Class & Object

# Class is a blueprint.
# Object is an instance of the class.

L = [1,2,3]
print(type(L)) # <class 'list'>

class Atm:
    # constructor
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
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
        self.balance = user_balance  

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
            print("Your pin:", self.balance)
        else:
            print("Invalid pin:")


    def withdraw_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount"))
            if amount > self.balance:
                print("Incifient Balance")
            else:
                self.balance = self.balance - amount
                print("Withdral successfully, now your current balance is:", self.balance)
        else:
            print("Invalid pin:")
        
        self.menu()
        
# To create an object of the class    
atmObj = Atm()
print(type(atmObj)) # <class '__main__.atm'>
print(atmObj.balance) # 0



## Create custom datatype: fraction
class Fraction:
    # parameterized constructor
    def __init__(self, x, y):
        self.num = x
        self.den = y
    
    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self, other):
        new_num = ((self.num * other.den) + (other.num * self.den))
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)
    
    def __sub__(self, other):
        new_num = ((self.num * other.den) - (other.num * self.den))
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return "{}/{}".format(new_num, new_den)

    def convert_to_decimal(self):
        return self.num / self.den
     

fr1 = Fraction(3, 4)
print(fr1) # 3/4
fr2 = Fraction(1, 2)
print(fr2) # # 1/2

print(fr1 + fr2) # 10/8
print(fr1 - fr2) # 2/8
print(fr1 * fr2) # 3/8
print(fr1 / fr2) # 6/4

print(fr1.convert_to_decimal()) # 0.75