# Activity 2: Library Management System (Intermediate Level)
# Task
    # Create a library system with Book and Library classes that interact with each other.
# Requirements
    # Book Class

    # Attributes: title, author, isbn, is_available, borrower, due_date
# Methods:

    # __init__(self, title, author, isbn)
    # borrow(self, borrower_name) - marks book as borrowed
    # return_book() - marks book as available
    # is_overdue() - checks if book is overdue (assume 14 days from borrow date)
    # __str__() and __repr__()



# Library Class

    # Attributes: name, books (list of Book objects)
# Methods:

    # __init__(self, name)
    # add_book(self, book) - adds a Book object to the library
    # find_book(self, title) - returns Book object if found
    # borrow_book(self, title, borrower) - borrows a book by title
    # return_book(self, title) - returns a book by title
    # get_available_books() - returns list of available books
    # get_overdue_books() - returns list of overdue books

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
        self.borrower = None
        self.due_date = None
        
        
    def borrow(self,borrower_name):
        if self.is_available:
            self.is_available = False
            self.borrower = borrower_name
            # add the due date logic later 
            return f"{self.title} borrowed by {self.borrower}"
        else:
            return f"{self.title} is already borrowed. "
    
    def returnbook(self):
        if not self.is_available:
            self.is_available = True
            # add the due logic later 
            return f"{self.title} returned successfully"
        else:
            return f"No borrow status for {self.title}"
    
    def is_overdue():
        # work on due date later 
        pass
    
    def __str__(self):
        Availability = ""
        if self.is_available:
            Availability = "Available"
        else: 
            Availability = "Not Available"
        return f"Book name : {self.title} by {self.author} \nBorrowed status : {Availability}  \nDue date : {self.due_date}" 
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', is_available=`{self.is_available}`,borrower=`{self.borrower}`, due_date=`{self.due_date}` )"

class Library:
    
    def __init__(self,name):
        self.name = name
        self.collection = []
        
    def add_book(self, name):
        self.collection.append(name)
    
    def find_book(self, title):
        # Access its title using book.title.
        for book in self.collection:
            if book.title == title:
                return True, book
        else:
            return False, None
            
    
    def borrow_book(self, title, borrower):
        book_found, book = self.find_book(title)
        if book_found and book.is_available : 
            book.borrower = borrower
            book.is_available = False
            return f"{book.title} by {book.author} borrowed by `{borrower}`successfully"
        else:
            return f"Book not found"
    
    def get_available_books(self):
        
        avilable_books = []
        
        if len(self.collection) != 0:
            for book in self.collection:
                if book.is_available == True:
                    avilable_books.append(f"{book.title} by {book.author}")
            
            return avilable_books
        else:
            return "All books are borrowed at the moment ! "
             
                
    
    def get_overdue_books(self):
        # I will implenet it later after I get the basic logic done
        pass
    
    def __str__(self):
       return f"Book collection - {self.collection}"

# Add books
book1 = Book("Python Programming", "John Smith", "978-1234567890")
book2 = Book("Data Structures", "Jane Doe", "978-0987654321")
book3 = Book("Web Development", "Mike Johnson", "978-1122334455")
book4 = Book("Software dev", "Mike Johnson", "978-1122334455")

library = Library("Samods super Library")

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
print(f"\n{library.borrow_book("Python Programming", "Alice")}")


# claude Review

# Good progress on Activity 2! You've got the basic structure working, but there are several issues to address. Let me give you detailed feedback:
# ✅ What You Did Well

# Basic class structure is correct
# Object interaction is working (Library calls Book methods)
# Core functionality is implemented
# Testing approach shows good understanding
# Incremental development (leaving complex parts for later) is smart

# ❌ Issues to Fix
# 1. Method Name Inconsistency
# python# Your Book class has:
# def returnbook(self):  # No underscore

# # But requirements specify:
# def return_book(self):  # With underscore
# 2. Logical Error in borrow_book()
# python# Your current implementation:
# def borrow_book(self, title, borrower):
#     book_found, book = self.find_book(title)
#     if book_found and book.is_available : 
#         book.borrower = borrower        # ❌ Direct attribute modification
#         book.is_available = False       # ❌ Direct attribute modification
#         return f"{book.title} by {book.author} borrowed by `{borrower}`successfully"
# Problem: You're bypassing the Book's borrow() method and directly modifying attributes. This breaks encapsulation.
# Better approach:
# pythondef borrow_book(self, title, borrower):
#     book_found, book = self.find_book(title)
#     if book_found:
#         return book.borrow(borrower)  # Use Book's method
#     else:
#         return f"Book '{title}' not found"
# 3. find_book() Return Format
# python# Your current implementation:
# def find_book(self, title):
#     for book in self.collection:
#         if book.title == title:
#             return True, book  # ❌ Returns tuple
#     else:
#         return False, None
# Problem: Requirements specify it should return the Book object if found, not a tuple.
# Better approach:
# pythondef find_book(self, title):
#     for book in self.collection:
#         if book.title.lower() == title.lower():  # Case-insensitive
#             return book
#     return None  # Book not found
# 4. Missing self Parameter
# pythondef is_overdue():  # ❌ Missing self parameter
#     pass
# Should be:
# pythondef is_overdue(self):
#     pass
# 5. Logic Error in get_available_books()
# python# Your current logic:
# if len(self.collection) != 0:
#     # ... find available books
# else:
#     return "All books are borrowed at the moment ! "  # ❌ Wrong logic
# Problem: If collection is empty, it doesn't mean all books are borrowed - it means there are no books!
# Better approach:
# pythondef get_available_books(self):
#     available = []
#     for book in self.collection:
#         if book.is_available:
#             available.append(book)
#     return available
# 6. Inconsistent Variable Names
# python# You use both:
# avilable_books = []  # ❌ Typo in "available"
# self.collection = []  # Different from requirements (should be self.books)
# 7. Missing return_book() Method in Library
# Your Library class is missing the return_book() method that's required.
# 🔧 Key Corrections Needed
# Fix the Library Class Methods:
# pythondef borrow_book(self, title, borrower):
#     book = self.find_book(title)
#     if book:
#         return book.borrow(borrower)  # Use Book's method
#     else:
#         return f"Book '{title}' not found"

# def return_book(self, title):
#     book = self.find_book(title)
#     if book:
#         return book.return_book()  # Use Book's method
#     else:
#         return f"Book '{title}' not found"

# def get_available_books(self):
#     return [book for book in self.collection if book.is_available]
# Fix the Book Class:
# pythondef return_book(self):  # Fix method name
#     if not self.is_available:
#         self.is_available = True
#         borrower = self.borrower
#         self.borrower = None
#         self.due_date = None
#         return f"{self.title} returned by {borrower}"
#     else:
#         return f"{self.title} was not borrowed"
# 🎯 Key Learning Points

# Use Object Methods: When Library needs to change Book state, call Book methods rather than directly modifying attributes
# Consistent Naming: Follow the exact method names specified in requirements
# Proper Encapsulation: Let each object manage its own state
# Return Appropriate Types: Methods should return what they promise (find_book should return Book object, not tuple)

# 🚀 Next Steps

# Fix the method names and missing methods
# Use proper object interaction (Library calls Book methods)
# Add the missing return_book() method to Library
# Test the return functionality
# Then tackle the date logic for due dates

# Your core understanding is solid - these are mostly implementation details that need polishing. The object interaction concept is working well!

