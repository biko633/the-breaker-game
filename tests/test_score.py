import pytest
from component.Scores import TurtleScores
import turtle
import json

class TestScores:

    def setup_method(self, method):
        print(f"SETUP METHOD {method} IS UP")
        self.score_turtle = TurtleScores()
        self.test_score = 142
        self.test_high_score = 44

    def teardown_method(self, method):
        print(f"TEARDOWN METHOD {method} IS DOWN")
        del self.score_turtle

    def test_started_score(self):
        assert self.score_turtle.score == 0

    def test_started_high_score(self):
        with open("component/scores.json", "r") as f:
            scores = json.load(f)
        assert self.score_turtle.high_score == scores["high_score"]


    def test_changing_scores(self):
        self.score_turtle.update_scores(self.test_score, self.test_high_score)
        self.score_turtle.save_scores()
        assert self.score_turtle.score == self.test_score
        assert self.score_turtle.high_score == self.test_high_score

    def test_loading_high_score(self):
        self.score_turtle.load_high_scores()
        with open("component/scores.json", "r") as f:
            scores = json.load(f)
        assert self.score_turtle.high_score == scores["high_score"]