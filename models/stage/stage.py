import pygame
from models.auxiliar.open_configs import open_configs
from models.player.main_player import Jugador
from models.enemy.enemy import Enemy
from models.bullet.bullet import Bullet
from models.platform.platforms import Platform
from models.traps.traps import Traps

class Stage():
    def __init__(self, screen: pygame.surface.Surface, stage: str) -> None:
        self.config = open_configs().get(stage)
        self.__screen = screen
        self.__background = pygame.image.load(self.config.get('background_img'))
        self.__player_configs = self.config.get('player')
        self.player = Jugador(self.__player_configs.get('coords')[0]["coord_x"], 
                                self.__player_configs.get('coords')[0]["coord_y"],
                                self.__player_configs.get('frame_rate'),
                                self.__player_configs.get('walk_speed'),
                                self.__player_configs.get('run_speed'),
                                self.__player_configs.get('gravity'),
                                self.__player_configs.get('jump'),
                                self.__player_configs.get('max_jumps'))
        

        self.__enemy_configs = self.config.get('enemy')        
        self.__bullet_configs = self.config.get('bullet')
        self.__platform_configs = self.config.get('platform')
        self.__stage_configs = self.config.get('stage')
        self.__traps_configs = self.config.get('traps')
        self.__floors_configs = self.config.get('floor')

        self.__platforms = list()
        self.create_platforms()

        self.__enemies = list()
        self.create_enemies()

        self.__traps = list()
        self.create_traps()

        self.__floors = list()
        self.create_floor()


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
    

    def set_background(self):
        self.__background = pygame.transform.scale(self.__background, (800, 600))
        self.__screen.blit(self.__background, (0, 0))


    def create_floor(self):
        for i in range(self.__stage_configs.get('max_amount_floors')):
            self.__floors.append(Platform(self.__platform_configs.get('platform_img_path'),
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
                                        self.player))
            


    def create_traps(self):
        for i in range(self.__stage_configs.get('max_amount_traps')):
            self.__traps.append(Traps(self.__traps_configs.get('trap_img_path'),
                                      self.__stage_configs.get('coords_trap')[i]['coord_x'],
                                      self.__stage_configs.get('coords_trap')[i]['coord_y'],
                                      self.__traps_configs.get('width'),
                                      self.__traps_configs.get('height'),
                                      self.__traps_configs.get('trap_type'),))
            
    def spawn_traps(self):
        for trap in self.__traps:
            trap.update(self.__screen)
            