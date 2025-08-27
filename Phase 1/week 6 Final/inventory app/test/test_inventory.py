# test inventory class 
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
manager.add_item(perishable)
manager.add_item(digital)


