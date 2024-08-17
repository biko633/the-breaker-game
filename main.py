from turtle import Turtle, Screen
from component.Scores import TurtleScores
from component.Lives import TurtleLives
from component.Background import TurtleBackground
from component.Player_paddle import TurtlePlayerPaddle
from component.Ball import TurtleBall
from component.bricks import TurtleBricks
from component.UserInterface import TurtleUserInterface
from component.sound_effect import play_sound_effect
from Screen_Info import width, height
import time


#---------Running the game ----------------------#
def main():
    class Game:
        def __init__(self):
            self.game_is_on = False
            self.ball_hit = False
            self.app_on = True
            self.screen_height = height
            self.screen_width = width
            self.player_turtle = None
            self.ball_turtle = None
            self.screen = None
            self.background_turtle = None
            self.lives_turtle = None
            self.bricks_turtle = None
            self.score_turtle = None
            self.start_button_turtle = None
            self.exit_button_turtle = None
            self.restart_button_turtle = None
            self.continue_button_turtle = None
            self.game_over_turtle = None
            self.game_won_turtle = None
            
            

        #-------------------Functions------------------------#

        def save_high_score(self):
            if self.score_turtle.check_high_score():
                self.score_turtle.update_high_score(new_score=self.score_turtle.score)
                self.score_turtle.save_high_score()
                return True
            
        def exit_game(self, x, y, turtle):
                turtle.exit_game(x, y)

        def restart_game(self, x, y, turtle, type):
            self.bricks_turtle.reset_bricks()
            self.ball_turtle.reset_ball()
            self.player_turtle.paddle_reset()
            if type == "won":
                self.game_is_on = turtle.click(x, y)
            else:
                self.lives_turtle.reset_lives()
                self.score_turtle.reset_score()
                self.game_is_on = turtle.click(x, y)

        def begin_game(self, x, y, turtle):
            self.game_is_on = turtle.click(x, y)
        #--------------------------------------------------#

        # Paddle movement
        def paddle_movement(self):
            # Check if the turtle is in the left or right corner
            if self.player_turtle.xcor() < self.screen_width / -2 + 80:
                # Disable the left and right arrow keys
                self.screen.onkeypress(None, "Left")
                self.screen.onkeypress(None, "a")
                return
                
            elif self.player_turtle.xcor() > self.screen_width / 2 - 80:
                self.screen.onkeypress(None, "Right")
                self.screen.onkeypress(None, "d")
                return
            else:
                # Enable the left and right arrow keys
                self.screen.onkeypress(self.player_turtle.go_left, "Left")
                self.screen.onkeypress(self.player_turtle.go_right, "Right")
                self.screen.onkeypress(self.player_turtle.go_left, "a")
                self.screen.onkeypress(self.player_turtle.go_right, "d")
                # self.screen.onkeypress(self.bricks_turtle.rem_all_bricks, "x")
                return
            
        def stop_paddle_movement(self):
            self.screen.onkeypress(None, "Left")
            self.screen.onkeypress(None, "Right")
            self.screen.onkeypress(None, "a")
            self.screen.onkeypress(None, "d")
            return

        #--------------------------------------------------#

        # Ball collision with right and left walls
        def ball_side_walls_collision(self):
                #Detect collision with right and left walls
            if self.ball_turtle.xcor() > (self.screen_width / 2) - 30 or self.ball_turtle.xcor() < (self.screen_width / -2) + 26:
                self.ball_turtle.bounce("side")
                play_sound_effect("bounce")
                return
            

        # Ball collision with top wall
        def ball_top_wall_collision(self):
                #Detect collision with top wall
            if self.ball_turtle.ycor() > self.screen_height / 2 - 72:
                self.ball_turtle.bounce("top")
                play_sound_effect("bounce")
                return
            

        # reset ball_hit flag when ball is not colliding with the paddle
        def reset_ball_hit(self):
                # Reset ball_hit flag when ball is not colliding with the paddle
            if self.ball_hit and self.ball_turtle.distance(self.player_turtle) >= 50:
                self.ball_hit = False
                return

        #--------------------------------------------------#

        # Ball collision with the paddle
        def check_collision_paddle(self, obj):                 # \/ bottom of paddle \/ middle of paddle \/ top of paddle
            if abs(self.ball_turtle.xcor() - obj.xcor()) < 55 and (obj.ycor() - 10 <= self.ball_turtle.ycor() <= obj.ycor() + 24) :
                return True
            
            return False

        # Ball collision with the bricks
        def check_collision_brick(self, obj):
            if abs(self.ball_turtle.xcor() - obj.xcor()) < 40 and obj.ycor() <= self.ball_turtle.ycor() + 10 <= obj.ycor() + 10 :
                # print("collided with the brick:", obj)
                return True
            return False

        def hit_bricks(self, brick_dictionary):
            for brick, index in brick_dictionary.items():
                if self.check_collision_brick(brick):
                    self.ball_turtle.bounce("brick")
                    play_sound_effect("hit-brick")
                    self.score_turtle.update_scores(new_score=self.score_turtle.score + 100, new_high_score=self.score_turtle.high_score)
                    # print(f"the index of the brick is -> {index}")      
                    brick.clear()
                    brick.hideturtle()
                    del brick_dictionary[brick]
                    break

        #--------------------------------------------------#

        # Paddle missing ball  
        def paddle_missing(self):
            if self.lives_turtle.lives == 0:
                play_sound_effect("game-over")
                self.game_is_on = False
                self.game_over_turtle.game_end_message()
                self.exit_button_turtle.showturtle()
                self.restart_button_turtle.showturtle()
                self.save_high_score()
                self.score_turtle.display_scores()
                time.sleep(0.01)
                self.screen.update()
            elif self.ball_turtle.ycor() < (self.screen_height / -2) - 20:
                play_sound_effect("lose-life")
                self.lives_turtle.update_lives()
                self.ball_turtle.reset_ball()
                self.player_turtle.paddle_reset()
        #------------------------------------------------------#

        #---------------Won game---------------------------#

        def won_game(self):
            if self.bricks_turtle.brick_list == {}:
                self.game_is_on = False
                self.game_won_turtle.game_end_message()
                self.exit_button_turtle.showturtle()
                self.continue_button_turtle.showturtle()
                self.save_high_score()
                self.score_turtle.display_scores()
                play_sound_effect("game-won-new")
                time.sleep(0.01)
                self.screen.update()
        #-------------------------------------------------#

        def close_game(self):
            self.app_on = False
            self.game_is_on = False

        def setup_game(self):
            # Set up the screen
            self.screen = Screen()
            self.screen.register_shape("images/start.gif")
            self.screen.register_shape("images/exit.gif")
            self.screen.register_shape("images/restart.gif")
            self.screen.register_shape("images/continue.gif")
            self.screen.setup(width=self.screen_width, height=self.screen_height)
            self.screen.tracer(0)

            # Set the background image
            self.screen.bgpic("images/91657.gif")

            # Disable the resizing of the screen
            self.screen.cv._rootwindow.resizable(False, False)

            # Set up the close game to x button on the top right
            self.screen.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", self.close_game)

        # ----------Create the background----------
            self.background_turtle = TurtleBackground()
        # ------------------------------------------#

        # ----------Create the score turtle----------#
            self.score_turtle = TurtleScores()

        #Display the scores
            self.score_turtle.display_scores()
        #--------------------------------------------#

        # ----------Create the lives turtle----------#
            self.lives_turtle = TurtleLives()

        #Display the lives
            self.lives_turtle.display_lives()
        #--------------------------------------------#

        #----------Create the player paddle------------#
            self.player_turtle = TurtlePlayerPaddle()
        #------------------------------------------------#

        #----------Create the ball----------------------#
            self.ball_turtle = TurtleBall()
        #-----------------------------------------------#  

        #----------Create the breaks-------------#
            self.bricks_turtle = TurtleBricks(lines=3, size=self.screen_width // 51, width=self.screen_width, height=self.screen_height)
        #-----------------------------------------------#

        #----------Create the user interface-------------#
            self.start_button_turtle = TurtleUserInterface(x=self.screen_width / 2, y=self.screen_height / 2, type="start")
            self.start_button_turtle.onclick(lambda x, y: self.begin_game(x, y, self.start_button_turtle), add=False, btn=1)
            self.restart_button_turtle = TurtleUserInterface(x=self.screen_width / 2, y=self.screen_height / 2, type="restart")
            self.restart_button_turtle.onclick(lambda x, y: self.restart_game(x, y, self.restart_button_turtle, type="lost"), add=False, btn=1)
            self.continue_button_turtle = TurtleUserInterface(x=self.screen_width / 2, y=self.screen_height / 2, type="continue")
            self.continue_button_turtle.onclick(lambda x, y: self.restart_game(x, y, self.continue_button_turtle, type="won"), add=False, btn=1)
            self.exit_button_turtle = TurtleUserInterface(x=self.screen_width / 2, y=self.screen_height / 2, type="exit")
            self.exit_button_turtle.onclick(lambda x, y: self.exit_game(x, y, self.exit_button_turtle), add=False, btn=1)
            self.game_over_turtle = TurtleUserInterface(x=self.screen_width / 2, y=self.screen_height / 2, type="game_over")
            self.game_won_turtle = TurtleUserInterface(x=self.screen_width / 2, y=self.screen_height / 2, type="game_won")  
        #-----------------------------------------------#

        #----------hide unused buttons and update the screen--------------------------------------#
            self.restart_button_turtle.hideturtle()
            self.continue_button_turtle.hideturtle()
            self.game_over_turtle.hideturtle()
            self.game_won_turtle.hideturtle()

        #----------------------------------------------------------------#

        #---------------Listen to the keyboard--------------#
            self.screen.listen()
        #-----------------------------------------------------#

        def start_game(self):
            # print(self.game_is_on)
            if not self.game_is_on:
                time.sleep(0.01)
                self.screen.update()
                self.stop_paddle_movement()
            while self.game_is_on:

                time.sleep(0.01)
                self.screen.update()

                self.ball_turtle.move_ball()
                self.paddle_movement()

                if self.check_collision_paddle(self.player_turtle) and not self.ball_hit:
                    play_sound_effect("bounce")
                    self.ball_turtle.bounce("paddle")

                self.hit_bricks(self.bricks_turtle.brick_list)

                self.ball_side_walls_collision()

                self.ball_top_wall_collision()

                self.reset_ball_hit()

                self.paddle_missing()

                self.won_game()
        #-------------------------------------------------#

    game = Game()
    game.setup_game()

    while game.app_on:
            game.start_game()

    # game.screen.mainloop()
    game.screen.bye()

if __name__ == "__main__":
    main()