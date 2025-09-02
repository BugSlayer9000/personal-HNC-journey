import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from managers.inventory_manager import InventoryManager
from patterns.singleton import Logger



def options():
    print(f"\n1.Add an Item\n2.Remove an Item\n3.Check one Item\n4.Search by Category\n5.Filter By Expiry Date\n")

def main():
    
    
    while True:
        manager = InventoryManager()
        logger = Logger()
        
        print(f"\n{"#"*14} INVENTORY MANAGER {"#"*14}")
              
        options()
        
        chosen = input("Enter the number of your choice : ")
            



main()
        


