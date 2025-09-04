from datetime import datetime, date


class ItemCollector:
    def __init__(self):
        self.data = {}
    
    def collect_item(self):
        self.data['id'] = input("Enter the id : ")
        self.data['name'] = input("Enter the name of the item : ")
        self.data['price'] = float(input("Enter the price of the item : "))
        self.data['quantitiy'] = int(input("Enter the number of items for the product : "))
    
        self.data['created_at'] = date.today()

        self.resolve_category()
        
        return self.data
    
    def resolve_category(self):
        raw_category = str(input("Enter the category of the item : ")).lower().strip()
        
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
        
        for category_class, items in items_dict.items():
            
            if raw_category in items:
                if category_class == "perishable items":
                    
                    self.data["category"] = "perishable items"
                    
                    raw_date = (input("Enter the expirydate (YYYY-MM-DD) : "))
                    
                    try:
                        date_obj = datetime.strptime(raw_date, "%Y-%m-%d").date()
                        self.data["expiry_date"] = date_obj
                        print(f"You choose {date_obj}")
                        
                        
                        
                    except:
                        ValueError("Invalid date format. Please use YYYY-MM-DD.")
                
                elif category_class == "digital items":
                    
                    self.data["category"] = "digital items"
                    
                    self.data["download-link"] = str(input("Enter the download link for the item :"))
                    self.data["download_size"] = str(input("Enter the download size for the item : "))
                    
                    
                else:
                    self.data["category"] = "unknown"
                    print("your item will be unknown")
                    
                     



