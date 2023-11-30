import pygame
from constantes import DEBUG

class Platform(pygame.sprite.Sprite):
    def __init__(self, plat_img_path, coord_x, coord_y, width, height) -> None:
        super().__init__()
        self.__platform_image = pygame.image.load(plat_img_path)
        self.__platform_image = pygame.transform.scale(self.__platform_image, (width, height))
        self.rect = self.__platform_image.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
        self.__platform_area = pygame.Rect(self.rect.x, self.rect.y, width, height)
        self.__platform_left_border = pygame.Rect(self.rect.left, self.rect.y, 2, height)
        self.__platform_right_border = pygame.Rect(self.rect.right, self.rect.y, 2, height)
        self.__platform_group = pygame.sprite.Group()
        self.__moving_down = False
    

    @property
    def get_platform_area(self):
        return self.__platform_area
    
    @property
    def get_platform_left_border(self):
        return self.__platform_left_border
    
    @property
    def get_platform_right_border(self):
        return self.__platform_right_border

    @property
    def get_platform_group(self):
        return self.__platform_group


    def move_platform_up_down(self):
        if self.__platform_area.bottom > 80 and not self.__moving_down:
            self.__platform_area.y -= 5
            if self.__platform_area.bottom <= 80:
                self.__moving_down = True

        elif self.__platform_area.top < 480 and self.__moving_down:
            self.__platform_area.y += 5
            if self.__platform_area.top >= 480:
                self.__moving_down = False


    def update(self, screen: pygame.surface.Surface):
        self.draw_platform(screen)
    

    def draw_platform(self, screen: pygame.surface.Surface):
        # pygame.draw.rect(screen, (0, 0, 255), self.__platform_area)
        # pygame.draw.rect(screen, (255, 0, 0), self.__platform_left_border)
        # pygame.draw.rect(screen, (255, 0, 0), self.__platform_right_border)
        screen.blit(self.__platform_image, self.__platform_area)