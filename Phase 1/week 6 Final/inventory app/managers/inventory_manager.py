from items.item import Item
from items.digital_item import DigitalItem
from items.perishable_item import PerishableItem

from datetime import datetime

class InventoryManager:
    def __init__(self) -> None:
        self.items = {}
    
    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("item is not compatible must be an instance of item class")
        
        if len(self.items) >= 1:

            for i in self.items:
                if i.id == item.id:
                    raise  ValueError("Each item must have a unique id")
                self.items[item.id] = item

    def remove_item(self, item_id):
        pass
    
    def get_an_item(self, item_id):
        pass
    
    def list_all_items(self):
        pass
    
    def search_by_category(self):
        pass
    
    def filter_by_expity_date(self):
        pass
    
    
