# samod subhasha 

# ✅ Exercise 1: Bank Account Class
# Task:
# Create a BankAccount class with the following:

# Private attributes: __balance, __account_holder

# Methods: deposit(amount), withdraw(amount), get_balance()

# Enforce that balance cannot go below 0 and deposit/withdraw must be positive.


class BankAccount:
    def __init__(self, balance, account_holder ):
        # suggested solution
        self.__balance = max(0,balance)
        
        # my solution 
        # self.__balance = balance
        self.__account_holder = account_holder
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False
    
    def withdraw(self, amount):
        
        # suggested solution
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False
        
        # My solution
            # if self.__balance > amount > 0:
            #     self.__balance -= amount
            #     print(f"{amount} has been withdrawn from your balance.")
            # else:
            #     print("Amount must be above the Bank balance !")  
                
    
    def get_balance(self):
        return self.__balance
    
    def get_account_holder(self):
        return self.__account_holder


bank = BankAccount(100, "samod")
bank.deposit(-100)
bank.deposit(100)
bank.withdraw(-50)
bank.withdraw(50)
bank.get_balance()




# ✅ What You Did Well (according to chat GPT)

    # Private attributes (__balance, __account_holder): ✅ Correct usage of name mangling to enforce encapsulation.

    # Basic validation on input: ✅ Checking for positive deposits and withdrawals.

    # Readable method names: ✅ Follows good naming conventions.

    # Simple, linear structure: ✅ Clear, maintainable control flow.

# ❌ What Needs Fixing or Improving

    # Flawed withdraw logic 
        # if self.__balance > amount > 0:
    
    # Return the massage and let the callser decide how to display
    
    # get_balance() should return the value
    
    # No Input Validation in Constructor (allowing negative initial balance)



 
