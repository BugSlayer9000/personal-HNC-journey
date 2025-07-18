# samod subhasha
# 18/07/25

# Online shopping cart with payment processing 

# Note - Main purpose of this exercise is Practicing and devoloping OOP concepts in Python. But I will be using some Advanced-for-my-level with the help of AI to make this as professional as posiible with the time I got 

from abc import ABC, abstractmethod
from enum import Enum
from uuid import uuid4
from datetime import datetime


class Product(ABC):
    def __init__(self, name, price, sku, description) -> None:
        super().__init__()
        self.name = name
        self.sku = sku
        self.price = price
        self.description = description
        
        
    @abstractmethod
    def get_tax(self):
        pass
    
    @abstractmethod
    def get_shipping_cost(self):
        pass
    
    def validate_price(self):
        pass


class DigitalProduct(Product):
    def __init__(self, name, price, sku, description, file_size, download_link) -> None:
        super().__init__(name, price, sku, description)
        self.file_size = file_size
        self.download_link = download_link
    
    
    def get_tax(self):
        # add degital tax rate
        pass
    
    def get_shipping_cost(self):
        # always set to zero
        pass


class PhysicalProduct(Product):
    def __init__(self, name, price, sku, description, weight, dimentions) -> None:
        super().__init__(name, price, sku, description)
        self.weight = weight
        self.dimensions = dimentions
    
    def get_tax(self): # Physical product tax
        pass
    
    def get_shipping_cost(self): # based on weight/dimensions
        pass


class ShoppingCart:
    def __init__(self, products = None) -> None:
        self.products = products if products is not None else []
    
    def add_product(self, product):
        pass
    
    def remove_product(self, product):
        pass
    
    def apply_discount(self, code):
        pass
    
    def validate_cart(self):
        pass




class PaymentProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod    
    def process_payment(self, amount):
        pass
    
class CreditCardProcessor(PaymentProcessor):
    def __init__(self) -> None:
        super().__init__()
        
    
    def process_payment(self, amount):
        # add logic here ?
        return super().process_payment(amount)
    
class PayPalProcessor(PaymentProcessor):
    def __init__(self) -> None:
        super().__init__()
        
        
    def process_payment(self, amount):
        # add logic here 
        return super().process_payment(amount)
        
    
        
class Order:
    def __init__(self, cart, payment_status) -> None:
        self.cart = cart
        self.payment_status = payment_status
        self.timestamp = datetime.now()
        self.order_id = uuid4()
    
    def calculate_final_total(self):
        pass
    
    def get_order_summary(self):
        pass