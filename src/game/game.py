import pygame
from models.stage.stage import Stage
from clock.timer import Timer
from constantes import *
from UI.form_pause import *
from db.ranking import *

class Game:
    def __init__(self, initial_stage = 'stage_1') -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
        self.clock = pygame.time.Clock()
        self.timer = Timer(100)
        self.enemy_timer = Timer(3)
        self.stage_transition_timer = Timer(5)
        self.pause_menu = Pause(self.screen, 100, 100, 100, 200, (130, 130, 130), (0, 0, 0), active=True)
        self.pause_timer = Timer(0)
        self.is_paused = False
        self.font = pygame.font.Font("./src/assets/fonts/FontsFree-Net-Horrorfind.ttf", 36)
        self.__game_over_screen = pygame.image.load("./src/assets/img/background/you are dead RE4.jpg")
        self.__game_over_screen = pygame.transform.scale(self.__game_over_screen, (ANCHO_VENT, ALTO_VENT))
        self.__game_win_screen = pygame.image.load("./src/assets/img/background/game win.png")
        self.__game_win_screen = pygame.transform.scale(self.__game_win_screen, (ANCHO_VENT, ALTO_VENT))
        self.death_transition_timer = Timer(2)
        self.running = True
        self.current_stage_key = initial_stage
        self.stage = Stage(self.screen, self.current_stage_key)

    def run(self):
        while self.running:
            delta_ms = self.clock.tick(FPS)
            self.handle_events()
            if not self.is_paused:
                self.update_player(delta_ms)
                self.update_timer(delta_ms/1000)
                self.blit(delta_ms, self.screen)
                pygame.display.update()

                for enemy in self.stage.get_enemies:
                    if not enemy.get_is_alive_status:
                        self.enemy_timer_update(delta_ms/1000)
                        if self.enemy_timer.is_expired():
                            self.stage.get_enemies.remove(enemy)
                            self.enemy_timer.reset()

                if self.stage.get_current_stage == 'stage_1':
                    if self.stage.player.get_player_lifes == 0:
                        self.death_transition_timer.update(delta_ms/1000)
                        if self.death_transition_timer.is_expired():
                            self.show_game_over_screen()
                            insert_values(input("Ingrese su nombre: "), self.stage.player.get_total_points)
                    if self.stage.check_stage_win() and self.stage.player.get_is_alive_status:
                        self.stage_transition_timer_update(delta_ms/1000)
                        if self.stage_transition_timer.is_expired():
                            self.stage.set_current_stage = 'stage_2'
                            print(self.stage.get_current_stage)
                            self.timer.reset()
                            self.stage = Stage(self.screen, 'stage_2')
                elif self.stage.get_current_stage == 'stage_2':
                    if self.stage.player.get_player_lifes == 0:
                        self.death_transition_timer.update(delta_ms/1000)
                        if self.death_transition_timer.is_expired():
                            self.show_game_over_screen()
                            insert_values(input("Ingrese su nombre: "), self.stage.player.get_total_points)
                    if self.stage.check_stage_win():
                        self.stage_transition_timer_update(delta_ms/1000)
                        if self.stage_transition_timer.is_expired():
                            self.stage.set_current_stage = 'stage_3'
                            print(self.stage.get_current_stage)
                            self.timer.reset()
                            self.stage = Stage(self.screen, 'stage_3')
                elif self.stage.get_current_stage == 'stage_3':
                    if self.stage.player.get_player_lifes == 0:
                        self.death_transition_timer.update(delta_ms/1000)
                        if self.death_transition_timer.is_expired():
                            self.show_game_over_screen()
                            insert_values(input("Ingrese su nombre: "), self.stage.player.get_total_points)
                    if self.stage.check_stage_win():
                        self.show_game_win_screen()
                        insert_values(input("Ingrese su nombre: "), self.stage.player.get_total_points)
                        self.running = False
                
            else:
                self.pause_timer.update(delta_ms/1000)
                pause_font = pygame.font.Font("./src/assets/fonts/FontsFree-Net-Horrorfind.ttf", 72)
                pause_text = "Pause"
                pause_text_surface = pause_font.render(pause_text, True, (155, 0, 0))
                self.screen.blit(pause_text_surface, (350, 250))
                pygame.display.update()
                
            
        pygame.mixer.music.stop()
        pygame.quit()


    def handle_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
                print("CERRANDO EL JUEGO")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.pause_game()
                    
                    


    def update_player(self, delta_ms):
        self.stage.player.update(delta_ms)


    def update_timer(self, delta_ms):
        self.timer.update(delta_ms)
        if self.timer.is_expired():
            print("Tiempo agotado, perdiste.")
            self.show_game_over_screen()
            self.running = False


    def enemy_timer_update(self, delta_ms):
        self.enemy_timer.update(delta_ms)

    def stage_transition_timer_update(self, delta_ms):
        self.stage_transition_timer.update(delta_ms)


    def pause_game(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            pygame.mixer.music.pause()
            self.pause_timer.pause()
        else:
            pygame.mixer.music.unpause()
            self.pause_timer.unpause()


    def show_game_over_screen(self):
        self.screen.blit(self.__game_over_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(3000)
        self.running = False

    def show_game_win_screen(self):
        self.screen.blit(self.__game_win_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(3000)
        pause_font = pygame.font.Font("./src/assets/fonts/FontsFree-Net-Horrorfind.ttf", 72)
        pause_text = "YOU WIN!!"
        pause_text_surface = pause_font.render(pause_text, True, (155, 0, 0))
        self.screen.blit(pause_text_surface, (350, 250))
        pygame.display.update()


    def blit(self, delta_ms, screen):
        self.stage.set_background()
        self.stage.spawn_floors()
        self.stage.spawn_platform()
        self.stage.spawn_coins(delta_ms)
        self.stage.spawn_traps(delta_ms)
        self.stage.spawn_lifes(delta_ms)
        if self.stage.get_current_stage == "stage_1":
            moving_platform = self.stage.get_platforms[4]
            moving_platform.move_platform_up_down(15)
        elif self.stage.get_current_stage == "stage_2":
            moving_platform_1 = self.stage.get_platforms[4]
            moving_platform_2 = self.stage.get_platforms[3]
            moving_platform_1.move_platform_up_down(10)
            moving_platform_2.move_platform_left_right(5)
            moving_trap_1 = self.stage.get_traps[0]
            moving_trap_2 = self.stage.get_traps[1]
            moving_trap_1.move_trap_up_down(15)
            moving_trap_2.move_trap_up_down(15)
        elif self.stage.get_current_stage == "stage_3":
            moving_platform_1 = self.stage.get_platforms[3]
            moving_platform_2 = self.stage.get_platforms[7]
            moving_platform_1.move_platform_up_down(10)
            moving_platform_2.move_platform_up_down(10)


        self.stage.player.check_platform_collision(self.stage.get_floors)
        self.stage.player.check_platform_collision(self.stage.get_platforms)
        self.stage.check_enemies(screen, delta_ms)
        self.stage.check_traps()
        self.stage.check_coins()
        self.stage.check_lifes()
        self.stage.player.draw_player(screen)
        self.stage.player.get_bullets.update(self.screen, delta_ms)

        time_text = f"Time: {self.timer.get_remaining_time} s"
        time_text_surface = self.font.render(time_text, True, (150, 0, 0))
        self.screen.blit(time_text_surface, (10, 10))

        score_text = "{}Score: {}".format('\t' * 8, self.stage.player.get_total_points)
        score_text_surface = self.font.render(score_text, True, (150, 0, 0))
        self.screen.blit(score_text_surface, (10, 10))

        lifes_text = "{}Lifes: {}".format('\t' * 16, self.stage.player.get_player_lifes)
        lifes_text_surface = self.font.render(lifes_text, True, (150, 0, 0))
        self.screen.blit(lifes_text_surface, (10, 10))