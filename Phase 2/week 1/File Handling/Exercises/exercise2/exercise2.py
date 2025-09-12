# samod subahsha
# 12/09/25

# A simple logger using file handling(txt) - Exercise 

# features
#   you can log your time with your massgege or view them all at once


from datetime import datetime
from pathlib import Path

logfile = Path("C:\\my stuff\\git\\personal-HNC-journey\\Phase 2\\week 1\\File Handling\\Exercises\\exercise2\\data.txt")
logfile.touch(exist_ok=True)

def write_log(msg:str):
    timestamp = datetime.now()
    with open(logfile, "a") as f:
        f.write(f"Date and time - {timestamp} -> msg - {msg}\n")

def read_log():
    with open(logfile, "r") as f:
        conetnt = f.readlines()
    
    for number, line in enumerate(conetnt, 1):
        print(f"{number}. {line}\n")


print("1.Enter a log entry\n2.view log entries")

user_input = int(input("Choose on option from below : "))


if user_input == 1:
    
    user_msg = input("Enter your masssage here : ")
    
    write_log(user_msg)
    
    print("Log entry added")
    
elif user_input == 2:
    
    read_log()

