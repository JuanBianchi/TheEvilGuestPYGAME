import pygame


class Traps(pygame.sprite.Sprite):
    def __init__(self, img_path ,pos_x, pos_y, width, height, trap_type) -> None:
        super().__init__()
        self.__trap_img = pygame.image.load(img_path)
        self.__trap_img = pygame.transform.scale(self.__trap_img, (width, height))
        self.__type = trap_type
        self.rect = self.__trap_img.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.rect_area = pygame.Rect(self.rect.x, self.rect.y, width, height)
        self.__trap_group = pygame.sprite.Group()
    

    





    def update(self, screen: pygame.surface.Surface):
        self.draw_trap(screen)


    def draw_trap(self, screen: pygame.surface.Surface):
        screen.blit(self.__trap_img, self.rect_area)