from turtle import Turtle, Screen
from component.Scores import TurtleScores
from component.Lives import TurtleLives
from component.Background import TurtleBackground
from component.Player_paddle import TurtlePlayerPaddle
from component.Ball import TurtleBall
from component.UserInterface import TurtleUserInterface
from Screen_Info import width, height
import time
import math

# ----------------Screen setup------------------------#
screen_width = width
screen_height = height

# Set up the screen
screen = Screen()
screen.register_shape("images/start.gif")
screen.register_shape("images/exit.gif")
screen.register_shape("images/game_over.gif")
screen.register_shape("images/again.gif")
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

# ----------Create the lives turtle----------#
lives_turtle = TurtleLives()

#Display the lives
lives_turtle.display_lives()
#--------------------------------------------#

#----------Create the player paddle------------#
player_turtle = TurtlePlayerPaddle()
# player_turtle.ondrag(player_turtle.movie_paddle)
#------------------------------------------------#

#----------Create the ball----------------------#
ball_turtle = TurtleBall()
#-----------------------------------------------#  

#---------------set the game on to true-------------------#
def set_game_on(x, y, turtle):
    global game_is_on, start_button_turtle, again_button_turtle, lives_turtle
    lives_turtle.reset_lives()
    game_is_on = turtle.click(x, y)

#--------------------------------------------------#

#----------Create the user interface-------------#
start_button_turtle = TurtleUserInterface(x=700, y=600, type="start")
exit_button_turtle = TurtleUserInterface(x=700, y=600, type="exit")

start_button_turtle.onclick(lambda x, y: set_game_on(x, y, start_button_turtle), add=False, btn=1)


#-----------------------------------------------#

#---------------Listen to the keyboard--------------#
screen.listen()
#-----------------------------------------------------#

#-------------------Functions------------------------#

# Paddle movement
def paddle_movement():
    global player_turtle, screen
    # Check if the turtle is in the left or right corner
    if player_turtle.xcor() < -400:
        # Disable the left and right arrow keys
        screen.onkeypress(None, "Left")
        screen.onkeypress(None, "a")
        return
        
    elif player_turtle.xcor() > 400:
        screen.onkeypress(None, "Right")
        screen.onkeypress(None, "d")
        return
    else:
        # Enable the left and right arrow keys
        screen.onkeypress(player_turtle.go_left, "Left")
        screen.onkeypress(player_turtle.go_right, "Right")
        screen.onkeypress(player_turtle.go_left, "a")
        screen.onkeypress(player_turtle.go_right, "d")
        return
    
def stop_paddle_movement():
    screen.onkeypress(None, "Left")
    screen.onkeypress(None, "Right")
    screen.onkeypress(None, "a")
    screen.onkeypress(None, "d")
    return

# Ball collision
def ball_collision(T1, T2):
    x_collision = (math.fabs(T1.xcor() - T2.xcor()) * 2) < (T1.the_width + T2.the_width)
    y_collision = (math.fabs(T1.ycor() - T2.ycor()) * 2) < (T1.the_height + T2.the_height)
    # print(f"this is x =   {x_collision}")
    # print(f"this is y =   {y_collision}")
    return (x_collision and y_collision)


# Ball collision with the paddle
def ball_paddle_collision():
    global ball_turtle, player_turtle, ball_hit

    # Detect ball collision with the paddle
    if ball_collision(ball_turtle, player_turtle) and not ball_hit:
        # Detect ball collision with the paddle left side
        if player_turtle.xcor() - ball_turtle.xcor() >= 0:
            # Detect player position right
            if player_turtle.xcor() >= 0:
                ball_hit = True
                print("the ball is colliding with the paddle player right ball left 1")
                ball_turtle.bounce_y()
                ball_turtle.bounce_x()
                return
            # Detect player position left
            else:
                ball_hit = True
                print("the ball is colliding with the paddle player left ball left 2")
                ball_turtle.bounce_y()
                return

        # Detect ball collision with the paddle right side
        else:
            # Detect player position right
            if player_turtle.xcor() >= 0:
                ball_hit = True
                print("the ball is colliding with the paddle player right ball right 3")
                ball_turtle.bounce_y()
                return
            # Detect player position left
            else:
                ball_hit = True
                print("the ball is colliding with the paddle player left ball right 4")
                ball_turtle.bounce_y()
                ball_turtle.bounce_x()
                return


# Ball collision with left and right walls
def ball_side_walls_collision():
    global ball_turtle
        #Detect collision with left and right walls
    if ball_turtle.xcor() > 460 or ball_turtle.xcor() < -465:
        ball_turtle.bounce_x()
        return
    

# Ball collision with top wall
def ball_top_wall_collision():
    global ball_turtle
        #Detect collision with top wall
    if ball_turtle.ycor() > 305:
        ball_turtle.bounce_y()
        return
    

# reset ball_hit flag when ball is not colliding with the paddle
def reset_ball_hit():
    global ball_hit
        # Reset ball_hit flag when ball is not colliding with the paddle
    if ball_hit and ball_turtle.distance(player_turtle) >= 50:
        ball_hit = False
        return

# Paddle missing ball  
def paddle_missing():
    global player_turtle, ball_turtle, lives_turtle, game_is_on, again_button_turtle
    if lives_turtle.lives == 0:
        game_is_on = False
        game_over_turtle = TurtleUserInterface(x=700, y=600, type="game_over")
        exit_button_turtle = TurtleUserInterface(x=700, y=600, type="exit")
        again_button_turtle = TurtleUserInterface(x=700, y=600, type="again")
        again_button_turtle.onclick(lambda x, y: set_game_on(x, y, again_button_turtle), add=False, btn=1)
        time.sleep(0.01)
        screen.update()
    elif ball_turtle.ycor() < -380:
        lives_turtle.update_lives()
        ball_turtle.reset_ball()
        player_turtle.paddle_reset()
#------------------------------------------------------#

# # Update the scores
# score_turtle.update_scores(2574, 455)
# score_turtle.save_scores()

# lives_turtle.update_lives()

#--------Variables----------#
# game_is_on is in TurtleUserInterface
game_is_on = False
app_on = True
ball_hit = False
#--------------------------------#

#---------Running the game ----------------------#

def start_game():
    global game_is_on, start_button_turtle, player_turtle, ball_turtle, screen
    print(game_is_on)
    if not game_is_on:
        time.sleep(0.01)
        screen.update()
        stop_paddle_movement()
    while game_is_on:
        time.sleep(0.01)
        screen.update()

        ball_turtle.move_ball()
        paddle_movement()

        ball_paddle_collision()

        ball_side_walls_collision()

        ball_top_wall_collision()

        reset_ball_hit()

        paddle_missing()
#-------------------------------------------------#

while app_on:
    start_game()

screen.mainloop()