
from student import Student
from marks_analyzer import MarksAnalyzer




def main():
    s = Student()
    m = MarksAnalyzer()
    
    _is_running = True
    
    _is_json = False
    
    while _is_running:
        print(f"{"#"*15}-----Welcome to the student marks database and analyzer-----{"#"*15}")
        print("\n(Enter 0 to exit\n\n1.View students and marks\n2.Add student and marks\n3.Remove students and marks\n4.Check who got the most marks\n5.See avarage marks per student")
        
        try:
            user_input = int(input("Enter you choice - "))
        except ValueError:
            print("Please enter a valid input !")
            continue
        
        if user_input == 0:
            _is_running = False
        
        elif user_input == 1:
            print("\nView Students and marks.")
            
            data = s.get_a_dict()
            
            if len(data) == 0:
                print("\nNo records found please add details")
            
            for number,i in enumerate(data,1):
                print(f"{number}.Name - {i["name"]} -- Subject - {i["subject"]} -- Marks - {i["score"]}")
            
        
        elif user_input == 2:
            print("\nAdd Marks")
            
            input_name = str(input("Enter thr name of the student : "))
            input_subject = str(input("Enter thr subject of the student : "))
            
            try:
                input_score = int(input(f"Enter the score {input_name} got : "))
            except ValueError:
                print("Score must be an int!")
                continue
            
            if len(input_name) > 2 and len(input_subject) > 3:
                s.add_student(input_name, input_subject, input_score)
        

        elif user_input == 3:
            print("\nRemove student marks")
            
            for number,i in enumerate(s.get_a_dict(),1):
                print(f"{number}.Name - {i["name"]} -- Subject - {i["subject"]} -- Marks - {i["score"]}")
            
            student_name_input = str(input("Enter the name of the student : "))
            
            s.remove_student(student_name_input)
            
            
        elif user_input == 4:
            print("\nCheck who got the most marks ")
            
            data = s.csv_to_json() # use the fuction that makes the json file 
            
            print(m.most_marks())
        
        elif user_input == 5:
            print("See avarage marks per student ")

            data = s.csv_to_json() # use the fuction that makes the json file 
            
            print(m.get_avarage_marks())
            

if __name__ == "__main__":
    main()

