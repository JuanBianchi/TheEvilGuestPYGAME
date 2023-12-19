import pygame
from models.items.items import Item

class Life(Item, pygame.sprite.Sprite):
    def __init__(self, type, sub_type, file_name, coord_x, coord_y, width, height, cols, rows, frame_rate, value) -> None:
        super().__init__(type, sub_type, file_name, coord_x, coord_y, width, height, cols, rows, frame_rate)
        self.__value = value
        self.__life_group = pygame.sprite.Group()
        self.__life_group.add(self)

    @property
    def get_extra_life(self):
        return self.__value

    @property
    def get_lifes_group(self):
        return self.__life_group
