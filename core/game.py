# core/game.py
import pygame
import sys
from settings import *
from core.state_machine import StateManager
from core.input_handler import InputHandler
from scenes.menu_scene import MenuScene
from scenes.game_scene import GameScene
from scenes.gameover_scene import GameOverScene
from managers.score_manager import ScoreManager

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ломатель блоков: Офлайн")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        
        # Системы
        self.input_handler = InputHandler()
        self.state_manager = StateManager(self)
        self.score_manager = ScoreManager()

        # Данные для передачи между сценами
        self.final_score = 0
        
        # Регистрация сцен
        self._setup_states()
        
        print("✅ Игра инициализирована")
        print(f"📦 Разрешение: {WIDTH}x{HEIGHT}")
        print(f"🎯 FPS: {FPS}")

    def _setup_states(self):
        """Регистрация всех сцен."""
        self.state_manager.add_state("menu", MenuScene(self))
        self.state_manager.add_state("game", GameScene(self))
        self.state_manager.add_state("gameover", GameOverScene(self))
        self.state_manager.change_state("menu")

    def run(self):
        """Главный игровой цикл."""
        running = True
        while running:
            # 1. Обработка событий
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            # 2. Обновление ввода
            self.input_handler.update(events)
            
            # 3. Расчёт delta time
            dt = self.clock.tick(FPS) / 1000.0
            
            # 4. Обновление состояния
            self.state_manager.handle_events(events)
            self.state_manager.update(dt)
            
            # 5. Отрисовка
            self.screen.fill(BG_COLOR)
            self.state_manager.draw()
            
            # 6. Обновление экрана
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()