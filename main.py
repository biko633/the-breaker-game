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

# # Update the scores
# score_turtle.update_scores(2574, 455)
# score_turtle.save_scores()


#--------Start the game----------#
game_is_on = True
ball_hit = False
while game_is_on:
    # print(ball_turtle.position())
    time.sleep(0.01)
    screen.update()
    ball_turtle.move_ball()
    print(ball_hit)
    # print(ball_turtle.position())

    #Detect collision with the paddle
    if ball_turtle.distance(player_turtle) < 35 and not ball_hit or ball_turtle.distance(player_turtle) < 35 and not ball_hit:
        print("collision")
        ball_turtle.bounce_y()
        ball_hit = True

    #Detect collision with left and right walls
    if ball_turtle.xcor() > 465 or ball_turtle.xcor() < -465:
        ball_turtle.bounce_x()

    #Detect collision with top wall
    if ball_turtle.ycor() > 300:
        ball_turtle.bounce_y()

    # Reset ball_hit flag when ball is not colliding with the paddle
    if ball_hit and ball_turtle.distance(player_turtle) >= 50:
        ball_hit = False

    
    # #Detect collision with the paddles
    # if ball_turtle.distance(player_turtle) < 50 and ball_turtle.xcor() > 340 or ball_turtle.distance(player_turtle) < 50 and ball_turtle.xcor() < -340:
    #     ball_turtle.bounce_x()

    # #Detect if the ball goes out of bounds
#--------------------------------#

screen.mainloop()