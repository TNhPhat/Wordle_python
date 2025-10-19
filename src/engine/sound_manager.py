import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import time
import random
from environment.setttings import ULTI_SOUND,ULTI_EXECUTE,WARING_SOUND,LOSE_SOUND

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.random_skin = -1
        self.random_pyke_skin()
        self.mixer = pygame.mixer.Sound(ULTI_SOUND[0][0])
        self.mixer_ulti_execute = pygame.mixer.Sound(ULTI_EXECUTE)
        self.mixer_warning = pygame.mixer.Sound(WARING_SOUND)
        self.mixer_lose = pygame.mixer.Sound(LOSE_SOUND)
        
    def random_pyke_skin(self):
        tmp = self.random_skin
        while tmp == self.random_skin:
            self.random_skin = random.randint(0,len(ULTI_SOUND) - 1)

    def reset(self):
        self.random_pyke_skin()
        self.stop_all()

    def play_warning_sound(self):
        self.mixer_warning.play()

    def play_lose_sound(self):
        self.stop_all()
        self.mixer_lose.play()

    def play_ulti_execute_sound(self):
        self.mixer_ulti_execute.play()

    def play_ulti_sound(self, number_green_word):
        self.mixer = pygame.mixer.Sound(ULTI_SOUND[self.random_skin][number_green_word - 1])
        self.mixer.play()

    def stop_all(self):
        pygame.mixer.stop()