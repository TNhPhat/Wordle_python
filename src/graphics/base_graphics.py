import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame

class Drawable:
    def draw(self, target: pygame.Surface):
        raise NotImplementedError("Drawable subclasses must implement draw()")
    def handle_event(self,event): pass
    def handle_input(self): pass
    def get_position(self): pass
    def set_position(self,x,y): pass
    def get_size(self): pass