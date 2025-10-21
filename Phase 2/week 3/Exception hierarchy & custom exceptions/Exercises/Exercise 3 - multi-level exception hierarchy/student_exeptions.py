# all custom exeptions here

class StudentSystemError(Exception):
    """Base for all student system errors"""
    pass

class InvalidStudentIDError(StudentSystemError):
    """Raised when student ID fromat is Invalid (Must be 6 digits)"""
    def __init__(self) -> None:
        massage = f"The ID format is invalid must be 6 digits ! "
        super().__init__(massage)

class DuplicateStudentError(StudentSystemError):
    """Raised when tried to add a student that's already exists"""
    def __init__(self,student_id) -> None:
        massage = f"A student under the id of - {student_id} Already exists in the system"
        super().__init__(massage)

class StudentNotFoundError(StudentSystemError):
    """Raised when student id doesn't exist in the system"""
    def __init__(self) -> None:
        massage = f"Student ID not found in the system !  "
        super().__init__(massage)




class GradeError(Exception):
    """Base for all gread relataed errors"""
    pass

class GradeOutOfRangeError(GradeError):
    """Raised when grade is not between 0-100"""
    
    def __init__(self) -> None:
        massage = f"The grade should be between 0-100 marks ! "
        super().__init__(massage)

class InvalidGradeTypeError(GradeError):
    """Raised when grade is not a number """
    
    def __init__(self) -> None:
        massage = f"The Grade must be a number !  "
        super().__init__(massage)