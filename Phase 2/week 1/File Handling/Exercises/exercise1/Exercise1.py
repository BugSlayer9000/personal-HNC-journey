# samod subhasha
# 10/09/25

# A program that writes your name, course, and today’s date into a file. Then read it back and display it.

# Covering - Phase 2 week 1 - File handling basics 

# Features 
    # Try to open a txt file from the given file path and if not creates one
    # different fucntions for appending and viewing the file without earing the history
    

from datetime import datetime

file_path = "C:\\my stuff\\git\\personal-HNC-journey\\Phase 2\\week 1\\File Handling\\Exercises\\exercise1\\data.txt"


def file_initiation() -> None:
    try:
        with open(file_path, "x"):   # Creates a file if one doesn't exixst in the given location
            pass
    except FileExistsError:
        with open(file_path, "r"):
            pass
            


def writeFiles(content) -> None:
    with open(file_path, "a") as write:
        content = write.write(content)

def readfiles():
    with open(file_path, "r") as read:
        return read.read()
        
file_initiation()


while True:
    
    user_input = int
    
    print("1.view file\n2.add details\n3.Delete an item\n")
    
    try:
        user_input = int(input("Enter the choice : "))
        if user_input >= 4:
            print("Enter a valid choice !")
            continue
        
    except ValueError:
        print("Enter a number please ! ")
    
    if user_input == 1:
        print("\nOption 1")
        print(readfiles())
        
    elif user_input == 2: # write files
        print("Option 2")
        
        student_name = str(input("Enter the name of the student : "))
        course_name = str(input("Enter the name of the course : "))
        
        full_detail = f"Student name - {student_name} -> course name - {course_name}"
        
        writeFiles(f"{full_detail}\n")
        
        print(f"{full_detail } - Added to the system")
    
    elif user_input == 3:
        print("\nOption 3 - Delete an item\n")
        
        
    
        
    
    