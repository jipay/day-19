from turtle import Turtle
import random


class MyTurtle:
    def __init__(self, x, y, color):
        self.t = Turtle()
        self.t.shape("turtle")
        self.t.color(color)
        self.t.penup()
        self.t.goto(x, y)

    def movefrwd(self):
        self.t.forward(random.randint(0, 10))

