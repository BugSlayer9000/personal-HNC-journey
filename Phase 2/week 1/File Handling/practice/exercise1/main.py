from file_handling_CSV import FileHandlingCSV
from file_handling_JSON import FileHandlingJSON
from student import Student
from marks_analyzer import MarksAnalyzer



s = Student()
m = MarksAnalyzer()

s.add_student("Samod", "science", 15)
s.add_student("Robert", "science",1)
s.add_student("Kelum", "science", 2)


s.remove_student("Robert")

print(s.convert_csv_to_json())

print(m.get_avarage_marks())
print(m.most_marks())

