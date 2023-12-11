import pygame
from UI.form_main_menu import MainMenu
from db.ranking import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    clock = pygame.time.Clock()
    #game_instance = Game()
    main_menu = MainMenu(screen, 0, 0, 800, 600, (155, 0, 0), (10, 10, 10), 5, True)

    create_table()

    while True:
        clock.tick(60)
        eventos = pygame.event.get()
        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((155,0,0))
        
        main_menu.update(eventos)
        pygame.display.update()