from turtle import Turtle
from Screen_Info import width, height
from component.utilities.Class_utility import get_all_instances
import random


# Total number of bricks that can fit in the screen width = (Total width / Width of each brick) + ((Total width / Width of each brick) - 1)

# Total width = 1000 Width of each brick = 102

# Total number of bricks = (1000 / 102) + ((1000 / 102) - 1) Total number of bricks = 9 + 8 = 17

# Therefore, with the 51-unit movement to the right to create a new brick, you can fit 17 bricks in the screen width.

# add one more brick to the right

class TurtleBricks(Turtle):
    def __init__(self):
        super().__init__()
        self.start_x = -self.getscreen().window_width() / 2 + 48.49
        self.start_y = self.getscreen().window_height() / 2 - 93.49
        self.speed(1)
        self.shape("square")
        self.color(self.generate_random_color())
        self.shapesize(stretch_wid=1, stretch_len=2.5)
        self.penup()
        self.goto(self.start_x, self.start_y)
        # print(self.pos())
        # (-451.51,306.51)
        # width = 102 half = 51
        # height = 42 half = 21

    def generate_brick(self):
        pass


    def generate_random_color(self):
        colors = ["#059212", "#06D001", "#9BEC00", "#F3FF90", "#FDA403", "#E8751A", "#898121", "#E5C287", "#51EAEA", "#AA26DA"]
        color = random.choice(colors)
        return color