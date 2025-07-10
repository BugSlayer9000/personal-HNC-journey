# samod subhasha
# ✅ Exercise 5: Inventory Item
# Task:
# Create an InventoryItem class:

# Private attributes: __name, __price, __stock

# Methods:

# restock(amount)

# sell(quantity)

# get_stock()

# get_details() – return a formatted string


class Inventoryitem:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    def restock(self, amount:int) -> bool:
        if 0 < amount:
            self.__stock += amount
            return True
        else:
            return False
    
    def sell(self, quantitiy:int) -> bool:
        if 0 < quantitiy and self.__stock >= quantitiy:
            self.__stock -= quantitiy
            return True
        else:
            return False 
    
    def get_stock(self) -> int:
        return self.__stock
    
    def get_details(self):
        return f"Product name - {self.__name} \nprice : £ {self.__price:.2f} \nstock available : {self.__stock}"


ineventory = Inventoryitem("Laptop", 999, 50)
print(ineventory.restock(10)) # True
print(ineventory.restock(-10)) # false
print(ineventory.sell(-10)) # false
print(ineventory.sell(10)) # True
print(ineventory.sell(1000)) # false
print(ineventory.get_stock()) 
print(ineventory.get_details())

# 📊 Final Scorecard
# Category	Score	Comments
# Encapsulation	✅ 5/5	Textbook example
# Validation Logic	✅ 5/5	Solid, failsafe
# Readability & Structure	⚠️ 4.5/5	Naming/casing
# Output Quality	✅ 5/5	Very clean and usable
# Reusability	✅ 5/5	Could be used in a real-world app

# 🔥 Final Verdict: 24.5 / 25 — You nailed it. This is professional-level work.


