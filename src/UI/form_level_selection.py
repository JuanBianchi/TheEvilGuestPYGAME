import pygame
from constantes import *
from pygame.locals import *
from game.game import Game
from UI.GUI_widget import *
from UI.GUI_button import Button
from UI.GUI_form import Form
from UI.GUI_label import Label
from UI.form_player_name import PlayerTextBox


class LevelSelect(Form):
    def __init__(self, screen, x: int, y: int, w: int, h: int, color_background, color_border="Black", border_size: int = -1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        self.flag_level_1 = False
        self.flag_level_2 = False

        self.level_select_label = Label(self._slave, 100, 50, 400, 50, "Select a level", "Horrorfind", 36, (155, 0, 0), "./src/assets/img/ui/Table.png")
        self.level_one_button = Button(self._slave, x, y, 210, 250, 200, 50, AZUL, ROJO, self.on_stage_one_select_click, "stage", "Stage 1", font="Horrorfind", font_size=20, font_color=NEGRO)
        self.level_two_button = Button(self._slave, x, y, 210, 350, 200, 50, AZUL, ROJO, self.on_stage_two_select_click, "stage", "Stage 2", font="Horrorfind", font_size=20, font_color=NEGRO)
        self.level_three_button = Button(self._slave, x, y, 210, 450, 200, 50, AZUL, ROJO, self.on_stage_three_select_click, "stage", "Stage 3", font="Horrorfind", font_size=20, font_color=NEGRO)
        self.go_back_button = Button(self._slave, x, y, 100, 500, 50, 50, AZUL, ROJO, self.go_back_menu, "nombre", "<-", font="Arial", font_size=36, font_color=NEGRO)


        self.lista_widgets.extend([self.level_select_label, self.level_one_button, self.level_two_button, self.level_three_button, self.go_back_button])


    def on_stage_one_select_click(self, param):
        self.player_textbox_form = PlayerTextBox(self._slave, 100, 100, 400, 200, (130, 130, 130), (0, 0, 0), 2)
        if self.player_textbox_form.active:
            self.player_textbox_form.update(pygame.event.get())

        self.player_textbox_form.show_dialog(self.player_textbox_form)

        self.__game = Game('stage_1') 
        self.__game.run()
        self.flag_level_1 = True

    def on_stage_two_select_click(self, param):
        if self.flag_level_1:
            self.__game = Game('stage_2') 
            self.__game.run()
            self.flag_level_2 = True
        else:
            print("Nivel bloqueado")
            self.flag_level_1 = False

    def on_stage_three_select_click(self, param):
        if self.flag_level_2:
            self.__game = Game('stage_3') 
            self.__game.run()
        else:
            print("Nivel bloqueado")

    def go_back_menu(self, param):
        self.go_back()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                for widget in self.lista_widgets:
                    widget.update(lista_eventos)
        else:
            self.hijo.update(lista_eventos)