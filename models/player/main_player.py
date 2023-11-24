import pygame as pg
from models.auxiliar.surface_manager import SurfaceManager as sfm
from models.bullet.bullet import Bullet
#from models.platform.platforms import Platform
from constantes import ANCHO_VENT, SHOT_COOLDOWN, DEBUG

class Jugador(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y, frame_rate, speed_walk = 6, speed_run = 12, gravity = 16, jump = 12, max_jumps = 1) -> None:
        super().__init__()
        self.__iddle_r = sfm.get_surface_from_spritesheet("./assets/img/player/iddle/leoniddle.png", 6, 1)
        self.__iddle_l = sfm.get_surface_from_spritesheet("./assets/img/player/iddle/leoniddle.png", 6, 1, flip=True)
        self.__walk_r = sfm.get_surface_from_spritesheet("./assets/img/player/walk/leonwalk.png", 8, 1)
        self.__walk_l = sfm.get_surface_from_spritesheet("./assets/img/player/walk/leonwalk.png", 8, 1, flip=True)
        self.__run_r = sfm.get_surface_from_spritesheet("./assets/img/player/run/leonrun.png", 8, 1)
        self.__run_l = sfm.get_surface_from_spritesheet("./assets/img/player/run/leonrun.png", 8, 1, flip=True)
        self.__jump_r = sfm.get_surface_from_spritesheet("./assets/img/player/jump/leonjump.png", 4, 1)
        self.__jump_l = sfm.get_surface_from_spritesheet("./assets/img/player/jump/leonjump.png", 4, 1, flip=True)
        self.__shoot_r = sfm.get_surface_from_spritesheet("./assets/img/player/shoot/leonshoot.png", 2, 1)
        self.__shoot_l = sfm.get_surface_from_spritesheet("./assets/img/player/shoot/leonshoot.png", 2, 1, flip=True)
        self.__speed_walk = speed_walk
        self.__speed_run = speed_run
        self.__frame_rate = frame_rate
        self.__player_move_time = 0
        self.__player_animation_time = 0
        self.__gravity = gravity
        self.__jump = jump
        self.__max_jumps = max_jumps
        self.__remaining_jumps = self.__max_jumps
        self.__is_jumping = False
        self.__is_still = True
        self.__initial_frame = 0
        self.__actual_animation = self.__iddle_r
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        self.rect = self.__actual_img_animation.get_rect()
        self.rect.x = coord_x
        self.rect.y = coord_y
        self.__player_group = pg.sprite.Group()
        self.__is_looking_right = True
        #Disparos
        self.__bullet_group = pg.sprite.Group()
        self.__is_ready = True
        self.__bullet_current_time = 0
        self.__bullet_cooldown = SHOT_COOLDOWN
        #Colisiones
        self.__is_on_platform = True
        # self.__puntaje


    @property
    def is_looking_right(self):
        return self.__is_looking_right

    @property
    def get_player_rect(self):
        return self.rect

    @property
    def get_bullets(self) -> pg.sprite.Group:
        return self.__bullet_group
    
    @property
    def get_player_group(self) -> pg.sprite.Group:
        return self.__player_group

    @property
    def get_player_group(self) -> pg.sprite.Group:
        return self.__player_group
    
    def __set_x_animations_preset(self, move_x, animation_list: list[pg.surface.Surface], look_r: bool):
        self.rect.x += move_x
        self.__actual_animation = animation_list
        self.__is_looking_right = look_r


    def __set_y_animations_preset(self):
        self.rect.y -= self.__jump
        self.__actual_animation = self.__jump_r if self.__is_looking_right else self.__jump_l
        self.__initial_frame = 0
        self.__is_jumping = True


    def walk(self, direction: str = 'Right'):
        match direction:
            case 'Right':
                look_right = True
                self.__set_x_animations_preset(self.__speed_walk, self.__walk_r, look_r=look_right)
            case 'Left':
                look_right = False
                self.__set_x_animations_preset(-self.__speed_walk, self.__walk_l, look_r=look_right)


    def stay(self):
        if self.__actual_animation != self.__iddle_l and self.__actual_animation != self.__iddle_r:
            self.__actual_animation = self.__iddle_r if self.__is_looking_right else self.__iddle_l
            self.__initial_frame = 0
            

    def run(self, direction: str = 'Right'):
            #self.__initial_frame = 0
            match direction:
                case 'Right':
                    look_right = True
                    self.__set_x_animations_preset(self.__speed_run, self.__run_r, look_r=look_right)
                case 'Left':
                    look_right = False
                    self.__set_x_animations_preset(-self.__speed_run, self.__run_l, look_r=look_right)

    
    def jump(self, jumping=True):
        if jumping and self.__remaining_jumps > 0 and not self.__is_jumping:
            self.__set_y_animations_preset()
            self.__is_jumping = True
            self.__remaining_jumps -= 1
        elif not self.__is_jumping:
            self.__is_jumping = False
            self.stay()

    
    def shoot(self, direction: str = 'Right'):
        if self.__is_still:
            match direction:
                case 'Right':
                    look_right = True
                    self.__set_x_animations_preset(0, self.__shoot_r, look_r=look_right)
                    self.__bullet_group.add(self.create_bullet())
                case 'Left':
                    look_right = False
                    self.__set_x_animations_preset(0, self.__shoot_l, look_r=look_right)
                    self.__bullet_group.add(self.create_bullet())


    def get_inputs(self):
        events_list = pg.event.get()
        for event in events_list:
            match event.type:
                case pg.KEYDOWN:
                    if event.key == pg.K_SPACE: #and player.__is_running
                        self.jump(True)
                case pg.KEYUP:
                    if event.key == pg.K_SPACE:
                        self.jump(False)
                

        # Esto hacerlo en un metodo de la clase Player que asigne las teclas.
        key_pressed_list = pg.key.get_pressed()
        if key_pressed_list[pg.K_d] and not key_pressed_list[pg.K_a]:
            self.walk('Right')
        if key_pressed_list[pg.K_a] and not key_pressed_list[pg.K_d]:
            self.walk('Left')
        if not key_pressed_list[pg.K_a] and not key_pressed_list[pg.K_d]:
            self.stay()
        if key_pressed_list[pg.K_d] and key_pressed_list[pg.K_LSHIFT] and not key_pressed_list[pg.K_a]:
            self.run('Right')
        if key_pressed_list[pg.K_a] and key_pressed_list[pg.K_LSHIFT] and not key_pressed_list[pg.K_d]:
            self.run('Left')
        if key_pressed_list[pg.K_f] and self.is_looking_right and self.__is_ready:
            self.shoot('Right')
            self.__is_ready = False
            self.__bullet_current_time = pg.time.get_ticks()
        if key_pressed_list[pg.K_f] and not self.is_looking_right and self.__is_ready:
            self.shoot('Left')
            self.__is_ready = False
            self.__bullet_current_time = pg.time.get_ticks()



    def shot_bullet(self):
        self.__bullet_group.add(self.create_bullet())


    def create_bullet(self):
        return Bullet(self.rect.centerx, self.rect.centery - 10, 50, "Right" if self.__is_looking_right else "Left")

    
    def shot_cooldown(self):
        if not self.__is_ready:
            current_time = pg.time.get_ticks()
            if current_time - self.__bullet_current_time >= self.__bullet_cooldown:
                self.__is_ready = True


    def __set_x_borders_limit(self):
        pixels_move = 0

        if self.rect.left < 0:
            pixels_move = -self.rect.left
        elif self.rect.right > ANCHO_VENT:
            pixels_move = ANCHO_VENT - self.rect.right

        return pixels_move



    def do_movement(self, delta_ms):
        self.__player_move_time += delta_ms
        if self.__player_move_time >= self.__frame_rate:
            self.__player_move_time = 0
            self.rect.x += self.__set_x_borders_limit()
            #self.rect.y += self.__gravity
            if self.rect.y < 400:
                self.rect.y += self.__gravity
            
            if self.__is_jumping:
                self.rect.y -= self.__jump
                if self.rect.y <= 0:
                    self.__is_jumping = False
    

    def do_animation(self, delta_ms):
        self.__player_animation_time += delta_ms
        if self.__player_animation_time >= self.__frame_rate:
            self.__player_animation_time = 0
            if not self.__is_jumping:
                if self.__initial_frame < len(self.__actual_animation) - 1:
                    self.__initial_frame += 1
                else:
                    self.__initial_frame = 0
            else:
                self.__actual_animation = self.__jump_r if self.__is_looking_right else self.__jump_l
                if self.__initial_frame < len(self.__actual_animation) - 1:
                    self.__initial_frame += 1
                else:
                    self.__initial_frame = 0
                    self.__is_jumping = False
                    

    def check_platform_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.get_platform_area):
                # Aquí puedes manejar las acciones que ocurren cuando hay colisión
                # Por ejemplo, detener el salto, ajustar la posición del jugador, etc.
                self.rect.y = platform.get_platform_area.top - self.rect.height
                self.__remaining_jumps = self.__max_jumps  # Reiniciar los saltos
                self.__is_jumping = False
            # SEGUIR. SI COLISIONA CON EL BOTTOM DE LA PLATAFORMA, QUE NO SUBA. LO MISMO CON EL LEFT Y EL RIGHT DE LA PLATAFORMA 


    def update(self, delta_ms):
        self.get_inputs()
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.shot_cooldown()

        if self.rect.y >= 400: # Si toca el '''suelo'''
            self.__remaining_jumps = self.__max_jumps

    def draw_player(self, screen: pg.surface.Surface):
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.rect)
        