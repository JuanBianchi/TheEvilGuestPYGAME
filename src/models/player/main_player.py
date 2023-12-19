import pygame as pg
from models.auxiliar.surface_manager import SurfaceManager as sfm
from models.bullet.bullet import Bullet
#from models.platform.platforms import Platform
from constantes import ANCHO_VENT, ALTO_VENT, ALTURA_MAX_SALTO, SHOT_COOLDOWN, DEBUG


class Jugador(pg.sprite.Sprite):
    def __init__(self, coord_x, coord_y, frame_rate, speed_walk, speed_run, gravity, jump, lifes, total_lifes, shot_cooldown, max_jumps = 1) -> None:
        super().__init__()
        pg.mixer.init()
        self.__iddle_r = sfm.get_surface_from_spritesheet("./src/assets/img/player/iddle/leoniddle.png", 6, 1)
        self.__iddle_l = sfm.get_surface_from_spritesheet("./src/assets/img/player/iddle/leoniddle.png", 6, 1, flip=True)
        self.__walk_r = sfm.get_surface_from_spritesheet("./src/assets/img/player/walk/leonwalk.png", 8, 1)
        self.__walk_l = sfm.get_surface_from_spritesheet("./src/assets/img/player/walk/leonwalk.png", 8, 1, flip=True)
        self.__run_r = sfm.get_surface_from_spritesheet("./src/assets/img/player/run/leonrun.png", 8, 1)
        self.__run_l = sfm.get_surface_from_spritesheet("./src/assets/img/player/run/leonrun.png", 8, 1, flip=True)
        self.__jump_r = sfm.get_surface_from_spritesheet("./src/assets/img/player/jump/leonjump.png", 4, 1)
        self.__jump_l = sfm.get_surface_from_spritesheet("./src/assets/img/player/jump/leonjump.png", 4, 1, flip=True)
        self.__shoot_r = sfm.get_surface_from_spritesheet("./src/assets/img/player/shoot/leonshoot.png", 2, 1)
        self.__shoot_l = sfm.get_surface_from_spritesheet("./src/assets/img/player/shoot/leonshoot.png", 2, 1, flip=True)
        self.__death_r = sfm.get_surface_from_spritesheet("./src/assets/img/player/death/leondeath.png", 6, 1)
        self.__death_l = sfm.get_surface_from_spritesheet("./src/assets/img/player/death/leondeath.png", 6, 1, flip=True)
        self.death_sound = pg.mixer.Sound("./src/assets/sounds/player/death/Leon Death Sound.wav")
        self.__speed_walk = speed_walk
        self.__speed_run = speed_run
        self.__frame_rate = frame_rate
        self.__player_move_time = 0
        self.__player_animation_time = 0
        self.__gravity = gravity
        self.__jump = jump
        self.__lifes = lifes
        self.__max_lifes = total_lifes
        self.__max_jumps = max_jumps
        self.__remaining_jumps = self.__max_jumps
        self.__is_alive = True
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
        self.__bullet_cooldown = shot_cooldown
        self.__bullet_damage = 100
        self.__shot_sound = pg.mixer.Sound("./src/assets/sounds/player/shot/re4 shot sound.wav")
        #Colisiones
        self.__is_on_platform = True
        self.__is_stunned = False
        self.__is_under_attack = False
        self.__attack_duration = 1000
        self.__attack_start_time = 0
        #Puntos
        self.__total_points = 0
    

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
    
    @property
    def get_player_health(self):
        return self.__health
    
    @get_player_health.setter
    def set_player_health(self, new_health):
        self.__health += new_health

    @property
    def get_player_lifes(self):
        return self.__lifes
    

    @get_player_lifes.setter    # Por si agarro un objeto vida
    def set_player_lifes(self, new_life):
        self.__lifes = new_life


    @property
    def get_player_max_lifes(self):
        return self.__max_lifes


    @property
    def get_is_alive_status(self):
        return self.__is_alive
    
    @property
    def get_bullet_damage(self):
        return self.__bullet_damage

    @property
    def get_total_points(self):
        return self.__total_points

    @get_total_points.setter
    def set_total_points(self, points):
        self.__total_points = points

    
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
        if self.__is_alive:
            match direction:
                case 'Right':
                    look_right = True
                    self.__set_x_animations_preset(self.__speed_walk, self.__walk_r, look_r=look_right)
                    self.__is_still = False
                case 'Left':
                    look_right = False
                    self.__set_x_animations_preset(-self.__speed_walk, self.__walk_l, look_r=look_right)
                    self.__is_still = False


    def stay(self):
        if self.__is_alive:
            if self.__actual_animation != self.__iddle_l and self.__actual_animation != self.__iddle_r:
                self.__actual_animation = self.__iddle_r if self.__is_looking_right else self.__iddle_l
                self.__initial_frame = 0
                self.__is_still = True
            

    def run(self, direction: str = 'Right'):
        if self.__is_alive:
            match direction:
                case 'Right':
                    look_right = True
                    self.__set_x_animations_preset(self.__speed_run, self.__run_r, look_r=look_right)
                    self.__is_still = False
                case 'Left':
                    look_right = False
                    self.__set_x_animations_preset(-self.__speed_run, self.__run_l, look_r=look_right)
                    self.__is_still = False

    
    def jump(self, jumping):
        if self.__is_alive:
            if jumping and self.__remaining_jumps > 0 and not self.__is_jumping:
                self.__set_y_animations_preset()
                self.__is_jumping = True
                self.__remaining_jumps -= 1
                self.__is_still = False
            elif not jumping and self.__is_jumping:
                self.__is_jumping = False
                self.stay()
            

    
    def shoot(self, direction: str = 'Right'):
        if self.__is_still and self.__is_alive:
            match direction:
                case 'Right':
                    look_right = True
                    self.__set_x_animations_preset(0, self.__shoot_r, look_r=look_right)
                    self.shot_bullet()
                case 'Left':
                    look_right = False
                    self.__set_x_animations_preset(0, self.__shoot_l, look_r=look_right)
                    self.shot_bullet()
                    


    def get_inputs(self):
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
            self.__shot_sound.play()
            self.__is_ready = False
            self.__bullet_current_time = pg.time.get_ticks()
        if key_pressed_list[pg.K_f] and not self.is_looking_right and self.__is_ready:
            self.shoot('Left')
            self.__shot_sound.play()
            self.__is_ready = False
            self.__bullet_current_time = pg.time.get_ticks()
        if key_pressed_list[pg.K_SPACE]:
            self.jump(True)
        else:
            self.jump(False)


    def hit_check(self, stunned):
        if stunned:
            self.__is_stunned = stunned
            self.is_under_attack = True
            self.attack_start_time = pg.time.get_ticks()


    def move_back(self, pixels):
        if self.__is_alive:
            if self.__is_looking_right and self.__is_stunned:
                self.rect.x -= pixels
            elif not self.__is_looking_right and self.__is_stunned:
                self.rect.x += pixels

    
    def under_attack_check(self):
        if self.__is_under_attack:
            current_time = pg.time.get_ticks()
            if current_time - self.__attack_start_time >= self.__attack_duration:
                self.__is_under_attack = False
                self.__attack_start_time = 0


    def shot_bullet(self):
        self.__bullet_group.add(self.create_bullet())


    def create_bullet(self):
        return Bullet("normal", self.rect.centerx, self.rect.centery - 10, 50, "Right" if self.__is_looking_right else "Left", self.__frame_rate)

    
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
        if self.__is_alive:
            self.__player_move_time += delta_ms
            if self.__player_move_time >= self.__frame_rate:
                self.__player_move_time = 0
                self.rect.x += self.__set_x_borders_limit()
                #self.rect.y += self.__gravity
                if self.rect.y < ALTO_VENT:
                    self.rect.y += self.__gravity
                
                if self.__is_jumping:
                    self.rect.y -= self.__jump
                    if self.rect.y <= ALTURA_MAX_SALTO:
                        self.__is_jumping = False

    

    def do_animation(self, delta_ms):
        if self.__is_alive:
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
        else:
            self.__actual_animation = self.__death_r if self.__is_looking_right else self.__death_l
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = len(self.__actual_animation) - 1
                self.__is_alive = False
                    

    def check_platform_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.get_platform_area):
                if self.rect.y < platform.get_platform_area.y:
                    self.rect.y = platform.get_platform_area.top - self.rect.height
                    self.__remaining_jumps = self.__max_jumps  # Reiniciar los saltos
                    self.__is_jumping = False
                elif self.rect.top >= platform.get_platform_area.y:
                    self.rect.y = platform.get_platform_area.bottom
                    self.__is_jumping = False
                
                if self.rect.x < platform.get_platform_area.left:
                    self.rect.right = platform.get_platform_area.left
                elif self.rect.x > platform.get_platform_area.right:
                    self.rect.left = platform.get_platform_area.right


    def reduce_lifes(self):
        if self.__is_alive:
            self.__lifes -= 1
            if self.__lifes <= 0:
                self.__is_alive = False

    def update(self, delta_ms):
        self.get_inputs()
        self.do_movement(delta_ms)
        self.do_animation(delta_ms)
        self.shot_cooldown()
        self.under_attack_check()

        if self.rect.y >= 600:
            self.__remaining_jumps = self.__max_jumps

    def draw_player(self, screen: pg.surface.Surface):
        self.__actual_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__actual_img_animation, self.rect)
        