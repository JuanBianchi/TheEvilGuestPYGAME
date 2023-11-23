import pygame
from models.constantes import *
from models.player.main_player import Jugador
from models.enemy.enemy import Enemy

screen = pygame.display.set_mode((ANCHO_VENT, ALTO_VENT))
pygame.init()
clock = pygame.time.Clock()

running = True

bg_color = (144, 210, 120)

player = Jugador(0, 0, PLAYER_FPS, 5, 12, 16, 35)
zombie = Enemy(0, 310, 1, 13, 19, 16, 800)

while running:
    
    # events = pygame.event.get()
    # for event in events:
    #     if event.type == pygame.QUIT:
    #         running = False

    screen.fill(bg_color)
    
    delta_ms = clock.tick(FPS)
    player.update(delta_ms)
    player.draw_player(screen)
    zombie.update(delta_ms, screen)
    for bullet in player.get_bullets:
        bullet.update(screen)
    pygame.display.update()

pygame.quit()

