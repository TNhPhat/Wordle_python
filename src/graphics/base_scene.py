
class Scene:
    def __init__(self,game,scale = [1,1]):
        self.scale = scale
        self.game_engine = game

    def handle_event(self,event):
        pass

    def set_scale(self,scale):
        self.scale = scale
    
    def update_layout(self,scale,window_width,window_height):
        pass

    def update(self, dt):
        pass

    def handle_input(self): 
        pass

    def render(self, surface):
        pass
