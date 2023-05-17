from turtle import Turtle
import random
list_of_colors = ["red", 'royal blue', "chartreuse", "yellow", "coral", "crimson", "magenta"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color(random.choice(list_of_colors))
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
        self.shapesize(1.2, 1.2)

    def eated(self):
        self.color(random.choice(list_of_colors))
        x_pos = random.randint(-280, 280)
        y_pos = random.randint(-280, 280)
        self.goto(x_pos, y_pos)
