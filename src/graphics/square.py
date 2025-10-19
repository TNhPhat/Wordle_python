
import pygame
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from environment.setttings import SQUARELEN,COLORS,BORDER_RADIUS,SQUARE_COLOR,SQUARE_COLOR_BORDER,SQUARE_BORDER_THIN,SQUARE_FLIP_SPEED,FONT_PATH,SQUARE_BASE_SCALE_ZOOM_ANIMATION,SQUARE_TARGET_SCALE_ZOOM_ANIMATION,SQUARE_SPEED_ZOOM_ANIMATION
from graphics.base_graphics import Drawable
print(Drawable)

class Square(Drawable):
    def __init__(self,scale = [1,1]):
        super().__init__(scale)
        self.square = pygame.Rect(0,0,SQUARELEN,SQUARELEN)
        self.color = COLORS[SQUARE_COLOR]
        self.character = ""
        self.font = pygame.font.Font(FONT_PATH, 2*SQUARELEN // 3)

        self.flipping = 0
        self.flip_progress = 0.0  
        self.flip_speed = float(SQUARE_FLIP_SPEED)
        self.flip_target_color = None
    
        self.scale_anima = SQUARE_BASE_SCALE_ZOOM_ANIMATION
        self.target_scale = SQUARE_BASE_SCALE_ZOOM_ANIMATION
        self.scale_speed = SQUARE_SPEED_ZOOM_ANIMATION  
        self.zoom_animating = False

    def update_layout(self, scale, window_width, window_height):
        self.set_scale(scale)
        self.font = pygame.font.Font(FONT_PATH,round(2*SQUARELEN*min(self.scale[0],self.scale[1]) / 3))
        return 
    
    def start_zoom_animation(self):
        self.scale_anima = SQUARE_BASE_SCALE_ZOOM_ANIMATION
        self.target_scale = SQUARE_TARGET_SCALE_ZOOM_ANIMATION
        self.zoom_animating = True
    
    def fliped(self):
        return (self.flipping == 3)

    def reset_state(self):
        self.set_position(0,0)
        self.color = COLORS[SQUARE_COLOR]
        self.character = ""
        self.flipping = 0
        self.flip_progress = 0.0  
        self.flip_target_color = None
    
    def setcharacter(self,char):
        char = char.upper()
        self.character = char
        self.start_zoom_animation()

    def start_flip(self):
        self.flipping = True
        self.flip_progress = 0.0

    def get_character(self):
        return self.character
    
    def set_color(self,color):
        self.flip_target_color = COLORS[color]

    def is_set_key(self):
        if self.character:
            return True
        else: 
            return False

    def get_position(self):
        return [self.square.x,self.square.y]
    
    def check_alpha_key(self,key):
        string_key = pygame.key.name(key)
        if(len(string_key) == 1 and string_key >= "a" and string_key <= "z"):
            return True
        return False
    
    def update(self,dt):
        if self.flipping == 1:
            self.flip_progress += dt * self.flip_speed
            if self.flip_progress >= 1.0:
                self.flip_progress = 1.0
                self.flipping = 3
    
        if self.zoom_animating:
            diff = self.target_scale - self.scale_anima
            self.scale_anima += diff * dt * self.scale_speed
            if abs(diff) < 0.01:
                if self.target_scale > 1.0:
                    self.target_scale = 1.0  
                else:
                    self.zoom_animating = False
        return 

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.check_alpha_key(event.key):
                self.setcharacter(pygame.key.name(event.key).upper())
                
    
    def handle_input(self):
        return
    
    def process_key(key):
        return 

    def set_position(self,x,y):
        self.square.x = x
        self.square.y = y

    def get_size(self):
        return [self.square.width*min(self.scale),self.square.height*min(self.scale)]

    def draw(self, target):
        scale = 1.0
        if self.flipping:
            if self.flip_progress < 0.5:
                scale = 1 - (self.flip_progress * 2)
            else:
                scale = (self.flip_progress - 0.5) * 2

            if self.flip_progress >= 0.5 and self.color != self.flip_target_color:
                self.color = self.flip_target_color

        rect = self.square.copy()
        rect.width *= min(self.scale)
        rect.height *= min(self.scale)
        new_height = int(rect.height * scale)
        rect.y += (rect.height - new_height) // 2
        rect.height = new_height
        
        if self.zoom_animating:
            scaled_w = int(rect.width * self.scale_anima)
            scaled_h = int(rect.height * self.scale_anima)
            rect.x = rect.centerx - scaled_w // 2
            rect.y = rect.centery - scaled_h // 2
            rect.width = scaled_w
            rect.height = scaled_h

        pygame.draw.rect(target, self.color, rect, border_radius=round(BORDER_RADIUS*min(self.scale)))
        if self.color != self.flip_target_color:
            border_color = COLORS[SQUARE_COLOR_BORDER]
            if self.is_set_key():
                border_color = COLORS["border_color_with_text"]
            pygame.draw.rect(target, border_color, rect, round(SQUARE_BORDER_THIN*min(self.scale)), border_radius=round(BORDER_RADIUS*min(self.scale)))

        if self.character and (self.flip_progress == 1.00 or self.flip_progress == 0.00):
            text_surface = self.font.render(self.character, True, COLORS["white"])
            text_rect = text_surface.get_rect(center=rect.center)
            target.blit(text_surface, text_rect)