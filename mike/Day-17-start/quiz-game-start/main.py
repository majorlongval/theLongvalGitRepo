from data import question_data
from Data2 import question_data2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for item in question_data2:
    question_bank.append(Question(**item))

qb = QuizBrain(question_bank)
while qb.question_available():
    qb.next_question()
    qb.check_answer()

    qb.print_score()

