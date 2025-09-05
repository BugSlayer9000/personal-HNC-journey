import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from items.item import Item
from datetime import datetime

class PerishableItem(Item):
    def __init__(self, _id: str, _name: str, _price: float, _quantity: int, _category: str, _created_at: datetime, _expiry_date:datetime) -> None:
        self._expiry_date = _expiry_date 
        super().__init__(_id, _name, _price, _quantity, _category, _created_at)
        
        

    @property
    def expiry_date(self):
        return self._expiry_date
    
    def to_dict(self):
        return super().to_dict() | {
            "expiry_date": self._expiry_date
        }
    



