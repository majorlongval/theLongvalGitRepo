from turtle import Turtle

ALIGNEMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.text = f"score {self.score}"
        self.draw_scoreboard()

    def update_score(self):
        self.score += 1
        self.text = f"score {self.score}"
        self.clear()
        self.draw_scoreboard()

    def draw_scoreboard(self):
        self.write(self.text, align=ALIGNEMENT, font=FONT)
        self.ht()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNEMENT, font=FONT)
