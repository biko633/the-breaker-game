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
        self.goto(0, -300)
        self.numbers = [3, -3]

        self.the_height = 10
        self.the_width = 10

        self.ball_y = self.ycor()
        self.ball_x = self.xcor()
        self.x_move = -3
        self.y_move = 3


    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    # def ball_collision(self, other):
    #     # Axis Aligned Bounding Box
    #     x_collision = (math.fabs(self.xcor() - other.xcor()) * 2) < (self.width + other.width)
    #     y_collision = (math.fabs(self.ycor() - other.ycor()) * 2) < (self.height + other.height)
    #     return (x_collision and y_collision)