from turtle import Turtle

# Create a turtle object
class TurtleLives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives = 3
        self.hideturtle()
        self.speed(10)
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.display_lives()

    def update_lives(self):
        self.lives -= 1
        self.display_lives()

    def display_lives(self):
        # Write the lives on the screen
        self.clear()
        self.penup()
        self.home()
        self.right(90)
        self.backward((self.getscreen().window_height() / 2) - 35)
        self.write(f"Lives: {self.lives}", align="right", font=("Arial", 20, "bold"))

    def reset_lives(self):
        self.lives = 3
        self.display_lives()