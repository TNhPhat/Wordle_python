import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pygame 
    
from pygame.locals import *
from environment.setttings import BASE_SCREEN_WIDTH,BASE_SCREEN_HEIGHT,TITLE,COLORS,MAX_GUESSES,FPS,FONT_PATH,WIN_STRING,LOSE_STRING,PRESS_ANY_KEY_SRING,WIN_LOSE_FONT_SIZE,PRESSED_ANY_KEY_FONT_SIZE,LINE_SPACE,DEFAULT_BLUR_AMOUNT,DEFAULT_DARK_ALPHA,ICON_PATH
from graphics.play_scene import PlayScene
from gameplay.game_logic import game_process
from engine.sound_manager import SoundManager

class game_engine:
    def __init__(self):
        pygame.init()
        icon = pygame.image.load(ICON_PATH)
        pygame.display.set_icon(icon)
        self.number_green_word = 0
        self.sound_manager = SoundManager()
        self.screen = pygame.display.set_mode((BASE_SCREEN_WIDTH, BASE_SCREEN_HEIGHT),pygame.RESIZABLE)
        pygame.display.set_caption(TITLE)
        self.running = False
        self.scale = [1,1]
        self.scene = PlayScene(self,self.scale)
        self.playing = True
        self.number_of_tried = 0
        self.font_win_lose = pygame.font.Font(FONT_PATH,WIN_LOSE_FONT_SIZE)
        self.font_pressed_key =  pygame.font.Font(FONT_PATH,PRESSED_ANY_KEY_FONT_SIZE)
        game_logic = game_process()
        self.win = False
        self.blured = False
        self.lose = False
        game_logic.random_word()

    def set_number_green_word(self,number):
        if number > 0:
            self.sound_manager.play_ulti_sound(number)
        self.number_green_word = max(number,self.number_green_word)

    def play_enter_sound(self):
        self.sound_manager.play_ulti_execute_sound()

    def blur_and_dark(self,surface, blur_amount=DEFAULT_BLUR_AMOUNT, dark_alpha=DEFAULT_DARK_ALPHA):
        w, h = surface.get_size()
        scale = 1.0 / blur_amount
        small = pygame.transform.smoothscale(surface, (int(w * scale), int(h * scale)))
        blurred = pygame.transform.smoothscale(small, (w, h))
        dark_overlay = pygame.Surface((w, h), pygame.SRCALPHA)
        dark_overlay.fill((0, 0, 0, dark_alpha))  
        blurred.blit(dark_overlay, (0, 0))
        return blurred

    def reset(self):
        self.sound_manager.reset()
        game_logic = game_process()
        game_logic.random_word()
        self.scene.reset_state()
        self.number_of_tried = 0
        self.number_green_word = 0
        self.win = False
        self.lose = False
        self.blured = False
        window_width, window_height = pygame.display.get_surface().get_size()
        self.scene.update_layout(self.scale,window_width,window_height)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                window_width, window_height = event.w, event.h
                self.screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
                self.scale[0] = window_width / BASE_SCREEN_WIDTH
                self.scale[1] = window_height / BASE_SCREEN_HEIGHT
                self.update_layout(window_width, window_height)
            elif self.win or self.lose:
                if event.type == pygame.KEYDOWN:
                    self.reset()
            else:
                self.scene.handle_event(event)
    
    def update_layout(self,window_width, window_height):
        self.font_win_lose = pygame.font.Font(FONT_PATH,round(WIN_LOSE_FONT_SIZE*min(self.scale)))
        self.font_pressed_key =  pygame.font.Font(FONT_PATH,round(PRESSED_ANY_KEY_FONT_SIZE*min(self.scale)))
        self.scene.update_layout(self.scale,window_width,window_height)
        return
    
    def set_number_of_tried(self,number_of_tried):
        if number_of_tried > self.number_of_tried and number_of_tried == 5:
            self.sound_manager.play_warning_sound()
        self.number_of_tried = number_of_tried


    def get_number_of_tried(self):
        return self.number_of_tried
    
    def set_lose(self):
        self.lose = True
        self.sound_manager.play_lose_sound()

    
    def set_win(self):
        self.win = True

    def change_scene(self, new_scene):
        self.scene = new_scene

    def update(self,dt):
        if self.win:
            return
        elif self.lose:
            return 
        else:
            self.scene.update(dt)
    
    def render(self):
        self.screen.fill(COLORS["background"])
        self.scene.render(self.screen)
        if self.win or self.lose:
            blur_surface = self.blur_and_dark(self.screen)
            self.screen.blit(blur_surface, (0, 0))
            self.blured = True
            title_text_surface = self.font_win_lose.render(WIN_STRING, True, COLORS["white"])
            if self.lose:
                title_text_surface = self.font_win_lose.render(LOSE_STRING, True, COLORS["white"])
            screen_rect = self.screen.get_rect()
            title_text_rect = title_text_surface.get_rect(center=screen_rect.center)
            
            press_key_text_surface = self.font_pressed_key.render(PRESS_ANY_KEY_SRING, True, COLORS["white"])
            press_key_text_rect = press_key_text_surface.get_rect(center=screen_rect.center)
            press_key_text_rect.y += (title_text_rect.height + LINE_SPACE*min(self.scale))

            self.screen.blit(title_text_surface, title_text_rect)
            self.screen.blit(press_key_text_surface, press_key_text_rect)
        pygame.display.flip()
    
    def run(self):
        self.running = True
        clock = pygame.time.Clock()
        dt = 0
        while self.running:
            dt = clock.tick(FPS)/1000
            self.handle_events()
            self.scene.handle_input()
            self.update(dt)
            self.render()
        return



    