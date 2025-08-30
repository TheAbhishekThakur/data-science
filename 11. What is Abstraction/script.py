# Abstraction

from abc import ABC, abstractmethod

class BankApp(ABC):
    def database(self):
        print("Connected to database")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def mobile_login(self):
        print("Login into mobile")

    def security(self):
        print("Mobile security")

mob = MobileApp()
mob.database()
mob.mobile_login()
mob.security()

# bankObj = BankApp() # Error: You can't create an object of abstract class