from turtle import Turtle
import random

# Total number of bricks that can fit in the screen width = (Total width / Width of each brick) + ((Total width / Width of each brick) - 1)

# Total width = 1000 Width of each brick = 102

# Total number of bricks = (1000 / 102) + ((1000 / 102) - 1) Total number of bricks = 9 + 8 = 17

# Therefore, with the 51-unit movement to the right to create a new brick, you can fit 17 bricks in the screen width.

# add one more brick to the right

class TurtleBricks():
    def __init__(self, size, lines, width, height):
        self.start_x = -width / 2 + 38
        self.start_y = height / 2 - 73
        self.brick_list = {}
        self.count = 0
        self.size = size
        self.lines = lines

        self.build_bricks(self.size, self.lines)

    def build_bricks(self, size, lines):
        for line in range(0 , lines):
            for order in range(0, size):
                temp_brick = self.generate_brick(number=order, line=line)
                self.brick_list[temp_brick] = self.count
                self.count += 1

    def reset_bricks(self):
        for brick in self.brick_list:
            brick.clear()
            brick.hideturtle()
            del brick

        self.brick_list = {}
        self.count = 0
        self.build_bricks(self.size, self.lines)

    def generate_brick(self, number, line):
        self.brick = Turtle()
        self.brick.speed(1)
        self.brick.shape("square")
        self.brick.color(self.generate_random_color())
        self.brick.shapesize(stretch_wid=1, stretch_len=2.5)
        self.brick.penup()
        self.brick.goto(self.start_x + (51 * number), self.start_y - (21 * line))
        return self.brick

    def generate_random_color(self):
        colors = ["#059212", "#06D001", "#9BEC00", "#F3FF90", "#FDA403", "#E8751A", "#898121", "#E5C287", "#51EAEA", "#AA26DA", "#36BA98", "#FFFF80", "#B784B7", "#F8DE22", "#D4D925"]
        color = random.choice(colors)
        return color
    
    # def rem_all_bricks(self):
    #     for brick in self.brick_list:
    #         brick.clear()
    #         brick.hideturtle()
    #         del brick

    #     self.brick_list = {}
    #     self.count = 0
