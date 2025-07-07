# Samod subhasha

# Activity 3: E-commerce System (Advanced Level)

# Task
    # Create a comprehensive e-commerce system with multiple interacting classes.

# Requirements

    # Product Class
        # Attributes: name, price, category, stock_quantity, product_id
        
        # Methods:

            # __init__(self, name, price, category, stock_quantity)
            # update_stock(self, quantity) - adds/removes stock
            # apply_discount(self, percentage) - applies discount to price
            # __str__(), __repr__(), __eq__()

    # Customer Class

    # Attributes: name, email, customer_id, purchase_history
    # Methods:

        # __init__(self, name, email)
        # add_purchase(self, product, quantity) - adds to purchase history
        # get_total_spent() - calculates total amount spent
        # get_purchase_history() - returns formatted purchase history



    # ShoppingCart Class

    # Attributes: customer, items (dictionary: product -> quantity)
    # Methods:

        # __init__(self, customer)
        # add_item(self, product, quantity) - adds product to cart
        # remove_item(self, product) - removes product from cart
        # update_quantity(self, product, new_quantity) - updates quantity
        # get_total() - calculates total price
        # checkout() - processes the order and updates stock



    # Store Class

    # Attributes: name, products, customers
    # Methods:

        # __init__(self, name)
        # add_product(self, product) - adds product to store
        # register_customer(self, customer) - registers a customer
        # find_product(self, name) - finds product by name
        # get_low_stock_products(self, threshold=5) - returns products with low stock



# Testing Your Solution
    # python# Test your e-commerce system
    # store = Store("TechMart Online")

    # # Add products
    # laptop = Product("Gaming Laptop", 999.99, "Electronics", 10)
    # mouse = Product("Wireless Mouse", 29.99, "Electronics", 50)
    # keyboard = Product("Mechanical Keyboard", 79.99, "Electronics", 25)

    # store.add_product(laptop)
    # store.add_product(mouse)
    # store.add_product(keyboard)

    # # Register customer
    # customer = Customer("John Doe", "john@email.com")
    # store.register_customer(customer)

    # # Create shopping cart
    # cart = ShoppingCart(customer)
    # cart.add_item(laptop, 1)
    # cart.add_item(mouse, 2)

    # print(f"Cart total: £{cart.get_total():.2f}")

    # # Process checkout
    # receipt = cart.checkout()
    # print(f"\nReceipt: {receipt}")

    # # Check updated stock
    # print(f"\nLaptop stock after purchase: {laptop.stock_quantity}")
    # print(f"Customer total spent: £{customer.get_total_spent():.2f}")
    # Challenges for Activity 3

    # Validation Challenge: Add comprehensive input validation for all classes
    # Persistence Challenge: Implement methods to save/load data from files
    # Advanced Features Challenge: Add features like:

    # Product reviews and ratings
    # Customer loyalty points
    # Discount codes and promotions
    # Order status tracking

# Challenge 
    # Error Handling Challenge: Implement robust error handling for all operations
    # Design Pattern Challenge: Implement the Observer pattern to notify customers of stock updates
    # Database Challenge: Modify classes to work with a simple database (using sqlite3)

class Product:
    # Attributes: name, price, category, stock_quantity, product_id
    
    def __init__(self, name, price, category, stock_quantitiy):
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantitiy = stock_quantitiy
        self.product_id = 0 # have to work on this 
    
    def update_stock(self, quantitiy): # adds/removes stock
        self.stock_quantitiy += quantitiy
    
    def apply_discount(self, percentage:int): # applies discount to price
        self.price = self.price * (percentage/100) 
    
    def __str__(self):
        return f"Product name = {self.name} \nPrice per 1  - 3{self.price} "
    
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r}, {self.category!r}, {self.stock_quantitiy!r})"
    
    def __eq__(self, value):
        return self.name == self.name
    
class Customer:
    # Attributes: name, email, customer_id, purchase_history
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.customer_id = 0
        self.purchase_history = []
    
    def add_purchase(self, product, quantitiy): #  adds to purchase history
        self.purchase_history[product] = quantitiy
    
    def get_total_spent(self): # calculates total amount spent
        total_spent = 0
        
        for product in self.purchase_history:
            total_spent += Product.price
        
        # add a try exept block later
    
    def get_purhcase_history(self): # returns formatted purchase history
        if len(self.purchase_history) != 0 :
            for product in self.purchase_history:
                return f"Product name = {product} X {self.purchase_history[product]}"
        else: 
            return f"No product history found ! "

class ShoppingCart:
    # Attributes: customer, items (dictionary: product -> quantity)
    
    def __init__(self, customer):
        self.customer = customer
        self.items = [] # (product -> quantity)
    
    def add_item(self, product, quantitiy): # adds product to cart
        self.items[product] = quantitiy
    
    def remove_item(self, product): # removes product from cart
        if product.Lower() in self.items.Lower():
            del self.items[product]
        else:
            print("Product not found !")
    
    def update_quantitiy(self, product, new_quantity): # updates quantity
        if product.Lower() in self.items.Lower():
            if not new_quantity < 0:
                self.items[product] = new_quantity
            else: 
                print("Quantity must be above 0 ")
        else:
            print("Product not found ! ")
    
    def get_total(self): # calculates total price
        for product in self.items.keys():
            print(product)
            # I'll complete this after Store Class 
    
    def checkout(self): # processes the order and updates stock
        pass
    # I'll complete this after Store Class 

class Store:
    # Attributes: name, products, customers
    
    def __init__(self, name):
        self.name = name
        self.products = []
        self.customers = []
    
    def add_products(self, product): # adds product to store
        self.products.append(product)
    
    def register_customer(self, customer): # registers a customer
        self.customers.append(customer)
    
    def find_products(self, name): # finds product by name
        if name in self.products:
            print(f"{name} available !")
        else:
            print(f"{name} not available ! ")
    
    def get_low_stock_products(self, threshhold = 5): # returns products with low stock
        low_stock = []
        for product in self.products:
            if product.stock_quantitiy < threshhold:
                low_stock.append(product.name)
            else:
                pass
        
        print("Low Stock products")
        for i,item  in enumerate(low_stock,1):
            print(f"{i}.{item}")

# Testing Your Solution
    # python# Test your e-commerce system
    store = Store("TechMart Online")

    # Add products
    laptop = Product("Gaming Laptop", 999.99, "Electronics", 10)
    mouse = Product("Wireless Mouse", 29.99, "Electronics", 50)
    keyboard = Product("Mechanical Keyboard", 79.99, "Electronics", 25)