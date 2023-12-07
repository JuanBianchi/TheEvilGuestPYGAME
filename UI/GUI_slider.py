import pygame
from UI.GUI_widget import Widget
import math
class Slider(Widget):
    def __init__(self,screen, master_x, master_y, x,y,w,h, value,color_background,  color_circulo):
        super().__init__(screen, x,y,w,h,color_background)

        self.value = value
        
        self.color_circulo = color_circulo

        self._slave = pygame.Surface((w, h))
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = x
        self.slave_rect.y = y

        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += master_x
        self.slave_rect_collide.y += master_y

        w_circulo = w / 20
        h_circulo = h * 2.5
        self.rectangulo_circulo = pygame.Rect(0, 0, w_circulo, h_circulo)
        self.rectangulo_circulo.center = (x + w * value, self.slave_rect.centery)

        diagonal = math.sqrt(w_circulo**2 + h_circulo**2)
        self.radio_circulo = diagonal / 2

        

        self.render()
    
    def render(self):
        self._slave.fill(self._color_background)

        
    def draw(self):
        super().draw()
        pygame.draw.circle(self._master, self.color_circulo, self.rectangulo_circulo.center, self.radio_circulo)

    def update(self, lista_eventos):
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if self.slave_rect_collide.collidepoint(mouse_pos):
                valor = (mouse_pos[0] - self.slave_rect_collide.x) / self._slave.get_width()
                
                self.value = round(valor * 100) / 100 # redondeo el valor
                
                self.rectangulo_circulo.center = (self.slave_rect.x + self._slave.get_width() * self.value, self.slave_rect.centery)
        self.draw()

    def get_value(self):
        return self.value