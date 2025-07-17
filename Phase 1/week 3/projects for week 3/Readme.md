# OOP EXERCISES - PROGRESSIVE DIFFICULTY  
# Instructions and Test Code Only - You Implement the Solutions!

"""
================================================================================
EXERCISE 1: LIBRARY MANAGEMENT SYSTEM (BEGINNER-INTERMEDIATE)
================================================================================

MODULES TO IMPORT:
- from datetime import datetime
- import re
- from collections import Counter

INSTRUCTIONS:
Create a library management system using solid object-oriented principles.

CLASS RESPONSIBILITIES:

1. Book:
   - Attributes: title, author, isbn, year, genre, _available
   - Methods:
     * checkout() - marks as checked out
     * return_book() - marks as available
     * is_available() - returns availability status
     * validate_isbn() - checks if ISBN is exactly 13 digits

2. Member:
   - Attributes: name, member_id, email, join_date, _borrowed_books
   - Methods:
     * borrow_book(book) - adds to borrowed list (max 3 books)
     * return_book(book) - removes from borrowed list
     * get_membership_duration() - returns days since joined
     * list_borrowed_books() - shows current borrowed books

3. Library:
   - Attributes: books (list), members (list)
   - Methods:
     * add_book(book), add_member(member)
     * search_books(by title/author/genre)
     * checkout_book(isbn, member_id)
     * return_book(isbn, member_id)
     * generate_report() - overdue books, popular genres
     * validate_member(member_id)

KEY OOP CONCEPTS TO APPLY:
- Encapsulation: Use protected attributes
- Abstraction: Hide internal search/validation logic
- Inheritance: Plan for extended Book types
- Polymorphism: Unified search interface

EXTRA CHALLENGE:
Implement a reservation system for checked-out books.
"""


"""
================================================================================
EXERCISE 2: ONLINE SHOPPING CART WITH PAYMENT PROCESSING (INTERMEDIATE)
================================================================================

MODULES TO IMPORT:
- from abc import ABC, abstractmethod
- from enum import Enum
- from decimal import Decimal
- from uuid import uuid4
- from datetime import datetime

INSTRUCTIONS:
Create an online store system supporting both digital and physical products.

CLASS RESPONSIBILITIES:

1. Product (Abstract Base):
   - Attributes: name, price, sku, description
   - Methods:
     * get_tax()
     * get_shipping_cost()
     * validate_price()
   - Abstract methods: get_tax(), get_shipping_cost()
   - **Responsibilities**
      * Store common product attributes (name, price, SKU, description)
      * Define abstract methods for tax calculation and shipping costs
      * Handle price validation

2. DigitalProduct (inherits Product):
   - Additional attributes: file_size, download_link
   - get_tax(): digital tax rate
   - get_shipping_cost(): always 0
   
   - **Responsibilities**
      * No shipping costs
      * Immediate delivery
      * Different tax rates
      * File size and download link attributes

3. PhysicalProduct (inherits Product):
   - Additional attributes: weight, dimensions
   - get_tax(): physical product tax
   - get_shipping_cost(): based on weight/dimensions
   - **Responsibilities**
      * Weight and dimensions for shipping calculation
      * Inventory tracking
      * Shipping costs based on weight/size
      * File size and download link attributes

4. ShoppingCart:
   - Attributes: product list
   - Methods:
     * add_product(), remove_product()
     * calculate_subtotal(), calculate_total()
     * apply_discount(code)
     * validate_cart()
   - **Responsibilities**
      * Add/remove products
      * Calculate subtotals, taxes, and shipping
      * Apply discount codes
      * Validate cart contents before checkout

5. PaymentProcessor (Abstract Base):
   - Method: process_payment(amount)
   - **Responsibilities**
      * Define common payment interface
      * Handle payment validation

6. CreditCardProcessor / PayPalProcessor:
   - Specific validation rules, fee structures
   - **Responsibilities**
      * Implement specific payment methods
      * Different validation rules
      * Different fee structures

7. Order:
   - Attributes: cart, timestamp, payment_status
   - Methods: calculate_final_total(), get_order_summary()
   - **Responsibilities**
        * Store order details and history
        * Track order status
        * Calculate final totals

KEY OOP CONCEPTS TO APPLY:
- Abstraction: Abstract base for Product and PaymentProcessor
- Inheritance: Digital and Physical Product types
- Polymorphism: PaymentProcessor interface
- Encapsulation: Price and payment logic


HOW IT SHOULD WORK
- How It Should Work: Users can add different types of products to their cart, apply discounts, choose payment methods, and complete purchases. The system should handle different tax rates, shipping costs, and payment processing fees.
Extra Challenge: Implement a decorator pattern for dynamic discount application (percentage off, buy-one-get-one, seasonal discounts) that can be stacked.



EXTRA CHALLENGE:
Implement a decorator system for dynamic discounts (BOGO, %, seasonal).
"""


"""
================================================================================
EXERCISE 3: TASK MANAGEMENT SYSTEM WITH USER ROLES & NOTIFICATIONS (ADVANCED)
================================================================================

MODULES TO IMPORT:
- from abc import ABC, abstractmethod
- from enum import Enum
- from datetime import datetime, timedelta
- import hashlib
- from functools import wraps
- import threading
- from collections import deque

INSTRUCTIONS:
Design a project management system with users, tasks, and role-based permissions.

CLASS RESPONSIBILITIES:

1. User (Abstract Base):
   - Attributes: username, email, _password_hash
   - Methods:
     * check_password(), get_role(), is_authorized()
   - Abstract methods: can_create_task(), can_assign_task()

2. Admin, Manager, Employee (inherit User):
   - Different roles, task limits, permissions
   - Override permissions accordingly

3. Task:
   - Attributes: title, description, status, priority, deadline
   - Methods:
     * assign_to(user)
     * change_status()
     * get_remaining_time()
     * log_history()

4. Project:
   - Attributes: tasks, members
   - Methods:
     * add_task(), remove_task()
     * progress_report(), filter_tasks()

5. NotificationService (Singleton):
   - Method: send_notification()
   - Tracks notification history

6. TaskObserver (Observer Pattern):
   - EmailNotifier, SlackNotifier, SMSNotifier
   - React to task status changes

7. TaskFactory:
   - Create specialized task types (Bug, Feature, Meeting)
   - Validate creation rules

KEY OOP CONCEPTS TO APPLY:
- Abstraction: User roles and observers
- Inheritance: Role-based user access
- Polymorphism: Notification handling
- Encapsulation: Hide user data
- Patterns: Singleton (Notification), Observer, Factory

EXTRA CHALLENGE:
Implement a command pattern with undo/redo for task operations.
"""
