# samod subhasha

# payment processing sys (Single responsibility and Open/closed)

# Design a payment system handling credit cards, PayPal, and bank transfers. Practice:

    # Each class having one reason to change (Single Responsibility Principle - SRP)
    # Adding new payment methods without modifying existing code (Open/Closed Principle - OCP)

    

from abc import ABC, abstractmethod
from datetime import timedelta,  datetime
 
class PaymentProcessor(ABC) :
    
    # Responsibility - Define the interface for all payment processors
    
    @abstractmethod
    def process_payment(self,amount:int) -> str:
        pass


class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number:str, expiry_date:str, cvv:str, card_holder_name:str) -> None:
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv
        self.card_holder_name = card_holder_name
    
    def __authenticate_card(self) -> bool:
        if len(self.card_number) == 16:
            if not len(self.card_holder_name) < 7:
                return True
            else:
                raise ValueError("Not a valid user name")
        else:
            raise ValueError("Not a valid Card number")

    
    
    def process_payment(self, amount) -> str:
        if self.__authenticate_card():
            return f"Payment processed {amount}"
        else:
            return("Authentication failed")    

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email:str, password:str, session_token:str) -> None:
        self.email = email 
        self.password = password
        self.session_toekn = session_token
    
    def __authenticate_account(self) -> bool:
        if "@" in self.email:
            if len(self.password) > 6:
                return True
            else:
                raise ValueError("Not a valid password")
        else:
            raise ValueError("Invalid email adress detected!")
    
    def process_payment(self, amount) -> str:
        if self.__authenticate_account() :
            return f"Payment processed {amount}"
        else:
            return f"Payment Failed"

class BankTransferProcessor(PaymentProcessor):
    def __init__(self, account_number:str, sort_code:str, account_holder_name:str, bank_name:str) -> None:
        self.account_number = account_number
        self.sort_code = sort_code
        self.account_holder_name = account_holder_name
        self.bank_name = bank_name if not len(bank_name) == 0 else "No bank name added"
    
    def __authenticate_bank_account(self) -> bool:
        if len(self.account_holder_name) >= 6:
            if len(self.sort_code) == 6:
                if len(self.account_number) == 12:
                    return True
                else:
                    raise ValueError("Invalid account number")
            else:
                raise ValueError("Invalid sort code detected!")
        else:
            raise ValueError("Not a valud account name") 
    
    def process_payment(self, amount) -> str:
        if self.__authenticate_bank_account():
            return f"Payment processed {amount}"
        else:
            return f"Payment process failed !"
        

credit_card_payment = CreditCardProcessor("1234567890123456", "06-05", "333", "Samod subhasha" )
payment1 = credit_card_payment.process_payment(500)
print(payment1)

pay_pal_payment = PayPalProcessor("myemail@gmail.com", "pakaya1", "123456")
payment2 = pay_pal_payment.process_payment(250)
print(payment2)
    
bank_transfer_payment = BankTransferProcessor("123456789012", "123456", "Samod subhasha", "Bank of America")
payment3 = bank_transfer_payment.process_payment(1000)
print(payment3)

# Output:
# Payment processed 500
# Payment processed 250
# Payment processed 1000    


# ✅ Final Assessment: SRP + OCP Design
# Class	            SRP ✅	OCP ✅	Comments
# PaymentProcessor	    ✅	    ✅	Pure interface abstraction
# CreditCardProcessor	✅	    ✅	Independent logic
# PayPalProcessor	    ✅	    ✅	Easily replaceable
# BankTransferProcessor	✅	    ✅	Clean boundary of responsibility


# adding extra class without changing existing code

class CryptoCurrencyProcessor(PaymentProcessor):
    def __init__(self, wallet_address:str, network:str) -> None:
        self.wallet_address = wallet_address
        self.network = network
    
    def __authenticate_wallet(self) -> bool:
        if len(self.wallet_address) > 10:
            if self.network in ["Bitcoin", "Ethereum", "Litecoin"]:
                return True
            else:
                raise ValueError("Unsupported network")
        else:
            raise ValueError("Invalid wallet address")
    
    def process_payment(self, amount) -> str:  
        if self.__authenticate_wallet():
            return f"Payment processed {amount} via {self.network}"
        else:
            return "Payment process failed !"

# Example usage of the new class
crypto_payment = CryptoCurrencyProcessor("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "Bitcoin")
payment4 = crypto_payment.process_payment(1)
print(payment4)  # Output: Payment processed 1 via Bitcoin

# ✅ Final Grade: 8.9 / 10