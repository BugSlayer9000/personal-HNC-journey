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
    
# New class that will inherit from the Book class and override one if the methods to show polumorphism

class EBook(Book):
    def __init__(self, title: str, author: str, isbn: int, year: int, genre: str, is_available: bool):
        super().__init__(title, author, isbn, year, genre, is_available)
        self.is_e_book = True
        self.download_count = 0
    
    def checkout(self) -> bool:
        if self.is_e_book == True:
            self._available = True
            self.download_count += 1
            return True
        else:
            return False
        
    
class Member:
    def __init__(self,name ,member_id:int, email:str, join_date): # join_date = datetime(2024, 7, 16)
        self._member_id = member_id
        self.email = email
        self.join_date = join_date
        self._borrowed_books = [] # list of books objects
        self.name = name
        
        
    @property
    def member_id(self):
        return self._member_id
        
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
    
    def __str__(self) -> str:
        return f"Member name - {self.name} member_id -  {self._member_id} email - {self.email} Num of books borrowed - {len(self._borrowed_books)}"
            

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
    
    def search_books(self, **kwargs):
        
        attrs = ["title", "author", "isbn", "year", "genre", "is_available" ]
        
        results = []
        
        for key,value in kwargs.items(): 
            if key in attrs:
                for book in self.books:
                    if getattr(book, key) == value:
                        if value not in results:
                            results.append(f"Result found - {book.title} Searched by - {key} - {value}")
                        else:
                            pass
            else:
                pass
                
        return results

        
    
    def checkout_book(self, isbn, member_id):
        # solution 1
        # running a loop untill i find them
        
        # for book in self.books:
            
        #     for member in self.members:
                
        #         if book.isbn == isbn and member._member_id == member_id:  
        #             # added the book to borroed books list
        #             if member.borrow_book(book):
        #                 print(f"{book.title} for member id - {member._member_id} added successfuly.")
        #                 break
        #             else:
        #                 print(f"{book.title} couldn't add")
        #                 break
        
        
        # solution 2
        # validate one loop then move into the other 
        
        is_isbn_valid = False
        valid_book = None
        is_member_id_valid = False
        valid_member = None
        
        
        for book in self.books: # checked if the isbn arg is valid
            if book.isbn == isbn:
                is_isbn_valid = True
                valid_book = book
                break
            else:
                pass
        
        if is_isbn_valid: # checked if the member_id arg is valid
            for member in self.members:
                if member.member_id == member_id:
                    is_member_id_valid = True
                    valid_member = member
                    break
                else:
                    pass
        
        if is_isbn_valid and is_member_id_valid and valid_member is not None and valid_book is not None: # run if both of the args are valid
            print(valid_member.borrow_book(valid_book))
        else:
            print(f"Couldn't add book isbn {isbn} to member id {member_id} ")

    
    def return_book(self, isbn, member_id):
        # solution 1
        # print("return book protocol")
        # for book in self.books:
            
        #     for member in self.members:
                
        #         if book.isbn == isbn and member._member_id == member_id:  
        #             # added the book to borroed books list
        #             if member.return_book(book):
        #                 print(f"{book.title} for member id - {member._member_id} returned successfuly.")
        #                 break
        #             else:
        #                 print(f"Error")
        #                 break
        
        # solution 2
        is_isbn_valid = False
        valid_book = None
        is_member_id_valid = False
        valid_member = None
        
        
        for book in self.books: # checked if the isbn arg is valid
            if book.isbn == isbn:
                is_isbn_valid = True
                valid_book = book
                break
            else:
                pass
        
        if is_isbn_valid: # checked if the member_id arg is valid
            for member in self.members:
                if member.member_id == member_id:
                    is_member_id_valid = True
                    valid_member = member
                    break
                else:
                    pass
        
        if is_isbn_valid and is_member_id_valid and valid_member is not None and valid_book is not None: # run if both of the args are valid
            print(valid_member.return_book(valid_book))
        else:
            print(f"Couldn't return book isbn {isbn} from member id - {member_id} ")

    
    def generate_report(self): # overdue books, popular genres
        avilable_books = []
        for book in self.books:
            if book.is_available():
                avilable_books.append(f"{book.title}")
            else:
                pass
           
        print("\nAvailable books ")
        for i,book in enumerate(avilable_books,1):
            print(f"{i}.{book}")
    
    def validate_member(self,member_id):
        for member in self.members:
            if member.member_id == member_id:
                return True
            else:
                return False


# Code tests #######################################

library = Library()

from datetime import datetime

# Test Books - Additional examples for your library system
book6 = Book("The Great Gatsby", "F. Scott Fitzgerald", 9780743273565, 1925, "Classic", True)
book7 = Book("Pride and Prejudice", "Jane Austen", 9780141439518, 1813, "Romance", True)
book8 = Book("The Catcher in the Rye", "J.D. Salinger", 9780316769174, 1951, "Fiction", True)
book9 = Book("Lord of the Flies", "William Golding", 9780571056866, 1954, "Fiction", True)
book10 = Book("The Da Vinci Code", "Dan Brown", 9780385504201, 2003, "Thriller", True)
book11 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 9780747532699, 1997, "Fantasy", True)
book12 = Book("The Alchemist", "Paulo Coelho", 9780062315007, 1988, "Fiction", True)
book13 = Book("Sapiens", "Yuval Noah Harari", 9780062316097, 2011, "Science", True)
book14 = Book("The Kite Runner", "Khaled Hosseini", 9781594631931, 2003, "Fiction", True)
book15 = Book("Gone Girl", "Gillian Flynn", 9780307588364, 2012, "Thriller", True)

# Test Members - Additional examples for your library system (updated with name parameter)
member5 = Member("Emma Watson", 678901, "emma@example.com", datetime(2023, 3, 8))
member6 = Member("Frank Rodriguez", 789012, "frank@example.com", datetime(2024, 2, 14))
member7 = Member("Grace Lee", 890123, "grace@example.com", datetime(2023, 9, 25))
member8 = Member("Henry Thompson", 901234, "henry@example.com", datetime(2022, 6, 18))
member9 = Member("Iris Chen", 112345, "iris@example.com", datetime(2024, 4, 12))
member10 = Member("Jack Wilson", 123450, "jack@example.com", datetime(2023, 12, 3))
member11 = Member("Karen Davis", 234561, "karen@example.com", datetime(2024, 5, 20))
member12 = Member("Liam O'Connor", 345672, "liam@example.com", datetime(2022, 10, 7))
member13 = Member("Mia Garcia", 456783, "mia@example.com", datetime(2023, 7, 15))
member14 = Member("Noah Martinez", 567894, "noah@example.com", datetime(2024, 1, 28))

# Test scenarios for your library system
print("=== Testing Library Management System ===")

# Add all books to library
library.add_book(book6)
library.add_book(book7)
library.add_book(book8)
library.add_book(book9)
library.add_book(book10)
library.add_book(book11)
library.add_book(book12)
library.add_book(book13)
library.add_book(book14)
library.add_book(book15)

# Add all members to library
library.add_member(member5)
library.add_member(member6)
library.add_member(member7)
library.add_member(member8)
library.add_member(member9)

# # Test checkout scenarios
# print("\n=== Testing Checkout Scenarios ===")
# library.checkout_book(9780743273565, 678901)  # The Great Gatsby to Emma Watson
# library.checkout_book(9780141439518, 678901)  # Pride and Prejudice to Emma Watson
# library.checkout_book(9780316769174, 789012)  # The Catcher in the Rye to Frank Rodriguez

# # Test return scenarios
# print("\n=== Testing Return Scenarios ===")
# library.return_book(9780743273565, 678901)  # Emma Watson returns The Great Gatsby

# # Test member functionality
# print("\n=== Testing Member Functionality ===")
# print(f"{member5.name}'s membership duration: {member5.get_membership_duration()} days")
# print(f"{member5.name}'s borrowed books: {member5.list_borrwed_books()}")

# # Test book validation
# print("\n=== Testing Book Validation ===")
# print(f"Book6 ISBN valid: {book6.validate_isbn()}")
# print(f"Book7 availability: {book7.is_available()}")

# # Test edge cases
# print("\n=== Testing Edge Cases ===")
# # Try to checkout the same book twice
# library.checkout_book(9780307588364, 789012)  # Should work
# library.checkout_book(9780307588364, 890123)  # Should fail (book not available)

# # Try to exceed member limit
# library.checkout_book(9781594631931, 890123)  # The Kite Runner 
# library.checkout_book(9780571056866, 890123)  # Grace Lee gets Lord of the Flies  
# library.checkout_book(9780385504201, 890123)  # Grace Lee gets Da Vinci Code
# library.checkout_book(9780747532699, 890123)  # Should fail (max 3 books)

# print("\n=== Library Status ===")
# print(f"Total books in library: {len(library.books)}")
# print(f"Total members in library: {len(library.members)}")

# # Display some book information
# print("\n=== Sample Book Information ===")
# print(book6)
# print(book7)
# print(book8)


# # Genarate report
# print("\n=== Genarate report ===")
# library.generate_report()





# print("\n=== SUBCLASS TEST ===")
# ######### SUB CLASS TEST ################

# # Create an Ebook instance
# ebook1 = EBook(
#     title="Digital Fortress",
#     author="Dan Brown",
#     isbn=1234567890123,
#     year=1998,
#     genre="Thriller",
#     is_available=True
# )

# # Test 1: Check initial availability (should always be True for eBooks)
# print(f"Is available: {ebook1.is_available()}")  # Expected: True

# # Test 2: Checkout/download the ebook (should increment download count)
# print(f"Checkout 1: {ebook1.checkout()}")         # Expected: True
# print(f"Downloads: {ebook1.download_count}")      # Expected: 1

# # Test 3: Multiple checkouts
# ebook1.checkout()
# ebook1.checkout()
# print(f"Total Downloads: {ebook1.download_count}")  # Expected: 3

# # Test 4: Set is_e_book to False, simulate invalid eBook
# ebook1.is_e_book = False
# print(f"Checkout non-eBook: {ebook1.checkout()}")   # Expected: False
# print(f"Downloads after fail: {ebook1.download_count}")  # Should stay at 3




print("\n=== SEARCH BOOKS TEST ===")

search1 = library.search_books(author = "F. Scott Fitzgerald", # works
                               isbn = 9780743273565, # works
                               title = "Lord of the Flies", # works
                               genre = "Fiction", # 4 results works
                            )

if search1:
    for i in search1:
        print(i)
else:
    print("No results found")

search2 = library.search_books(author = "pakaya",
                               isbn = 218764846187264,
                               title = "harrry potter")

if search2:
    for i in search2:
        print(i)
else:
    print("no results found for search 2")

