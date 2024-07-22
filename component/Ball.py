from cgitb import reset
from turtle import Turtle
from random import choice

class TurtleBall(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.reset_position = (0, (self.getscreen().window_height() / 2) * -1 + 100)
        self.goto(self.reset_position)

        # first one left second one right
        self.ball_direction = ((-3, 3), (3, 3))
        self.chosen_direction = choice(self.ball_direction)

        self.the_height = 10
        self.the_width = 10

        # self.ball_y = self.ycor()
        # self.ball_x = self.xcor()
        self.x_move = self.chosen_direction[0]
        self.y_move = self.chosen_direction[1]


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(self.reset_position)
        self.bounce_y()