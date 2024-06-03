from turtle import Turtle

class TurtleBackground(Turtle):
    def __init__(self):
        super().__init__()
        # Hide the turtle
        self.hideturtle()

        # Set the turtle's speed and shape
        self.speed(10)
        self.shape("turtle")
        self.pensize(25)
        self.color("white")
        self.penup()

        # Draw the background
        self.backward((self.getscreen().window_width() / 2) - 10)
        self.left(90)
        self.backward((self.getscreen().window_height() / 2) - 10)
        self.left(180)
        self.pendown()
        self.backward((self.getscreen().window_height()) - 80)
        self.right(90)
        self.backward((self.getscreen().window_width()) - 25)
        self.right(90)
        self.backward((self.getscreen().window_height()))