from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=1000, height=1000)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(scoreboard.snake_speed)
    snake.move()

    if snake.snake_head.distance(food) < 20:
        scoreboard.add_point()
        food.move_food()
        snake.add_snake_body()

    if snake.snake_head.xcor() < -490 or snake.snake_head.xcor() > 490 or snake.snake_head.ycor() < -490 or snake.snake_head.ycor() > 490:
        scoreboard.reset_score()
        snake.reset_snake()

    if snake.collision():
        scoreboard.reset_score()
        snake.reset_snake()

screen.exitonclick()
