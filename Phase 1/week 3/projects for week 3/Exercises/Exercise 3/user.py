from abc import abstractmethod, ABC
import hashlib # Use Case: Password hashing for secure user credentials
from enum import Enum

class UserRoles(Enum):
    ADMIN = "Admin"
    MANAGER = "Manager"
    EMPLOYEE = "Employeee"

class User(ABC):
    def __init__(self, user_name:str, email:str, password_hash:str ) -> None:
        self.user_name = user_name
        self.email = email
        self._password_hash = self.hash_password(password_hash) # hashed password

    def hash_password(self, password:str) -> str:
        return hashlib.sha256(password.encode("utf-8")).hexdigest()
    
    def check_password(self, input_password) -> bool: # validates password input
        return self.hash_password(input_password) == self._password_hash
    
    @abstractmethod
    def get_role(self) -> str: # Returns your role
        pass
    
    def is_authorized(self, action):#
        pass
    
    @abstractmethod
    def can_create_task(self) -> bool:
        pass
    
    @abstractmethod
    def can_assign_task(self) -> bool:
        pass
    
    @abstractmethod
    def can_delete_task(self) -> bool:
        pass




class Admin(User): # full permissions
    def __init__(self, user_name: str, email: str, password_hash:str) -> None:
        super().__init__(user_name, email, password_hash)
        self.role = UserRoles.ADMIN.value

    def get_role(self) -> str:
        return f"{self.role}"
    
    def can_delete_task(self) -> bool:
        return True
    
    def can_assign_task(self) -> bool:
        return True
    
    def can_create_task(self) -> bool:
        return True

class Manager(User): # Can assign items to employees
    def __init__(self, user_name: str, email: str, password_hash:str) -> None:
        super().__init__(user_name, email, password_hash)
        self.role = UserRoles.MANAGER.value

    def get_role(self) -> str:
        return f"{self.role}"
    
    def can_delete_task(self) -> bool:
        return False
    
    def can_assign_task(self) -> bool:
        return True
    
    def can_create_task(self) -> bool:
        return True

class Employee(User): # can work on the assigned work
    def __init__(self, user_name: str, email: str, password_hash:str) -> None:
        super().__init__(user_name, email, password_hash)
        self.role = UserRoles.EMPLOYEE.value
    
    def get_role(self) -> str:
        return f"{self.role}"
    
    def can_assign_task(self) -> bool:
        return False

    def can_delete_task(self) -> bool:
        return False
    
    def can_create_task(self) -> bool:
        return False
    
    
admin1 = Admin("samod", "samod@gmail.com", "pakaya")
print(admin1.check_password("pakaya"))
print(admin1.get_role())