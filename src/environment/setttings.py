#SCREEN CONFIG
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 720
FPS = 60
TITLE = "wordle"
#PATH
RAW_WORDLIST_PATH = "assets\word_list\words_alpha.txt"
PROCESSED_WORDLIST_PATH = "assets\word_list\words_len_5.txt"

COLORS = {
    "green": (55, 151, 119),
    "yellow": (244, 206, 20),
    "gray": (58, 58, 60),
    "white": (245, 247, 248),
    "black": (0, 0, 0),
    "background":(69, 71, 75)
}

#FONTS settings
FONT_NAME = "arial"

#game config
SQUARE_COLOR = "white"
SQUARE_COLOR_BORDER = "black"
SQUARE_BORDER_THIN = 5
SQUARELEN = 100
BORDER_RADIUS = 20
SQUARE_SPACE = 20

#Game play settins
WORD_LENGTH = 5
MAX_GUESSES = 6