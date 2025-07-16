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
