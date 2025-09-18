from pathlib import Path
import csv
import json

# csv file structure will be a list of dicts = [{'name': 'samod', 'subject': 'science', 'score': 20}, {'name': 'robert', 'subject': 'maths', 'score': 40}]

# json file structure will include two more items with 


class FileHandlingCSV():
    
    
    student_details_csv = Path("Phase 2\\week 1\\File Handling\\practice\\exercise1\\files\\student_details.csv")
    student_details_csv.touch(exist_ok=True)
    
    def __init__(self) -> None:
        self._initialize_file()
    
    def _initialize_file(self):
        with open(self.student_details_csv, "w", newline="")as f:
            writer = csv.writer(f)
            writer.writerow(["name", "subject","score"])
    
    def _load_file(self):
        with open(self.student_details_csv, "r") as f:
            reader = csv.reader(f)
            next(reader)
            return list(reader)
    
    def _save_file(self, name, subject, score):
        with open(self.student_details_csv , "a", newline="")as f:
            writer = csv.writer(f)
            writer.writerow([name, subject, score])
    
    def rewrite_csv(self, updated_student_list):
        with open(self.student_details_csv, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["name","subject","score"])
            writer.writerows(updated_student_list)
    
    def csv_to_dict(self):
        with open(self.student_details_csv, "r") as f:
            reader = (csv.DictReader(f))
            return list(reader)
        
# Json file strucrue

# [{"name": "samod", "subject": "science", "score": 10}]


