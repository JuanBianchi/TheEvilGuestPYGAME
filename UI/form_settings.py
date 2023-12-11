import pygame
from constantes import *
from pygame.locals import *

from UI.GUI_button import Button, pygame
from UI.GUI_form import Form
from UI.GUI_label import Label
from UI.GUI_slider import Slider

class Settings(Form):
    def __init__(self, screen, x: int, y: int, w: int, h: int, color_background, color_border="Black", border_size: int = -1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volume = 1
        self.flag_play = True
        self.background_img = pygame.image.load("./assets/img/background/zombie background.jpg")
        self.background_img = pygame.transform.scale(self.background_img, (w, h))

        self.settings_label = Label(self._slave, 200, 50, 400, 50, "Settings", "Horrorfind", 36, (155, 0, 0), "./UI/resources/Table.png")
        self.volume_label = Label(self._slave, 470, 400, 50, 50, "50%", "Horrorfind", 36, (155, 0, 0), "./UI/resources/Table.png")
        self.volume_slider = Slider(self._slave, x, y, 150, 420, 300, 10, self.volume, AZUL, BLANCO)
        self.play_pause_button = Button(self._slave, x, y, 400, 500, 150, 45, ROJO, ROJO, self.play_pause_music, None, "PAUSE ||", "Arial", 36, BLANCO)
        self.go_back_button = Button(self._slave, x, y, 100, 500, 50, 50, AZUL, ROJO, self.go_back_menu, "nombre", "<-", font="Arial", font_size=36, font_color=NEGRO)

        self.lista_widgets.extend([self.settings_label, self.volume_label, self.volume_slider, self.play_pause_button, self.go_back_button])


    def play_pause_music(self, param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.play_pause_button._color_background = VERDE_OSCURO
            self.play_pause_button._font_color = BLANCO
            self.play_pause_button.set_text("PLAY |>")
        else:
            pygame.mixer.music.unpause()
            self.play_pause_button._color_background = ROJO
            self.play_pause_button._font_color = BLANCO
            self.play_pause_button.set_text("PAUSE ||")
        self.flag_play = not self.flag_play

    def update_volumen(self):
        self.volume = self.volume_slider.value
        self.volume_label.set_text(f"{round(self.volume * 100)}%")
        pygame.mixer.music.set_volume(self.volume)

    def go_back_menu(self, param):
        self.go_back()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
                self.update_volumen()
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.blit(self.background_img, (0, 0))