from bank_exeptions import NegativeAmountError, InsufficientFundsError, AccountError


class BankAccount:
    
    def __init__(self, initial_balance: float = 0) -> None:
        """Initialize bank account with optional starting balance"""
        self.balance = initial_balance
    
    def deposit(self, amount: float):
        """Add money to account"""
        if amount < 0:
            raise NegativeAmountError(amount)
        
        self.balance += amount
        print(f"Deposit successful! New balance: £{self.balance:.2f}")
        return self.balance
    
    def withdraw(self, amount: float):
        """Remove money from account"""
        if amount < 0:
            raise NegativeAmountError(amount)
        
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        
        self.balance -= amount
        print(f"Withdrawal successful! New balance: £{self.balance:.2f}")
        return self.balance
    
    def get_balance(self):
        """Return current balance"""
        return self.balance