from turtle import Turtle

class TurtlePlayerPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.left(90)
        self.backward((self.getscreen().window_height() / 2) - 30)
        self.reset_cords = (self.xcor(), self.ycor())
        self.the_height = 35
        self.the_width = 115

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def paddle_reset(self):
        self.goto(self.reset_cords)