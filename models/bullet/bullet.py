import pygame
from models.auxiliar.surface_manager import SurfaceManager as sfm
from models.constantes import ANCHO_VENT



class Bullet(pygame.sprite.Sprite):
    def __init__(self, type, pos_x, pos_y, speed, direction, frame_rate) -> None:
        super().__init__()
        self.__bullet_img = self.load_img(type, direction)
        self.__speed = speed
        self.__frame_rate = frame_rate
        self.__bullet_animation_time = 0
        self.__initial_frame = 0
        self.__actual_animation = self.__bullet_img
        self.__bullet_img_animation = self.__actual_animation[self.__initial_frame]
        self.rect = self.__bullet_img_animation.get_rect(center=(pos_x, pos_y))
        #self.bullet_rect = self.__bullet_img.get_rect(center=(pos_x, pos_y))
        self.__direction = direction

    @property
    def get_bullet_rect(self):
        return self.bullet_rect

    def load_img(self, bullet_type, direction):
        if bullet_type == 'normal':
            if direction == "Right":
                self.__bullet_img = [pygame.image.load("./assets/img/bullet/bullet_r.png")]
            elif direction == "Left":
                self.__bullet_img = [pygame.image.load("./assets/img/bullet/bullet_l.png")]
        elif bullet_type == 'hatchet':
            if direction == 'Right':
                self.__bullet_img = sfm.get_surface_from_spritesheet("./assets/img/projectile/hatchet/hatchet.png", 7, 1)
            elif direction == 'Left':
                self.__bullet_img = sfm.get_surface_from_spritesheet("./assets/img/projectile/hatchet/hatchet.png", 7, 1, flip=True)

        return self.__bullet_img
    

    def do_animation(self, delta_ms):
        self.__bullet_animation_time += delta_ms
        if self.__bullet_animation_time >= self.__frame_rate:
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0

    # def bullet_movement(self, direction):
        # match self.__direction:
        #         case 'Left':
        #             self.rect.x -= self.__speed
        #             if self.rect.x >= 800:
        #                 self.kill()
        #         case 'Right':
        #             self.rect.x += self.__speed
        #             if self.rect.x <= 0:
        #                 self.kill()

    def update(self, screen: pygame.surface.Surface, delta_ms):
        match self.__direction:
            case 'Left':
                self.rect.x -= self.__speed
                if self.rect.x <= 0:
                    self.kill()
            case 'Right':
                self.rect.x += self.__speed
                if self.rect.x >= ANCHO_VENT:
                    self.kill()
        
        self.do_animation(delta_ms)
        self.draw(screen)

    def draw(self, screen: pygame.surface.Surface):
        self.__bullet_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__bullet_img_animation, self.rect)    
    
