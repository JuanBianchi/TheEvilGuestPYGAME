import pygame
from models.auxiliar.surface_manager import SurfaceManager as sfm
from constantes import ALTO_VENT, ANCHO_VENT

class Traps(pygame.sprite.Sprite):
    def __init__(self, img_path, pos_x, pos_y, width, height, trap_type, frame_rate) -> None:
        super().__init__()
        self.__width = width
        self.__height = height
        self.__trap_img = self.load_image(trap_type)
        self.__frame_rate = frame_rate
        self.__trap_animation_time = 0
        self.__initial_frame = 0
        self.__actual_animation = self.__trap_img
        self.__trap_img_animation = self.__actual_animation[self.__initial_frame]
        self.__trap_img_animation = pygame.transform.scale(self.__trap_img_animation, (ANCHO_VENT, ALTO_VENT))
        self.rect = pygame.Rect(pos_x, pos_y, self.__width, self.__height)
        self.rect.x = pos_x
        self.rect.y = pos_y
        #self.rect_area = 
        self.__moving_down = False
        self.__trap_group = pygame.sprite.Group()
        self.__trap_group.add(self)


    @property
    def get_trap_group(self):
        return self.__trap_group


    def load_image(self, trap_type):
        if trap_type == "spikes":
            self.__trap_img = [pygame.image.load("./src/assets/img/traps/spikes/spikes_long.png")]
            self.__trap_img = [pygame.transform.scale(img, (self.__width, self.__height)) for img in self.__trap_img]
        elif trap_type == "saw":
            self.__trap_img = sfm.get_surface_from_spritesheet("./src/assets/img/traps/saw/saw.png", 4, 1)
            self.__trap_img = [pygame.transform.scale(img, (self.__width, self.__height)) for img in self.__trap_img]

        return self.__trap_img
    
    def do_animation(self, delta_ms):
        self.__trap_animation_time += delta_ms
        if self.__trap_animation_time >= self.__frame_rate:
            if self.__initial_frame < len(self.__actual_animation) - 1:
                self.__initial_frame += 1
            else:
                self.__initial_frame = 0


    def move_trap_up_down(self, speed):
        if self.rect.bottom > 80 and not self.__moving_down:
            self.rect.y -= speed
            if self.rect.bottom <= 80:
                self.__moving_down = True

        elif self.rect.top < 480 and self.__moving_down:
            self.rect.y += speed
            if self.rect.top >= 480:
                self.__moving_down = False


    def update(self, screen: pygame.surface.Surface, delta_ms):
        self.do_animation(delta_ms)
        self.draw_trap(screen)


    def draw_trap(self, screen: pygame.surface.Surface):
        self.__trap_img_animation = self.__actual_animation[self.__initial_frame]
        screen.blit(self.__trap_img_animation, self.rect)