from turtle import Turtle
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
        elif self.type == "exit":
            self.shape("images/exit.gif")
            self.goto(190, -200)
            print("exit is ")
            print(self.pos())
        else :
            self.shape("images/again.gif")
            self.goto(-200, -200)
            print("again is ")
            print(self.pos())
        self.shapesize(stretch_wid=2, stretch_len=8)
        self.onclick(self.click)

    def click(self, x, y):
        self.hideturtle()
        self.is_hidden = True
        all_buttons = get_all_instances(TurtleUserInterface)
        for button in all_buttons:
            if button.is_hidden == False:
                button.hideturtle()
                button.write("Thank you!", align='center', font=('Arial', 18, 'bold'))
        self.write("Thank you!", align='center', font=('Arial', 18, 'bold'))
