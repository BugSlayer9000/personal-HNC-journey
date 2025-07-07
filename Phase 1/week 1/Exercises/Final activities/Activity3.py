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


