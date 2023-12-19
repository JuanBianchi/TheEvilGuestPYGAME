import pygame
from models.items.items import Item

class Coin(Item, pygame.sprite.Sprite):
    def __init__(self, type, sub_type, file_name, coord_x, coord_y, width, height, cols, rows, frame_rate, points) -> None:
        super().__init__(type, sub_type, file_name, coord_x, coord_y, width, height, cols, rows, frame_rate)
        self.__points = points
        self.__coins_group = pygame.sprite.Group()
        self.__coins_group.add(self)
    
    @property
    def get_points(self):
        return self.__points
    
    @property
    def get_coins_group(self):
        return self.__coins_group