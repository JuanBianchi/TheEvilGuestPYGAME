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


class Stage():
    def __init__(self, screen: pygame.surface.Surface, stage: str) -> None:
        self.config = open_configs().get(stage)
        self.__screen = screen
        self.__background = pygame.image.load(self.config.get('background_img'))
        #self.__bgm = self.set_background_music() 
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
                                self.__player_configs.get('max_jumps'))
        
        self.__enemy_configs = self.config.get('enemy')        
        self.__bullet_configs = self.config.get('bullet')
        self.__platform_configs = self.config.get('platform')
        self.__stage_configs = self.config.get('stage')
        self.__traps_configs = self.config.get('traps')
        self.__floors_configs = self.config.get('floor')
        self.__coins_configs = self.config.get('coins')
        self.__lifes_configs = self.config.get('lifes')


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
                #AGREGAR EFECTO DE SONIDO
                enemy.attack()
                self.player.reduce_lifes()
                print(self.player.get_player_lifes)
                # EN REALIDAD TIENE QUE RESTARSELE UNA VIDA AL JUGADOR
            for bullet in enemy.get_enemy_bullet_group:
                if pygame.sprite.collide_rect(bullet, self.player):
                    # SI EL JUGADOR MUERE, MOSTRAR PANTALLA DE 'YOU ARE DEAD'.
                    #AGREGAR EFECTO DE SONIDO
                    print("Me pegó")
                    self.player.reduce_lifes()
                    print(self.player.get_player_lifes)
                    bullet.kill()

    
    def check_traps(self):
        for trap in self.get_traps:
            if pygame.sprite.collide_rect(self.player, trap):
                print("Estoy en la trampa")
                self.player.reduce_lifes()
                # JUGADOR MUERE. SE LE DESCUENTAN TODAS LAS VIDAS.


    def check_coins(self):
        for coin in self.get_coins:
            if pygame.sprite.spritecollide(self.player, coin.get_item_group, True):
                print("Colisión con moneda detectada")
                #AGREGAR EFECTO DE SONIDO
                self.player.set_total_points += coin.get_points
                print(f"Total points: {self.player.get_total_points}")


    def check_lifes(self):
        for life in self.get_lifes:
            if pygame.sprite.collide_rect(life, self.player):
                if self.player.get_player_lifes < self.player.get_player_max_lifes:
                    self.player.set_player_lifes += life.get_extra_life
                    life.kill()
                elif self.player.get_player_lifes == self.player.get_player_max_lifes:
                    pass


    def check_stage_win(self):
        if self.__enemies == 0:
            print("Juego terminado")

    
