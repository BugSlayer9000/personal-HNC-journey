# Exercise 3: Database Access Layer (Dependency Inversion)
# Build a data access system for a student management application. Practice:

# Depending on abstractions rather than concrete implementations (Dependency Inversion Principle - DIP)
# Creating interfaces for data access that can work with different databases

from abc import ABC, abstractmethod
from student import Student



class IStudentRepository(ABC):
    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def add_student(self,student):
        pass
    
    @abstractmethod
    def get_student(self, student_name):
        pass
    
    @abstractmethod
    def remove_student(self, student_name):
        pass
    
    @abstractmethod
    def list_all_students(self):
        pass

class JSONStudentRepository(IStudentRepository):
    def __init__(self) -> None:
        super().__init__()
    
    def add_student(self, student):
        pass

    def get_student(self, student_name):
        pass
    
    def remove_student(self, student_name):
        pass
    
    def list_all_students(self):
        pass

