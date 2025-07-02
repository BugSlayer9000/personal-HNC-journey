# 🔧 Activity 1: Car Class
# Create a Car class with attributes: make, model, year. Add a method start_engine() that prints "Engine started for <make> <model>".

# 🔁 Extend: Add a method display_info() to print all attributes.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print(f"Engine startrd for {self.make} {self.model}")
    
    def display_info(self):
        print(f"\nMake Company - {self.make}")
        print(f"\nModel of the vehicle - {self.model}")
        print(f"\nYear of release - {self.year}")


car = Car("Nissan", "GTR", 2019)
car.start_engine()
car.display_info()

# extend exersise
