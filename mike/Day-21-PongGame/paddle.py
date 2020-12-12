from turtle import Turtle
from typing import List

# Paddle = List[Turtle]


class Paddle(List[Turtle]):

    def __init__(self):
        super().__init__()

        self.length = 4

