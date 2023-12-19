import pygame
from pygame.locals import *
from UI.GUI_widget import *

class Button(Widget):
    def __init__(self, screen,master_x,master_y, x,y,w,h,color_background,color_border, onclick, onclick_param, text, font, font_size, font_color):
        super().__init__(screen, x,y,w,h,color_background,color_border)
        
        pygame.font.init()
        
        self._onclick = onclick
        self._onclick_param = onclick_param
        self._text = text
        self._font = pygame.font.SysFont(font,font_size)
        self._font_color = font_color
        self._master_x = master_x
        self._master_y = master_y
        
        self.isclicked = False
        
        self.render()
        
        
 
    def render(self):
        image_text = self._font.render(self._text, True, self._font_color, self._color_background)
        
        self._slave = pygame.surface.Surface((self._w,self._h))#superficie que se adapte a la del boton
        self.slave_rect = self._slave.get_rect()
        
        self.slave_rect.x = self._x
        self.slave_rect.y = self._y
        
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self._master_x
        self.slave_rect_collide.y += self._master_y 
        
        
        self._slave.fill(self._color_background)
        
        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self._w / 2
        media_vertical = self._h / 2

        diferencia_horizontal = media_horizontal - media_texto_horizontal 
        diferencia_vertical = media_vertical - media_texto_vertical
        
        self._slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))
    
    def update(self, lista_eventos):
        self.isclicked = False
        for evento in lista_eventos:
           if evento.type == pygame.MOUSEBUTTONDOWN:
               if self.slave_rect_collide.collidepoint(evento.pos):
                   self.isclicked = True
                   self._onclick(self._onclick_param)
                   break
        self.draw()
                    
    def set_text(self, text):
        self._text = text
        self.render()
