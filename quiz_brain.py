
class Quizbrain:
    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list

    def still_has_questions(self):
        index_lquest = len(self.question_list)
        return self.question_number >= index_lquest

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        self.question_number+=1
        input(f'Q.{self.question_number}: {current_question}. (True/False) : ')
