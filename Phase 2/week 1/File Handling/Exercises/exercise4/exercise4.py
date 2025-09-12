# samod subhasha
# 12/09/25

# CSV intermidiate level

# exercise - same as exercise 3 - collects student id, name and grade then read it a s dict and then turn it into a json format

# this exersice includes 
    # dictreader - for more readablity
    # turning the CSV file into a json


import csv
import json
from pathlib import Path

csv_file_path = Path("Phase 2\\week 1\\File Handling\\Exercises\\exercise4\\student_data.csv")
json_file_path = Path("Phase 2\\week 1\\File Handling\\Exercises\\exercise4\\student_data.json")

csv_file_path.touch(exist_ok=True)
json_file_path.touch(exist_ok=True) # Makes sure that file the file exists if not creates one


# Ads the header row to the csv file for a proper initialization
def setup_csv():
    with open(csv_file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id","name","grade"])

#gets the detials and then ads it to the csv file
def student_details(id, name, grade):
    with open(csv_file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([id, name, grade])

# Read the written file normally
def read_students_normal():
    with open(csv_file_path, "r") as file:
        reader = csv.reader(file)
        
        next(file) # skips the header
        
        for row in reader:
            id, name, grade = row
            print(f"id-{id} -- name-{name} -- grade-{grade}")

# uses the Dictreader and returns a dict for each row 
def read_students_dict():
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file) # puts data into dict for rach row
        for row in reader:
            print(row)
    
# Uses the fict reader to get a dict then ads it to the json file
def csv_to_json():
    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)          
        data = list(reader)  #  makes a list of made dicts from the prevoise line
        print(f"data - {data}")
    
    with open(json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)   # to lists of dict
        print("Json dump sucessful ! ")

# loads the json file then reads it
def reading_json():
    with open(json_file_path, "r") as file:
        data = json.load(file)
    
    return data

setup_csv()

student_details(1, "samod", "A")
student_details(2, "Robert", "A")
student_details(3, "Yoshi", "F")
student_details(4, "kelum", "C")

print("\nNormal CSV reading")

read_students_normal()


print("\nReading the data into a dict")

read_students_dict()

csv_to_json()

print("\nReading the JSON file")

print(reading_json())


print("\nReading the JSON file proerly")

data = reading_json()

for item in data:
    print(f"name - {item["name"]} - Grade - {item["grade"]}")
        