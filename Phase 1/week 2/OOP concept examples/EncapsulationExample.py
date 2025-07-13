# ENCAPSULATION 

class BankAccount:
    def __init__(self):
        self._balance = 0.0 #  Encapsulationg by adding a protected attribute
        
        # adding property method for getting balance 
        
    @property
    def balance(self):
        return self._balance
        
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

account = BankAccount()
print(account._balance)
account.deposit(1.99)
print(account._balance)
account.withdraw(1)
print(account._balance)