# Factory Example

from abc import ABC, abstractmethod

# product
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self,amount) -> str:
        pass

# Contrete products 
class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount) -> str:
        return f"Paid £{amount} via credit card"

class PayPalProcessor(PaymentProcessor):
    def pay(self, amount) -> str:
        return f"Paid £{amount} via Pay Pal"

# Factory
class PaymentProcesorFactory:
    @staticmethod
    def get_processor(method):
        if method == "credit":
            return CreditCardProcessor()
        elif method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Unsupported payement method")
    

# client code 
processor = PaymentProcesorFactory.get_processor("paypal")
print(processor.pay(100))

processor1 = PaymentProcesorFactory.get_processor("credit")
print(processor1.pay(200))
