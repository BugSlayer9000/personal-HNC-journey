# Cheks there is only one inventory is present 




class Logger:

    _instance = None
    
    def __new__(cls, *args, **kwargs) :
        
        if not cls._instance :
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def log(self, massage):
        print(f"[LOG]: {massage}")


    
    

                