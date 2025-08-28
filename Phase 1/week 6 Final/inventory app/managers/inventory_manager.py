import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from items.item import Item


from datetime import datetime

class InventoryManager:
    def __init__(self) -> None:
        self.items = {}
    
    def __list_keys(self):
        return list(self.items.keys())
    
    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("item is not compatible must be an instance of item class")
        
        
        if len(self.items) >= 1: 
            id_status = False
            
            for list_item in self.items.keys():
                if list_item == item.id:
                    raise ValueError("item id must be uniqe")
                else:
                    id_status = True
            
            if id_status:
                 self.items[item.id] = item
            
            
        else:
            self.items[item.id] = item

    def remove_item(self, item_id:str):
        
        if len(self.items) == 0:
            raise ValueError("No items found in the system")
        
        if item_id  in self.__list_keys():
            del self.items[item_id]
        else:
            raise ValueError("Item not found")
        
    
    def get_an_item(self, item_id):
        if len(self.items) == 0:
            raise ValueError("Invenotry is empty")
        
        if item_id in self.__list_keys():
            return self.items[item_id]
        else:
            raise ValueError("item is not in the inventory")
        
    
    def list_all_items(self):
        return self.items
    
    def search_by_category(self):
        pass
    
    def filter_by_expity_date(self):
        pass
    
