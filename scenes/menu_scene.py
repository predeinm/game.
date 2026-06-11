# scenes/menu_scene.py
from scenes.base_scene import BaseScene
from settings import *

class MenuScene(BaseScene):
    def draw(self):
        self.screen.fill(BG_COLOR)
        
        # Заголовок
        title = self.font.render("ЛОМАТЕЛЬ БЛОКОВ: ОФФЛАЙН", True, WHITE)
        title_rect = title.get_rect(center=(WIDTH//2, 150))
        self.screen.blit(title, title_rect)
        
        # Инструкция
        hint = self.font.render("Нажмите SPACE для старта", True, (150, 150, 150))
        hint_rect = hint.get_rect(center=(WIDTH//2, HEIGHT//2))
        self.screen.blit(hint, hint_rect)
        
        # Управление
        controls = self.font.render("Управление: ← → или мышь", True, (100, 100, 100))
        controls_rect = controls.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
        self.screen.blit(controls, controls_rect)
        
        # Версия
        version = self.font.render("v1.0", True, (80, 80, 80))
        self.screen.blit(version, (10, HEIGHT - 30))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.state_manager.change_state("game")
                elif event.key == pygame.K_ESCAPE:
                    self.game.running = False