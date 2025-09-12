# samod subhasha
# 12/09/2025

# program - Student grade data with name , student id, grade
# CSV file handling Basics 

# Features 
    # This programe creates a CSV file if one doesn't exist 
    # Asks for the name of the student then the grade they got
    # You can check back the grandes they got

import csv
from pathlib import Path

file_path = Path("C:\\my stuff\\git\\personal-HNC-journey\\Phase 2\\week 1\\File Handling\\Exercises\\exercise3\\data.csv")

file_path.touch(exist_ok=True)


def setup_csv():
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id","name","grade"]) # Header row


# newline = ""              --- says not to add an extra line between rows
# writer = csv.writer(file) --- Basically calls for a function that knows how to write rows and lines right

#  adding student details
def add_details(id, name, grade):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id,name,grade])


# Read the file
def read_students():
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        next(reader) # Skips header
        
        for row in reader:
            student_id, student_name, student_grade = row
            print(f"Student id = {student_id} - name = {student_name} - grade = {student_grade}")
            

# run program
setup_csv()

add_details(1, "Alice", "A")
add_details(2, "Bob", "B")
add_details(3, "Charlie", "C")

print("\nReading Student records")

read_students()