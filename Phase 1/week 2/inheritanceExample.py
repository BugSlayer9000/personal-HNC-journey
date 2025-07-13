# Inheritance

# for example a car and a bike is two different objects but share the similarities from a vehicle like engine start model brand etc.

class vehicle:
    def __init__(self, brand, model, year):  #  every vehicle have those things (attributes) in common
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("start")  # Every vehicle have this functionality
        
    def stop(self):
        print("Vehicle stopping")
    
    # all specific vehicle like cars bikes planes can inherit this commmon vehicle behavior
    

class Car(vehicle): # This car class is inheritinh all the attributes and functions from the vehicle class
    # we can also add some extra attributes or methods that a re specific to acar vehicle but not all the vehicles 
    
    def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
        super().__init__(brand, model, year) #  calls the __init__ method in vehicle and acess its attributes 
        
        self.number_of_doors = number_of_doors #  this attribute is unique to this car class 
        self.number_of_wheels = number_of_wheels #  this attribute is unique to this car class


class Bike(vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year) # again accessing to all the attributes in the vehicle class
        
        self.number_of_wheels = number_of_wheels # this attribute only belong to this bike class 


# creating sum instances 

car = Car("Ford", "Focus", 2003, 5, 4) # you have to pass in the args for vehicle class and then car class asweel which means 5 arguments in total 3 from the Vehicle class and 2 from the car class 

bike = Bike("Honda", "CBR", 2003, 2) # you also have to pass in args for vehicle class and then for Bike class which means 4 args in  total 3 args for Vehicle class and 1 for Bike class

print(bike.__dict__) # prints all the attributes of class includeing the superclasses attributes 

car.start() 
bike.stop()
        
        