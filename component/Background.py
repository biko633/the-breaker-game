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

        # game window size
        self.game_width = self.getscreen().window_width()
        self.game_height = self.getscreen().window_height()

        # Draw the background
        # left side
        self.goto(-self.game_width / 2, -self.game_height / 2)
        self.left(90)
        self.pendown()
        self.forward((self.game_height) - 50)

        # middle side left
        self.right(90)
        self.forward(self.game_width / 2)

        # right side
        self.penup()
        self.goto((self.game_width / 2) - 6, -self.game_height / 2)
        self.left(90)
        self.pendown()
        self.forward((self.game_height) - 50)

        # middle side right
        self.left(90)
        self.forward(self.game_width / 2)