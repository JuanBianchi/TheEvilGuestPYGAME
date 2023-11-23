import pygame
from models.surface_manager import SurfaceManager as sfm
from models.constantes import ALTO_VENT, ANCHO_VENT

class Enemy(pygame.sprite.Sprite):
    def __init__(self, coord_x, coord_y: tuple, frame_rate, walk_speed, run_speed, gravity, constraint_x) -> None:
        super().__init__()
        self.__walk_r = sfm.get_surface_from_spritesheet("./assets/img/enemies/walk/1.png", 8, 1)
        self.__walk_l = sfm.get_surface_from_spritesheet("./assets/img/enemies/walk/1.png", 8, 1, flip=True)
        #self.__spawn = initial_position
        self.__run = run_speed
        self.__gravity = gravity
        self.__frame_rate = frame_rate
        self.__enemy_move_time = 0
        self.__enemy_is_looking_right = True
        self.__enemy_animation_time = 0
        self.__initial_frame = 0
        self.__actual_animation = self.__walk_r
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        #self.__actual_img_animation = pygame.transform.scale(self.__actual_img_animation, (10, 10))
        self.__rect = self.__actual_img_animation.get_rect()
        self.__rect.x = coord_x
        self.__rect.y = coord_y
        self.max_x_constraint = constraint_x

    
    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.__enemy_is_looking_right:
            if self.__rect.right < self.max_x_constraint:
                #self.rect.left += self.speed
                self.__rect.x += self.__run
            else:
                self.__enemy_is_looking_right = False
        else:
            if self.__rect.left > 0:
                #self.rect.right -= self.speed
                self.__rect.x -= self.__run
            else:
                self.__enemy_is_looking_right = True

    
    def do_movement(self, delta_ms):
        self.__enemy_move_time+= delta_ms
        if self.__enemy_move_time >= self.__frame_rate:
            self.constraint()


    def do_animation(self, delta_ms):
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
        


    def update(self, delta_ms, screen: pygame.surface.Surface):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.draw_player(screen)

    
    def draw_player(self, screen: pygame.surface.Surface,):
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.__rect)