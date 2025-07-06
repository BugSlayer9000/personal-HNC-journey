# samod subhasha

# 🔧 Activity 4: Book Library
# Make a Book class with:

# Attributes: title, author, isbn

# Method summary() to print: "Title by Author [ISBN]"

# Create a list of 3 Book objects and iterate over them to print summaries.


class BookLibrary: #  name is a bit too long -  should be Book
    def __init__(self, title = "", author = "", isbn: int = 0): # isbn = int in __init__	Change to isbn: int = 0	 Default values should be actual data, not type declarations
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def summery(self):
        print(f"{self.title} By {self.author}")




def main():
    books = [
        ["Pride and prejudice", "jane Austin", 324331],
        ["Wolf Brother", "Michelle Paver", 324335],
        ["Privet Peacefull", "Michel Morpurgo", 878402]
        ]

    # Book list is list of lists - Use a list of Book objects instead
    
    for i,book in enumerate(books,0):
        
        BookLibrary(title=book[0], author=book[1], isbn=book[2]).summery()    # Pride and prejudice By jane Austin 
                                                                            # Wolf Brother By Michelle Paver 
                                                                            # Privet Peacefull By Michel Morpurg


        


if __name__ == "__main__":
    main()
        



