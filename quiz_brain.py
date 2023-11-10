
class Quizbrain:
    def __init__(self, quest_list):
        self.question_number = 0
        self.question_list = quest_list

    def next_question(self):
        current_question = self.question_list[self.question_number].text
        input(f'Q.{self.question_number + 1}: {current_question}. (True/False)')
