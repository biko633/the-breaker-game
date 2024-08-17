import pygame
from threading import Thread

# Initialize the mixer module
pygame.mixer.init()

# Preload sound effects
sounds_effect = {
    "bounce": pygame.mixer.Sound("sounds/bounce.mp3"),
    "hit-brick": pygame.mixer.Sound("sounds/hit-brick.mp3"),
    "lose-life": pygame.mixer.Sound("sounds/lose-life.mp3"),
    "game-start": pygame.mixer.Sound("sounds/game-start.mp3"),
    "game-over": pygame.mixer.Sound("sounds/game-over.mp3"),
    "game-won-new": pygame.mixer.Sound("sounds/game-won-new.mp3")
}

def play_sound_effect(sound_name):
    def play():
        try:
            sounds_effect[sound_name].play()
        except KeyError:
            print(f"Sound '{sound_name}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    thread = Thread(target=play)
    thread.start()
