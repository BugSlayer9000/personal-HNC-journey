# samod subhasha
#  Exercise 3: Car Speed Control
# Task:
# Create a Car class with:

# Private attribute: __speed

# Method: accelerate(amount), brake(amount), get_speed()

# Ensure speed never goes negative or exceeds 200.

class Car:
    def __init__(self, speed:int):
        self.__speed = max(0, speed)
    
    def accelerate(self, amount:int) -> bool:
        maximum_speed = 200
        if 0 <= amount and self.__speed + amount <= maximum_speed:
            self.__speed += amount
            return True
        else:
            # capping the spedd at 200 
            self.__speed = min(self.__speed + amount, 200)
            return False
    
    def brake(self, amount:int) -> bool:
        if 0 < amount < self.__speed:
            self.__speed -= amount
            return True
        else:
            return False
    
    def get_speed(self) -> int:
        return self.__speed


car  = Car(100)
print(car.accelerate(-20))
print(car.accelerate(60))
print(car.brake(-200))
print(car.brake(20))
print(car.get_speed())

# ✅ What You Did Well

    # ✅ Encapsulation
    # ✅ Constructor Safeguard
    # ✅ Speed Limits Enforced
    # ✅ Brake Logic is Defensive
    # ✅ Type Hints

# ❌ Improvements Needed

    # Incorrect Return Type in get_speed()
    # Missing Handling for Exceeding Max Speed Gracefully
    
    