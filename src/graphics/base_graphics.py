import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame

class Drawable:
    def __init__(self,scale = 1):
        self.scale = scale

    def draw(self, target: pygame.Surface):
        raise NotImplementedError("Drawable subclasses must implement draw()")
    def handle_event(self,event): pass
    def handle_input(self): pass
    def get_position(self): pass
    def update_layout(self,scale,window_width,window_height):
        pass
    def set_scale(self,scale): 
        self.scale = scale
    def set_position(self,x,y): pass
    def get_size(self): pass
    def update(self,dt):pass