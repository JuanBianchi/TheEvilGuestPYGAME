import pygame
from models.auxiliar.surface_manager import SurfaceManager as sfm
from constantes import ALTO_VENT, ANCHO_VENT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, coord_x, coord_y: tuple, frame_rate, walk_speed, run_speed, gravity, constraint_x_right, constraint_x_left) -> None:
        super().__init__()
        self.__walk_r = sfm.get_surface_from_spritesheet("./assets/img/enemies/walk/1.png", 8, 1)
        self.__walk_l = sfm.get_surface_from_spritesheet("./assets/img/enemies/walk/1.png", 8, 1, flip=True)
        self.__death_r = sfm.get_surface_from_spritesheet("./assets/img/enemies/death/0.png", 5, 1)
        self.__death_l = sfm.get_surface_from_spritesheet("./assets/img/enemies/death/0.png", 5, 1, flip=True)
        self.__walk = walk_speed
        self.__run = run_speed
        self.__gravity = gravity
        self.__frame_rate = frame_rate
        self.__enemy_move_time = 0
        self.__enemy_is_looking_right = True
        self.__enemy_animation_time = 0
        self.__enemy_group = pygame.sprite.Group()
        self.__initial_frame = 0
        self.__actual_animation = self.__walk_r
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        #self.__actual_img_animation = pygame.transform.scale(self.__actual_img_animation, (10, 10))
        self.rect = self.__actual_img_animation.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
        self.__max_x_constraint = constraint_x_right
        self.__min_x_constraint = constraint_x_left
        self.is_alive = True

    @property
    def get_enemy_rect(self):
        return self.rect

    @property
    def get_enemy_group(self):
        return self.__enemy_group
    
    # @property
    # def get_is_alive(self):
    #     return self.__is_alive
    
    # @get_is_alive.setter
    # def set_is_alive(self, is_alive: bool):
    #     self.__is_alive = is_alive


    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.__enemy_is_looking_right and self.is_alive:
            if self.rect.right < self.__max_x_constraint:     # Mi nuevo max_x_constraint deberia ser el el limite x de la plataforma (si esta en la plataforma)
                #self.rect.left += self.speed
                self.rect.x += self.__walk
            else:
                self.__enemy_is_looking_right = False
        else:
            if self.rect.left >= self.__min_x_constraint:          # Y esto lo mismo
                #self.rect.right -= self.speed
                self.rect.x -= self.__walk
            else:
                self.__enemy_is_looking_right = True

    
    def do_movement(self, delta_ms):
        if self.is_alive:
            self.__enemy_move_time+= delta_ms
            if self.__enemy_move_time >= self.__frame_rate:
                self.constraint()


    def do_animation(self, delta_ms):
        if self.is_alive:
            self.__enemy_animation_time += delta_ms
            if self.__enemy_animation_time >= self.__frame_rate:
                self.__enemy_animation_time = 0

                if self.__initial_frame < len(self.__actual_animation) - 1:
                    self.__initial_frame += 1
                else:
                    self.__actual_animation = self.__walk_r if self.__enemy_is_looking_right else self.__walk_l
                    if self.__initial_frame < len(self.__actual_animation) - 1:
                        self.__initial_frame += 1
                    else:
                        self.__initial_frame = 0
        else:
            self.__enemy_animation_time += delta_ms
            if self.__enemy_animation_time >= self.__frame_rate:
                self.__enemy_animation_time = 0

                self.__actual_animation = self.__death_r if self.__enemy_is_looking_right else self.__death_l
                if self.__initial_frame < len(self.__actual_animation) - 1:
                    self.__initial_frame += 1
                else:
                    self.__initial_frame = 4
        


    def update(self, delta_ms, screen: pygame.surface.Surface):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.draw_enemy(screen)

    
    def draw_enemy(self, screen: pygame.surface.Surface,):
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.rect)