from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class BaseClassItem(ABC):
    def __init__(self, _id:str, _name:str, _price:float, _quantity:int, _category:str, _created_at:datetime) -> None:
        self._id = _id
        self._name =_name
        self._price = _price
        self._quantity = _quantity
        self._category = _category
        self._created_at = _created_at
        self._attribute_check()
        
    def _attribute_check(self):
        
        if not isinstance(self._price, (int, float)):
            raise TypeError("Price must be a float")
        
        if type(self._id) != str:
            raise TypeError("Id type must be String")
        
        if not type(self._quantity) == int:
            raise TypeError("Quantity type must be int")
        
        if self._quantity <= 0 :
            raise ValueError("Error in the quantity attribute")
        
        if self._price < 0 :
            raise ValueError("Error in the price attribute")
        
        if not len(self._name) > 1:
            raise ValueError("Name attribute must have at least 2 characters")
        
        if self._created_at is None:
            self._created_at = datetime.now()
        elif not isinstance(self._created_at,  datetime):
            raise TypeError("created_at must be a datetime object")
        
    
    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def quantity(self) -> int:
        return self._quantity
    
    
    def update_quantity(self, amount:int):
        if amount > 0 :
            self._quantity = amount 
        else:
            raise ValueError("Amount must be above 0")
    
    def get_total_value(self) -> float:
        return self._price * self._quantity
    
    
    def __str__(self) -> str:
        return f"Item({self._id}, {self._name}, {self._price}, {self._quantity}, {self._category}, {self._created_at})"

    def __repr__(self) -> str:
        return self.__str__()

    @abstractmethod
    def get_item_type(self):
        pass
    
    @abstractmethod
    def to_dict(self):
        pass
    
    @abstractmethod
    def apply_discount(self, percentage: float):
        pass