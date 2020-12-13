from turtle import Turtle
from turtle import Screen


class Score(Turtle):
    def __init__(self, screen: Screen):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,240)
        self.screen = screen
        self.current_score = [0,0]
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(self.score_str(), align="center", font=("Courier", 14, "normal"))

    def score_str(self):
        return f"{self.current_score[0]} : {self.current_score[1]}"

    def left_inc(self):
        self.current_score[0] += 1

    def right_inc(self):
        self.current_score[1] += 1
