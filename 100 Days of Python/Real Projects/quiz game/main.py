#If you want to known why we are doing this refer lec 158 (100 days of python code)

from data import question_data
from question_model import Question

        
question_bank = []        
for question in question_data:
    question_text = question['text']
    question_ans = question['answer']
    question_bank.append(Question(question_text, question_ans))
    
print(question_bank)
