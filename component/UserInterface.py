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
    def __init__(self, x, y, type, score=0, high_score=0):
        super().__init__()
        self.penup()
        self.is_hidden = False
        self.type = type
        self.score = score
        self.high_score = high_score
        if self.type == "start":
            self.shape("images/start.gif")
            self.goto(x / 3 * -1 - 50, y / 3 * -1 - 50)
            print("start is ")
            print(self.pos())
            self.onclick(self.click)
        elif self.type == "exit":
            self.shape("images/exit.gif")
            self.goto(x / 3 + 50, y / 3 * -1 - 50) 
            print("exit is ")
            print(self.pos())
            self.onclick(self.click)
        elif self.type == "game_over":
            self.hideturtle()
            self.color("#de1b4a")
            self.goto(0, 0)
            self.write("Game Over", align="center", font=("Arial", 40, "bold"))
            print("game over is ")
            print(self.pos())
        elif self.type == "game_won":
            self.hideturtle()
            self.color("#de1b4a")
            self.goto(0, 0)
            self.write("Game Won", align="center", font=("Arial", 40, "bold"))
            print("game won is ")
            print(self.pos())
        elif self.type == "continue":
            self.shape("images/continue.gif")
            self.goto(x / 3 * -1 - 50, y / 3 * -1 - 50)
            print("continue is ")
            print(self.pos())
            self.onclick(self.click)
        else:
            self.shape("images/restart.gif")
            self.goto(x / 3 * -1 - 50, y / 3 * -1 - 50)
            print("restart is ")
            print(self.pos())
            self.onclick(self.click)
        self.shapesize(stretch_wid=2, stretch_len=8)

    def start_game(self):
        pass

    def exit_game(self):
        pass

    def game_over(self):
        pass

    def game_won(self):
        pass

    def continue_game(self):
        pass

    def restart_game(self):
        pass

    def click(self, x, y):
        self.hideturtle()
        self.is_hidden = True
        if self.type == "exit":
            self.exit_game()
        elif self.type == "start":
            print("this is start")
            self.hide_all_buttons()
            play_sound_effect("game-start")
            return True
        elif self.type == "restart":         
            self.hide_all_buttons()
            return True
        elif self.type == "continue":
            print("this is continue")
            self.hide_all_buttons()
            return True
        else:
            print("this is not a button")
            return False

    def exit_game(self):
        self.check_high_score()
        print(self.score)
        print(self.high_score)
        turtle.bye()

    def check_high_score(self):
        if self.score > self.high_score:
            print("new high score")
            with open("component/scores.json", "r+") as f:              
                data = json.load(f)
                data["high_score"] = self.score
                f.seek(0)
                json.dump(data, f)
                f.truncate()

    def hide_all_buttons(self):
        all_buttons = get_all_instances(TurtleUserInterface)
        for button in all_buttons:
            button.clear()
            button.hideturtle()