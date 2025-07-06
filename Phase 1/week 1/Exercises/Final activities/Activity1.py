# Student Management System
# Activity 1: Student Management System (Beginner Level)
# Task
    # Create a Student class that manages student information and grades for a college system.
    
    
# Requirements

    # Create a class called Student with the following attributes:

        # name (string)
        # student_id (string)
        # course (string)
        # grades (list of integers)


# Implement these methods:

    # __init__(self, name, student_id, course) - constructor
    # add_grade(self, grade) - adds a grade to the student's record
    # get_average() - calculates and returns the average grade
    # get_letter_grade() - returns letter grade based on average (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
    # __str__() - returns a formatted string representation

class Student:
    
    student_count = 0
    
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.grades = []
        Student.student_count += 1 #  increment when used 
    
    def add_grade(self,grade):
        # adds a grade to the student's record
        self.grades.append(grade)
    
    def get_average(self):
        # Calculate and returns the avarage grade
        
        # my solution unnecessarily complex
        # self.total = 0
        # for i,grade in enumerate(self.grades,1):
        #     self.total += grade
        
        # return self.total/i
        
        # Better solution
        # Use in built fuctions 
        if not self.grades:
            return 0 
        
        return sum(self.grades) / len(self.grades)
        
                
    
    def get_letter_grade(self):
        # Create a letter based on the grade (A: 90+, B: 80-89, C: 70-79, D: 60-69, F: <60)
       
        # My solution - Hidden dipendancies between methods. this should be self contained
        # if self.total >= 90:
        #     return f"Grade is A"
        # elif 89 >= self.total >= 80 :
        #     return f"Grade is B"
        # elif 79 >= self.total >= 70 :
        #     return f"Grade is C"
        # elif 69 >= self.total >= 60 :
        #     return f"Grade is D"
        # else:
        #     return f"Grade is F"
        
        # suggested solution 
        # self contained 
        
        avarage = self.get_average()
        if avarage >= 90:
            return f"Grade is A"
        elif 89 >= avarage >= 80 :
            return f"Grade is B"
        elif 79 >= avarage >= 70 :
            return f"Grade is C"
        elif 69 >= avarage >= 60 :
            return f"Grade is D"
        else:
            return f"Grade is F"
        
    def __str__(self):
        return f"Name of the Student : {self.name} \nStudent ID : {self.student_id} \nCourse : {self.course} "
    
# Test your class with this code
student1 = Student("Alice Johnson", "S001", "Computer Science")
student2 = Student("Bob Smith", "S002", "Software Engineering")

student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2.add_grade(95)
student2.add_grade(88)

print(student1)
print(f"Average: {student1.get_average():.1f}")
print(f"Letter Grade: {student1.get_letter_grade()}")
print()
print(student2)
print(f"Average: {student2.get_average():.1f}")
print(f"Letter Grade: {student2.get_letter_grade()}")

# review 
# 🎯 Key Learning Points

# Method Independence: Each method should work independently without relying on side effects from other methods
# Use Built-in Functions: Python's sum() and len() are more readable than manual loops for simple operations
# Handle Edge Cases: Always consider what happens with empty lists or invalid data
# Clear Return Values: Return exactly what the method name suggests (letter grade should return just the letter)

# 🚀 Next Steps
# Try implementing the challenges:

# Add input validation for grades (0-100)
# Properly implement the student counter
# Add a remove_grade(index) method
# Implement __eq__() for student comparison

# Your foundation is solid - these fixes will make your code more robust and professional!