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


