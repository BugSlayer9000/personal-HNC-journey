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
    
    def apply_discount(self, discount):
        if discount != 0:
            discounted_price = self.price - (discount * self.price) 
            return discounted_price
        else:
            return self.price
        
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
        
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
    
    def __str__(self) -> str:
        return f"Product name - {self.name}, Price - {self.price}, Description - {self.description}, Quantity - {self.quantity}"
    
    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, description={self.description}, quantity={self.quantity}, file_size={self.file_size}, download_link={self.download_link})"

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
    
    def __str__(self) -> str:
        return f"Product name - {self.name}, Price - {self.price}, Description - {self.description}, Quantity - {self.quantity}"
    
    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, description={self.description}, quantity={self.quantity}, weight={self.weight}, dimensions={self.dimensions})"
    
    
    # after fixing logic in _get_weight_fee() and adding a list method to self.dimentions along with some typos
    # Score: 7.8 / 10 (HNC Level 7 standard — above-average student work with near-industry design but minor flaws in validation and consistency) by chatGPT

       
class ShoppingCart:
    def __init__(self) -> None:
        self.products = []
        self.discount_codes = {"samod10": 0.15,
                               "robert": 0.25,
                               "kelum": 0.10}
    
    def add_product(self, product) -> bool:
        if product not in self.products:
            if isinstance(product, Product):
                self.products.append(product)
                return True
            else:
                return False
        else:
            return False
    
    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)
            return True
        else:
            return False
    
    def apply_discount(self, code):
        for product in self.products:
            for discount_code, dicount_value in self.discount_codes.items():
                if code == discount_code:
                    product.price = product.apply_discount(dicount_value) 
                    
            
            
            # if code == discount_code:
            #     for product in self.products:
            #         if product.apply_discount(dicount_value) :
            #             return True
            #         else:
            #             return False
            # else:
            #     return False 
    
    def get_products(self):
        return self.products
                
    
    def validate_cart(self):
        is_valid = True
        
        if not self.products:
            is_valid = False
            raise ValueError("There is no products in Cart")

        for product in self.products:
            if 0 >= product.price or 0 >= product.quantity:
                is_valid = False
                raise ValueError(f"Failed to validate product = {product}")
        
        return is_valid

class PaymentProcessor(ABC):
    def __init__(self,order) :
        super().__init__()
        self.order = order
    
    @abstractmethod    
    def process_payment(self, amount) -> str:
        pass
            
    
class CreditCardProcessor(PaymentProcessor):
    def __init__(self,order) :
        super().__init__(order)
    
    def process_payment(self, amount)  -> str:
        if not self.order.cart.validate_cart():
            return "Cart validation failed"
        else:
            # Simulate payment processing using the amount
            if self.order.calculate_final_total() == amount:
                return f"Payment successfull"
            else:
                return "Payment failed"
    
class PayPalProcessor(PaymentProcessor):
    def __init__(self,order) :
        super().__init__(order)
        
        
    def process_payment(self, amount)  -> str:
        if not self.order.cart.validate_cart():
            return "Cart validation failed"
        else:
            # Simulate payment processing using the amount
            if self.order.calculate_final_total() == amount:
                return f"Payment successfull"
            else:
                return "Payment failed "
            
            
class Order:
    def __init__(self, cart) -> None:
        self.cart = cart
        self.payment_status = None
        self.timestamp = datetime.now()
        self.order_id = uuid4()
        
    # genarate uuid4 later 
    
    def calculate_final_total(self) -> int:
        final_total = 0
        
        if self.cart.validate_cart():
            for product in self.cart.products:
                final_total += product.get_price()
        
        return final_total
    
    def get_order_summary(self):
        product_summery = {}
        
        if self.cart.validate_cart():
            for product in self.cart.products:
                product_summery[product.get_name()] = product.get_price()
            
            return product_summery
                
        
        
            


                


# add a product and test your product classes 

# === Product Instances ===
digital = DigitalProduct(
    name="Online Course",
    price=100.0,
    description="Masterclass in AI",
    quantity=1,
    file_size="2GB",
    download_link="https://course.link"
)

physical = PhysicalProduct(
    name="Mechanical Keyboard",
    price=150.0,
    description="RGB, clicky keys",
    quantity=2,
    weight=1.5,
    dimensions=(45, 15, 5)
)

physical1 = PhysicalProduct(
    name="Computer",
    price=200.0,
    description="RGB, clicky keys",
    quantity=5,
    weight=2,
    dimensions=(20, 10, 10)
)

# === Shopping Cart Setup ===
cart = ShoppingCart()

# checking remove product
print(cart.remove_product(digital)) # False
print(cart.remove_product(physical)) # False

# checks add_product function
print(cart.add_product(digital)) # True
print(cart.add_product(physical)) # True
print(cart.add_product(physical1)) # True

# checks if apply discount works
print(cart.apply_discount("samod10")) # True
print(cart.apply_discount("samod15")) # False

print(cart.validate_cart()) # True



print(cart.get_products())
    

order1 = Order(cart)
print(order1.calculate_final_total())






