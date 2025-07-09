# ✅ Exercise 2: Student Record System
# Task:
# Create a Student class:

# Private attributes: __name, __grades (list of ints)

# Methods:

# add_grade(grade) – Only allow 0–100.

# average_grade() – Return average.

# get_name() – Return name.

class Student:
    def __init__(self, name, grades:int = []):
        self.__name = name
        self.__grades = grades # List of ins
    
    def add_grade(self, grade):
        if 100 > grade > 0 :
            self.__grades.append(grade)
            return True
        else:
            return False

    def avarage_grade(self):
        if not len(self.__grades) == 0:
            return sum(self.__grades) / len(self.__grades) 
    
    def get_name(self):
        return self.__name

student = Student("samod", [50, 30, 75, 80, 50])
print(student.add_grade(50))
print(student.add_grade(150))
print(student.avarage_grade())
print(student.get_name())