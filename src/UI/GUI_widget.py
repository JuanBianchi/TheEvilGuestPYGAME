import pygame
class Widget:
    def __init__(self, screen: pygame.Surface, x: int, y: int, w: int, h:int, color_background = "Black", color_border = "Red", 
                 border_size: int = -1):
        
        self._master = screen
        self._x = x
        self._y = y
        self._w = w
        self._h = h
        self._color_background = color_background
        self._color_border = color_border
        self._slave = None
        self.slave_rect = None
        self.border_size = border_size
        
    
    def render(self):
        pass
    
    def update(self, lista_eventos):
        pass
    
    def draw(self):
        self._master.blit(self._slave,self.slave_rect)
        pygame.draw.rect(self._master, self._color_border, self.slave_rect, self.border_size)