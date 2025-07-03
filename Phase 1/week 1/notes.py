#  samod subhasha
# This is the synatx overview for a class 

class Dog:
    
    dogs = ""
    
    def __init__(self, name, breed): #  construckter 
        self.name = name
        self.breed = breed #  attributes 
    
    def bark(self):
        print(f"{self.name} says woof! ")

# creating an object
dog1 = Dog("Max", "Labrador")
dog1.bark() # Max says woof! 


