import pygame
from models.stage.stage import Stage
from constantes import *

screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
pygame.init()
clock = pygame.time.Clock()

running = True

bg_color = (144, 210, 120)


stage = Stage(screen, 'stage_1')


while True:
    events_list = pygame.event.get()
    for event in events_list:
        match event.type:
            case pygame.QUIT:
                    print("CERRANDO EL JUEGO")
                    running = False
                    break
             
    screen.fill(bg_color)
    delta_ms = clock.tick(FPS)

    stage.player.update(delta_ms)
    for enemy in stage.get_enemies:
        enemy.update(delta_ms, screen)
        if pygame.sprite.spritecollide(enemy, stage.player.get_bullets, True) and enemy.is_alive:
            print("Le pegaste")
            enemy.is_alive = False
        if pygame.sprite.collide_rect(stage.player, enemy):
            print("Me esta pegando")
            # EN REALIDAD TIENE QUE RESTARSELE UNA VIDA AL JUGADOR
    stage.spawn_platform()
    stage.player.check_platform_collision(stage.get_platforms)
    stage.player.draw_player(screen)
    stage.player.get_bullets.update(screen)
    


    pygame.display.update()

pygame.quit()