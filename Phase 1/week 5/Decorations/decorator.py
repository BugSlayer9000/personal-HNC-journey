# This is to demonstrate the use case of property getter and setter methods 


class circle:
    def __init__(self, radius) -> None:
        self._radius = radius
    
    @property # this will let use acess the atrribute without having to interact with a privet atrribute directly
    def radius(self):
        return self._radius
    
    @radius.setter # this is a setter method
    def radius(self, value):
        # to set the value for self._radius
        
        if value > 0:
            self._radius = value
        else:
            raise ValueError("Value must be above 0")
    
    @property
    def diameter(self):
        # get the diameter of the circle
        return self._radius * 2



c = circle(5)
print(c.radius) # 5   # Because of the property decorator we use this fucntion as an atrribute it acts as one
print(c.diameter) # 10

c.radius = 10 # here we are using the setter decorator the code is executed under the radius.setter and the value is added 

print(c.radius) # 10
print(c.diameter) # 20

    
    