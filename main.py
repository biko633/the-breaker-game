from turtle import Turtle, Screen
from component.Scores import TurtleScores
from component.Background import TurtleBackground
from component.Player_paddle import TurtlePlayerPaddle
from component.Ball import TurtleBall
import time

# ----------------Screen setup------------------------#
screen_width = 1000
screen_height = 800

# Set up the screen
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

# Set the background image
screen.bgpic("images/91657.gif")

# Disable the resizing of the screen
screen.cv._rootwindow.resizable(False, False)
# ----------------------------------------#

# ----------Create the background----------
background_turtle = TurtleBackground()
# ------------------------------------------#

# ----------Create the score turtle----------#
score_turtle = TurtleScores()

#Display the scores
score_turtle.display_scores()
#--------------------------------------------#

#----------Create the player paddle------------#
player_turtle = TurtlePlayerPaddle()
player_turtle.ondrag(player_turtle.movie_paddle)
#------------------------------------------------#

#----------Create the ball----------------------#
ball_turtle = TurtleBall()
#-----------------------------------------------#  


# # Update the scores
# score_turtle.update_scores(2574, 455)
# score_turtle.save_scores()


#--------Start the game----------#
game_is_on = True
while game_is_on:
    # print(ball_turtle.position())
    time.sleep(0.005)
    screen.update()
    ball_turtle.move_ball()

    #Detect collision with the paddle
    if ball_turtle.distance(player_turtle) < 70 and ball_turtle.xcor() > 310:
        print("collision")
        ball_turtle.bounce_y()

    #Detect collision with left and right walls
    if ball_turtle.xcor() > 465 or ball_turtle.xcor() < -465:
        ball_turtle.bounce_x()

    #Detect collision with top wall
    if ball_turtle.ycor() > 300:
        ball_turtle.bounce_y()


    
    # #Detect collision with the paddles
    # if ball_turtle.distance(player_turtle) < 50 and ball_turtle.xcor() > 340 or ball_turtle.distance(player_turtle) < 50 and ball_turtle.xcor() < -340:
    #     ball_turtle.bounce_x()

    # #Detect if the ball goes out of bounds
#--------------------------------#

screen.mainloop()