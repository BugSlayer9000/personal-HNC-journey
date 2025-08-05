

class Student():
    def __init__(self, student_name:str, student_id:int, student_dob:str) -> None:
        self.student_name = student_name
        self.student_id = student_id 
        self.student_dob = student_dob
    
    def to_dict(self) -> dict:
        return {
            "name": self.student_name,
            "ID": self.student_id,
            "DOB": self.student_dob
        }
    