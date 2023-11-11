
class Quizbrain:
    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list
        self.score = 0

    def still_has_questions(self):
        index_lquest = len(self.question_list)
        return self.question_number < index_lquest

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        current_answer = self.question_list[self.question_number].answer
        self.question_number+=1
        user_answer = input(f'Q.{self.question_number}: {current_question}. (True/False) : ')
        self.check_answer(user_answer, current_answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            self.score+=1
            print(f"Correct Answer and Your Score is {self.score}")
        else:
            print("Wrong")


