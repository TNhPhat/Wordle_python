import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphics.base_graphics import Drawable
from environment.setttings import COLORS,FONT_PATH,KEYBOARD_CHAR,ALPHA_KEY_LEN,KEY_SPACE
from graphics.keyboard_row import keyboard_row

class keyboard(Drawable):
    def __init__(self,scale = [1,1]):
        super().__init__(scale)
        self.key_rows = []
        for i in range(0,3):
            self.key_rows.append(keyboard_row(i,self.scale))
        self.format_col()
        self.format_row()
           
    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        for i in self.key_rows:
            i.update_layout(scale, window_width, window_height)
        self.format_col()
        self.format_row()
        return 
    
    def reset_state(self):
        for i in self.key_rows:
            i.reset_state()
        self.format_col()
        self.format_row()
    
    def format_row(self):
        row1_pos = self.key_rows[0].get_position()[0]
        row1_sz = self.key_rows[0].get_size()[0]
        row1_center = (row1_pos + row1_sz)/2
        for i in range(1,3):
            pos = self.key_rows[i].get_position()[0] 
            sz = self.key_rows[i].get_size()[0] 
            center = (pos + sz)/2
            self.key_rows[i].set_position(pos + (row1_center - center),self.key_rows[i].get_position()[1])

    def format_col(self):
        for i in range(1,3):
            self.key_rows[i].set_position(self.key_rows[i - 1].get_position()[0],self.key_rows[i - 1].get_position()[1] + self.key_rows[i - 1].get_size()[1] + KEY_SPACE*min(self.scale))
        return
    
    def get_color(self,char):
        for i in range(0,3):
            if char in KEYBOARD_CHAR[i]:
                return self.key_rows[i].get_color(char)

    def set_color(self,char,color):
        for i in self.key_rows:
            if i.set_color(char,color):
                return
        return

    def update(self,dt):
        for i in self.key_rows:
            i.update(dt)
        return 
    
    def get_size(self):
        return [self.key_rows[0].get_size()[0],self.key_rows[0].get_size()[1]*len(self.key_rows) + KEY_SPACE*min(self.scale)*(len(self.key_rows) - 1)]
    
    def draw(self, target):
        for i in self.key_rows:
            i.draw(target)
        return 
    
    def handle_event(self, event):
        return 
    
    def handle_input(self):
        return 
    
    def set_position(self, x, y):
        self.key_rows[0].set_position(x,y)
        self.format_col()
        self.format_row()
        return 
    
    def get_position(self):
        return self.key_rows[0].get_position()
