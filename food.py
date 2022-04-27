from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("yellow")
        self.shape("circle")
        self.move_food()

    def move_food(self):
        random_x = random.randint(-460, 460)
        random_y = random.randint(-460, 460)
        self.goto(random_x, random_y)
