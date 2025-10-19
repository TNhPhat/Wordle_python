
import pygame
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment.setttings import SQUARELEN,COLORS,BORDER_RADIUS,SQUARE_COLOR,SQUARE_COLOR_BORDER,SQUARE_BORDER_THIN,SQUARE_FLIP_SPEED,FONT_PATH
from graphics.base_graphics import Drawable
print(Drawable)

class Square(Drawable):
    def __init__(self,scale = [1,1]):
        super().__init__(scale)
        self.square = pygame.Rect(0,0,SQUARELEN,SQUARELEN)
        self.color = COLORS[SQUARE_COLOR]
        self.character = ""
        self.font = pygame.font.Font(FONT_PATH, 2*SQUARELEN // 3)
        self.flipping = 0
        self.flip_progress = 0.0  
        self.flip_speed = float(SQUARE_FLIP_SPEED)
        self.flip_target_color = None

    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        self.font = pygame.font.Font(FONT_PATH,round(2*SQUARELEN*min(self.scale[0],self.scale[1]) / 3))
        return 
    
    def fliped(self):
        return (self.flipping == 3)

    def reset_state(self):
        self.set_position(0,0)
        self.color = COLORS[SQUARE_COLOR]
        self.character = ""
        self.flipping = 1
        self.flip_progress = 0.0  
        self.flip_target_color = None
    
    def setcharacter(self,char):
        char = char.upper()
        self.character = char

    def start_flip(self):
        self.flipping = True
        self.flip_progress = 0.0

    def get_character(self):
        return self.character
    
    def set_color(self,color):
        self.flip_target_color = COLORS[color]

    def is_set_key(self):
        if self.character:
            return True
        else: 
            return False

    def get_position(self):
        return [self.square.x,self.square.y]
    
    def check_alpha_key(self,key):
        string_key = pygame.key.name(key)
        if(len(string_key) == 1 and string_key >= "a" and string_key <= "z"):
            return True
        return False
    def update(self,dt):
        if self.flipping == 1:
            self.flip_progress += dt * self.flip_speed
            if self.flip_progress >= 1.0:
                self.flip_progress = 1.0
                self.flipping = 3
        return 

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.check_alpha_key(event.key):
                self.setcharacter(pygame.key.name(event.key).upper())
                
    
    def handle_input(self):
        return
    
    def process_key(key):
        return 

    def set_position(self,x,y):
        self.square.x = x
        self.square.y = y

    def get_size(self):
        return [self.square.width*min(self.scale),self.square.height*min(self.scale)]

    def draw(self, target):
        scale = 1.0
        if self.flipping:
            if self.flip_progress < 0.5:
                scale = 1 - (self.flip_progress * 2)
            else:
                scale = (self.flip_progress - 0.5) * 2

            if self.flip_progress >= 0.5 and self.color != self.flip_target_color:
                self.color = self.flip_target_color

        rect = self.square.copy()
        new_height = int(rect.height * scale)
        rect.width *= min(self.scale)
        rect.y += (rect.height - new_height) // 2
        rect.height = new_height
        rect.height *= min(self.scale)

        pygame.draw.rect(target, self.color, rect, border_radius=BORDER_RADIUS)
        if self.color != self.flip_target_color:
            pygame.draw.rect(target, COLORS[SQUARE_COLOR_BORDER], rect, SQUARE_BORDER_THIN, border_radius=BORDER_RADIUS)

        if self.character and (self.flip_progress == 1.00 or self.flip_progress == 0.00):
            text_surface = self.font.render(self.character, True, COLORS["white"])
            text_rect = text_surface.get_rect(center=rect.center)
            target.blit(text_surface, text_rect)