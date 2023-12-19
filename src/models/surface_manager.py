import pygame

class SurfaceManager:
    @staticmethod
    def get_surface_from_spritesheet(img_path: str, cols: int, rows: int, step= 1, flip: bool = False) -> list[pygame.surface.Surface]:
        sprite_list = []
        img_surface = pygame.image.load(img_path)
        frame_widht = int(img_surface.get_width()/cols)
        frame_height = int(img_surface.get_height()/rows)

        for row in range(rows):
            for column in range(0, cols, step):
                x_axis = column * frame_widht
                y_axis = row * frame_height

                frame_surface = img_surface.subsurface(x_axis, y_axis, frame_widht, frame_height)

                if flip:
                    frame_surface = pygame.transform.flip(frame_surface, True, False)
                sprite_list.append(frame_surface)

        return sprite_list