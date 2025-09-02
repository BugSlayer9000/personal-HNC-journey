import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from managers.inventory_manager import InventoryManager
from patterns.singleton import Logger
from datetime import datetime, timedelta, date



def options():
    print(f"\n1.Add an Item\n2.Remove an Item\n3.Check one Item\n4.Search by Category\n5.Filter By Expiry Date\n6. Exit\n")

"""
    This class down below contains the basic inputs for an item and then extra inputs needed under different item category
""" 
class Item:
    
    def item_inputs(self):
        id = int(input("Enter the id : "))
        price = float(input("Enter the price of the item : "))
        quantitiy = int(input("Enter the number of items for the product : "))
        category = self.check_category()
        created_at = datetime.now()
        
    
    def check_category(self):
        
        raw_category = str(input("Enter the category of the item : "))
        
        items_dict = items_dict = {
                                    "digital items": [
                                        "ebook",
                                        "online course",
                                        "software license",
                                        "music album",
                                        "video game"
                                    ],
                                    "perishable items": [
                                        "milk",
                                        "eggs",
                                        "cheese",
                                        "fresh strawberries",
                                        "yogurt"
                                    ]
                                }
        
        for category_class, items in items_dict.items(): # goes through the dict 
            
            if raw_category.lower() in items: # checks if the input is in the dict
                
                
                
                if category_class == "perishable items": # run if the input is in the Perishable item category
                    
                    date = input("Enter the expirydate (YYYY-MM-DD) : ")
                    
                    try:
                        date_obj = datetime.strptime(date, "%Y-%m-%d").date()
                        self.get_expiry_date(date_obj)
                        print(f"You choose {date_obj}")
                    except:
                        ValueError("Invalid date format. Please use YYYY-MM-DD.")
                
                elif category_class == "digital items": # run if the input is in the Digital item category
                    # file size function and download link function
                    
                    
                    download_link = str(input("Enter the download link : "))
                    download_size = float(input("ENter the download size (in GB): "))
                    
                    if len(download_link) > 1 and download_size >= 0 :
                        self.get_download_link(download_link)
                        self.get_download_size(download_size)
                    else:
                        print("download link must be above 0  and download link must be longer")
                    
                    
                else:
                    print("Items must be from the library")
                
            
        return "None"
                

    
    def get_expiry_date(self, date:date):
        expiry_date = date
    
    def get_download_link(self,link):
        download_link = link
    
    def get_download_size(self, size):
        download_size = size 
        
    


        

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
            item = Item()
            item.item_inputs()
            
            
            
        
            
        


main()
        


