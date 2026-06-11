# managers/resource_mgr.py
import pygame
from settings import *

class ResourceManager:
    """Кэширование ресурсов."""
    
    def __init__(self):
        self.images = {}
        self.fonts = {}
        self.sounds = {}  # Не используем, но структура готова

    def get_font(self, name, size):
        key = (name, size)
        if key not in self.fonts:
            self.fonts[key] = pygame.font.SysFont(name, size)
        return self.fonts[key]