import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
import math

class Drawable:
    def __init__(self,scale = 1):
        self.scale = scale
    
    def lerp_color(self,start_color, end_color, progress):
        progress = max(0, min(progress, 1))
        return (
            int(start_color[0] + (end_color[0] - start_color[0]) * progress),
            int(start_color[1] + (end_color[1] - start_color[1]) * progress),
            int(start_color[2] + (end_color[2] - start_color[2]) * progress)
        )
    
    def wave_bounce(self,t, amplitude=6, damping=2):
        return math.sin(t * math.pi) * amplitude
        
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