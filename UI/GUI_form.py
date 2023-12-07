import pygame
from pygame.locals import *

from UI.GUI_button import *
#No se instancia. Es la base de la jerarquia
class Form(Widget):
    def __init__(self, screen:pygame.Surface, x: int, y:int, w:int ,h: int, color_background,color_border = "Black", border_size: int = -1, active = True):
        super().__init__(screen, x,y,w,h, color_background, color_border, border_size)
        self._slave = pygame.Surface((w,h))
        self.slave_rect = self._slave.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        self.lista_widgets = []
        self.hijo = None
        self.dialog_result = None
        self.padre = None
    
    def show_dialog(self, formulario):
        self.hijo = formulario
        self.hijo.padre = self

    def end_dialog(self):
        self.dialog_result = "OK"
        self.close()

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None
 

    
