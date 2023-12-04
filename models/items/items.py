import pygame
from constantes import IMG_PATH
from models.surface_manager import SurfaceManager as sfm

class Item(pygame.sprite.Sprite):
    def __init__(self, type, sub_type, file_name, coord_x, coord_y, width, height, cols, rows, frame_rate) -> None:
        super().__init__()
        self.__type = type
        self.__sub_type = sub_type
        self.__file_name = file_name
        self.__img_cols = cols
        self.__img_rows = rows
        self.__img_widht = width
        self.__img_height = height
        self.__img = self.load_img()
        self.__actual_animation = self.__img
        self.__initial_frame = 0
        self.__item_animation_time = 0
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        self.__frame_rate = frame_rate
        self.rect = self.__actual_img_animation.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
        self.__item_group = pygame.sprite.Group()
        self.__item_group.add(self)
        

    @property
    def get_item_group(self):
        return self.__item_group
    

    def load_img(self):
        self.__img = sfm.get_surface_from_spritesheet(IMG_PATH + f"/{self.__type}/{self.__sub_type}/{self.__file_name}.png", self.__img_cols, self.__img_rows)
        self.__img = [pygame.transform.scale(img, (self.__img_widht, self.__img_height)) for img in self.__img]
        return self.__img
    
    def do_animation(self, delta_ms):
        self.__item_animation_time += delta_ms
        if self.__item_animation_time >= self.__frame_rate:
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0


    def update(self, screen: pygame.surface.Surface, delta_ms):
        self.do_animation(delta_ms)
        self.draw(screen)

    def draw(self, screen: pygame.surface.Surface):
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.rect)   