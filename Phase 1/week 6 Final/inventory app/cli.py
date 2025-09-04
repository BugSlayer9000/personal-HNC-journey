import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from managers.inventory_manager import InventoryManager
from patterns.singleton import Logger
from datetime import datetime, timedelta, date

from items.base_item import BaseClassItem
from items.item import Item
from items.digital_item import DigitalItem
from items.perishable_item import PerishableItem

from item_collect import ItemCollector

def options():
    print(f"\n1.Add an Item\n2.Remove an Item\n3.Check one Item\n4.Search by Category\n5.Filter By Expiry Date\n6. Exit\n")



    
    
    
        
    


        

def main():
    
    
    while True:
        manager = InventoryManager()
        logger = Logger()
        
        chosen = 0
        
        print(f"\n{"#"*14} INVENTORY MANAGER {"#"*14}")
              
        options()
        
        try:
            chosen = int(input("Enter the number of your choice : "))
        except:
            ValueError("Input must be a number")
        
        if chosen > 6:
            print("Choose a number between 1-6")
            pass
        elif chosen == 1:
            item = ItemCollector()
            data = item.collect_item()
            
            
            
        
            
        


main()
        


