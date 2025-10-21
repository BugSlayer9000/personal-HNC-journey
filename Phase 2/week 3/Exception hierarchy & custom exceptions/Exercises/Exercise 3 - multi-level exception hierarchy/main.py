# samod subhasha
# make a program that tests out the features in the exeptions

from grade_book import Gradebook
from student_exeptions import StudentNotFoundError,DuplicateStudentError,InvalidStudentIDError,GradeOutOfRangeError,InvalidGradeTypeError


grade_book = Gradebook()

print("\nAdding three students with ids")
grade_book.add_student("1234567","samod")
grade_book.add_student("1222222","Robert")
grade_book.add_student("1333333","Kelum")

print("\nAdding grades to the student - 1234567 - Samod ")
grade_book.add_grades("1234567","Math",40)
grade_book.add_grades("1234567","English",60)
grade_book.add_grades("1234567","Science",20)
print("Done")

print("\nAdding grades to the student - 1222222 - Robert ")
grade_book.add_grades("1222222","Math",43)
grade_book.add_grades("1222222","English",77)
grade_book.add_grades("1222222","Science",60)
print("Done")

print("\nAdding grades to the student - 1333333 - Kelum ")
grade_book.add_grades("1333333","Math",55)
grade_book.add_grades("1333333","English",69)
grade_book.add_grades("1333333","Science",82)
print("Done")

print("\nDisplaying all students")
grade_book.display_grade_book()


print("\nTesting exeption type")
print("\nTest : 1.Try to add a student with invalid ID format")
try:
    grade_book.add_student("sdfgfaevsad","Samod")
except InvalidStudentIDError as e:
    print(f"Error : {e}\n")

print("Test : 2.Try to add a duplicate student")
try:
    grade_book.add_student("1234567","samod")
except DuplicateStudentError as e : 
    print(f"Error : {e}\n")

print("Test : 3.Try to add grade for non-existent student")
try:
    grade_book.add_grades("000000","English",77)
except StudentNotFoundError as e : 
    print(f"Error : {e}\n")

print("Test : 4.Try to add grade outside 0-100 range")
try:
    grade_book.add_grades("1333333","English",169)
except GradeOutOfRangeError as e : 
    print(f"Error : {e}\n")


print("Test : 5.Try to add non-numeric grade")
try:
    grade_book.add_grades("1333333","English","aaaa")
except InvalidGradeTypeError as e : 
    print(f"Error : {e}\n")
    
print("Test : 6.Try to get non-existent student")
try:
    grade_book.get_student("000000")
except StudentNotFoundError as e : 
    print(f"Error : {e}\n")


