# Notifier + subclasses (Email, SMS)

# ✔ Uses a simple observer model
# ✔ Register notifiers to a task and trigger on change_status

 


from abc import abstractmethod, ABC

class Notifier(ABC):
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def update(self):
        pass

class EmailNotofier(Notifier):
    def __init__(self) -> None:
        super().__init__()
    
    def update(self):
        return super().update()

class SMSNotifier(Notifier):
    def __init__(self) -> None:
        super().__init__()
    
    def update(self):
        return super().update()