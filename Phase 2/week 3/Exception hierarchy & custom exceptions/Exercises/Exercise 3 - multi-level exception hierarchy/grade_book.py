from student_exeptions import StudentNotFoundError,DuplicateStudentError,InvalidStudentIDError,GradeOutOfRangeError,InvalidGradeTypeError

class Gradebook():
    
    
    
    def __init__(self) -> None:
        
        self.grade_book = { }

        # key : student_id(str)
        # value : dectionary with "name" and "grades" (dict of subject:grade pairs)
    
    def get_list_of_student_id(self):
        
        id_list = []
        
        for id in self.grade_book.keys():
            id_list.append(id)
        
        return id_list

    
    def add_student(self,student_id:str,name:str):
        
        if not student_id.isdigit() or len(student_id) < 7 :
            raise InvalidStudentIDError
        
        if student_id in self.get_list_of_student_id():
            raise DuplicateStudentError(student_id)
        
        
        self.grade_book.update(
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
        
        print(f"Successfully added Student - {name} under {student_id}")
        
    def add_grades(self,student_id, subject, grade):
        
        grade = str(grade)
        
        subjects = ["Math","English","Science","Computing"]
        
        if student_id not in self.get_list_of_student_id():
            raise StudentNotFoundError
        
        if not grade.isdigit():
            raise InvalidGradeTypeError
        
        if not 0 <= int(grade) <= 100:
            raise GradeOutOfRangeError
        
        for i in subjects:
            if subject.lower() == i.lower():
                self.grade_book[student_id]["grades"].update({i:grade})
        
    def get_student(self,student_id):
        
        if student_id not in self.get_list_of_student_id():
            raise StudentNotFoundError
        else:
            print(f"\nStudent name     - {(self.grade_book[student_id]["name"]).capitalize()}")
            print(f"Student id       - {student_id}")
            print(f"Math Grades      - {self.grade_book[student_id]["grades"]["Math"]}%")
            print(f"English Grades   - {self.grade_book[student_id]["grades"]["English"]}%")
            print(f"Science Grades   - {self.grade_book[student_id]["grades"]["Science"]}%")
            print(f"Computing Grades - {self.grade_book[student_id]["grades"]["Computing"]}%")
    
    
    # Challenge
    def get_avarage(self,student_id):
        
        if student_id not in self.get_list_of_student_id():
            raise StudentNotFoundError
        else:
            # first solution
            # math_grades = self.grade_book[student_id]["grades"]["Math"]
            # english_grades = self.grade_book[student_id]["grades"]["English"]
            # science_grades = self.grade_book[student_id]["grades"]["Science"]
            # computing_grades = self.grade_book[student_id]["grades"]["Computing"]
            
            # second solution
            # can take any number of subjects not just the given ones like in previous solution
            total = 0
            num_of_subjects = len(self.grade_book[student_id]["grades"])
            
            for i in self.grade_book[student_id]["grades"].values():
                total += int(i)
            
            avarage = total/num_of_subjects
            
            print(f"\nStudent name     - {(self.grade_book[student_id]["name"]).capitalize()}")
            print(f"Student id       - {student_id}")
            print(f"Student Avarage  - {avarage} out of {num_of_subjects} subjects.")
    
    def display_grade_book(self):
        
        if len(self.grade_book) == 0:
            print("No grade_book registerd ! ")
            return
        
        for i in self.grade_book.items():
            
            print(f"\nStudent id   - {i[0]}")
            print(f"Student name - {i[1]["name"]}")
            print(f"Math grade   - {i[1]["grades"]["Math"]} %")
            print(f"English grade   - {i[1]["grades"]["English"]} %")
            print(f"Science grade   - {i[1]["grades"]["Science"]} %")
            print(f"Computing grade   - {i[1]["grades"]["Computing"]} %")
            
        
        
    
            
        
            
        
        





        
        

