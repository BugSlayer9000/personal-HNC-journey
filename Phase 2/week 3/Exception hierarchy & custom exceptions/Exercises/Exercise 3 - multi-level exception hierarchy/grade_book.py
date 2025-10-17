from student_exeptions import StudentNotFoundError,DuplicateStudentError,InvalidStudentIDError,GradeOutOfRangeError,InvalidGradeTypeError

class Gradebook():
    
    
    
    def __init__(self) -> None:
        
        self.students = {
            "100001": {
                "name": "Alice Johnson",
                "grades": {
                    "Math": 88,
                    "English": 92,
                    "Science": 79,
                    "Computing": 85
                }
            },
            "100002": {
                "name": "Brian Smith",
                "grades": {
                    "Math": 76,
                    "English": 81,
                    "Science": 74,
                    "Computing": 90
                }
            },
            "100003": {
                "name": "Chloe Williams",
                "grades": {
                    "Math": 93,
                    "English": 87,
                    "Science": 91,
                    "Computing": 89
                }
            },
            "100004": {
                "name": "David Brown",
                "grades": {
                    "Math": 69,
                    "English": 73,
                    "Science": 70,
                    "Computing": 78
                }
            }
        }

        # key : student_id(str)
        # value : dectionary with "name" and "grades" (dict of subject:grade pairs)
    
    def get_list_of_student_id(self):
        
        id_list = []
        
        for id in self.students.keys():
            id_list.append(id)
        
        return id_list
    
    #test method
    def print_dict(self):
        print(self.students)
    
    def add_student(self,student_id:str,name:str):
        
        if not student_id.isdigit() or len(student_id) < 7 :
            raise InvalidStudentIDError
        
        if student_id in self.get_list_of_student_id():
            raise DuplicateStudentError(student_id)
        
        
        self.students.update(
            {student_id:
                {
                "name":name,
                "grades":
                    {
                    "Math"      : None,
                    "English"   : None,
                    "Science"   : None,
                    "Computing" : None,
                    }
                
                }
            }
            )
        
        return f"Successfully added Student - {name} under {student_id}"
        
    def add_grades(self,student_id, subject, grade):
        
        subjects = ["Math","English","Science","Computing"]
        
        if student_id not in self.get_list_of_student_id():
            raise StudentNotFoundError
        
        if not grade.isdigit():
            raise InvalidGradeTypeError
        
        if not 0 <= int(grade) <= 100:
            raise GradeOutOfRangeError
        
        for i in subjects:
            if subject.lower() == i.lower():
                self.students[student_id]["grades"].update({i:grade})
        
    def get_student(self,student_id):
        
        if student_id not in self.get_list_of_student_id():
            raise StudentNotFoundError
        else:
            print(f"\nStudent name     - {(self.students[student_id]["name"]).capitalize()}")
            print(f"Student id       - {student_id}")
            print(f"Math Grades      - {self.students[student_id]["grades"]["Math"]}%")
            print(f"English Grades   - {self.students[student_id]["grades"]["English"]}%")
            print(f"Science Grades   - {self.students[student_id]["grades"]["Science"]}%")
            print(f"Computing Grades - {self.students[student_id]["grades"]["Computing"]}%")
    
    
    
    
            
        
            
        
        


G = Gradebook()

G.add_student("0123456","samod")

G.add_grades("0123456","math","25")
G.add_grades("0123456","English","45")
G.add_grades("0123456","Science","70")
G.add_grades("0123456","Computing","62")

G.get_student("0123456")

G.get_avarage("0123456")


        
        

