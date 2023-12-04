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
        self.font = pygame.font.Font("./assets/fonts/FontsFree-Net-Horrorfind.ttf", 36)
        self.running = True
        self.stage = Stage(self.screen, 'stage_1')


    def run(self):
        while self.running:
            self.handle_events()
            delta_ms = self.clock.tick(FPS)
            self.update_chars(delta_ms)
            self.update_timer(delta_ms/1000)
            self.blit(delta_ms, self.screen)
            pygame.display.update()

        pygame.quit()


    def handle_events(self):
        events= pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                print("CERRANDO EL JUEGO")
                self.running = False


    def update_chars(self, delta_ms):
        self.stage.player.update(delta_ms)


    def update_timer(self, delta_ms):
        self.timer.update(delta_ms)
        if self.timer.is_expired():
            print("Tiempo agotado, perdiste.")
            self.running = False


    def blit(self, delta_ms, screen):
        self.stage.set_background()
        self.stage.spawn_floors()
        self.stage.spawn_platform()
        moving_platform = self.stage.get_platforms[4]
        moving_platform.move_platform_up_down()
        self.stage.spawn_coins(delta_ms)
        self.stage.spawn_traps(delta_ms)
        self.stage.player.check_platform_collision(self.stage.get_floors)
        self.stage.player.check_platform_collision(self.stage.get_platforms)
        self.stage.check_enemies(screen, delta_ms)
        self.stage.check_traps()
        self.stage.check_coins()
        self.stage.player.draw_player(screen)
        self.stage.player.get_bullets.update(self.screen, delta_ms)

        time_text = f"Time: {self.timer.get_remaining_time} s"
        time_text_surface = self.font.render(time_text, True, (150, 0, 0))
        self.screen.blit(time_text_surface, (10, 10))

        score_text = "{}Score: {}".format('\t' * 8, self.stage.player.get_total_points)
        score_text_surface = self.font.render(score_text, True, (150, 0, 0))
        self.screen.blit(score_text_surface, (10, 10))