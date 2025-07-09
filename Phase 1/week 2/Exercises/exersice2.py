# ✅ Exercise 2: Student Record System
# Task:
# Create a Student class:

# Private attributes: __name, __grades (list of ints)

# Methods:

# add_grade(grade) – Only allow 0–100.

# average_grade() – Return average.

# get_name() – Return name.

class Student:
    def __init__(self, name, grades = None):
        self.__name = name
        self.__grades = grades if grades is not None else [] # List of ins
    
    def add_grade(self, grade:int) -> bool:
        if 100 >= grade >= 0 :
            self.__grades.append(grade)
            return True
        else:
            return False

    def average_grade(self) -> float:
        if not len(self.__grades) == 0:
            return sum(self.__grades) / len(self.__grades) 
    
    def get_name(self) -> str:
        return self.__name

student = Student("samod", [50, 30, 75, 80, 50])
print(student.add_grade(50))
print(student.add_grade(150))
print(student.average_grade())
print(student.get_name())

# ✅ What You Did Well
# 1. Encapsulation:
# ✅ __name and __grades are correctly marked as private.

# ✅ Access to internal state only happens through methods.

# 2. Validation on Input:
# ✅ You check that grades are between 0–100.

# ✅ You prevent invalid grades from polluting the record.

# 3. Method Structure:
# ✅ add_grade() returns a boolean, allowing callers to handle logic externally.

# ✅ average_grade() is separated out — good SRP (Single Responsibility Principle).


# ❌ What Needs Fixing or Improving

#  ❗ Default Argument Misuse
# Typo in average_grade() name
# add_grade logic not accepting 0 and 100
# 