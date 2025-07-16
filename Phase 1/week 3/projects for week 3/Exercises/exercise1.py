# This is exercise 1 

#  this is a library management system 

from datetime import datetime
import re
from collections import Counter

class Book:
    def __init__(self, title:str, author:str, isbn:int, year:int, genre:str, is_available:bool):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.genre = genre
        self._available = is_available
    
    def checkout(self) -> bool: #  marked as checked out
        if self._available == False:
            return False
        else:
            self._available = False
            return True
    
    def return_book(self): # marks as available
        if self._available == True:
            return False
        else:
            self._available = True
            return True
    
    def is_available(self) -> bool : # returns avilability status
        return self._available 
    
    def validate_isbn(self) -> bool: # checks if isbn is 13 digits
        ISBN_LEGNTH = 13
        if len(self.isbn) == ISBN_LEGNTH:
            return True
        else:
            return False
    
    def __str__(self):
        available = ""
        if self.is_available == True:
            available = "Available"
        else:
            available = "Not Avilable"
        
        return f"Book name - {self.author} by {self.author} \nBorrowed Status - {available}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', is_available=`{self._available}`, genre=`{self.genre}`, year=`{self.year}` )"
    
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


book = Book("life of Pi","samod", 1234567890123, 2005, "male", True )
print(book.checkout())
print(book.is_available())