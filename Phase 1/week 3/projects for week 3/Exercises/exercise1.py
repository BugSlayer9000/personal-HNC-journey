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
        if self._available == True:
            available = "Available"
        else:
            available = "Not Avilable"
        
        return f"Book name - {self.title} by {self.author} Is available - {available} Isbn - {self.isbn}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', is_available=`{self._available}`, genre=`{self.genre}`, year=`{self.year}` )"
    
class Member:
    def __init__(self,name ,member_id:int, email:str, join_date,): # join_date = datetime(2024, 7, 16)
        self._member_id = member_id
        self.email = email
        self.join_date = join_date
        self._borrowed_books = [] # list of books objects
        self.name = name
        
    def borrow_book(self, book) -> bool: # adds to the borrwed list maximum is 3 books
        MAXIMUM_NUMBER_OF_BOOKS = 3
        
        if len(self._borrowed_books) >= MAXIMUM_NUMBER_OF_BOOKS:
            print("Maximum number of books per member reached")
            return False
        else:
            if book.checkout(): #  make sure the availability chanched before adding the item to the list 
                self._borrowed_books.append(book)
                return True
            else:
                return False
            
    
    def return_book(self, book): # removed from borrow list 
        if book in self._borrowed_books:
            book.return_book()
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
    
    def add_book(self, book):
        if book in self.books:
            return "This book is already exists"
        else:
            self.books.append(book)
            return "Book added"
            
    
    def add_member(self, member):
        if member in self.members:
            return "This member already exists"
        else:
            self.members.append(member)
            return "member added "
    
    def search_books(self, by_title = None, auther = None , genre = None):
        pass
        # implement it later
    
    def checkout_book(self, isbn, member_id):
        
        for book in self.books:
            
            for member in self.members:
                
                if book.isbn == isbn and member._member_id == member_id:  
                    # added the book to borroed books list
                    if member.borrow_book(book):
                        print(f"{book.title} for member id - {member._member_id} added successfuly.")
                        
                    else:
                        print("Error")
                    break
               
    
    def return_book(self, isbn, member_id):
        print("return book protocol")
        for book in self.books:
            
            for member in self.members:
                
                if book.isbn == isbn and member._member_id == member_id:  
                    # added the book to borroed books list
                    if member.return_book(book):
                        print(f"{book.title} for member id - {member._member_id} returned successfuly.")
                    else:
                        print("Error")
                    break
    
    def generate_report(self): # overdue books, popular genres
        pass
    
    def validate_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return True
            else:
                return False



book1 = Book("Life of Pi", "Yann Martel", 9780156027328, 2001, "Fiction", True)
book2 = Book("1984", "George Orwell", 9780451524935, 1949, "Dystopian", True)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 9780061120084, 1960, "Classic", True)
book4 = Book("The Hobbit", "J.R.R. Tolkien", 9780547928227, 1937, "Fantasy", True)
book5 = Book("A Brief History of Time", "Stephen Hawking", 9780553380163, 1988, "Science", True)


member = Member("John Smith", 123456, "pakaya@email.com", datetime(2024, 7, 6))
member1 = Member("Alice Johnson", 234567, "alice@example.com", datetime(2023, 5, 12))
member2 = Member("Bob Williams", 345678, "bob@example.com", datetime(2022, 11, 30))
member3 = Member("Carol Brown", 456789, "carol@example.com", datetime(2024, 1, 15))
member4 = Member("Dave Miller", 567890, "dave@example.com", datetime(2021, 8, 22))








 