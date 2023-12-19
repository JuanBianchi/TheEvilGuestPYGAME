import pygame
from pygame.locals import *
from constantes import *

from UI.GUI_button_image import *
from UI.GUI_form import *
from UI.GUI_label import *

class Ranking(Form):
    def __init__(self, screen, x: int, y: int, w: int, h: int, color_background, path_image, scoreboard, margen_y, margen_x, espacio, 
                 color_border="Black", border_size: int = -1, active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.background_img = pygame.image.load("./src/assets/img/background/scoreboard bg.jpg")
        self.background_img = pygame.transform.scale(self.background_img, (ANCHO_VENT, ALTO_VENT))
        self._slave = aux_image
        self._score = scoreboard
        self._margen_y = margen_y
        
        self.player_bar = Label(screen=self._slave, x=margen_x+10,y=20,w=w/2-margen_x-10,h=50,text = "Player", font="Verdana",font_size=30,font_color=(255,255,255),path_image="./src/assets/img/ui/bar.png")
        self.score_bar = Label(screen=self._slave, x=margen_x+300,y=20,w=w/2-margen_x-10,h=50,text = "Score", font="Verdana",font_size=30,font_color=(255,255,255),path_image="./src/assets/img/ui/bar.png")
        self.home_button = Button_Image(screen = self._slave, master_x=x, master_y=y, x = w-70, y = h-70, w = 50, h = 50, path_image = "./src/assets/img/ui/home.png", onclick = self.btn_home_click, onclick_param = "")

        self.lista_widgets.extend([self.player_bar, self.score_bar, self.home_button])

        pos_inicial_y = 100


        for j in self._score:
            pos_inicial_x = margen_x
            for n,s in j.items():
                cadena = "" 
                cadena = f"{s}"
                pos = Label(screen=self._slave, x=pos_inicial_x,y=pos_inicial_y,
                            w=w/2-margen_x,h=100,text = cadena, font="Verdana",font_size=30,
                            font_color=(255,255,255),path_image="./src/assets/img/ui/Table.png")
                self.lista_widgets.append(pos)
                pos_inicial_x += w/2-margen_x
                
            pos_inicial_y+=100 + espacio

    def btn_home_click(self, param):
        self.go_back()

    def update_ranking(self, player_name, score):
        player_info = f"Player: {player_name}, Score: {score}"


    def update(self, lista_eventos):
        if self.active:
            for widget in self.lista_widgets:
                widget.update(lista_eventos)
            self.draw()
            self.render()

    def render(self):
        self._slave.blit(self.background_img, (0, 0))