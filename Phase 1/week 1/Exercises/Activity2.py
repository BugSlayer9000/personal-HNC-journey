# samod subhasha
# 🔧 Activity 2: Student Management
# Create a Student class with name, student_id, course.
# Add a method enroll() that prints "Student <name> enrolled in <course>".

# 🔁 Extend: Create 3 different student objects with different data.

class StudentManagement: # change the name to `Student`
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
    
    def enroll(self):
        print(f"Student ID = {self.student_id}") # Added some details to the method
        print(f"{self.name} has enrolled in {self.course}. ")

def main():
    student1_details = StudentManagement("samod",1234567,"HND computing")
    student1_details.enroll()

    # Extended Exersise
    student2_details = StudentManagement("Robert", 12345678, "HND Gardning")
    student2_details.enroll()

    student3_details = StudentManagement("Kelum", 12345678, "HND Web Dev")
    student3_details.enroll()

    student4_details = StudentManagement("Ash", 12345678, "HND Computing")
    student4_details.enroll()

if __name__ == "__main__":
    main()

# things I should add to class 
# def __str__(self):
#     return f"Name: {self.name}, ID: {self.student_id}, Course: {self.course}"


    