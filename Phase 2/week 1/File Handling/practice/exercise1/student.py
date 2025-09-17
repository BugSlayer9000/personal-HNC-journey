from file_handling_CSV import FileHandlingCSV
from file_handling_JSON import FileHandlingJSON


class Student():
    
    def __init__(self) -> None:
        self.JSON_file = FileHandlingJSON()
        self.CSV_file = FileHandlingCSV()
    
    def add_student(self, name, subject, score:int):
        self.CSV_file._save_file(name, subject, score)
        print(f"{name} Added to the system. Marks =  {subject} - {score}/100")
    
    def remove_student(self, name):
        item_found = False
        
        student_details = self.CSV_file._load_file()
        
        updated_student_details = [row for row in student_details if row[0] != name]
        
        if len(student_details) == 0:
            return "No Records found"
        
        if len(student_details) > len(updated_student_details):
            self.CSV_file.rewrite_csv(updated_student_details)
            print(f"{name} deleted sucessfully")
        else:
            print(f"{name} not found ")

    def get_student(self, name):
        student_found = False
        
        students =  self.CSV_file.csv_to_dict()         
        
        for student in students:
            if student["name"] == name:
                print(f"Student found \nName = {student["name"]}\nSubject = {student["subject"]}\nscore = {student["score"]}/100 ")
                student_found = True
        
        if not student_found:
            print("student not found in the system")
            
                
        
        
        
        
        

