#SCREEN CONFIG
BASE_SCREEN_WIDTH = 1080
BASE_SCREEN_HEIGHT = 720
FPS = 60
TITLE = "wordle"
#PATH
RAW_WORDLIST_PATH = "assets\word_list\\valid-wordle-words.txt"
PROCESSED_WORDLIST_PATH = "assets\word_list\words_len_5.txt"

COLORS = {
    "green": (121, 184, 81),
    "yellow": (243, 194, 55),
    "gray": (61, 64, 84),
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "darker_white":(240,240,240),
    "background":(25, 26, 36),
    "light_black":(25, 26, 36),
    "text_color":(57,62,76),
    "border_color":(123,127,152),
    "keyboard_key_color":(101,103,128)
}

#keyboard settings
KEYBOARD_CHAR = [['Q','W','E','R','T','Y','U','I','O','P'],
                 ['A','S','D','F','G','H','J','K','L'],
                 ['BACKSPACE','Z','X','C','V','B','N','M','ENTER']]
ALPHA_KEY_LEN = 50
KEY_SPACE = 4

#FONTS settings
FONT_NAME = "ClearSans-Bold"
FONT_PATH = "assets\\fonts\ClearSans-Bold.ttf"

#game config
SQUARE_COLOR = "light_black"
SQUARE_COLOR_BORDER = "border_color"
SQUARE_BORDER_THIN = 5
SQUARELEN = 70
BORDER_RADIUS = 10
SQUARE_SPACE = 5
SQUARE_FLIP_SPEED = 3
SQUARE_FLIP_DELAY = 0.16
SQUARE_SHAKE_DURATION = 0.4  
SQUARE_SHAKE_AMPLITUDE = 20
SQUARE_SHAKE_FREQUENCY = 7

#Game play settings
WORD_LENGTH = 5
MAX_GUESSES = 6