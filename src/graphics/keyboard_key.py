import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphics.base_graphics import Drawable
from environment.setttings import COLORS,FONT_PATH,BORDER_RADIUS,KEYBOARD_CHAR
import pygame

class keyboard_key(Drawable):
    def __init__(self,character,width,height,scale = [1,1]):
        super().__init__(scale)
        self.rect = pygame.Rect(0,0,width,height)
        self.color = COLORS["keyboard_key_color"]
        self.character = character
        self.font = pygame.font.Font(FONT_PATH, 3*min(width,height) //(4*len(character)))
        

    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        self.font = pygame.font.Font(FONT_PATH,round(3*min(self.rect.width*self.scale[0],self.rect.height*self.scale[1]) / (4*len(self.character))))
        return 

    def reset_state(self):
        self.set_position(0,0)
        self.color = COLORS["keyboard_key_color"]

    def get_character(self):
        return self.character
    
    def set_color(self,color):
        self.color = COLORS[color]

    def get_color(self):
        return self.color

    def get_position(self):
        return [self.rect.x,self.rect.y]
    
    def check_key(self,key):
        string_key = pygame.key.name(key)
        if(string_key == self.character):
            return True
        return False
    
    def update(self,dt):
        return 

    def handle_event(self, event):
        return
                
    def handle_input(self):
        return
    
    def process_key(key):
        return 

    def set_position(self,x,y):
        self.rect.x = x
        self.rect.y = y

    def get_size(self):
        return [self.rect.width*self.scale[0],self.rect.height*self.scale[1]]

    def draw(self, target):
        rect = self.rect.copy()
        rect.width *= self.scale[0]
        rect.height *= self.scale[1]
        pygame.draw.rect(target, self.color, rect, border_radius= round(BORDER_RADIUS*min(self.scale)))
        text_surface = self.font.render(self.character, True, COLORS["white"])
        text_rect = text_surface.get_rect(center=rect.center)
        target.blit(text_surface, text_rect)