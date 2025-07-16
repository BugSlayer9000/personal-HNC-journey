# This is exercise 1 

#  this is a library management system 

from datetime import datetime
import re
from collections import Counter

class Book:
    def __init__(self, title, auther, isbn, year, genre, is_available):
        self.title = title
        self.auther = auther
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self._available = is_available
    
    def checkout(self): #  amrked as checked out
        pass
    
    def return_book(self): # marks as available
        pass
    
    def is_available(self) -> bool : # returns avilability status
        pass
    
    def validate_isbn(self): # checks if isbn is 13 digits
        pass
    
class Member:
    def __init__(self, member_id, email, join_date, _borrowed_books):
        self._member_id = member_id
        self.email = email
        self.join_date = join_date
        self._borrowed_books = _borrowed_books
        
    def borrow_book(self, book): # adds to the borrwed list maximum is 3 books
        pass
    
    def return_book(self, book): # removed from borrow list 
        pass
    
    def get_membership_duration(self): # returns days since the join
        pass
    
    def list_borrwed_books(self): # Show current borrowe books
        pass

class Library:
    def __init__(self,books = None, members = None):
        self.books = books if books is not None else [] 
        self.members = members if members is not None else []
    
    def add_book(book):
        pass
    
    def add_member(member):
        pass
    
    def search_books(by_title = None, auther = None , genre = None):
        pass
    
    def checkout_book(isbn, member_id):
        pass
    
    def return_book(isbn, member_id):
        pass
    
    def generate_report(self): # overdue books, popular genres
        pass
    
    def validate_member(self):
        pass
    