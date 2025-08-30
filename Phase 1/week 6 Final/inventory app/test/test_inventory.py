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
perishable1 = PerishableItem("7", "Cheese", 4.00, 5, "Groceries", datetime.now(), datetime.now() + timedelta(days=10))
perishable2 = PerishableItem("8", "Yogurt", 2.50, 20, "Groceries", datetime.now(), datetime.now() + timedelta(days=5))



digital = DigitalItem("3", "E-Book", 5.99, 100, "E-Books", datetime.now(), 2.5, "http://example.com/ebook")
digital1 = DigitalItem("4", "E-Book", 5.99, 100, "E-Books", datetime.now(), 2.5, "http://example.com/ebook")
digital2 = DigitalItem("5", "E-Book", 5.99, 100, "NFT", datetime.now(), 2.5, "http://example.com/ebook")
digital3 = DigitalItem("6", "E-Book", 5.99, 100, "NFT", datetime.now(), 2.5, "http://example.com/ebook")



manager.add_item(perishable)
manager.add_item(digital)
manager.add_item(digital1) # added three items 
manager.add_item(digital2)
manager.add_item(digital3)

manager.add_item(perishable1)
manager.add_item(perishable2)

print(manager.list_all_items()) # Showes 3 items 


manager.remove_item("3") # removes item under the id "3"



print(manager.list_all_items()) # Showed 2 items

print(manager.get_an_item("2")) #  returns the items with the id 2 


print(manager.search_by_category("NFT")) # Works



print(len(manager.list_all_items()))
print(manager.filter_by_expity_date(datetime.now() + timedelta(days=5))) # returns a list of lists 
# [[1, 'Milk'], [4, 'Cheese'], [-1, 'Yogurt']]



