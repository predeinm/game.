import pygame
import random
import math

class Particle:
    def __init__(self, x, y, color):
        self.color = color
        self.pos = [float(x), float(y)]
        self.radius = random.uniform(2, 5)
        self.life = 45
        self.max_life = 45

        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 7)
        self.vx = speed * math.cos(angle)
        self.vy = speed * math.sin(angle)
        if self.vy > 0:
            self.vy *= 0.3  

    def update(self):
        self.pos[0] += self.vx
        self.pos[1] += self.vy
        self.vy += 0.15  
        self.life -= 1

    def draw(self, screen):
        if self.life <= 0:
            return
        ratio = self.life / self.max_life
        current_r = max(0.5, self.radius * ratio)
        alpha = int(200 * ratio)
        particle_color = (*self.color[:3], alpha)

        size = int(current_r * 2 + 2)
        surf = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(surf, particle_color, (size // 2, size // 2), int(current_r))
        screen.blit(surf, (self.pos[0] - size // 2, self.pos[1] - size // 2))
