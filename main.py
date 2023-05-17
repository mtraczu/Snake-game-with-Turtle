from turtle import Screen
from board import Board
from food import Food
from snake import Snake
import time

game_on = True
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=620, height=620)

snake = Snake()
food = Food()
screen.listen()
board = Board()

screen.onkeypress(snake.move_up, "Up")
screen.onkeypress(snake.move_down, "Down")
screen.onkeypress(snake.move_left, "Left")
screen.onkeypress(snake.move_right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # eat food
    if snake.head.distance(food) < 20:
        snake.extend_snake(snake.snake_body[-1].position(), food.color()[1])
        food.eated()
        board.update_score()
    # collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        board.game_over()
    # snake collision with body
    for body in snake.snake_body[1:]:
        if snake.head.distance(body) < 1:
            game_on = False
            board.game_over()

screen.exitonclick()
