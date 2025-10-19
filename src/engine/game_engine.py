import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame 
    
from pygame.locals import *
from environment.setttings import BASE_SCREEN_WIDTH,BASE_SCREEN_HEIGHT,FPS,TITLE,COLORS,MAX_GUESSES
from graphics.play_scene import PlayScene
from gameplay.game_logic import game_process

class game_engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT),pygame.RESIZABLE)
        pygame.display.set_caption(TITLE)
        self.running = False
        self.scale = [1,1]
        self.scene = PlayScene(self,self.scale)
        self.playing = True
        self.number_of_tried = 0
        game_logic = game_process()
        game_logic.random_word()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                self.screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                self.scale[0] = window_width / BASE_SCREEN_WIDTH
                self.scale[1] = window_height / BASE_SCREEN_HEIGHT
                self.update_layout(window_width, window_height)
            else:
                self.scene.handle_event(event)
    
    def update_layout(self,window_width, window_height):
        self.scene.update_layout(self.scale,window_width,window_height)
        return
    
    def set_number_of_tried(self,number_of_tried):
        self.number_of_tried = number_of_tried

    def get_number_of_tried(self):
        return self.number_of_tried
    
    def is_lose(self):
        if(self.number_of_tried >= MAX_GUESSES):
            return True
        return False

    def change_scene(self, new_scene):
        self.scene = new_scene

    def update(self,dt):
        self.scene.update(dt)
    
    def render(self):
        self.screen.fill(COLORS["background"])
        self.scene.render(self.screen)
        pygame.display.flip()
    
    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        dt = 0
        while self.running:
            dt = clock.tick(FPS)/1000
            self.handle_events()
            self.scene.handle_input()
            self.update(dt)
            self.render()
        return



    