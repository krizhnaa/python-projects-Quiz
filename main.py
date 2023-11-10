from question_model import Question
from data import question_data

# question = question_data[]['text']
# ans = question_data[]['answer']

q1 = Question(question_data[0]['text'], question_data[0]['answer'])

print(q1.text, q1.answer)

