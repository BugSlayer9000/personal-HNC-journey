
from bank_exeptions import NegativeAmountError, InsufficiebtFunds

class BankAccount():
    
    def __init__(self,initial_amount:float) -> None:
        self.balance = 0 if initial_amount is None else initial_amount
    
    def deposit(self,amount:float):
        if amount < 0:
            return NegativeAmountError
        else:
            self.balance += amount
            print(f"Balance Updated \nNew Balance = {self.balance}")
        
    def withdraw(self,amount:float):
        
        if amount < 0:
            return InsufficiebtFunds
        
        if amount > self.balance:
            return InsufficiebtFunds
        else:
            self.balance -= amount
            print(f"{amount} Withdrawn sucessfully. \nNew available balance is  = {self.balance}")
    
    def get_balance(self):
        return self.balance