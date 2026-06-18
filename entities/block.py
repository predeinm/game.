import pygame
from settings import *

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, block_type=1):
        super().__init__()
        self.type = block_type
        self.health = block_type
        self.points = block_type * 10 
        
        color = BLOCK_COLORS.get(block_type, BLUE)
        
        self.image = pygame.Surface((BLOCK_W, BLOCK_H))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def hit(self, damage=1):
        """Получить урон. Возвращает True, если блок уничтожен."""
        self.health -= damage
        if self.health <= 0:
            self.kill()  # Удалить из группы Sprite
            return True
        return False

    def draw(self, screen):
        if self.health > 0:
            screen.blit(self.image, self.rect)
