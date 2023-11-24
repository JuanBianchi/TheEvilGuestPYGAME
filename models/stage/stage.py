import pygame
from models.auxiliar.open_configs import open_configs
from models.player.main_player import Jugador
from models.enemy.enemy import Enemy
from models.platform.platforms import Platform

class Stage():
    def __init__(self, screen: pygame.surface.Surface, stage: str) -> None:
        self.config = open_configs().get(stage)
        self.__screen = screen
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

        self.__platforms_list = list()
        self.create_platforms()

    @property
    def get_platforms(self):
        return self.__platforms_list


    def create_platforms(self):
        for i in range(self.__stage_configs.get('max_amount_platforms')):
            self.__platforms_list.append(Platform(self.__platform_configs.get('platform_img_path'),
                                             self.__stage_configs.get('coords_platforms')[i]['coord_x'],
                                             self.__stage_configs.get('coords_platforms')[i]['coord_y'],
                                             200,
                                             20))
            
    def platform(self):
        for platform in self.__platforms_list:
            platform.update(self.__screen)

    
    # def player_platform_collision_x(self):
    #     #player_sprites = self.player.get_player_group.sprites()

    #     for platform in self.__platforms_list:
    #         for sprite in platform.get_platform_group.sprites():
    #             if sprite.rect.colliderect(self.player.rect):
    #                 if self.player.rect.x < 0:
    #                     self.player.rect.left = sprite.rect.right
    #                 elif self.player.rect.x > 0:
    #                     self.player.rect.right = sprite.rect.left


    # def player_platform_collision_y(self):
    #     #player_sprites = self.player.get_player_group.sprites()

    #     for platform in self.__platforms_list:
    #         for sprite in platform.get_platform_group.sprites():
    #             if sprite.rect.colliderect(self.player.rect):
    #                 if self.player.rect.y < 0:
    #                     self.player.rect.bottom = sprite.rect.top
    #                 elif self.player.rect.y > 0:
    #                     self.player.rect.top = sprite.rect.bottom                

