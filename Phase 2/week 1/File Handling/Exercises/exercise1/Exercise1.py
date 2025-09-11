# samod subhasha
# 10/09/25

# A program that writes your name, course, and today’s date into a file. Then read it back and display it.

# Covering - Phase 2 week 1 - File handling basics 

# Features 
    # Try to open a txt file from the given file path and if not creates one
    # different fucntions for appending and viewing the file without earing the history


# Notes - Exercise 1 added (Basic file handling)
# Notes - Exercise 2 added (Reading lines and chars)

from datetime import datetime

file_path = "C:\\my stuff\\git\\personal-HNC-journey\\Phase 2\\week 1\\File Handling\\Exercises\\exercise1\\data.txt"

            


def writeFiles(content) -> None:
    with open(file_path, "a") as write:
        content = write.write(content)

def readfiles():
    with open(file_path, "r") as read:
        return read.read()
    
    
def readlines():
    with open(file_path, "r") as f:
        return f.readlines()




while True:
    
    user_input = int
    
    print("\n0.Enter 0 to exit\n1.view file(Exercise 1)\n2.add details(Exercise 1)\n3.Delete an item(Extra)\n4.Line counter (Exercise 2)")
    
    try:
        user_input = int(input("Enter the choice : "))
        if user_input >= 5:
            print("Enter a valid choice !")
            continue
        
    except ValueError:
        print("Enter a number please ! ")

    if user_input == 0:
        break
    
    if user_input == 1:
        print("\nOption 1")
        print(readfiles())
        
    elif user_input == 2: # write files
        print("Option 2")
        
        student_name = str(input("Enter the name of the student : ")).lower().strip()
        course_name = str(input("Enter the name of the course : ")).lower().strip()
        
        full_detail = f"Student name - {student_name} -> course name - {course_name}"
        
        writeFiles(f"{full_detail}\n")
        
        print(f"{full_detail } - Added to the system")
    
    elif user_input == 3:
        print("\nOption 3 - Delete an item\n")
        
        line_list = readlines()
        
        for number ,line in enumerate(line_list , 1):
            print(f"{number}. {line}")
        
        delete_input = str(input("Enter the name of the student you want to delete : ")).lower().strip()
        
        
        with open(file_path, "w") as f: #  need to keep file open then work in it to work otherwise it will overwrite the same file again and again
            for line in line_list:
                if delete_input not in line:
                    f.write(line)
    
    elif user_input == 4:
        print("\nLine count")
        
        with open(file_path, "r") as f:
            content = f.read()
            lines_show = content.splitlines()
        
        
        
            
        
        print(f"Number of lines - {len(lines_show)}")
        print(f"Number of charachters - {len(content)}")
        
        
        
            
        
        
            
        
    
        
    
    