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
        # 45 to 135
        self.ball_direction = (45, 135)

        self.last_bounce_time = 0

        self.setheading(choice(self.ball_direction))

    def move_ball(self):
        self.forward(5)

    def bounce_ball(self):
        self.setheading(360 - self.heading())

    def reset_ball(self):
        self.goto(self.reset_position)
        self.setheading(choice(self.ball_direction))

    def bounce(self, context):
        # paddle
        if context == "paddle":
            current_time = time.time()
            if current_time - self.last_bounce_time > 1:
                print("paddle")
                print(self.heading())
                self.bounce_ball()
                self.last_bounce_time = current_time
        # top or brick
        elif context == "top" or context == "brick":
            print("top or brick")
            print(self.heading())
            self.bounce_ball()
        # when ball moving up
        elif 180 > self.heading() >= 0:
            self.setheading(180 - self.heading())
        # when ball moving down
        elif 180 <= self.heading() < 360:
            self.setheading(540 - self.heading())