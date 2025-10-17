import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphics.square import Square
from graphics.base_graphics import Drawable
from environment.setttings import WORD_LENGTH, SQUARE_SPACE

class row_square(Drawable):

    def __init__(self):
        self.square_list = [Square() for _ in range(WORD_LENGTH)]
        self.format_row()
        
    def format_row(self):
        for i in range(1,WORD_LENGTH):
            self.square_list[i].set_position(self.square_list[i - 1].get_position()[0] + self.square_list[i - 1].get_size()[0] + SQUARE_SPACE,self.square_list[i - 1].get_position()[1])

    def get_size(self):
        return [self.square_list[0].get_position()[0] + self.square_list[0].get_size()[0]*WORD_LENGTH + SQUARE_SPACE*(WORD_LENGTH - 1),self.square_list[0].get_size()[1]]
    
    def draw(self, target):
        for i in range(0,WORD_LENGTH):
            self.square_list[i].draw(target)
        return 
    
    def handle_event(self, event):
        return 
    
    def handle_input(self):
        return 
    
    def set_position(self, x, y):
        self.square_list[0].set_position(x,y)
        self.format_row()
        return 
    
    def get_position(self):
        return self.square_list[0].get_position()
