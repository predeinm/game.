from scenes.base_scene import BaseScene
from settings import *

class GameOverScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.final_score = 0

    def enter(self):
        self.final_score = self.game.final_score

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        # Заголовок
        title = self.font.render("ИГРА ОКОНЧЕНА", True, RED)
        title_rect = title.get_rect(center=(WIDTH//2, 200))
        self.screen.blit(title, title_rect)
        
        # Счёт
        score_text = self.font.render(f"Ваш счёт: {self.final_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH//2, 280))
        self.screen.blit(score_text, score_rect)
        
        # Инструкция
        hint = self.font.render("SPACE - В меню", True, (150, 150, 150))
        hint_rect = hint.get_rect(center=(WIDTH//2, 380))
        self.screen.blit(hint, hint_rect)
        
        esc_hint = self.font.render("ESC - Выход", True, (100, 100, 100))
        esc_rect = esc_hint.get_rect(center=(WIDTH//2, 420))
        self.screen.blit(esc_hint, esc_rect)
        hs_text = self.font.render(f"Рекорд: {self.game.score_manager.high_score}", True, YELLOW)
        self.screen.blit(hs_text, (WIDTH//2 - hs_text.get_width()//2, 290))
        
        hint = self.font.render("SPACE - В меню", True, (150, 150, 150))
        self.screen.blit(hint, (WIDTH//2 - hint.get_width()//2, 380))
        
        esc_hint = self.font.render("ESC - Выход", True, (100, 100, 100))
        self.screen.blit(esc_hint, (WIDTH//2 - esc_hint.get_width()//2, 420))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.state_manager.change_state("menu")
                elif event.key == pygame.K_ESCAPE:
                    self.game.running = False
