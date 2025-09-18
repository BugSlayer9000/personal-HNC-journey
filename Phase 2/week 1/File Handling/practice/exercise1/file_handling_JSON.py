import json
from pathlib import Path

class FileHandlingJSON():

    
    student_details_with_marks_json = Path("Phase 2\\week 1\\File Handling\\practice\\exercise1\\files\\student_details_with_marks.json")
    student_details_with_marks_json.touch(exist_ok=True)
    

    
    def __init__(self) -> None:
        self._initialize_file()
    
    def  _initialize_file(self):
        with open(self.student_details_with_marks_json,"w") as f:
            json.dump([], f, indent=4)
    
    def _load_file(self):
        with open(self.student_details_with_marks_json, "r") as f:
            return json.load(f)
            
    
    def _save_file(self, data):
        with open(self.student_details_with_marks_json, "w") as file:
            json.dump(data, file, indent=4)
    
    def _get_file_content(self):
        data = self._load_file()
        return list(data)




