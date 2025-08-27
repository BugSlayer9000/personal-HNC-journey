# test inventory class 








# Step 1: Create InventoryManager
manager = InventoryManager()

# Step 2: Add items
perishable = PerishableItem("2", "Milk", 3.50, 10, "Groceries", datetime.now(), datetime.now() + timedelta(days=7))
digital = DigitalItem("3", "E-Book", 5.99, 100, "E-Books", datetime.now(), 2.5, "http://example.com/ebook")
manager.add_item(perishable)
manager.add_item(digital)


