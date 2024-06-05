from turtle import Turtle, Screen
from component.Scores import TurtleScores
from component.Background import TurtleBackground
from component.Player_paddle import TurtlePlayerPaddle
from component.Ball import TurtleBall
import time
import math

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
# player_turtle.ondrag(player_turtle.movie_paddle)
#------------------------------------------------#

#----------Create the ball----------------------#
ball_turtle = TurtleBall()
#-----------------------------------------------#  


#---------------Listen to the keyboard--------------#
screen.listen()
screen.onkeypress(player_turtle.go_left, "Left")
screen.onkeypress(player_turtle.go_right, "Right")
screen.onkeypress(player_turtle.go_left, "a")
screen.onkeypress(player_turtle.go_right, "d")
#-----------------------------------------------------#

#--------------check for collision-------------------#
def ball_collision(T1, T2):
    x_collision = (math.fabs(T1.xcor() - T2.xcor()) * 2) < (T1.the_width + T2.the_width)
    y_collision = (math.fabs(T1.ycor() - T2.ycor()) * 2) < (T1.the_height + T2.the_height)
    print(f"this is x =   {x_collision}")
    print(f"this is y =   {y_collision}")

    return (x_collision and y_collision)
#-----------------------------------------------------#

# # Update the scores
# score_turtle.update_scores(2574, 455)
# score_turtle.save_scores()


#--------Start the game----------#
game_is_on = True
ball_hit = False
while game_is_on: 
    time.sleep(0.1)
    screen.update()
    ball_turtle.move_ball()

    # Detect collision with the paddle
    if ball_collision(ball_turtle, player_turtle) and not ball_hit:
        ball_hit = True
        print("the ball is colliding with the paddle")
        ball_turtle.bounce_y()

    #Detect collision with left and right walls
    if ball_turtle.xcor() > 465 or ball_turtle.xcor() < -465:
        ball_turtle.bounce_x()

    #Detect collision with top wall
    if ball_turtle.ycor() > 300:
        ball_turtle.bounce_y()

    # Reset ball_hit flag when ball is not colliding with the paddle
    if ball_hit and ball_turtle.distance(player_turtle) >= 50:
        ball_hit = False

#--------------------------------#

screen.mainloop()