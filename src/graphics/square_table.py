import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from graphics.row_square import row_square
from graphics.base_graphics import Drawable
from environment.setttings import MAX_GUESSES,SQUARE_SPACE

class square_table(Drawable):

    def __init__(self):
        self.row_square_list = [row_square() for _ in range(MAX_GUESSES)]
        self.format_col()
        
    def format_col(self):
        for i in range(1,MAX_GUESSES):
            self.row_square_list[i].set_position(self.row_square_list[i - 1].get_position()[0],self.row_square_list[i - 1].get_position()[1] + self.row_square_list[i - 1].get_size()[1] + SQUARE_SPACE)
        return

    def get_size(self):
       return [self.row_square_list[0].get_size()[0],self.row_square_list[0].get_size()[1]*MAX_GUESSES + SQUARE_SPACE*(MAX_GUESSES - 1)]
    
    def draw(self, target):
        for i in range(0,MAX_GUESSES):
            self.row_square_list[i].draw(target)
        return 
    
    def handle_event(self, event):
        return 
    
    def handle_input(self):
        return 
    
    def set_position(self, x, y):
        self.row_square_list[0].set_position(x,y)
        self.format_col()
        return 
    
    def get_position(self):
        return self.row_square_list[0].get_position()
