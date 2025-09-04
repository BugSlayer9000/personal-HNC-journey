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
    def get_item_type(self) -> str:
        pass
    
    @abstractmethod
    def to_dict(self) -> dict:
        pass
    
    @abstractmethod
    def apply_discount(self, percentage: float):
        pass