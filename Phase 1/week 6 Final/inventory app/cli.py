import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from managers.inventory_manager import InventoryManager
from datetime import datetime, timedelta, date


from item_collect import ItemCollector
from patterns.item_factory import ItemFactory

def options():
    print(f"\n1.Add an Item\n2.Remove an Item\n3.Check one Item\n4.Search by Category\n5.Filter By Expiry Date\n6. Exit\n")
        

def main():
    
    
    while True:
        manager = InventoryManager()
        
        chosen = 0
        
        print(f"\n{"#"*14} INVENTORY MANAGER {"#"*14}")
              
        options()
        
        try:
            chosen = int(input("Enter the number of your choice : "))
        except:
            ValueError("Input must be a number")
        
        if chosen > 6:
            print("Choose a number between 1-6")
            continue
            
        elif chosen == 1:
            Collector = ItemCollector() # Collects all the data for the item
            
            
            data = Collector.collect_item() # turns it all into a dictionary
            
            
            item = ItemFactory.create(data) # creates an item based using the made dict 
            
            manager.add_item(item)
            
        elif chosen == 2: # remove an item
            
            input_id = None
            item_list = manager.list_all_items() # get the dict directly
            
            if len(item_list) <= 0: # chekcks the item list before proceeding
                print("No items in the Inventory")
                continue
            
            list_of_id = []
            
            for id , item in item_list.items(): # prints the id and item name to the user 
                list_of_id.append(id)
                print(f"{id} - {item.get_name}")
            
            try:
                input_id = str(input("Enter the id of the item : "))
            except:
                ValueError("Input Invalid")
            
            if  input_id not in list_of_id:
                print("Id Not found")
                continue
            
            print(f"item Sucessfully removed from the inventory ")
            
            manager.remove_item(str(input_id))
            
            
            
        elif chosen == 3: # chekc one item
            input_id = None
            item_list = manager.list_all_items() # get the dict directly
            
            if len(item_list) <= 0: # chekcks the item list before proceeding
                print("No items in the Inventory")
                continue
            
            list_of_id = []
            
            for id , item in item_list.items(): # prints the id and item name to the user 
                list_of_id.append(id)
                print(f"{id} - {item.get_name}")
            
            try:
                input_id = str(input("Enter the id of the item : "))
            except:
                ValueError("Input Invalid")
            
            if  input_id not in list_of_id:
                print("Id Not found")
                continue
            
            result = manager.get_an_item(input_id)
        
            print(result.to_dict())
            
            
            print("\nItem Details\n")
            for key, value in result.to_dict().items():
                print(f"{key} : {value}")
            
        elif chosen == 4: # search by category
            pass
            
            
            
            
            
            
            
        
            
        


main()
        


