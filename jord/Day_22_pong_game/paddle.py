from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_pos):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.position = init_pos
        self.goto(self.position[0], self.position[1])

    def go_up(self):
        self.position = (self.position[0], self.position[1] + 20)
        self.update_position()

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
        self.update_position()

    def update_position(self):
        self.goto(self.position[0], self.position[1])

