# samod subhasha
# 🔧 Activity 3: BankAccount Class
# Build a class with:

# Attributes: account_number, balance

# Methods: deposit(amount), withdraw(amount), check_balance()

# Test the object with deposits and withdrawals.

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print(f"Your new balance is £{self.balance}")
    
    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(f"Withdraw amount - £{withdraw_amount} ")
        print(f"Available balance - £{self.balance}")
    
    def check_balance(self):
        print(f"Available balance for account no - {self.account_number} - £{self.balance}")

def main():
    bank_account = BankAccount(12345,100)
    bank_account.deposit(200) # Your new balance is £300
    bank_account.withdraw(100) # Withdraw amount - £100 Available balance - £200 
    bank_account.check_balance() # Available balance for account no - 12345 - £200


if __name__ == "__main__":
    main()

                           


