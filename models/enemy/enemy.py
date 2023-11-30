import pygame
from models.auxiliar.surface_manager import SurfaceManager as sfm
from models.bullet.bullet import Bullet
from constantes import ALTO_VENT, ANCHO_VENT, SHOT_COOLDOWN

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_type: str, coord_x, coord_y: tuple, frame_rate, walk_speed, run_speed, gravity, constraint_x_right, constraint_x_left,
                walk_img_path, attack_img_path, death_img_path, iddle_img_path, walk_cols, attack_cols, death_cols, iddle_cols, player) -> None:
        super().__init__()
        self.__walk_r = sfm.get_surface_from_spritesheet(walk_img_path, walk_cols, 1)
        self.__walk_l = sfm.get_surface_from_spritesheet(walk_img_path, walk_cols, 1, flip=True)
        self.__attack_r = sfm.get_surface_from_spritesheet(attack_img_path, attack_cols, 1)
        self.__attack_l = sfm.get_surface_from_spritesheet(attack_img_path, attack_cols, 1, flip=True)
        self.__attack_framerate = frame_rate * 1
        self.__death_r = sfm.get_surface_from_spritesheet(death_img_path, death_cols, 1)
        self.__death_l = sfm.get_surface_from_spritesheet(death_img_path, death_cols, 1, flip=True)
        self.__iddle_r = sfm.get_surface_from_spritesheet(iddle_img_path, iddle_cols, 1)
        self.__iddle_l = sfm.get_surface_from_spritesheet(iddle_img_path, iddle_cols, 1, flip=True)
        self.__type = enemy_type
        # self.__img_cols = cols
        # self.__img_rows = rows
        self.__walk = walk_speed
        self.__run = run_speed
        self.__gravity = gravity
        self.__frame_rate = frame_rate
        self.__enemy_move_time = 0
        self.__enemy_is_looking_right = True
        self.__enemy_animation_time = 0
        self.__enemy_group = pygame.sprite.Group()
        self.__enemy_group.add(self)
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
        # Ataques
        self.__is_attacking = False
        self.__last_attack_time = 0
        self.__attack_cooldown = 2000
        self.__player = player
        # Disparos
        self.__bullet_group = pygame.sprite.Group()
        self.__is_ready = True
        self.__bullet_current_time = 0
        self.__bullet_cooldown = 1000

    @property
    def get_enemy_rect(self):
        return self.rect

    @property
    def get_enemy_group(self):
        return self.__enemy_group

    @property
    def get_enemy_bullet_group(self):
        return self.__bullet_group  
    


    def constraint(self):  # Ajusta al jugador a los limites de la pantalla
        if self.__enemy_is_looking_right and self.is_alive:
            if self.rect.right < self.__max_x_constraint:    
                self.rect.x += self.__walk
            else:
                self.__enemy_is_looking_right = False
        else:
            if self.rect.left >= self.__min_x_constraint:         
                self.rect.x -= self.__walk
            else:
                self.__enemy_is_looking_right = True

    
    def do_movement(self, delta_ms):
        if self.is_alive:
            self.__enemy_move_time += delta_ms
            if self.__is_attacking:
                current_time = pygame.time.get_ticks()
                if current_time - self.__last_attack_time >= self.__attack_cooldown:
                    self.__is_attacking = False

            if not self.__is_attacking and self.__enemy_move_time >= self.__frame_rate:
                self.constraint()

    
    def attack(self):
        if self.is_alive and self.rect.colliderect(self.__player.get_player_rect):
            self.__is_attacking = True
            self.hit_player_check(self.__is_attacking)
            self.__last_attack_time = pygame.time.get_ticks()
            self.__initial_frame = 0
        elif self.is_alive:
            self.__is_attacking = False
            self.hit_player_check(self.__is_attacking)


    def hit_player_check(self, check):
        self.__player.hit_check(check)
        self.__player.move_back(50)


    def shot_bullet(self):
        self.__bullet_group.add(self.create_bullet())


    def create_bullet(self):
        return Bullet("hatchet", self.rect.centerx, self.rect.centery - 10, 30, "Right" if self.__enemy_is_looking_right else "Left", self.__frame_rate)

    
    def shot_cooldown(self):
        if not self.__is_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.__bullet_current_time >= self.__bullet_cooldown:
                self.__is_ready = True
    

    def shoot_is_ready(self):
        if self.__is_ready and self.is_alive:
            self.shot_bullet()
            self.__is_ready = False
            self.__bullet_current_time = pygame.time.get_ticks()    


    def update_bullets(self, screen: pygame.surface.Surface, delta_ms):
        for bullet in self.__bullet_group.sprites():
            bullet.update(screen, delta_ms)


    def do_animation(self, delta_ms):
        if self.is_alive:
            self.__enemy_animation_time += delta_ms

            if self.__is_attacking:
                self.attack_animation()
            else:
                self.walk_animation()
        else:
            self.__enemy_animation_time += delta_ms
            if self.__enemy_animation_time >= self.__frame_rate:
                self.__enemy_animation_time = 0

                self.__actual_animation = self.__death_r if self.__enemy_is_looking_right else self.__death_l
                if self.__initial_frame < len(self.__actual_animation) - 1:
                    self.__initial_frame += 1
                else:
                    self.__initial_frame = 4
        

    def walk_animation(self):
        self.__actual_animation = self.__walk_r if self.__enemy_is_looking_right else self.__walk_l
        if self.__enemy_animation_time >= self.__frame_rate:
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0


    def attack_animation(self):
        self.__actual_animation = self.__attack_r if self.__enemy_is_looking_right else self.__attack_l
        if self.__enemy_animation_time >= self.__attack_framerate:
            #self.__actual_animation = self.__attack_r if self.__enemy_is_looking_right else self.__attack_l
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__is_attacking = False
                self.__actual_animation = self.__walk_r if self.__enemy_is_looking_right else self.__walk_l
                self.__initial_frame = 0


    def update(self, delta_ms, screen: pygame.surface.Surface):
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.shot_cooldown()
        self.shoot_is_ready()
        self.update_bullets(screen, delta_ms)
        self.draw_enemy(screen)

    
    def draw_enemy(self, screen: pygame.surface.Surface,):
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.rect)
        #self.__bullet_group.draw(screen)