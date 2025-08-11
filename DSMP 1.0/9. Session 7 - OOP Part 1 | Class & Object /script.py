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