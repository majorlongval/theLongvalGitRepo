from pdb import set_trace

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.answer = None

    def print_score(self):
        print(f"Your score: {self.score} out of {len(self.question_list)}")


    def next_question(self):
        print(f"Q{self.question_number+1}: {self.question_list[self.question_number].text} ")
        self.answer = input('True/False >> ')
        self.question_number += 1

    def question_available(self):
        """"Return True if there is a question available
        and False if not"""
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self):
        correct_answer = self.question_list[self.question_number-1].answer
        if self.answer == correct_answer:
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        print(f"Answer is {correct_answer}")
