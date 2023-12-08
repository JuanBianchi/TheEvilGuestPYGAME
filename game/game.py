import pygame
from models.stage.stage import Stage
from clock.timer import Timer
from constantes import *

class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
        self.clock = pygame.time.Clock()
        self.timer = Timer(100)
        self.enemy_timer = Timer(3)
        self.stage_transition_timer = Timer(5)
        self.font = pygame.font.Font("./assets/fonts/FontsFree-Net-Horrorfind.ttf", 36)
        self.running = True
        self.current_stage_key = 'stage_1'
        self.stage = Stage(self.screen, self.current_stage_key)

    def run(self):
        while self.running:
            self.handle_events()
            delta_ms = self.clock.tick(FPS)
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
                if self.stage.check_stage_win() and self.stage.player.get_is_alive_status:
                    self.stage_transition_timer_update(delta_ms/1000)
                    if self.stage_transition_timer.is_expired():
                        self.stage.set_current_stage = 'stage_2'
                        print(self.stage.get_current_stage)
                        self.timer.reset()
                        self.stage = Stage(self.screen, 'stage_2')
            elif self.stage.get_current_stage == 'stage_2':
                if self.stage.check_stage_win():
                    self.stage_transition_timer_update(delta_ms/1000)
                    if self.stage_transition_timer.is_expired():
                        self.stage.set_current_stage = 'stage_3'
                        print(self.stage.get_current_stage)
                        self.timer.reset()
                        self.stage = Stage(self.screen, 'stage_3')
        
        pygame.mixer.music.stop()
        pygame.quit()


    def handle_events(self):
        events= pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                print("CERRANDO EL JUEGO")
                self.running = False


    def update_player(self, delta_ms):
        self.stage.player.update(delta_ms)


    def update_timer(self, delta_ms):
        self.timer.update(delta_ms)
        if self.timer.is_expired():
            print("Tiempo agotado, perdiste.")
            self.running = False


    def enemy_timer_update(self, delta_ms):
        self.enemy_timer.update(delta_ms)

    def stage_transition_timer_update(self, delta_ms):
        self.stage_transition_timer.update(delta_ms)


    def pause_game(self):
        pass


    def blit(self, delta_ms, screen):
        self.stage.set_background()
        self.stage.spawn_floors()
        self.stage.spawn_platform()
        self.stage.spawn_coins(delta_ms)
        self.stage.spawn_traps(delta_ms)
        self.stage.spawn_lifes(delta_ms)
        if self.stage.get_current_stage == "stage_1":
            moving_platform = self.stage.get_platforms[4]
            moving_platform.move_platform_up_down(5)
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