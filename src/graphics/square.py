
import pygame
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment.setttings import SQUARELEN,COLORS,BORDER_RADIUS,SQUARE_COLOR,SQUARE_COLOR_BORDER,SQUARE_BORDER_THIN
from graphics.base_graphics import Drawable
print(Drawable)

class Square(Drawable):
    def __init__(self):
        super().__init__()
        self.square = pygame.Rect(0,0,SQUARELEN,SQUARELEN)
        self.color = COLORS[SQUARE_COLOR]
        self.character = ""
        #self.font = pygame.font.Font("C:\\Users\Phat Truong\Documents\GitHub\Wordle_python\\assets\\fonts\\arial.ttf", SQUARELEN - 20)

    # def setcharacter(self,char):
    #     char = char.upper()
    #     self.character = char

    def get_position(self):
        return [self.square.x,self.square.y]
    
    def handle_event(self, event):
        return 
    
    def handle_input(self):
        return
    
    def process_key(key):
        return 

    def set_position(self,x,y):
        self.square.x = x
        self.square.y = y

    def get_size(self):
        return [self.square.width,self.square.height]

    def draw(self, target):
        pygame.draw.rect(target, self.color, self.square,border_radius= BORDER_RADIUS)

        pygame.draw.rect(target, COLORS[SQUARE_COLOR_BORDER], self.square, SQUARE_BORDER_THIN ,border_radius= BORDER_RADIUS)

        if self.character:
            text_surface = self.font.render(self.character, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.square.center)
            target.blit(text_surface, text_rect)