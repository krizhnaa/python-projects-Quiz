
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

new_q = Question("first question", "True")
print(new_q.text, new_q.answer)