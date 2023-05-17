from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SPEED = 20
start_snake_body = [(0, 0), (-20, 0), (-40, 0)]


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in start_snake_body:
            self.extend_snake(position, "white")

    def extend_snake(self, position, color):
        snake = Turtle()
        snake.shape("square")
        snake.color(color)
        snake.penup()
        snake.goto(position)
        self.snake_body.append(snake)

    def move(self):
        # [1 (0, 0), 2 - (20, 0),  - (40, 0)]
        for body in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body - 1].xcor()
            new_y = self.snake_body[body - 1].ycor()
            self.snake_body[body].goto(new_x, new_y)
        self.head.forward(SPEED)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
