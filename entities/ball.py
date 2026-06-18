import pygame
import math
import random
from settings import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, paddle=None, speed_mult=1.0):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS*2, BALL_RADIUS*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)
        self.rect = self.image.get_rect()
        self.vx = 0
        self.vy = 0
        self.speed_mult = speed_mult  # ← Параметр принят и сохранён

        if paddle:
            self.reset(paddle)

    def reset(self, paddle):
        """Сброс мяча на платформу."""
        self.rect.centerx = paddle.rect.centerx
        self.rect.bottom = paddle.rect.top - 5
        direction = 1 if random.random() > 0.5 else -1
        current_speed = BALL_SPEED * self.speed_mult
        self.vx = current_speed * direction
        self.vy = -current_speed

    def update(self):
        """Обновление позиции мяча."""
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.left <= 0:
            self.rect.left = 0
            self.vx = -self.vx
        if self.rect.right >= WIDTH:
            self.rect.right = WIDTH
            self.vx = -self.vx
        if self.rect.top <= 0:
            self.rect.top = 0
            self.vy = -self.vy

        if self.rect.top > HEIGHT:
            return "lost"
        return None

    def bounce_off_paddle(self, paddle):
        """Расчёт угла отскока от платформы."""
        offset = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
        offset = max(-0.95, min(0.95, offset))
        
        angle = math.radians(offset * 70)
        speed = BALL_SPEED * self.speed_mult  # ← Учитываем ускорение
        self.vx = speed * math.sin(angle)
        self.vy = -speed * math.cos(angle)
        
        self.rect.bottom = paddle.rect.top

    def draw(self, screen):
        screen.blit(self.image, self.rect)
