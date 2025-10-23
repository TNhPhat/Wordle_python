import sys, os, math
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame
from graphics.square import Square
from graphics.base_graphics import Drawable
from environment.setttings import WORD_LENGTH, SQUARE_SPACE,SQUARE_FLIP_DELAY,SQUARE_SHAKE_AMPLITUDE,SQUARE_SHAKE_DURATION,SQUARE_SHAKE_FREQUENCY,COLORS,SQUARE_BOUNCE_DELAY

class row_square(Drawable):
    def __init__(self,scale = 1):
        super().__init__(scale)
        self.time_counter = 0
        self.flipping = False
        self.flip_index = 0
        self.square_list = [Square(scale) for _ in range(WORD_LENGTH)]
        self.format_row()
        self.string_len = 0
        self.shaking = False
        self.shake_time_counter = 0
        self.shake_duration = SQUARE_SHAKE_DURATION
        self.shake_amplitude = SQUARE_SHAKE_AMPLITUDE
        self.shake_frequency = SQUARE_SHAKE_FREQUENCY
        self.pos_before_shake = [0,0]

        self.bouncing = False
        self.bounce_index = 0
        self.bounce_time_counter = 0

    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        for i in self.square_list:
            i.update_layout(scale, window_width, window_height)
        return 
    
    def flipped(self):
        res = True
        for i in self.square_list:
            res = res and i.fliped()
        return res
    
    def start_shake(self):
        if self.shaking: 
            return
        self.pos_before_shake = self.get_position()
        self.shaking = True
        self.shake_time_counter = 0
        return        

    def reset_state(self):
        self.time_counter = 0
        self.flipping = False
        self.shaking = False
        self.flip_index = 0
        for i in self.square_list:
            i.reset_state()
        self.format_row()
        self.string_len = 0
        
    def format_row(self):
        for i in range(1,WORD_LENGTH):
            self.square_list[i].set_position(self.square_list[i - 1].get_position()[0] + self.square_list[i - 1].get_size()[0] + SQUARE_SPACE*min(self.scale),self.square_list[i - 1].get_position()[1])

    def get_size(self):
        return [self.square_list[0].get_size()[0]*WORD_LENGTH + SQUARE_SPACE*min(self.scale)*(WORD_LENGTH - 1),self.square_list[0].get_size()[1]]
    
    def draw(self, target):
        for i in range(0,WORD_LENGTH):
            self.square_list[i].draw(target)
        return 
    
    def get_string_len(self):
        return self.string_len
    
    def apply_colors(self,colors):
        if(len(colors) < WORD_LENGTH):
            return
        for i in range(0,WORD_LENGTH):
            self.square_list[i].set_color(colors[i])

    def get_string(self):
        res = ""
        for i in self.square_list:
            res = res + i.get_character()
        return res
    
    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and self.string_len >= 1:
                self.square_list[self.string_len - 1].setcharacter("")
                self.string_len -= 1
        if(self.string_len < 5):
            self.square_list[self.string_len].handle_event(event)
        return 
    
    def start_bounce(self):
        self.bounce_index = 0
        self.bouncing = True
        self.bounce_time_counter = 0

    def bounced(self):
        if self.bouncing:
            return False
        else:
            for i in self.square_list:
                if not i.bounced():
                    return False
        return True
    
    def update(self,dt):
        while self.string_len < 5 and self.square_list[self.string_len].is_set_key():
            self.string_len += 1
        if(self.flipping):
            self.time_counter += dt
            while self.flip_index < WORD_LENGTH:
                if(self.time_counter > self.flip_index*SQUARE_FLIP_DELAY):
                    if self.flip_index == 5:
                        self.flipping = False
                    self.square_list[self.flip_index].start_flip()
                    self.flip_index += 1
                else:
                    break
        else:
            self.time_counter = 0    
            self.flip_index = 0

        if(self.shaking):
            for i in self.square_list:
                i.set_border_color(COLORS["red"])
            self.shake_time_counter += dt
            shake_process = self.shake_time_counter/self.shake_duration
            offset_x = int(self.shake_amplitude*min(self.scale) * math.sin(shake_process * math.pi * self.shake_frequency))
            offset_x *= (1 - shake_process)
            self.set_position(self.pos_before_shake[0] + offset_x,self.get_position()[1])
            if self.shake_time_counter >= self.shake_duration:
                self.shaking = False
                self.shake_time_counter = 0
                self.set_position(self.pos_before_shake[0],self.pos_before_shake[1])

        if self.bouncing:
            self.bounce_time_counter += dt
            while self.bounce_index < 5:
                if self.bounce_time_counter >= self.bounce_index*SQUARE_BOUNCE_DELAY:
                    self.square_list[self.bounce_index].start_bounce_animation()
                    self.bounce_index+=1
                    if self.bounce_index == 5:
                        self.bouncing = False
                else:
                    break
            
        for i in self.square_list:
            i.update(dt)
        return 
    def handle_input(self):
        return 
    
    def start_flip(self):
        self.flipping = True
    
    def set_position(self, x, y):
        self.square_list[0].set_position(x,y)
        self.format_row()
        return 
    
    def get_position(self):
        return self.square_list[0].get_position()
