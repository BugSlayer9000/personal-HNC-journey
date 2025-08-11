# Singlton pattern




class Logger:
    _instance = None
    
    def __new__(cls, *args, **Kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(self, massage):
        print(f"[LOG]: {massage}")
    
# Both variables point to the same instance 
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2) # True
logger1.log("sys started")