# entities/paddle.py
import pygame
from settings import *

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_W, PADDLE_H))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 20

    def update(self, input_handler):
        # Клавиатура
        dx = 0
        if input_handler.is_key_pressed(pygame.K_LEFT):
            dx = -PADDLE_SPEED
        if input_handler.is_key_pressed(pygame.K_RIGHT):
            dx = PADDLE_SPEED
        
        self.rect.x += dx
        
        # Мышь (альтернатива)
        mouse_x, _ = input_handler.get_mouse_pos()
        if abs(mouse_x - self.rect.centerx) > 5:  # Небольшой мёртвый зона
            # Опционально: раскомментировать для управления мышью
            # self.rect.centerx = mouse_x
            pass
        
        # Границы
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)