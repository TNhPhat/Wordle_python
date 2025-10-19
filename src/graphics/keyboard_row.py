import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphics.base_graphics import Drawable
from environment.setttings import COLORS,FONT_PATH,KEYBOARD_CHAR,ALPHA_KEY_LEN,KEY_SPACE
from graphics.keyboard_key import keyboard_key
import pygame

class keyboard_row(Drawable):
    def __init__(self,row_index,scale = [1,1]):
        super().__init__(scale)
        self.keys = []
        self.row_index = row_index
        for i in KEYBOARD_CHAR[row_index]:
            if i == "ENTER" or i == "BACKSPACE":
                self.keys.append(keyboard_key(i,ALPHA_KEY_LEN*3,ALPHA_KEY_LEN,self.scale))
            else:
                self.keys.append(keyboard_key(i,ALPHA_KEY_LEN,ALPHA_KEY_LEN,self.scale))
        self.format_col()
    
    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        for i in self.keys:
            i.update_layout(scale, window_width, window_height)
        return 
    
    def set_color(self,char,color):
        for i in range(len(self.keys)):
            if char == self.keys[i].get_character():
                self.keys[i].set_color(color)
                return True
        return False

    def reset_state(self):
        for i in self.keys:
            i.reset_state()
        self.format_col()
    
    def format_col(self):
        for i in range(1,len(self.keys)):
            self.keys[i].set_position(self.keys[i - 1].get_position()[0] + self.keys[i - 1].get_size()[0] + KEY_SPACE*min(self.scale),self.keys[i - 1].get_position()[1])
        return

    def update(self,dt):
        for i in self.keys:
            i.update(dt)
        return 
    
    def get_size(self):
       szx = 0
       for i in self.keys:
           szx += i.get_size()[0]
       return [szx + KEY_SPACE*min(self.scale)*(len(self.keys) - 1),self.keys[0].get_size()[1]]
    
    def draw(self, target):
        for i in range(len(self.keys)):
            self.keys[i].draw(target)
        return 
    
    def handle_event(self, event):
        return 
    
    def handle_input(self):
        return 
    
    def set_position(self, x, y):
        self.keys[0].set_position(x,y)
        self.format_col()
        return 
    
    def get_position(self):
        return self.keys[0].get_position()
