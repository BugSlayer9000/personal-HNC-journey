OOP Classes and Objects - Knowledge Check Activities
Activity 1: Student Management System (Beginner Level)
Task
Create a Student class that manages student information and grades for a college system.
Requirements

Create a class called Student with the following attributes:

name (string)
student_id (string)
course (string)
grades (list of integers)


Implement these methods:

__init__(self, name, student_id, course) - constructor
add_grade(self, grade) - adds a grade to the student's record
get_average() - calculates and returns the average grade
get_letter_grade() - returns letter grade based on average (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
__str__() - returns a formatted string representation



Testing Your Solution
python# Test your class with this code
student1 = Student("Alice Johnson", "S001", "Computer Science")
student2 = Student("Bob Smith", "S002", "Software Engineering")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(95)
student2.add_grade(88)

print(student1)
print(f"Average: {student1.get_average():.1f}")
print(f"Letter Grade: {student1.get_letter_grade()}")
print()
print(student2)
print(f"Average: {student2.get_average():.1f}")
print(f"Letter Grade: {student2.get_letter_grade()}")
Challenges for Activity 1

Validation Challenge: Add input validation to ensure grades are between 0-100
Class Attribute Challenge: Add a class attribute to track the total number of students created
Method Challenge: Add a remove_grade(index) method that removes a grade at a specific position
Comparison Challenge: Implement __eq__() method to compare students by student_id


Activity 2: Library Management System (Intermediate Level)
Task
Create a library system with Book and Library classes that interact with each other.
Requirements
Book Class

Attributes: title, author, isbn, is_available, borrower, due_date
Methods:

__init__(self, title, author, isbn)
borrow(self, borrower_name) - marks book as borrowed
return_book() - marks book as available
is_overdue() - checks if book is overdue (assume 14 days from borrow date)
__str__() and __repr__()



Library Class

Attributes: name, books (list of Book objects)
Methods:

__init__(self, name)
add_book(self, book) - adds a Book object to the library
find_book(self, title) - returns Book object if found
borrow_book(self, title, borrower) - borrows a book by title
return_book(self, title) - returns a book by title
get_available_books() - returns list of available books
get_overdue_books() - returns list of overdue books



Testing Your Solution
python# Test your classes
from datetime import datetime, timedelta

library = Library("City Central Library")

# Add books
book1 = Book("Python Programming", "John Smith", "978-1234567890")
book2 = Book("Data Structures", "Jane Doe", "978-0987654321")
book3 = Book("Web Development", "Mike Johnson", "978-1122334455")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Test borrowing
print(library.borrow_book("Python Programming", "Alice"))
print(library.borrow_book("Data Structures", "Bob"))

# Display available books
print("\nAvailable Books:")
for book in library.get_available_books():
    print(f"- {book}")

# Try to borrow already borrowed book
print(f"\n{library.borrow_book('Python Programming', 'Charlie')}")
Challenges for Activity 2

Date Management Challenge: Use Python's datetime module to track actual borrow dates and calculate due dates
Search Challenge: Implement search_books(self, keyword) that searches by title or author
Statistics Challenge: Add methods to get library statistics (total books, borrowed books, etc.)
Error Handling Challenge: Add proper error handling for cases like book not found, already borrowed, etc.
Advanced Search Challenge: Implement filtering by author, availability status, or ISBN


Activity 3: E-commerce System (Advanced Level)
Task
Create a comprehensive e-commerce system with multiple interacting classes.
Requirements
Product Class

Attributes: name, price, category, stock_quantity, product_id
Methods:

__init__(self, name, price, category, stock_quantity)
update_stock(self, quantity) - adds/removes stock
apply_discount(self, percentage) - applies discount to price
__str__(), __repr__(), __eq__()



Customer Class

Attributes: name, email, customer_id, purchase_history
Methods:

__init__(self, name, email)
add_purchase(self, product, quantity) - adds to purchase history
get_total_spent() - calculates total amount spent
get_purchase_history() - returns formatted purchase history



ShoppingCart Class

Attributes: customer, items (dictionary: product -> quantity)
Methods:

__init__(self, customer)
add_item(self, product, quantity) - adds product to cart
remove_item(self, product) - removes product from cart
update_quantity(self, product, new_quantity) - updates quantity
get_total() - calculates total price
checkout() - processes the order and updates stock



Store Class

Attributes: name, products, customers
Methods:

__init__(self, name)
add_product(self, product) - adds product to store
register_customer(self, customer) - registers a customer
find_product(self, name) - finds product by name
get_low_stock_products(self, threshold=5) - returns products with low stock



Testing Your Solution
python# Test your e-commerce system
store = Store("TechMart Online")

# Add products
laptop = Product("Gaming Laptop", 999.99, "Electronics", 10)
mouse = Product("Wireless Mouse", 29.99, "Electronics", 50)
keyboard = Product("Mechanical Keyboard", 79.99, "Electronics", 25)

store.add_product(laptop)
store.add_product(mouse)
store.add_product(keyboard)

# Register customer
customer = Customer("John Doe", "john@email.com")
store.register_customer(customer)

# Create shopping cart
cart = ShoppingCart(customer)
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)

print(f"Cart total: £{cart.get_total():.2f}")

# Process checkout
receipt = cart.checkout()
print(f"\nReceipt: {receipt}")

# Check updated stock
print(f"\nLaptop stock after purchase: {laptop.stock_quantity}")
print(f"Customer total spent: £{customer.get_total_spent():.2f}")
Challenges for Activity 3

Validation Challenge: Add comprehensive input validation for all classes
Persistence Challenge: Implement methods to save/load data from files
Advanced Features Challenge: Add features like:

Product reviews and ratings
Customer loyalty points
Discount codes and promotions
Order status tracking


Error Handling Challenge: Implement robust error handling for all operations
Design Pattern Challenge: Implement the Observer pattern to notify customers of stock updates
Database Challenge: Modify classes to work with a simple database (using sqlite3)


Assessment Criteria
For Each Activity, Check:

Correct Class Structure: Are classes properly defined with appropriate attributes and methods?
Encapsulation: Are attributes properly encapsulated and accessed through methods?
Method Implementation: Do methods perform their intended functionality correctly?
Object Interaction: Do objects interact properly with each other?
Error Handling: Are edge cases and errors handled appropriately?
Code Quality: Is the code readable, well-commented, and follows Python conventions?

Progressive Difficulty

Activity 1: Tests basic class creation, instance attributes, and simple methods
Activity 2: Tests object interaction, class relationships, and more complex logic
Activity 3: Tests advanced OOP concepts, multiple class interactions, and real-world application

Complete each activity before moving to the next, and tackle the challenges to deepen your understanding!