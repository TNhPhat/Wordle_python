
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from graphics.base_scene import Scene
from graphics.square_table import square_table
from environment.setttings import SCREEN_WIDTH,SCREEN_HEIGHT

class PlayScene(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.square = square_table()
        posx = (SCREEN_WIDTH - self.square.get_size()[0])//2
        posy = (SCREEN_HEIGHT - self.square.get_size()[1])//2
        self.square.set_position(posx,posy)

    def handle_event(self,event):
        self.square.handle_event(event)
        return
    

    def handle_input(self): 
        self.square.handle_input()

    def update(self, dt):
        return
    def render(self, surface):
        self.square.draw(surface)
