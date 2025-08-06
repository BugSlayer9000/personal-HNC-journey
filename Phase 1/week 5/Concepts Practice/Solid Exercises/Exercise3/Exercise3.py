# Exercise 3: Database Access Layer (Dependency Inversion)
# Build a data access system for a student management application. Practice:

# Depending on abstractions rather than concrete implementations (Dependency Inversion Principle - DIP)
# Creating interfaces for data access that can work with different databases

from abc import ABC, abstractmethod
from student import Student
import json
import csv
import os


class IStudentRepository(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def add_student(self,student) -> str:
        pass
    
    @abstractmethod
    def get_student(self, student_name) -> str:
        pass
    
    @abstractmethod
    def remove_student(self, student_name) -> str:
        pass
    
    @abstractmethod
    def list_all_students(self) -> list:
        pass

class JSONStudentRepository(IStudentRepository):
    
    FILE_NAME = "students.json"
    FILE_PATH = "C:/my stuff/git/personal-HNC-journey/Phase 1/week 5/Concepts Practice/Solid Exercises/Exercise3/students.json"
    
    def __init__(self) -> None:
        super().__init__()
        self.students = self.__load_students()
    
    def __load_students(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w") as f:
                json.dump([], f) 
            return []
        else:
            with open(self.FILE_PATH, "r") as file:
                return json.load(file)
    
    def _save_students(self,students):
        with open(self.FILE_PATH, "w") as file:
            json.dump(students, file, indent=4)
    
    def add_student(self, student) -> str:
        if not student.to_dict() in self.students:
            self.students.append(student.to_dict())
            self._save_students(self.students)
            return f"Student added sucessfully"
        else:
            return f"This student already exixsts"

    def get_student(self, student_name:str) -> str:
        for student in self.students:
            if   student["name"] == student_name:
                return str(student)
        return f"Student not found"
  
    def remove_student(self, student_name) -> str:
        original_count = len(self.students)
        
        self.students = [s for s in self.students if s["name"] != student_name] # "Keep every student s in the list except the one whose name matches student_name."
        
        if len(self.students) == original_count:
            return f"Student was not found"
        
        self._save_students(self.students) # rewriting the whole file because json doesn't support partial deletetion
        return f"Student removed sucessfully"
    
    def list_all_students(self) -> list[dict[str,str]]:
        return self.students


import csv
import os
from typing import List
 # assuming this interface exists and is properly defined

class CSVStudentRepository(IStudentRepository):
    FILE_PATH = "C:/my stuff/git/personal-HNC-journey/Phase 1/week 5/Concepts Practice/Solid Exercises/Exercise3/students.csv"

    def __init__(self) -> None:
        super().__init__()
        self.students = self.__load_students()

    def __load_students(self) -> List[dict[str, str]]:
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, "w", newline='') as f:
                writer = csv.DictWriter(f, fieldnames=["name", "ID", "DOB"])
                writer.writeheader()
            return []

        with open(self.FILE_PATH, "r", newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def _save_students(self, students: List[dict[str, str]]) -> None:
        with open(self.FILE_PATH, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "ID", "DOB"])
            writer.writeheader()
            writer.writerows(students)

    def add_student(self, student) -> str:
        student_dict = student.to_dict()
        if student_dict not in self.students:
            self.students.append(student_dict)
            self._save_students(self.students)
            return "Student added successfully"
        return "This student already exists"

    def get_student(self, student_name: str) -> str:
        for student in self.students:
            if student["name"] == student_name:
                return str(student)
        return "Student not found"

    def remove_student(self, student_name: str) -> str:
        original_count = len(self.students)
        self.students = [s for s in self.students if s["name"] != student_name]
        if len(self.students) == original_count:
            return "Student was not found"
        self._save_students(self.students)
        return "Student removed successfully"

    def list_all_students(self) -> List[dict[str, str]]:
        return self.students



student1 = Student("John Doe", 12345, "2000-01-01")
student2 = Student("Jane Smith", 67890, "1999-12-31")
student3 = Student("Alice Johnson", 11223, "2001-05-15")


repo = JSONStudentRepository()

print(repo.add_student(student1))
print(repo.add_student(student2))
print(repo.add_student(student3))

print(repo.list_all_students()) # fix

print(repo.get_student("John Doe"))

print(repo.remove_student("Jane Smith"))

students_lsit = repo.list_all_students

for student in repo.list_all_students():
    studen_name = student["name"]
    student_id = student["ID"]
    student_DOB = student["DOB"]
    print(f"\n\nStudent name = {studen_name}. \nStudent ID = {student_id}. \nStudent DOB = {student_DOB}")



repo = CSVStudentRepository()

# Add students
print(repo.add_student(student1))
print(repo.add_student(student2))
print(repo.add_student(student3))

# List all students
print("All Students:")
for student in repo.list_all_students():
    print(student)

# Get a student
print("Get John Doe:")
print(repo.get_student("John Doe"))

# Remove a student
print("Remove Jane Smith:")
print(repo.remove_student("Jane Smith"))

# Final list
print("Final List of Students:")
for student in repo.list_all_students():
    print(student)