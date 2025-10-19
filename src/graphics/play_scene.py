
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphics.base_scene import Scene
from graphics.square_table import square_table
from environment.setttings import BASE_SCREEN_HEIGHT,BASE_SCREEN_WIDTH,COLORS,MAX_GUESSES
from graphics.keyboard import keyboard
import pygame

class PlayScene(Scene):
    def __init__(self, game,scale = [1,1]):
        super().__init__(game,scale)
        self.square = square_table(game,scale)
        self.keyboard = keyboard(scale)
        self.color_keyboard_queue = []
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
        self.keyboard.reset_state()
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
                if len(colors_dict):
                    self.color_keyboard_queue.append([self.square.get_number_of_tried(),colors_dict])

        self.square.handle_event(event)
        self.game_engine.set_number_of_tried(self.square.get_number_of_tried())
        return

    def handle_input(self): 
       return

    def update(self, dt):
        win_game = False
        while len(self.color_keyboard_queue) > 0:
            row_index = self.color_keyboard_queue[0][0]
            color_list = self.color_keyboard_queue[0][1]
            if self.square.flipped(row_index):
                number_of_green = 0
                for i in color_list:
                    char = i[0]
                    color = i[1]
                    if self.keyboard.get_color(char) != COLORS["green"]:
                        if self.keyboard.get_color(char) != COLORS["yellow"]:
                            self.keyboard.set_color(char,color)
                        elif color != "grey":
                            self.keyboard.set_color(char,color)
                    if color == "green":
                        number_of_green += 1
                    if number_of_green == 5:
                        win_game = True
                self.game_engine.set_number_green_word(number_of_green)
                tmp = self.color_keyboard_queue.pop(0)
                print(tmp)
                print(self.color_keyboard_queue)
            else: 
                break
        if len(self.color_keyboard_queue) == 0 and self.square.get_number_of_tried() >= MAX_GUESSES:
            self.game_engine.set_lose()
        if(win_game):
            self.game_engine.set_win()
        self.square.update(dt)
        return
    
    def render(self, surface):
        self.square.draw(surface)
        self.keyboard.draw(surface)
