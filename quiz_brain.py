class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        self.question_number = ((self.question_number + 1) % len(self.question_list))

    def get_question(self):
        return input(f"Q:{self.question_number + 1} - {self.question_list[self.question_number].text} (True of False)?")


    def check_answer(self, question, resp):
        if question.answer == resp:
            print("That's correct!")
            self.score += 1
        else:
            print("That's incorrect!")

    def is_there_another_q(self):
        if self.question_list[self.question_number]:
            return True
        else:
            return False

    def score_total(self):
        print(self.score)
