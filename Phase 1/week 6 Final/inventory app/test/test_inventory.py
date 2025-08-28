# test inventory class 
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from items.item import Item
from items.base_item import BaseClassItem
from items.digital_item import DigitalItem
from items.perishable_item import PerishableItem
from managers.inventory_manager import InventoryManager
from datetime import datetime, timedelta





# Step 1: Create InventoryManager
manager = InventoryManager()

# Step 2: Add items
perishable = PerishableItem("2", "Milk", 3.50, 10, "Groceries", datetime.now(), datetime.now() + timedelta(days=7))
digital = DigitalItem("3", "E-Book", 5.99, 100, "E-Books", datetime.now(), 2.5, "http://example.com/ebook")
digital1 = DigitalItem("4", "E-Book", 5.99, 100, "E-Books", datetime.now(), 2.5, "http://example.com/ebook")



manager.add_item(perishable)
manager.add_item(digital)
manager.add_item(digital1) # added three items 

print(manager.list_all_items()) # Showes 3 items 


manager.remove_item("3") # removes item under the id "3"

print(manager.list_all_items()) # Showed 2 items


