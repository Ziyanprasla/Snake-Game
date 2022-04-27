from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_SPEED = 20


class Snake:
    def __init__(self):
        self.body = []
        self.create_starting_snake()
        self.snake_head = self.body[0]

    def create_starting_snake(self):
        for position in POSITIONS:
            body = Turtle()
            body.penup()
            body.shape("circle")
            body.color("green")
            body.goto(position)
            self.body.append(body)

    def move(self):
        for position in range(len(self.body) - 1, 0, -1):
            previous_x = self.body[position - 1].xcor()
            previous_y = self.body[position - 1].ycor()
            self.body[position].goto(previous_x, previous_y)
        self.snake_head.forward(MOVE_SPEED)

    def add_snake_body(self):
        x = self.body[-1].xcor()
        y = self.body[-1].ycor()
        body = Turtle()
        body.penup()
        body.shape("circle")
        body.color("green")
        body.goto(x, y)
        self.body.append(body)

    def collision(self):
        for body in self.body[1:]:
            if self.snake_head.distance(body) < 10:
                return True

    def reset_snake(self):
        for block in self.body:
            block.goto(2000, 2000)
        self.body.clear()
        self.create_starting_snake()
        self.snake_head = self.body[0]

    def up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)
