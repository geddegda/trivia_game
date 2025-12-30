from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

quiz = QuizBrain(question_bank)
i = 0
#for question in quiz.question_list:
while quiz.is_there_another_q():

    response = quiz.get_question()
    #quiz.check_answer(question, response)
    quiz.check_answer(quiz.question_list[i], response)

    quiz.next_question()

    i = (i + 1)%len(question_bank)
    quiz.score_total()

#for element in question_bank:
#    print(f"This is the question: {element.text} and this is the answer: {element.answer}")
