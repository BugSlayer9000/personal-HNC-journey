import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from items.item import Item
from items.base_item import BaseClassItem
from items.digital_item import DigitalItem
from items.perishable_item import PerishableItem
from managers.inventory_manager import InventoryManager
from datetime import datetime, timedelta


class ItemFactory:
    
    @staticmethod
    def create(data:dict):
        if data["category"] == "perishable items":
            return PerishableItem(
                data["id"], data["name"],
                data["price"], data["quantitiy"],
                data["category"], data["created_at"],
                data["expiry_date"]
                )
        
        elif data["category"] == "digital items":
            return DigitalItem(
                data["id"], data["name"],
                data["price"], data["quantitiy"], 
                data["category"], data["created_at"],
                data["download_size"], data["download_link"] 
            )
        
        else:
            return Item(
                data["name"], data["name"],
                data["price"], data["quantitiy"], 
                data["category"], data["created_at"]
            )