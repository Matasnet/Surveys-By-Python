from openpyxl import Workbook
import random

# List of questions with answers
questions = [
    {"question": "Sex", "answers": ["Female", "Male"]}, #0
    {"question": "Age", "answers": ["19-20", "21-22", "23-24", "25-26", "27 or more"]}, #1
    {"question": "Country", "answers": ["Poland", "USA", "China", "Russia", "Other"]}#2
   # Add more questions here

]

multi_choice_questions = [
    {"question": "Check 1, 2, 3 or all", "options": ["1","2","3"]},
   # Add more questions here
]

# Create 100 answers
wb = Workbook()
ws = wb.active
ws.append(["Question"] + [q["question"] for q in questions + multi_choice_questions])

for i in range(1, 101):
    row = [i]
    for q in questions:
        answer = random.choice(q["answers"])
        row.append(answer)
    for q in multi_choice_questions:
        num_answers = random.randint(1, len(q["options"]))
        answers = random.sample(q["options"], num_answers)
        row.append(', '.join(answers))
    ws.append(row)
    
wb.save("questions.xlsx")
print("Excel file was created.")