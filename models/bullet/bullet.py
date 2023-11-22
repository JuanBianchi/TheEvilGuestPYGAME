import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, speed, direction) -> None:
        super().__init__()
        self.__bullet_img = pygame.image.load("./assets/img/bullet/bullet.png")
        self.__speed = speed
        self.__bullet_rect = self.__bullet_img.get_rect()
        self.__direction = direction

    
    def update(self, screen: pygame.surface.Surface):
        match self.__direction:
            case 'Left':
                self.__bullet_rect.x += self.__speed
                if self.__bullet_rect.x >= 600:
                    self.kill()
            case 'Right':
                self.__bullet_rect.x -= self.__speed
                if self.__bullet_rect.x <= 0:
                    self.kill()
        
        self.draw(screen)

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.__bullet_img, self.__bullet_rect)    
    
