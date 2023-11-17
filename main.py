import pygame
from models.constantes import *
from models.player.main_player import Jugador

screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
pygame.init()
clock = pygame.time.Clock()

running = True

bg_color = (144, 210, 120)

player = Jugador(0, 0, 10, 5)

while running:
    events_list = pygame.event.get()
    for event in events_list:
        match event.type:
            # case pygame.KEYDOWN:
            #     if event.key == pygame.K_SPACE:
            #         print("Estoy saltando")
            # case pygame.KEYUP:
            #     if event.key == pygame.K_SPACE:
            #         print("Deje de saltar")
            case pygame.QUIT:
                print("CERRANDO EL JUEGO")
                running = False
                break

    key_pressed_list = pygame.key.get_pressed()
    if key_pressed_list[pygame.K_d] and not key_pressed_list[pygame.K_a]:
        player.walk('Right')
    if key_pressed_list[pygame.K_a] and not key_pressed_list[pygame.K_d]:
        player.walk('Left')
    if not key_pressed_list[pygame.K_a] and not key_pressed_list[pygame.K_d]:
        player.stay()

    screen.fill(bg_color)
    
    delta_ms = clock.tick(FPS)
    player.update(delta_ms)
    player.draw_player(screen)
    pygame.display.update()

pygame.quit()

