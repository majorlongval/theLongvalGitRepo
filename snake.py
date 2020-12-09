from turtle import Turtle
import time


class Snake:
    def __init__(self):
        self.nb_segments = 3
        self.starting_position = (0, 0)
        self.segment_width = 20
        self.segments = self.initiate_segments()

    def initiate_segments(self):
        segments = []
        for i in range(0, self.nb_segments):
            new_segment = Turtle("square")
            new_segment.color('white')
            new_segment.penup()
            new_segment.setx(-self.segment_width*i)
            segments.append(new_segment)
        return segments

    def move(self):
        inv_segments = self.segments[::-1]
        for i, seg in enumerate(inv_segments[:-1]):
            seg.goto(x=inv_segments[i + 1].xcor(), y=inv_segments[i + 1].ycor())
        self.segments[0].forward(20)
