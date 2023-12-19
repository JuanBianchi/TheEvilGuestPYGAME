import pygame
from models.auxiliar.open_configs import open_configs
from models.player.main_player import Jugador
from models.enemy.enemy import Enemy
from models.bullet.bullet import Bullet
from models.platform.platforms import Platform
from models.traps.traps import Traps
from models.items.items import Item
from models.items.coins import Coin
from models.items.life import Life
from clock.timer import Timer


class Stage():
    def __init__(self, screen: pygame.surface.Surface, current_stage) -> None:
        pygame.mixer.init()
        self.__current_stage_key = current_stage
        self.config = open_configs().get(self.__current_stage_key)
        self.__screen = screen
        self.__background = pygame.image.load(self.config.get('background_img'))
        pygame.mixer.music.load(self.config.get('stage_music'))
        pygame.mixer.music.set_volume(0.09)
        pygame.mixer.music.play(-1)
        self.__player_configs = self.config.get('player')
        self.player = Jugador(self.__player_configs.get('coords')[0]["coord_x"], 
                                self.__player_configs.get('coords')[0]["coord_y"],
                                self.__player_configs.get('frame_rate'),
                                self.__player_configs.get('walk_speed'),
                                self.__player_configs.get('run_speed'),
                                self.__player_configs.get('gravity'),
                                self.__player_configs.get('jump'),
                                self.__player_configs.get('lifes'),
                                self.__player_configs.get('total_lifes'),
                                self.__player_configs.get('shoot_cooldown'),
                                self.__player_configs.get('max_jumps'))
        
        self.__enemy_configs = self.config.get('enemy')        
        self.__bullet_configs = self.config.get('bullet')
        self.__platform_configs = self.config.get('platform')
        self.__stage_configs = self.config.get('stage')
        self.__traps_configs = self.config.get('traps')
        self.__floors_configs = self.config.get('floor')
        self.__coins_configs = self.config.get('coins')
        self.__lifes_configs = self.config.get('lifes')

        self.__coin_sound = pygame.mixer.Sound('./src/assets/sounds/items/coins/RE4 pesetas sound.wav')
        self.__life_sound = pygame.mixer.Sound('./src/assets/sounds/items/lifes/RE4 herb sound.wav')
        self.__stage_won = pygame.mixer.Sound('./src/assets/sounds/stage/Victory fanfare.wav')


        self.__platforms = list()
        self.create_platforms()

        self.__enemies = list()
        self.create_enemies()

        self.__traps = list()
        self.create_traps()

        self.__floors = list()
        self.create_floor()

        self.__coins = list()
        self.create_coins()

        self.__lifes = list()
        self.create_lifes()


    @property
    def get_current_stage(self):
        return self.__current_stage_key
    
    @get_current_stage.setter
    def set_current_stage(self, stage):
        self.__current_stage_key = stage

    @property
    def get_platforms(self):
        return self.__platforms

    @property
    def get_enemies(self):
        return self.__enemies

    @property
    def get_traps(self):
        return self.__traps
    
    @property
    def get_floors(self):
        return self.__floors
    
    @property
    def get_coins(self):
        return self.__coins
    
    @property
    def get_lifes(self):
        return self.__lifes
    

    def set_background(self):
        self.__background = pygame.transform.scale(self.__background, (800, 600))
        self.__screen.blit(self.__background, (0, 0))


    def create_floor(self):
        for i in range(self.__stage_configs.get('max_amount_floors')):
            self.__floors.append(Platform(self.__floors_configs.get('floor_img_path'),
                                         self.__stage_configs.get('coords_floors')[i]['coord_x'],
                                         self.__stage_configs.get('coords_floors')[i]['coord_y'], 
                                         self.__floors_configs.get('width'),
                                         self.__floors_configs.get('height')))
            
    def spawn_floors(self):
        for floor in self.__floors:
            floor.update(self.__screen)
                                          

    def create_platforms(self):
        for i in range(self.__stage_configs.get('max_amount_platforms')):
            self.__platforms.append(Platform(self.__platform_configs.get('platform_img_path'),
                                            self.__stage_configs.get('coords_platforms')[i]['coord_x'],
                                            self.__stage_configs.get('coords_platforms')[i]['coord_y'],
                                             self.__stage_configs.get('platform_measurements')[i]['width'],
                                            self.__stage_configs.get('platform_measurements')[i]['height']))
            
    def spawn_platform(self):
        for platform in self.__platforms:
            platform.update(self.__screen)
    

    def create_enemies(self):
        for i in range(self.__stage_configs.get('max_amount_enemies')):
            self.__enemies.append(Enemy(self.__enemy_configs.get('type'),
                                        self.__stage_configs.get('coords_enemies')[i]['coord_x'],
                                        self.__stage_configs.get('coords_enemies')[i]['coord_y'],
                                        self.__enemy_configs.get('frame_rate'),
                                        self.__enemy_configs.get('walk_speed'),
                                        self.__enemy_configs.get('run_speed'),
                                        self.__enemy_configs.get('gravity'),
                                        self.__platforms[i].get_platform_right_border.right,
                                        self.__platforms[i].get_platform_left_border.left,
                                        self.__enemy_configs.get('walk_img_path'),
                                        self.__enemy_configs.get('attack_img_path'),
                                        self.__enemy_configs.get('death_img_path'),
                                        self.__enemy_configs.get('iddle_img_path'),
                                        self.__enemy_configs.get('walk_img_cols'),
                                        self.__enemy_configs.get('attack_img_cols'),
                                        self.__enemy_configs.get('death_img_cols'),
                                        self.__enemy_configs.get('iddle_img_cols'),
                                        self.player,
                                        self.__enemy_configs.get('health'),
                                        self.__enemy_configs.get('kill_points')
                                        ))


    def create_traps(self):
        for i in range(self.__stage_configs.get('max_amount_traps')):
            self.__traps.append(Traps(self.__traps_configs.get('trap_img_path'),
                                      self.__stage_configs.get('coords_trap')[i]['coord_x'],
                                      self.__stage_configs.get('coords_trap')[i]['coord_y'],
                                      self.__traps_configs.get('width'),
                                      self.__traps_configs.get('height'),
                                      self.__stage_configs.get('trap_type'),
                                      self.__traps_configs.get('frame_rate')
                                      ))
            
    def spawn_traps(self, delta_ms):
        for trap in self.__traps:
            trap.update(self.__screen, delta_ms)

    
    def create_coins(self):
        for i in range(self.__stage_configs.get('max_amount_coins')):
            self.__coins.append(Coin(self.__coins_configs.get('type'),
                                    self.__coins_configs.get('sub_type'),
                                    self.__coins_configs.get('name'),
                                    self.__stage_configs.get('coords_coins')[i]['coord_x'],
                                    self.__stage_configs.get('coords_coins')[i]['coord_y'],
                                    self.__coins_configs.get('width'),
                                    self.__coins_configs.get('height'),
                                    self.__coins_configs.get('img_columns'),
                                    self.__coins_configs.get('img_rows'),
                                    self.__coins_configs.get('frame_rate'),
                                    self.__coins_configs.get('points')
                                    ))


    def spawn_coins(self, delta_ms):
        for coin in self.__coins:
            coin.get_coins_group.update(self.__screen, delta_ms)
            

    def create_lifes(self):
        for i in range(self.__stage_configs.get('max_amount_lifes')):
            self.__lifes.append(Life(self.__lifes_configs.get('type'),
                                    self.__lifes_configs.get('sub_type'),
                                    self.__lifes_configs.get('name'),
                                    self.__stage_configs.get('coords_lifes')[i]['coord_x'],
                                    self.__stage_configs.get('coords_lifes')[i]['coord_y'],
                                    self.__lifes_configs.get('width'),
                                    self.__lifes_configs.get('height'),
                                    self.__lifes_configs.get('img_columns'),
                                    self.__lifes_configs.get('img_rows'),
                                    self.__lifes_configs.get('frame_rate'),
                                    self.__lifes_configs.get('value')
                                    ))

    
    def spawn_lifes(self, delta_ms):    
        for life in self.__lifes:
            life.get_lifes_group.update(self.__screen, delta_ms)


    def check_enemies(self, screen, delta_ms):
        for enemy in self.get_enemies:
            enemy.update(delta_ms, screen)
            if pygame.sprite.spritecollide(enemy, self.player.get_bullets, True) and enemy.get_is_alive_status:
                #AGREGAR EFECTO DE SONIDO
                print("Le pegaste")
                enemy.reduce_health(self.player.get_bullet_damage)
                #enemy.is_alive = False
                if not enemy.get_is_alive_status and not enemy.get_has_been_counted:
                    self.player.set_total_points += enemy.get_enemy_kill_points
                    enemy.set_has_been_counted = True


            if pygame.sprite.spritecollide(self.player, enemy.get_enemy_group, False) and enemy.get_is_alive_status:
                # SI EL JUGADOR MUERE, MOSTRAR PANTALLA DE 'YOU ARE DEAD'.
                enemy.attack()
                self.player.reduce_lifes()
            
            for bullet in enemy.get_enemy_bullet_group:
                if pygame.sprite.collide_rect(bullet, self.player):
                    # SI EL JUGADOR MUERE, MOSTRAR PANTALLA DE 'YOU ARE DEAD'.
                    print("Me pegó")
                    self.player.reduce_lifes()
                    bullet.kill()
        
        
    def check_traps(self):
        for trap in self.get_traps:
            if pygame.sprite.collide_rect(self.player, trap):
                print("Estoy en la trampa")
                self.player.reduce_lifes()
                # JUGADOR MUERE. SE LE DESCUENTAN TODAS LAS VIDAS, MOSTRAR PANTALLA DE 'YOU ARE DEAD'.


    def check_coins(self):
        for coin in self.get_coins:
            if pygame.sprite.spritecollide(self.player, coin.get_item_group, True):
                print("Colisión con moneda detectada")
                self.__coin_sound.play()
                self.player.set_total_points += coin.get_points
                print(f"Total points: {self.player.get_total_points}")


    def check_lifes(self):
        for life in self.get_lifes:
            if pygame.sprite.collide_rect(life, self.player):
                if self.player.get_player_lifes < self.player.get_player_max_lifes:
                    life.kill()
                    self.player.set_player_lifes += life.get_extra_life
                    self.__life_sound.play()
                elif self.player.get_player_lifes == self.player.get_player_max_lifes:
                    pass


    def play_stage_music(self):
        self.background_music = pygame.mixer.Sound(self.config.get('stage_music'))
        self.background_music.play(-1)
        self.background_music.set_volume(0.1)


    def check_stage_win(self):
        rtn = None
        if len(self.__enemies) == 0:
            print("You killed them all!")
            rtn = True
        else:
            rtn = False

        return rtn