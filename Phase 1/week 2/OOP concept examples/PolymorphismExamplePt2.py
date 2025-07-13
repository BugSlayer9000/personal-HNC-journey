# Polymorphism


##################################  REFACOTORED SOLUTION #########################################

class Vehicles:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def start(self):
        print("vehicle starting")
    
    def stop(self):
        print("vehilce Stoping")

class Car(Vehicles):
    def __init__(self, brand, model, year, number_of_doors):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
    
    # def start(self):   #  we are ooveriding the class method by giving it the same as Vehicles
    #     print("The car is starting")
    
    # def stop(self):
    #     print("The car is stopping") # we are going to inherit the method from the main class form now on

class Bike(Vehicles):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels
    
    # def start_bike(self):
    #     print("The car is starting")
    
    # def stop_bike(self):
    #     print("The car is stopping") # # we are going to inherit the method from the main class form now on
        
        
vehicles : list[Vehicles] = [        
    Car("Ford", "Focus", 2003, 4),
    Bike("Honda","CBR", 2013, 2)
]

# changes of the solution

for vehicle in vehicles:
      # the problem here is we have different classes we have to deal with seprate type of objects
      
      # if I typed vehicle.start() if wont work because it's not a common method Car Object has start() method and the bike has start_bike() method 
      
      # what we can do in this situation is add a if loop and use the isinstance(list, object) to check if it's the right object 
      
    # if isinstance(vehicle, Car):
    #     print(f"Inspecting {vehicle.brand} {vehicle.model}  ({type(vehicle).__name__})")
    #     vehicle.start()
    #     vehicle.stop()
    # elif isinstance(vehicle, Bike):
    #     print(f"Inspecting {vehicle.brand} {vehicle.model}  ({type(vehicle).__name__})") # {type(vehicle).__name__} gives the name of the class 
    #     vehicle.start_bike()
    #     vehicle.stop_bike()
    # else:
    #     raise Exception("object is not a vali vehicel")
    
    # works with the if loop
    
    

 



