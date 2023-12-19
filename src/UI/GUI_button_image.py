import pygame
from pygame.locals import *
from UI.GUI_widget import *

FPS = 18
    
class Button_Image(Widget):
    def __init__(self, screen,master_x,master_y, x,y,w,h, path_image,
                onclick=None, onclick_param=None, text="", font="Arial", font_size=12, font_color="Black",
                color_background = None, color_border = "Black", border_size = -1):
        super().__init__(screen, x,y,w,h,color_background,color_border, border_size)
        
        pygame.font.init()
        
        self._onclick = onclick
        self._onclick_param = onclick_param
        self._text = text
        self._font = pygame.font.SysFont(font,font_size)
        self._font_color = font_color
        self._master_x = master_x
        self._master_y = master_y
        
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        
        self.isclicked = False
        self.contador_click = 0
        
        self.render()
        
     
 
    def render(self):
        image_text = self._font.render(self._text, True, self._font_color, self._color_background)
        
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y
        
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self._master_x
        self.slave_rect_collide.y += self._master_y 
        
        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self._w / 2
        media_vertical = self._h / 2
        diferencia_horizontal = media_horizontal - media_texto_horizontal 
        diferencia_vertical = media_vertical - media_texto_vertical
        
        self._slave.blit(image_text,(diferencia_horizontal,diferencia_vertical))
    
    def update(self, lista_eventos):
        self.isclicked = False
        if self.contador_click > FPS/2:
            
            for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.slave_rect_collide.collidepoint(evento.pos):
                        if self._onclick != None and self._onclick_param!=None:
                            self._onclick(self._onclick_param)
                        self.isclicked = True
                        self.contador_click = 0
        else:
            self.contador_click += 1
        
        self.draw()