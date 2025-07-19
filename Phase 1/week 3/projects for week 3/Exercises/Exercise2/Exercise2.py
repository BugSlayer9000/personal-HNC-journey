# samod subhasha
# 18/07/25

# Online shopping cart with payment processing 

# Note - Main purpose of this exercise is Practicing and devoloping OOP concepts in Python. But I will be using some Advanced-for-my-level with the help of AI to make this as professional as posiible with the time I got 

from abc import ABC, abstractmethod # for abstract methods 
from enum import Enum # clean constant definition
from uuid import uuid4 # get unique Ids 
from datetime import datetime # get timestamps and date and time


class Product(ABC):
    def __init__(self, name, price, description = None, quantity = None) -> None:
        super().__init__()
        self.name = name
        self.sku = self.__genarate_sku()
        self.price = price
        self.description = description if description is not None else "No description"
        self.quantity = quantity if quantity is not None else 1
        
        # weak encapsulation add privet attributes 
    
    def __genarate_sku(self):
        prefix = "PHYS" if isinstance(self, PhysicalProduct) else "DIGI"
        short_name = self.name[:4].upper()
        unique = str(uuid4())[:4].upper() # Take the first 4 characters of a UUID and make them uppercase.
        
        return f"{prefix}-{unique}-{short_name}"
        
        
    @abstractmethod
    def get_tax(self) -> float:
        pass
    
    @abstractmethod
    def get_shipping_cost(self) -> float:
        pass
    
    def validate_price(self) -> bool :
        is_valid = False
        
        if self.price < 0 and len(self.name) < 2 :
            raise ValueError("Check the price or the name of the prodcut")
        else:
            is_valid = True
        
        return is_valid
            


class DigitalProduct(Product):
    def __init__(self, name, price, description, quantity , file_size, download_link) -> None:
        super().__init__(name, price, description, quantity)
        self.file_size = file_size
        self.download_link = download_link
    
    
    def get_tax(self) -> int :
        # add degital tax rate
        return self.price * 0
    
    # remove the hardcoded tex rates and add them throght added constants through Enum check chatGPT
    
    def get_shipping_cost(self):
        # always set to zero
        return self.price * 0


class PhysicalProduct(Product):
    def __init__(self, name, price, description, quantity, weight, dimensions:tuple) -> None:
        super().__init__(name, price, description, quantity)
        self.weight = weight
        self.dimensions = dimensions
    
    def get_tax(self) -> float: # Physical product tax
        return self.price * 0.10
    
    def _get_weight_fee(self) -> float :
        RATE_FOR_FIRST_5KG = 1
        RATE_FOR_NEXT_15KG = 1.5
        RATE_FOR_OVER_20KG = 2.0
        
        
        if self.weight <= 5:
            return self.weight * RATE_FOR_FIRST_5KG
        elif 0 < self.weight - 5 <= 20 :
            return (5 * RATE_FOR_FIRST_5KG) + ((self.weight - 5) * RATE_FOR_NEXT_15KG)
        else:
            return (5 * RATE_FOR_FIRST_5KG) + (15 * RATE_FOR_NEXT_15KG) + ((self.weight - 20) * RATE_FOR_OVER_20KG)
        
    def _get_volume_surcharge(self) -> float:
        BASE_VOLUME = 30000
        legnth, width, height = self.dimensions
        volume = legnth * width * height
        
        if volume > BASE_VOLUME:
            return 5
        return 0
        
            
    
    def get_shipping_cost(self) -> float : # based on weight/dimensions
        BASE_RATE = 2.50
        
        total = 0
        
        weight_fee = self._get_weight_fee()
        volume_surcharge = self._get_volume_surcharge() if self._get_volume_surcharge() != 0 else 1
        
        total = (BASE_RATE * weight_fee * (volume_surcharge or 1)) * self.quantity
        
        return total
    
    # after fixing logic in _get_weight_fee() and adding a list method to self.dimentions along with some typos
    # Score: 7.8 / 10 (HNC Level 7 standard — above-average student work with near-industry design but minor flaws in validation and consistency) by chatGPT
        
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

# add a product and test your product classes 