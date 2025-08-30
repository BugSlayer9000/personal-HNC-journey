import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from items.base_item import BaseClassItem
from datetime import datetime



class Item(BaseClassItem):
    def __init__(self, _id: str, _name: str, _price: float, _quantity: int, _category: str, _created_at: datetime) -> None:
        super().__init__(_id, _name, _price, _quantity, _category, _created_at)
        
    
        
    
    
    def get_item_type(self) -> str:
        return self._category
    

    def to_dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "quantity": self._quantity,
            "category": self._category,
            "created_at": self._created_at
        }
    
    def apply_discount(self, percentage: float):
        if isinstance(percentage, (int, float)):
            if 0 < percentage < 100:
                discount_amount = self._price * (percentage / 100)
                self._price -= discount_amount
            else:
                raise ValueError("Invalid discount percentage")



