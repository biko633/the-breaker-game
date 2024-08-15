from turtle import Turtle
import turtle
from component.utilities.Class_utility import get_all_instances
from component.sound_effect import play_sound_effect
import json

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
        self.shapesize(stretch_wid=2, stretch_len=8)
        if type == "start":
            self.start_button_turtle(x, y, type)
        elif type == "exit":
            self.exit_button_turtle(x, y, type)
        elif type == "restart":
            self.restart_button_turtle(x, y, type)
        elif type == "continue":
            self.continue_button_turtle(x, y, type)
        elif type == "game_over":
            self.game_over_turtle(type)
        elif type == "game_won":
            self.game_won_turtle(type)

    def start_button_turtle(self, x, y, type):
        self.type = type
        self.shape("images/start.gif")
        self.goto(x / 3 * -1 - 50, y / 3 * -1 - 50)
        self.onclick(self.click)

    def exit_button_turtle(self, x, y, type):
        self.type = type
        self.shape("images/exit.gif")
        self.goto(x / 3 + 50, y / 3 * -1 - 50)

    def game_over_turtle(self, type):
        self.type = type
        self.hideturtle()
        self.color("#de1b4a")
        self.goto(0, 0)

    def game_won_turtle(self, type):
        self.type = type
        self.hideturtle()
        self.color("#de1b4a")
        self.goto(0, 0)

    def continue_button_turtle(self, x, y, type):
        self.type = type
        self.shape("images/continue.gif")
        self.goto(x / 3 * -1 - 50, y / 3 * -1 - 50)
        self.onclick(self.click)

    def restart_button_turtle(self, x, y, type):
        self.type = type
        self.shape("images/restart.gif")
        self.goto(x / 3 * -1 - 50, y / 3 * -1 - 50)
        self.onclick(self.click)

    # x and y is needed so the user can click the button
    # click return true so game_is_on = True so the game can start or restart
    def click(self, x, y):
        self.hideturtle()
        self.hide_all_buttons()
        play_sound_effect("game-start")
        return True

    def exit_game(self, x, y):
        turtle.bye()

    def game_end_message(self):
        if self.type == "game_over":
            self.write("Game Over", align="center", font=("Arial", 40, "bold"))
        elif self.type == "game_won":
            self.write("Game Won", align="center", font=("Arial", 40, "bold"))

    def hide_all_buttons(self):
        all_buttons = get_all_instances(TurtleUserInterface)
        for button in all_buttons:
            button.clear()
            button.hideturtle()