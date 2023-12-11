import pygame
from constantes import *
from pygame.locals import *
from UI.GUI_widget import *
from UI.GUI_button import Button
from UI.GUI_form import Form
from UI.GUI_label import Label
from UI.form_level_selection import *
from UI.form_settings import *
from UI.form_ranking import *
from db.ranking import *

class MainMenu(Form):
    def __init__(self, screen: pygame.Surface, x:int, y:int, w:int, h:int, color_background, color_border: (0,0,0), border_size: int = -1, active = True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)


        self.menu_label = Label(self._slave, 200, 50, 400, 50, "The Evil Guest", "Horrorfind", 36, (155, 0, 0), "./UI/resources/Table.png")
        self.button_level_select = Button(self._slave, x, y, 270, 250, 200, 50, AZUL, ROJO, self.on_level_select_click, "nombre","Seleccion de niveles", font="Horrorfind", font_size=20, font_color=NEGRO)
        self.button_sound_config = Button(self._slave, x, y, 270, 350, 200, 50, AZUL, ROJO, self.on_settings_click, "nombre","Configuracion de sonido", font="Horrorfind", font_size=20, font_color=NEGRO)
        self.button_ranking = Button(self._slave, x, y, 270, 450, 200, 50, AZUL, ROJO, self.on_ranking_click, "nombre","Ranking", font="Horrorfind", font_size=20, font_color=NEGRO)

        self.lista_widgets.extend([self.button_level_select, self.button_sound_config, self.button_ranking, self.menu_label])

        self.background_image = pygame.image.load("./assets/img/background/background.jpg")
        self.background_image = pygame.transform.scale(self.background_image, (w, h))

        pygame.mixer.music.load("./assets/sounds/bg ost/Resident Evil 4 Remake OST - Main Menu Theme.wav")
        pygame.mixer.music.set_volume(0.9)
        pygame.mixer.music.play(-1)
        
        self.__form_stage = LevelSelect(self._master, 0, 0, ANCHO_VENT, ALTO_VENT, (0, 0, 0), (100, 100, 100), active=True)
        self.__settings = Settings(self._master, 0, 0, ANCHO_VENT, ALTO_VENT, (0, 0, 0), (0, 0, 0), active=True)


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
        self._slave.blit(self.background_image, (0, 0)) 


    def on_level_select_click(self, texto):
        print("Seleccion de niveles clickeado")
        self.__form_stage.active = True
        self.show_dialog(self.__form_stage)


    def on_settings_click(self, texto):
        print("Configuracion de sonido clikeado")
        self.__settings.active = True
        self.show_dialog(self.__settings)


    def on_ranking_click(self, texto):
        print("Ranking clickeado")
        list_dict_ranking = self.get_db_ranking()
        ranking = Ranking(self._master, 0, 0, ANCHO_VENT, ALTO_VENT, NEGRO, "./UI/resources/Window.png", list_dict_ranking, 10, 100, 10)
        ranking.active = True
        self.show_dialog(ranking)

    def get_db_ranking(self):
        lines = get_table()
        list_data = []
        for line in lines:
            dict_line = {}
            for i in range(len(line)):
                col_name = lines[0][i]
                value = line[i]
                dict_line[col_name] = value
            list_data.append(dict_line)
        
        return list_data