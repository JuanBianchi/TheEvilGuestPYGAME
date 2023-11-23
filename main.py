import pygame
from models.constantes import *
from models.player.main_player import Jugador
from models.enemy.enemy import Enemy

screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
pygame.init()
clock = pygame.time.Clock()

running = True

bg_color = (144, 210, 120)

player = Jugador(0, 0, 10, 5, 12, 16, 35)
zombie = Enemy((400, 0), 1, 13, 19, 16, 800)

while running:
    events_list = pygame.event.get()
    for event in events_list:
        match event.type:
            case pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #and player.__is_running
                    player.jump(True)
            case pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    player.jump(False)
            case pygame.QUIT:
                print("CERRANDO EL JUEGO")
                running = False
                break

    # Esto hacerlo en un metodo de la clase Player que asigne las teclas.
    key_pressed_list = pygame.key.get_pressed()
    if key_pressed_list[pygame.K_d] and not key_pressed_list[pygame.K_a]:
        player.walk('Right')
    if key_pressed_list[pygame.K_a] and not key_pressed_list[pygame.K_d]:
        player.walk('Left')
    if not key_pressed_list[pygame.K_a] and not key_pressed_list[pygame.K_d]:
        player.stay()
    if key_pressed_list[pygame.K_d] and key_pressed_list[pygame.K_LSHIFT] and not key_pressed_list[pygame.K_a]:
        player.run('Right')
    if key_pressed_list[pygame.K_a] and key_pressed_list[pygame.K_LSHIFT] and not key_pressed_list[pygame.K_d]:
        player.run('Left')
    if key_pressed_list[pygame.K_f] and player.is_looking_right:
        player.shoot('Right')
    if key_pressed_list[pygame.K_f] and not player.is_looking_right:
        player.shoot('Left')
    #

    screen.fill(bg_color)
    
    delta_ms = clock.tick(FPS)
    player.update(delta_ms)
    player.draw_player(screen)
    zombie.update(delta_ms, screen)
    for bullet in player.get_bullets:
        bullet.update(screen)
    pygame.display.update()

pygame.quit()

