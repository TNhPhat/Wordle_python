
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphics.base_scene import Scene
from graphics.square_table import square_table
from environment.setttings import BASE_SCREEN_HEIGHT,BASE_SCREEN_WIDTH
from graphics.keyboard import keyboard
import pygame

class PlayScene(Scene):
    def __init__(self, game,scale = [1,1]):
        super().__init__(game,scale)
        self.square = square_table(scale)
        self.keyboard = keyboard(scale)
        self.color_keyboard_queue = {}
        posx = (BASE_SCREEN_WIDTH - self.square.get_size()[0])//2
        posy = (2*BASE_SCREEN_HEIGHT/3 - self.square.get_size()[1])//2
        self.square.set_position(posx,posy)
        posx = (BASE_SCREEN_WIDTH - self.keyboard.get_size()[0])//2
        posy = (BASE_SCREEN_HEIGHT + 2*BASE_SCREEN_HEIGHT/3 - self.keyboard.get_size()[1])//2
        self.keyboard.set_position(posx,posy)


    def update_layout(self,scale, window_width, window_height):
        self.scale = scale
        self.square.update_layout(scale, window_width, window_height)
        self.keyboard.update_layout(scale,window_height,window_width)
        posx = (window_width - self.square.get_size()[0])//2
        posy = (2*window_height/3 - self.square.get_size()[1])//2
        self.square.set_position(posx,posy)
        posx = (window_width - self.keyboard.get_size()[0])//2
        posy = (window_height + 2*window_height/3 - self.keyboard.get_size()[1])//2
        self.keyboard.set_position(posx,posy)
        return 
    
    def reset_state(self):
        self.square.reset_state()
        posx = (BASE_SCREEN_WIDTH - self.square.get_size()[0])//2
        posy = (BASE_SCREEN_HEIGHT - self.square.get_size()[1])//2
        self.square.set_position(posx,posy)
        posx = (BASE_SCREEN_WIDTH - self.keyboard.get_size()[0])//2
        posy = (BASE_SCREEN_HEIGHT - self.keyboard.get_size()[1])//2
        self.keyboard.set_position(posx,posy)

    def handle_event(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                colors_dict = self.square.get_color()
                if len(colors_dict) == 5:
                    self.color_keyboard_queue.update({self.square.get_number_of_tried():colors_dict})

        self.square.handle_event(event)
        self.game_engine.set_number_of_tried(self.square.get_number_of_tried())
        return

    def handle_input(self): 
       return
    
    def update(self, dt):
        for row_index,color_dict in self.color_keyboard_queue.items():
            if self.square.flipped(row_index):
                for char,color in color_dict.items():
                    self.keyboard.set_color(char,color)
        self.square.update(dt)
        return
    
    def render(self, surface):
        self.square.draw(surface)
        self.keyboard.draw(surface)
