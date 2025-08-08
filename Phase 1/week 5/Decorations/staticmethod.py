# Staticmethod decorator will be used to donate a method inside of a class as static


class math:
    
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
    

# usage

print(math.add(5,8)) # calling the method without the instance 
