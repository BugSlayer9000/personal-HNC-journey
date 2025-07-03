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

