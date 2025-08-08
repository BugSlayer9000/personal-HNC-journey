# To show an example of dataclass decorator

# A usual boilerplate for a class 

class Product:
    def __init__(self, name:str , price:float, quantitiy:int) -> None:
        self.name = name
        self.price = price
        self.quantitiy = quantitiy
    
    def total_cost(self) -> float:
        return self.price * self.quantitiy
    
    def __repr__(self) -> str:
        return f"Product(name={self.name}, price={self.price}, quantity={self.quantitiy})"
    
    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Product):
            return NotImplemented
        return (self.name, self.price, self.quantitiy) == (value.name, value.price, value.quantitiy)




# Using the dataclass decorator

# The biolder plate we have above is automatically implemented for us and fucntions as the same  

from dataclasses import dataclass

@dataclass
class Product2:
    name:str
    price:float
    quantity:int = 0
    
    def total_cost(self) -> float:
        return self.price * self.quantity


# Uscase of Boiler Plate vs Dataclass
# Both classes will behave the same way, but Product2 is more concise and easier to read

p1 = Product("Apple", 0.5, 10)
p2 = Product("Apple", 0.5, 10)
p3 = Product("Apple", 0.5, 10)

print(p1)
print(p1.total_cost())
print(p1 == p2)  # True, because they have the same attributes

p4 = Product2("Banana", 0.3, 5)
p5 = Product2("Banana", 0.3, 5)
print(p4)
print(p4.total_cost())
print(p4 == p5)  # True, because they have the same attributes