import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, direction) -> None:
        super().__init__()
        self.__bullet_img = self.load_img(direction)
        self.__speed = speed
        self.rect = self.__bullet_img.get_rect(center=(pos_x, pos_y))
        #self.bullet_rect = self.__bullet_img.get_rect(center=(pos_x, pos_y))
        self.__direction = direction

    @property
    def get_bullet_rect(self):
        return self.bullet_rect

    def load_img(self, direction):
        if direction == "Right":
            self.__bullet_img = pygame.image.load("./assets/img/bullet/bullet_r.png")
        elif direction == "Left":
            self.__bullet_img = pygame.image.load("./assets/img/bullet/bullet_l.png")

        return self.__bullet_img
    
    def update(self, screen: pygame.surface.Surface):
        match self.__direction:
            case 'Left':
                self.rect.x -= self.__speed
                if self.rect.x >= 800:
                    self.kill()
            case 'Right':
                self.rect.x += self.__speed
                if self.rect.x <= 0:
                    self.kill()
        
        self.draw(screen)

    def draw(self, screen: pygame.surface.Surface):
        screen.blit(self.__bullet_img, self.rect)    
    
