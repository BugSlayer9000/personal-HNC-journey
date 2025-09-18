from file_handling_CSV import FileHandlingCSV
from file_handling_JSON import FileHandlingJSON
from student import Student



s = Student()

s.add_student("Samod", "science", 30)
s.add_student("Robert", "science", 30)
s.add_student("Kelum", "science", 30)

print(s.convert_csv_to_json())