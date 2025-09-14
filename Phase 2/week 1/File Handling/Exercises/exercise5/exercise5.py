# samod subhasha
# 13/09/25

# JSON file handling and practicing

# Exercise - 
    # A quiz game where you can add questions and store them in a JSOn File
    # Store you score and name in a different JSON file
    # view the questions and score board


import json
from datetime import datetime
from pathlib import Path

"""
Plan of JSON File
[
  {
    "question": "What is the capital of France?",
    "answer": "Paris"
  },
  {
    "question": "What does OOP stand for?",
    "answer": "Object-Oriented Programming"
  }
]

    list of dicts 
    
    steps- 
        Load up ths json and start as a list then append the questions as you go along


"""


class QuizzGame():
    QUESTIONS = Path("Phase 2\\week 1\\File Handling\\Exercises\\exercise5\\questions.json")
    SCORE_BOARD = Path("Phase 2\\week 1\\File Handling\\Exercises\\exercise5\\score_board.json")

    QUESTIONS.touch(exist_ok=True)
    SCORE_BOARD.touch(exist_ok=True)
    
    def __init__(self) -> None:
        pass
    
    def add_question(self, question, answer):
        # add the questions
        with open(self.QUESTIONS, "r") as read_file:
            data = json.load(read_file)
            print(len(data))
            print(data)
        
        
        with open(self.QUESTIONS, "w") as file:
            json.dump({question:[answer]}, file, indent=4)
    
    def delete_questions(self, question):
        # delete the question
        pass
    
    def get_questions(self):
        # return all the questions
        pass
    
    def add_score(self, player_name, score):
        pass
    
    def get_score(self):
        pass



