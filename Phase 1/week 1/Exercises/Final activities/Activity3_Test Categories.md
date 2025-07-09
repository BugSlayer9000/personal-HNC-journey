Basic tests on Activity 3 Review by Chat GPT

✅ What’s Working Well
Modular OOP design: Classes are well-separated (Product, Customer, ShoppingCart, Store).

Use of dunder methods (__str__, __repr__, __eq__, __hash__): Great professional touch.

Object referencing: Using objects as dictionary keys (ShoppingCart.items) is advanced and handled correctly.

Dynamic cart/checkout functionality is working.

Clean use of list-of-lists for purchase history: correct for traceability.

get_total_spent() is accurate and demonstrates understanding of accumulation logic.

❌ Critical Problems & Required Fixes
🔺 apply_discount logic is wrong
python
Copy
Edit
self.price = self.price * (percentage / 100)
This makes the price only the discount portion, not the discounted price.

✅ Fix logic:

python
Copy
Edit
self.price *= (1 - (percentage / 100))
🔺 get_purhcase_history() returns only the first entry, not a full list
python
Copy
Edit
return f"Product name = {product} X {self.purchase_history[product]}"
return inside a loop terminates after the first item.

You’re treating purchase_history (a list of lists) as a dictionary.

✅ Fix strategy:

Build a string result with join() or print() line-by-line.

Or return the full list of strings.

🔺 ShoppingCart.checkout() uses customer.add_purchase() but references an external variable customer
python
Copy
Edit
customer.add_purchase(product_name, product_price, quantitiy)
This works only because of the global customer used for testing.

It won’t work in production with multiple customers.

✅ Fix:

python
Copy
Edit
self.customer.add_purchase(product_name, product_price, quantitiy)
🔺 update_stock() logic allows underflow
python
Copy
Edit
if quantitiy < self.stock_quantity:
    self.stock_quantity -= quantitiy
If quantity == stock_quantity, the subtraction is blocked.

Doesn’t protect against quantity > stock_quantity.

✅ Replace with:

python
Copy
Edit
if 0 <= quantity <= self.stock_quantity:
    self.stock_quantity -= quantity
else:
    print("Not enough stock available.")
⚠️ Minor/Stylistic Fixes
🟡 __str__() in Product typo:
python
Copy
Edit
return f"Product name = {self.name} \nPrice per 1  - 3{self.price} "
"3" before price is a typo.

✅ Should be:

python
Copy
Edit
return f"Product name: {self.name}\nPrice per unit: £{self.price:.2f}"
🟡 Method name typo
python
Copy
Edit
def update_quantitiy(self, ...)
✅ Rename to:

python
Copy
Edit
def update_quantity(self, ...)
🟡 find_products() does identity comparison, not name match
python
Copy
Edit
if name in self.products:
It will always return False, because name is a string and self.products contains Product objects.

✅ Loop through products and check:

python
Copy
Edit
for product in self.products:
    if product.name == name:
        return product
🧠 Suggested Enhancements (Advanced HNC Practice)
Auto-increment product/customer ID using a class-level counter or UUID.

Persistent storage: Save/load products and customer data using json, csv, or pickle.

Validation wrappers: Add type-checks and input guards (assert, try/except, or @staticmethod validators).

Better formatting in receipt (checkout() should format return cleanly).

Add timestamps in purchase history (datetime.now()).

Use logging module instead of print() for real-world production readiness.

Add unit tests using unittest for each class.

🔚 Final Evaluation (HNC Level 7 Criteria)
Category	Grade	Notes
OOP Design & Structure	✅ Merit	Solid class interaction, good encapsulation
Code Logic & Accuracy	⚠️ Pass	Several logic flaws, but can be corrected easily
Error Handling	❌ Fail	Missing completely, expected at this level
User Experience & Output	⚠️ Pass	Functional, but lacks polish (typos, messages, formatting)
Extendability & Features	✅ Merit	Easy to expand (good architecture)

✅ To-do List (from this review)
 Fix apply_discount math

 Rewrite get_purchase_history() for full output

 Remove global dependency from checkout()

 Handle stock underflow properly in update_stock()

 Fix all naming typos and string formatting issues

 Implement proper find_product() search

 Add at least one layer of input validation or error handling

 Bonus: start logging, timestamping, or persistence features






###Advanced Testing

Test Categories Explained: (Powerd by claude ai)
1. Product Class Logic Tests

Unique ID generation - ensures each product gets a unique identifier
Stock management - tests positive/negative stock updates and boundary conditions
Discount applications - tests single and multiple discount scenarios
Product equality - verifies your __eq__ implementation works correctly

2. Customer Class Logic Tests

Customer ID uniqueness - similar to products
Purchase history tracking - ensures all purchases are recorded correctly
Total spent calculation - verifies math is correct across multiple purchases
Purchase history formatting - checks your display format

3. Shopping Cart Logic Tests

Item addition/removal - tests cart manipulation
Quantity updates - including edge cases like setting to 0
Total calculation - ensures pricing math is accurate
Dictionary handling - verifies the product→quantity mapping works

4. Store Class Logic Tests

Product management - adding and finding products
Customer registration - managing customer database
Low stock detection - testing inventory alerts with different thresholds
Search functionality - including case sensitivity testing

5. Integration Tests

Full workflow - complete purchase from cart to checkout
Cross-class communication - ensures objects update each other correctly
Multiple customers - tests system with concurrent users
Stock synchronization - verifies inventory updates properly

6. Edge Case Tests

Empty operations - empty carts, zero quantities
Boundary conditions - negative numbers, out-of-stock scenarios
Extreme discounts - 100%+ discount handling
Invalid operations - testing system robustness

7. Performance Tests

Large datasets - how system handles many products/customers
Search efficiency - performance with large inventories
Calculation speed - complex cart totals with many items

Key Logic Checks These Tests Verify:

Data Integrity: Do objects maintain consistent state?
Business Logic: Are business rules enforced correctly?
Object Relationships: Do classes interact properly?
Edge Case Handling: Does system behave predictably in unusual situations?
Performance: Does system scale reasonably?

How to Use These Tests:

Run incrementally - start with Product tests, then Customer, etc.
Fix issues as you find them - don't move to next test until current one passes
Add print statements in your methods to trace execution
Compare expected vs actual results for each test
Use these as development guides - they show what functionality you need

Additional Custom Tests You Can Add:

Inventory turnover - track which products sell fastest
Customer loyalty - test repeat purchase patterns
Seasonal pricing - test dynamic pricing changes
Bulk operations - test adding many items at once
Data persistence - test saving/loading store state

These tests will reveal logical flaws, edge cases you missed, and help you build a robust system that handles real-world scenarios!

#########################################################################################
#########################################################################################

# Activity 3: E-commerce System - Comprehensive Testing Scenarios

# ============================================================================
# TEST SET 1: PRODUCT CLASS LOGIC TESTS
# ============================================================================

def test_product_functionality():
    print("=== PRODUCT CLASS TESTS ===")
    
    # Test 1: Product ID generation (should be unique)
    product1 = Product("Laptop", 1000, "Electronics", 5)
    product2 = Product("Mouse", 25, "Electronics", 10)
    product3 = Product("Laptop", 1000, "Electronics", 5)  # Same name, different object
    
    print(f"Product 1 ID: {product1.product_id}")
    print(f"Product 2 ID: {product2.product_id}")
    print(f"Product 3 ID: {product3.product_id}")
    print(f"Are IDs unique? {len({product1.product_id, product2.product_id, product3.product_id}) == 3}")
    
    # Test 2: Stock update logic (positive and negative)
    print(f"\nInitial stock: {product1.stock_quantity}")
    product1.update_stock(3)  # Add stock
    print(f"After adding 3: {product1.stock_quantity}")
    product1.update_stock(-2)  # Remove stock
    print(f"After removing 2: {product1.stock_quantity}")
    
    # Test 3: Stock update with insufficient stock
    result = product1.update_stock(-20)  # Try to remove more than available
    print(f"Trying to remove 20 from {product1.stock_quantity}: {result}")
    print(f"Stock after failed removal: {product1.stock_quantity}")
    
    # Test 4: Multiple discount applications
    original_price = product1.price
    print(f"\nOriginal price: £{original_price}")
    product1.apply_discount(10)  # 10% discount
    print(f"After 10% discount: £{product1.price}")
    product1.apply_discount(20)  # Another 20% discount on already discounted price
    print(f"After additional 20% discount: £{product1.price}")
    
    # Test 5: Product equality testing
    product4 = Product("Laptop", 1000, "Electronics", 5)
    product5 = Product("Laptop", 1000, "Electronics", 5)
    print(f"\nProduct equality test:")
    print(f"product4 == product5: {product4 == product5}")
    print(f"product1 == product4: {product1 == product4}")

# ============================================================================
# TEST SET 2: CUSTOMER CLASS LOGIC TESTS
# ============================================================================

def test_customer_functionality():
    print("\n=== CUSTOMER CLASS TESTS ===")
    
    customer = Customer("Alice Johnson", "alice@email.com")
    
    # Test 1: Customer ID generation
    customer2 = Customer("Bob Smith", "bob@email.com")
    print(f"Customer 1 ID: {customer.customer_id}")
    print(f"Customer 2 ID: {customer2.customer_id}")
    
    # Test 2: Purchase history tracking
    laptop = Product("Gaming Laptop", 999.99, "Electronics", 10)
    mouse = Product("Wireless Mouse", 29.99, "Electronics", 50)
    
    customer.add_purchase(laptop, 1)
    customer.add_purchase(mouse, 2)
    customer.add_purchase(laptop, 1)  # Same product, different purchase
    
    print(f"\nPurchase history:")
    print(customer.get_purchase_history())
    
    # Test 3: Total spent calculation
    print(f"Total spent: £{customer.get_total_spent():.2f}")
    
    # Test 4: Multiple purchases of same product
    keyboard = Product("Mechanical Keyboard", 79.99, "Electronics", 25)
    customer.add_purchase(keyboard, 3)
    
    print(f"After buying 3 keyboards:")
    print(f"Total spent: £{customer.get_total_spent():.2f}")
    
    # Test 5: Purchase history format verification
    history = customer.get_purchase_history()
    print(f"Purchase history contains product names: {'Gaming Laptop' in history}")
    print(f"Purchase history contains quantities: {'x1' in history or '1x' in history}")

# ============================================================================
# TEST SET 3: SHOPPING CART LOGIC TESTS
# ============================================================================

def test_shopping_cart_functionality():
    print("\n=== SHOPPING CART TESTS ===")
    
    customer = Customer("Charlie Brown", "charlie@email.com")
    cart = ShoppingCart(customer)
    
    laptop = Product("Gaming Laptop", 999.99, "Electronics", 10)
    mouse = Product("Wireless Mouse", 29.99, "Electronics", 50)
    keyboard = Product("Mechanical Keyboard", 79.99, "Electronics", 25)
    
    # Test 1: Adding items to cart
    cart.add_item(laptop, 1)
    cart.add_item(mouse, 2)
    print(f"Cart after adding items: {len(cart.items)} different products")
    print(f"Total mice in cart: {cart.items.get(mouse, 0)}")
    
    # Test 2: Adding same product multiple times
    cart.add_item(laptop, 1)  # Should increase quantity, not add new entry
    print(f"Laptops in cart after adding another: {cart.items.get(laptop, 0)}")
    
    # Test 3: Updating quantities
    cart.update_quantity(mouse, 5)
    print(f"Mice after updating to 5: {cart.items.get(mouse, 0)}")
    
    # Test 4: Setting quantity to 0 (should remove item)
    cart.update_quantity(mouse, 0)
    print(f"Mice after setting to 0: {cart.items.get(mouse, 0)}")
    print(f"Mouse still in cart: {mouse in cart.items}")
    
    # Test 5: Removing items
    cart.add_item(keyboard, 1)
    cart.remove_item(keyboard)
    print(f"Keyboard in cart after removal: {keyboard in cart.items}")
    
    # Test 6: Cart total calculation
    cart.add_item(mouse, 3)  # Add back for total calculation
    expected_total = (laptop.price * 2) + (mouse.price * 3)
    actual_total = cart.get_total()
    print(f"Expected total: £{expected_total:.2f}")
    print(f"Actual total: £{actual_total:.2f}")
    print(f"Total calculation correct: {abs(expected_total - actual_total) < 0.01}")

# ============================================================================
# TEST SET 4: STORE CLASS LOGIC TESTS
# ============================================================================

def test_store_functionality():
    print("\n=== STORE CLASS TESTS ===")
    
    store = Store("TechMart Online")
    
    # Test 1: Product management
    laptop = Product("Gaming Laptop", 999.99, "Electronics", 10)
    mouse = Product("Wireless Mouse", 29.99, "Electronics", 50)
    keyboard = Product("Mechanical Keyboard", 79.99, "Electronics", 2)  # Low stock
    headphones = Product("Wireless Headphones", 199.99, "Electronics", 3)  # Low stock
    
    store.add_product(laptop)
    store.add_product(mouse)
    store.add_product(keyboard)
    store.add_product(headphones)
    
    print(f"Total products in store: {len(store.products)}")
    
    # Test 2: Product search (case sensitivity)
    found_laptop = store.find_product("Gaming Laptop")
    found_laptop_lower = store.find_product("gaming laptop")
    print(f"Found laptop with exact case: {found_laptop is not None}")
    print(f"Found laptop with lower case: {found_laptop_lower is not None}")
    
    # Test 3: Customer registration
    customer1 = Customer("Alice Johnson", "alice@email.com")
    customer2 = Customer("Bob Smith", "bob@email.com")
    
    store.register_customer(customer1)
    store.register_customer(customer2)
    print(f"Total registered customers: {len(store.customers)}")
    
    # Test 4: Low stock detection
    low_stock_products = store.get_low_stock_products(threshold=5)
    print(f"Products with stock <= 5: {len(low_stock_products)}")
    for product in low_stock_products:
        print(f"  - {product.name}: {product.stock_quantity} units")
    
    # Test 5: Custom threshold testing
    very_low_stock = store.get_low_stock_products(threshold=2)
    print(f"Products with stock <= 2: {len(very_low_stock)}")

# ============================================================================
# TEST SET 5: INTEGRATION TESTS (MULTIPLE CLASSES WORKING TOGETHER)
# ============================================================================

def test_integration_scenarios():
    print("\n=== INTEGRATION TESTS ===")
    
    # Setup
    store = Store("TechMart Online")
    laptop = Product("Gaming Laptop", 999.99, "Electronics", 3)
    mouse = Product("Wireless Mouse", 29.99, "Electronics", 10)
    
    store.add_product(laptop)
    store.add_product(mouse)
    
    customer = Customer("Diana Prince", "diana@email.com")
    store.register_customer(customer)
    
    # Test 1: Full purchase workflow
    cart = ShoppingCart(customer)
    cart.add_item(laptop, 1)
    cart.add_item(mouse, 2)
    
    initial_laptop_stock = laptop.stock_quantity
    initial_mouse_stock = mouse.stock_quantity
    
    print(f"Initial stock - Laptop: {initial_laptop_stock}, Mouse: {initial_mouse_stock}")
    
    receipt = cart.checkout()
    
    print(f"After checkout - Laptop: {laptop.stock_quantity}, Mouse: {mouse.stock_quantity}")
    print(f"Stock correctly updated: {laptop.stock_quantity == initial_laptop_stock - 1 and mouse.stock_quantity == initial_mouse_stock - 2}")
    
    # Test 2: Customer purchase history updated
    total_spent = customer.get_total_spent()
    expected_total = 999.99 + (29.99 * 2)
    print(f"Customer total spent: £{total_spent:.2f}")
    print(f"Expected total: £{expected_total:.2f}")
    print(f"Purchase history updated correctly: {abs(total_spent - expected_total) < 0.01}")
    
    # Test 3: Multiple customers, separate carts
    customer2 = Customer("Bruce Wayne", "bruce@email.com")
    cart2 = ShoppingCart(customer2)
    cart2.add_item(laptop, 2)  # Try to buy 2 laptops
    
    print(f"Laptops available: {laptop.stock_quantity}")
    print(f"Trying to buy 2 laptops...")
    
    # This should test insufficient stock handling
    if laptop.stock_quantity >= 2:
        receipt2 = cart2.checkout()
        print("Purchase successful")
    else:
        print("Should handle insufficient stock scenario")

# ============================================================================
# TEST SET 6: EDGE CASE AND BOUNDARY TESTS
# ============================================================================

def test_edge_cases():
    print("\n=== EDGE CASE TESTS ===")
    
    # Test 1: Empty cart checkout
    customer = Customer("Test User", "test@email.com")
    empty_cart = ShoppingCart(customer)
    
    print(f"Empty cart total: £{empty_cart.get_total():.2f}")
    empty_receipt = empty_cart.checkout()
    print(f"Empty cart checkout: {empty_receipt}")
    
    # Test 2: Zero quantity operations
    product = Product("Test Product", 10.0, "Test", 5)
    cart = ShoppingCart(customer)
    
    cart.add_item(product, 0)  # Add 0 quantity
    print(f"Adding 0 quantity result: {product in cart.items}")
    
    # Test 3: Negative quantity operations
    cart.add_item(product, 1)
    cart.update_quantity(product, -1)  # Negative quantity
    print(f"Product in cart after negative update: {product in cart.items}")
    
    # Test 4: Product with 0 stock
    out_of_stock = Product("Out of Stock", 50.0, "Test", 0)
    cart.add_item(out_of_stock, 1)
    checkout_result = cart.checkout()
    print(f"Checkout with out-of-stock item: {checkout_result}")
    
    # Test 5: Discount edge cases
    test_product = Product("Discount Test", 100.0, "Test", 1)
    test_product.apply_discount(100)  # 100% discount
    print(f"Price after 100% discount: £{test_product.price:.2f}")
    
    test_product2 = Product("Discount Test 2", 100.0, "Test", 1)
    test_product2.apply_discount(150)  # More than 100% discount
    print(f"Price after 150% discount: £{test_product2.price:.2f}")

# ============================================================================
# TEST SET 7: PERFORMANCE AND SCALE TESTS
# ============================================================================

def test_performance_scenarios():
    print("\n=== PERFORMANCE TESTS ===")
    
    # Test 1: Large inventory search
    store = Store("Large Store")
    
    # Add many products
    for i in range(1000):
        product = Product(f"Product {i}", 10.0 + i, "Category", 5)
        store.add_product(product)
    
    # Test search performance
    import time
    start_time = time.time()
    found_product = store.find_product("Product 500")
    search_time = time.time() - start_time
    
    print(f"Search in 1000 products took: {search_time:.4f} seconds")
    print(f"Product found: {found_product is not None}")
    
    # Test 2: Large cart operations
    customer = Customer("Big Buyer", "big@email.com")
    big_cart = ShoppingCart(customer)
    
    # Add many items
    for i in range(0, 100, 10):  # Every 10th product
        product = store.find_product(f"Product {i}")
        if product:
            big_cart.add_item(product, 1)
    
    start_time = time.time()
    total = big_cart.get_total()
    calc_time = time.time() - start_time
    
    print(f"Cart total calculation for {len(big_cart.items)} items: {calc_time:.4f} seconds")
    print(f"Total: £{total:.2f}")

# ============================================================================
# MAIN TESTING FUNCTION
# ============================================================================

def run_all_tests():
    """Run all test scenarios"""
    print("COMPREHENSIVE TESTING FOR E-COMMERCE SYSTEM")
    print("=" * 60)
    
    test_product_functionality()
    test_customer_functionality()
    test_shopping_cart_functionality()
    test_store_functionality()
    test_integration_scenarios()
    test_edge_cases()
    test_performance_scenarios()
    
    print("\n" + "=" * 60)
    print("TESTING COMPLETE")
    print("Review the output above to verify your implementation handles all scenarios correctly.")

# To run tests, call:
# run_all_tests()