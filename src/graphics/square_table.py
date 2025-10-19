import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
from graphics.row_square import row_square
from graphics.base_graphics import Drawable
from environment.setttings import MAX_GUESSES,SQUARE_SPACE,WORD_LENGTH
from gameplay.game_logic import game_process

class square_table(Drawable):
    
    def __init__(self,scale = [1,1]):
        super().__init__(scale)
        self.row_square_list = [row_square(scale) for _ in range(MAX_GUESSES)]
        self.format_col()
        self.number_of_tried = 0
    
    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        for i in self.row_square_list:
            i.update_layout(scale, window_width, window_height)
        return 
    
    def reset_state(self):
        for i in self.row_square_list:
            i.reset_state()
        self.format_col()
        self.number_of_tried = 0
    
    def format_col(self):
        for i in range(1,MAX_GUESSES):
            self.row_square_list[i].set_position(self.row_square_list[i - 1].get_position()[0],self.row_square_list[i - 1].get_position()[1] + self.row_square_list[i - 1].get_size()[1] + SQUARE_SPACE*min(self.scale))
        return
    
    def get_number_of_tried(self):
        return self.number_of_tried

    def update(self,dt):
        for i in self.row_square_list:
            i.update(dt)
        return 
    
    def get_size(self):
       return [self.row_square_list[0].get_size()[0],self.row_square_list[0].get_size()[1]*MAX_GUESSES + SQUARE_SPACE*min(self.scale)*(MAX_GUESSES - 1)]
    
    def draw(self, target):
        for i in range(0,MAX_GUESSES):
            self.row_square_list[i].draw(target)
        return 
    
    def get_color(self):
        game_logic = game_process()
        user_input = self.row_square_list[self.number_of_tried].get_string()
        res = {}
        if game_logic.in_dictionary(user_input):
            colors = game_logic.getcolor(user_input)
            for i in range(0,WORD_LENGTH):
                res.update({user_input[i]:colors[i]})
        return res
    
    def flipped(self,row_index):
        return self.row_square_list[row_index].flipped()

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and self.row_square_list[self.number_of_tried].get_string_len() == 5:
                game_logic = game_process()
                user_input = self.row_square_list[self.number_of_tried].get_string()
                if game_logic.in_dictionary(user_input):
                    colors = game_logic.getcolor(user_input)
                    self.row_square_list[self.number_of_tried].apply_colors(colors)
                    self.row_square_list[self.number_of_tried].start_flip()
                    self.number_of_tried+=1
                else:
                    self.row_square_list[self.number_of_tried].start_shake()
        if(self.number_of_tried < MAX_GUESSES):
            self.row_square_list[self.number_of_tried].handle_event(event)
        return 
    
    def handle_input(self):
        return 
    
    def set_position(self, x, y):
        self.row_square_list[0].set_position(x,y)
        self.format_col()
        return 
    
    def get_position(self):
        return self.row_square_list[0].get_position()
