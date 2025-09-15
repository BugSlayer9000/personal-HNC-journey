from exercise5 import QuizzGame

q = QuizzGame()

q._initial_json_file_questions()
q._initial_json_file_score()


q.add_question("ubada pakaya mamada1", "1")
q.add_question("ubada pakaya mamada2", "2")
q.add_question("ubada pakaya mamada3", "3")


# todo - add other features

qestions = q.get_questions()

input_to_del = "ubada pakaya mamada1"

# tested the delete logic before applying it into a feature

# updated_questions = []

# for i in qestions:
#     if not i["question"] == "ubada pakaya mamada1":
        
#         updated_questions.append(i)

# print(updated_questions)

q.delete_question(input_to_del) # deletes the first item in the list

q.add_score("samod", 1)
q.add_score("samod", 2)
q.add_score("Robert", 2)


