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

2. DigitalProduct (inherits Product):
   - Additional attributes: file_size, download_link
   - get_tax(): digital tax rate
   - get_shipping_cost(): always 0

3. PhysicalProduct (inherits Product):
   - Additional attributes: weight, dimensions
   - get_tax(): physical product tax
   - get_shipping_cost(): based on weight/dimensions

4. ShoppingCart:
   - Attributes: product list
   - Methods:
     * add_product(), remove_product()
     * calculate_subtotal(), calculate_total()
     * apply_discount(code)
     * validate_cart()

5. PaymentProcessor (Abstract Base):
   - Method: process_payment(amount)

6. CreditCardProcessor / PayPalProcessor:
   - Specific validation rules, fee structures

7. Order:
   - Attributes: cart, timestamp, payment_status
   - Methods: calculate_final_total(), get_order_summary()

KEY OOP CONCEPTS TO APPLY:
- Abstraction: Abstract base for Product and PaymentProcessor
- Inheritance: Digital and Physical Product types
- Polymorphism: PaymentProcessor interface
- Encapsulation: Price and payment logic

EXTRA CHALLENGE:
Implement a decorator system for dynamic discounts (BOGO, %, seasonal).
"""
