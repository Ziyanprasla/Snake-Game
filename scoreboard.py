from turtle import Turtle


class ScoreBoard:
    def __init__(self):
        self.score = Turtle()
        self.score.color("white")
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(0, 470)
        self.point = 0
        self.snake_speed = 0.08
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.update_score()

    def update_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.point}  High score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def add_point(self):
        self.point += 1
        self.update_score()
        self.snake_speed *= .9

    def reset_score(self):
        if self.point > self.high_score:
            self.high_score = self.point
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.point}")
        self.point = 0
        self.snake_speed = 0.08
        self.update_score()
