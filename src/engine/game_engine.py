import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame 
    
from pygame.locals import *
from environment.setttings import SCREEN_WIDTH,SCREEN_HEIGHT,FPS,TITLE,COLORS
from graphics.play_scene import PlayScene
class game_engine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(TITLE)
        self.running = False
        self.scene = PlayScene(self)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.scene.handle_event(event)

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
        self.quit()



    