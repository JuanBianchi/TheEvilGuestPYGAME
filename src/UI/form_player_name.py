import pygame
from pygame.locals import *
from constantes import *

from UI.GUI_button import Button, pygame
from UI.GUI_textbox import TextBox
from UI.GUI_label import Label
from UI.GUI_form import Form

class PlayerTextBox(Form):
    def __init__(self, screen, x: int, y: int, w: int, h: int, color_background, color_border, border_size):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size)

        self.background_img = pygame.image.load("./src/assets/img/background/zombie background.jpg")
        self.background_img = pygame.transform.scale(self.background_img, (ANCHO_VENT, ALTO_VENT))

        self.name_label = Label(self._slave, 100, 50, 400, 50, "Introduce yourself", "Horrorfind", 36, (155, 0, 0), "./src/assets/img/ui/Table.png")
        self.accept_button = Button(self._slave, x, y, 210, 450, 200, 50, AZUL, ROJO, self.on_accept_button_click, "stage", "Stage 3", font="Horrorfind", font_size=20, font_color=NEGRO)
        self.text = TextBox(self._slave, x, y, 50, 50, 150, 30, "gray","white","red","blue", 2, "Horrorfind", 15, "black")

        self.__name_introduced = self.input_player_name()

        self.lista_widgets.extend([self.name_label, self.accept_button, self.text])


    @property
    def get_name_introduced(self):
        return self.__name_introduced

    def input_player_name(self):
        self.__name_introduced = self.text.get_text()
    
    def on_accept_button_click(self, param):
        self.go_back()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.blit(self.background_img, (0, 0))