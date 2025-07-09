# samod subhasha 

# ✅ Exercise 1: Bank Account Class
# Task:
# Create a BankAccount class with the following:

# Private attributes: __balance, __account_holder

# Methods: deposit(amount), withdraw(amount), get_balance()

# Enforce that balance cannot go below 0 and deposit/withdraw must be positive.


class BankAccount:
    def __init__(self, balance, account_holder ):
        self.__balance = balance
        self.__account_holder = account_holder
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} has been added to your balance.")
        else:
            print("Amount must be above 0 !") 
    
    def withdraw(self, amount):
            if self.__balance > amount > 0:
                self.__balance -= amount
                print(f"{amount} has been withdrawn from your balance.")
            else:
                print("Amount must be above the Bank balance !")  
                
    
    def get_balance(self):
        print(f"{self.__account_holder} your account balance is {self.__balance}")


bank = BankAccount(100, "samod")
bank.deposit(-100)
bank.deposit(100)
bank.withdraw(-50)
bank.withdraw(50)
bank.get_balance()

    
