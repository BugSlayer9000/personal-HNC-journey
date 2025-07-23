from abc import abstractmethod, ABC
import hashlib # Use Case: Password hashing for secure user credentials

class User(ABC):
    def __init__(self, user_name:str, email:str, password_hash:str ) -> None:
        self.user_name = user_name
        self.email = email
        self._password_hash = password_hash # hashed password
    
    def check_password(self, password): # validates password input
        pass
    
    def get_role(self): # Returns your role
        pass
    
    def is_authorized(self, action):#
        pass
    
    @abstractmethod
    def can_create_task(self) -> bool:
        pass
    
    @abstractmethod
    def can_assign_task(self) -> bool:
        pass
    
class Admin(User): # full permissions
    def __init__(self, user_name: str, email: str, password_hash:str) -> None:
        super().__init__(user_name, email, password_hash)
        
    def can_assign_task(self) -> bool:
        return True
    
    def can_create_task(self) -> bool:
        return True

class Manager(User): # Can assign items to employees
    def __init__(self, user_name: str, email: str, password_hash:str) -> None:
        super().__init__(user_name, email, password_hash)
    
    def can_assign_task(self) -> bool:
        return True
    
    def can_create_task(self) -> bool:
        return True

class Employee(User): # can work on the assigned work
    def __init__(self, user_name: str, email: str, password_hash:str) -> None:
        super().__init__(user_name, email, password_hash)
    
    def can_assign_task(self) -> bool:
        return False
    
    def can_create_task(self) -> bool:
        return False