from cgitb import reset
from turtle import Turtle
from random import choice
import time

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
        self.ball_direction = (45, 135)
        self.chosen_direction = choice(self.ball_direction)

        # self.the_height = 10
        # self.the_width = 10

        # self.can_bounce = True
        self.last_bounce_time = 0

        # self.ball_y = self.ycor()
        # self.ball_x = self.xcor()
        # self.x_move = self.chosen_direction[0]
        # self.y_move = self.chosen_direction[1]

        self.setheading(self.chosen_direction)


    def move_ball(self):
        self.forward(5)
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor() + self.y_move
        # self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def bounce_off_top_or_paddle(self):
        self.setheading(360 - self.heading())

    def reset_ball(self):
        self.goto(self.reset_position)
        self.setheading(self.chosen_direction)
        # self.bounce_y()

    def bounce(self, context):
        # paddle
        if context == "paddle":
            current_time = time.time()
            if current_time - self.last_bounce_time > 1:
                print("paddle")
                print(self.heading())
                self.bounce_off_top_or_paddle()
                self.last_bounce_time = current_time
        # top
        elif context == "top":
            print("paddle")
            print(self.heading())
            self.bounce_off_top_or_paddle()
        # when ball moving up
        elif 180 > self.heading() >= 0:
            self.setheading(180 - self.heading())
        # when ball moving down
        elif 180 <= self.heading() < 360:
            self.setheading(540 - self.heading())