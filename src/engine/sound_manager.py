import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import time
import random
from environment.setttings import ULTI_SOUND

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.random_skin = 0
        self.random_pyke_skin()
        self.mixer = pygame.mixer.Sound(ULTI_SOUND[0][0])
        
    def random_pyke_skin(self):
        self.random_skin = (self.random_skin + 1) % (len(ULTI_SOUND))

    def reset(self):
        self.random_pyke_skin()
        self.stop_all()

    def play_ulti_sound(self, number_green_word):
        self.mixer = pygame.mixer.Sound(ULTI_SOUND[self.random_skin][number_green_word - 1])
        self.mixer.play()

    def stop_all(self):
        pygame.mixer.stop()