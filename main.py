from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []

for question in question_data:
    qtext = question['text']
    qans = question['answer']
    new_question = Question(qtext, qans)
    question_bank.append(new_question)

quiz = Quizbrain(question_bank)
quiz.next_question()



