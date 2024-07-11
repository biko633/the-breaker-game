from turtle import Turtle

class TurtlePlayerPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(1)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.left(90)
        self.backward((self.getscreen().window_height() / 2) - 30)
        self.the_height = 35
        self.the_width = 115
        # self.movie_paddle(0, -370)

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def paddle_reset(self):
        self.goto(0, -370)

    # def movie_paddle(self, x, y):
    #     # check if the paddle is out of bounds left or right
    #     if self.xcor() < -390:
    #         self.goto(-390, -370) 
    
    #         # self.ondrag(self.movie_paddle)
    #     elif self.xcor() > 390:
    #         self.goto(390, -370) 
    
    #         # self.ondrag(self.movie_paddle)
    #     else:
    #         # stop backtracking 
    #         self.ondrag(None)  
    
    #     # move the turtle's angle and direction  
    #     # towards x and y 
    #         self.setheading(self.towards(x, -370)) 
    
    #     # go to x, y 
    #         self.goto(x, -370) 
    
    #     # call again 
    #         self.ondrag(self.movie_paddle)