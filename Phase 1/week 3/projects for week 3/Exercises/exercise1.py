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
        if len(str(self.isbn)) == ISBN_LEGNTH:
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
    def __init__(self, member_id:int, email:str, join_date, _borrowed_books = None): # join_date = datetime(2024, 7, 16)
        self._member_id = member_id
        self.email = email
        self.join_date = join_date
        self._borrowed_books = _borrowed_books if _borrowed_books is not None else [] # list of books objects
        
    def borrow_book(self, book) -> bool: # adds to the borrwed list maximum is 3 books
        MAXIMUM_NUMBER_OF_BOOKS = 3
        
        if len(self._borrowed_books) <= MAXIMUM_NUMBER_OF_BOOKS:
            return False
        else:
            self._borrowed_books.append(book)
            return True
    
    def return_book(self, book): # removed from borrow list 
        if book in self._borrowed_books:
            self._borrowed_books.remove(book)
            return True
        else:
            return False
    
    def get_membership_duration(self): # returns days since the join
        return (datetime.now() - self.join_date).days
    
    def list_borrwed_books(self): # Show current borrowe books
        list_of_books = []
        
        for book in self._borrowed_books:
            list_of_books.append(f"{book.title} by {book.author}")
        
        return list_of_books
            

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