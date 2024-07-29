from turtle import Turtle
import turtle
from Screen_Info import width, height
from component.utilities.Class_utility import get_all_instances

# x = 700 and y = 600
# -200 -200 is left bottom button
# width / 2 - x, height / 2 - y
# 190 -200 is right bottom button
# width / 2 - (x / 2) + 40, height / 2 - y

# onclick need x and y even if i don't use it

class TurtleUserInterface(Turtle):
    def __init__(self, x, y, type):
        super().__init__()
        self.penup()
        self.is_hidden = False
        self.type = type
        if self.type == "start":
            self.shape("images/start.gif")
            self.goto(-200, -200)
            print("start is ")
            print(self.pos())
            self.onclick(self.click)
        elif self.type == "exit":
            self.shape("images/exit.gif")
            self.goto(190, -200)
            print("exit is ")
            print(self.pos())
            self.onclick(self.click)
        elif self.type == "game_over":
            self.hideturtle()
            self.color("#de1b4a")
            self.goto(0, 0)
            self.write("Game Over", align="center", font=("Arial", 40, "bold"))
            # self.shape("images/game_over.gif")
            # self.goto(0, 0)
            print("game over is ")
            print(self.pos())
        else:
            self.shape("images/again.gif")
            self.goto(-200, -200)
            print("again is ")
            print(self.pos())
            self.onclick(self.click)
        self.shapesize(stretch_wid=2, stretch_len=8)

    def click(self, x, y):
        self.hideturtle()
        self.is_hidden = True
        if self.type == "exit":
            self.exit_game()
        elif self.type == "start":
            print("this is start")
            self.hide_all_buttons()
            return True
        elif self.type == "again":         
            self.hide_all_buttons()
            return True
        else:
            print("this is not a button")
            return False

    def exit_game(self):
        turtle.bye()

    def hide_all_buttons(self):
        all_buttons = get_all_instances(TurtleUserInterface)
        for button in all_buttons:
            button.clear()
            button.hideturtle()