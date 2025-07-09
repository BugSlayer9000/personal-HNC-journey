# samod subhasha 
# Encapsulation adn subclassing 

# What is Encapsulation in python
    # One of the por principles in OOP 
    
    # Encapsulation means that restricting direct access to and object's internal state and requirong interaction through methods


# How python implement Encapsulation 

# Public atrributes/methods (Default - accessible from anywhere)
    
class Product:
    def __init__(self, name):
        self.name = name # public

p = Product("Laptop")
print(p.name) # ✅ works






# Protected atrributes (Single underscore __name )
    # convention only not enforced 

class Product2:
    def __init__(self, name):
        self._name = name # Mean to be internal

print(p.name) # ❌ shouldn't be accessed directly, but python allowes it 




# Privet attributes (Double underscore __name )
    # Python uses name mangling to make it harder to acess 
    

class Product3:
    def __init__(self, name):
        self.__name = name # True encapsulation

p = Product3("Laptop")
# print(p.__name) # Attribute error

# But technically still posible
print(p._Product3__name) #  works due to name magling
 





    
    