from pathlib import Path
import os
import json

class MarksAnalyzer:
    
    
    def __init__(self) -> None:
        self.JSON_file  =  Path("Phase 2\\week 1\\File Handling\\practice\\exercise1\\files\\student_details_with_marks.json")
    
    def _get_details(self):
        try:
            with open(self.JSON_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print("File not found")
            return []
    
    def get_avarage_marks(self):
        data = self._get_details()
        
        score_list = [int(i["score"]) for i in data]
        
        total_marks = 0
        
        for i in score_list:
            total_marks += i

        return total_marks/len(data)

    def most_marks(self):
        data = self._get_details()
        
        most_marks = 0
        student_name = ""
        
        for i in data:
            if int(i["score"]) >= most_marks:
                most_marks = int(i["score"])
                student_name = i["name"]
        
        return f"Student name - {student_name} --  Most Marks - {most_marks}"

         
    



