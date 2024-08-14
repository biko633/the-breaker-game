from playsound import playsound
from threading import Thread


sounds_effect = {
    "bounce": "sounds/bounce.mp3",
    "hit-brick": "sounds/hit-brick.mp3",
    "lose-life": "sounds/lose-life.mp3",
    "game-start": "sounds/game-start.mp3",
    "game-over": "sounds/game-over.mp3",
    "game-won": "sounds/game-won.mp3",
}
def trigger_sound(sound_path):
    playsound(sound_path)

def play_sound_effect(sound_name):
    sound_path = sounds_effect[sound_name]
    thread = Thread(target=lambda: trigger_sound(sound_path))
    thread.start()