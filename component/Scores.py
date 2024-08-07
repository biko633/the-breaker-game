from turtle import Turtle
import json
import os

# Create a turtle object
class TurtleScores(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0 
        self.hideturtle()
        self.speed(10)
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.load_high_scores()

    def save_scores(self):
        with open("component/scores.json", "w") as f:
            json.dump({"high_score": self.high_score}, f)
 
    def load_high_scores(self):
        if os.path.exists("component/scores.json"):
            with open("component/scores.json", "r") as f:
                scores = json.load(f)
            self.high_score = scores["high_score"]
        else:
            self.save_scores()

    def update_scores(self, new_score, new_high_score):
        self.high_score = new_high_score
        self.score = new_score
        self.display_scores()

    def display_scores(self):
        # Write the score on the screen
        self.clear()
        self.penup()
        self.home()
        self.backward((self.getscreen().window_width() / 2) - 10)
        self.right(90)
        self.backward((self.getscreen().window_height() / 2) - 35)
        self.write(f"Score: {self.score}", align="left", font=("Arial", 20, "bold"))

        # Write the highest score on the screen
        self.home()
        self.right(180)
        self.backward((self.getscreen().window_width() / 2) - 10)
        self.left(90)
        self.backward((self.getscreen().window_height() / 2) - 35)
        self.write(f"Highest Score: {self.high_score}", align="right", font=("Arial", 20, "bold"))
        


#### SCORE TURTLE ####



##################