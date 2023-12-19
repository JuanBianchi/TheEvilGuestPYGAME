import pygame
from constantes import *
from pygame.locals import *
from UI.GUI_widget import *
from UI.GUI_button import Button
from UI.GUI_form import Form
from UI.GUI_label import Label
from UI.form_level_selection import *
from UI.form_settings import *

class Pause(Form):
    def __init__(self, screen: pygame.Surface, x:int, y:int, w:int, h:int, color_background, color_border: (0,0,0), border_size: int = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.volume = 1
        self.flag_play = True

        self.pause_label = Label(self._slave, 200, 50, 400, 50, "PAUSED", "Horrorfind", 36, (155, 0, 0), "./src/assets/img/ui/Table.png")
        self.volume_label = Label(self._slave, 470, 400, 50, 50, "50%", "Horrorfind", 36, (155, 0, 0), "./src/assets/img/ui/Table.png")
        self.volume_slider = Slider(self._slave, x, y, 150, 420, 300, 10, self.volume, AZUL, BLANCO)
        self.play_pause_button = Button(self._slave, x, y, 400, 500, 150, 45, ROJO, ROJO, self.play_pause_music, None, "PAUSE ||", "Arial", 36, BLANCO)
        self.back_menu_button = Button(self._slave, x, y, 270, 450, 50, 50, AZUL, ROJO, self.go_back_menu, "nombre", "<-", font="Arial", font_size=36, font_color=NEGRO)

        self.lista_widgets.extend([self.pause_label, self.volume_label, self.back_menu_button, self.volume_slider, self.play_pause_button])


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
                #self.update_volumen()
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.fill(self._color_background)