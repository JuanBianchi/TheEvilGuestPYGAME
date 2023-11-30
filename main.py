import pygame
from models.stage.stage import Stage
from constantes import *

screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
pygame.init()
clock = pygame.time.Clock()

running = True

bg_color = (144, 210, 120)

stage = Stage(screen, 'stage_1')
moving_platorm = stage.get_platforms[4]

while True:
    stage.set_background()

    events_list = pygame.event.get()
    for event in events_list:
        match event.type:
            case pygame.QUIT:
                    print("CERRANDO EL JUEGO")
                    running = False
                    break
             
    delta_ms = clock.tick(FPS)

    stage.player.update(delta_ms)
    for enemy in stage.get_enemies:
        enemy.update(delta_ms, screen)
        if pygame.sprite.spritecollide(enemy, stage.player.get_bullets, True) and enemy.is_alive:
            print("Le pegaste")
            enemy.is_alive = False
        if pygame.sprite.spritecollide(stage.player, enemy.get_enemy_group, False) and enemy.is_alive:
            enemy.attack()
            print("aya")
            # EN REALIDAD TIENE QUE RESTARSELE UNA VIDA AL JUGADOR
        for bullet in enemy.get_enemy_bullet_group:
            if pygame.sprite.collide_rect(bullet, stage.player):
                print("Me pegó")
                bullet.kill()
    

    stage.spawn_floors()
    stage.spawn_platform()
    moving_platorm.move_platform_up_down()
    stage.spawn_traps()
    stage.player.check_platform_collision(stage.get_floors)
    stage.player.check_platform_collision(stage.get_platforms)
    stage.player.draw_player(screen)
    stage.player.get_bullets.update(screen, delta_ms)
    
    pygame.draw.line(screen, (255, 0, 0), (320,550), (460, 550), 2)


    pygame.display.update()

pygame.quit()