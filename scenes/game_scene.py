import pygame
from scenes.base_scene import BaseScene
from entities.paddle import Paddle
from entities.ball import Ball
from entities.particle import Particle
from managers.level_manager import LevelManager
from settings import *

class GameScene(BaseScene):
    def __init__(self, game):
        super().__init__(game)
        self.paddle = None
        self.ball = None
        self.score = 0
        self.lives = 3
        self.blocks_group = pygame.sprite.Group()
        self.particles = []
        self.level_manager = LevelManager(game)
        self.exploding = False
        self.explode_timer = 0
        self.paused = False          
        self.speed_mult = 1.0        

    def enter(self):
        self.paddle = Paddle()
        self.score = 0
        self.lives = 3
        self.blocks_group.empty()
        self.particles = []
        self.exploding = False
        self.paused = False
        
        self.speed_mult = 1.0 + (self.level_manager.current_level_id - 1) * 0.15
        self.ball = Ball(self.paddle, speed_mult=self.speed_mult)
        
        blocks = self.level_manager.load_level(self.level_manager.current_level_id)
        for block in blocks:
            self.blocks_group.add(block)

    def exit(self):
        self.game.final_score = self.score
        self.game.score_manager.check_and_save(self.score)  

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.state_manager.change_state("menu")
                elif event.key == pygame.K_p:   
                    self.paused = not self.paused

    def update(self, dt):
        if self.paused:  
            return

        if self.exploding:
            for p in self.particles:
                p.update()
            self.particles = [p for p in self.particles if p.life > 0]
            self.explode_timer -= 1
            if self.explode_timer <= 0 and len(self.particles) == 0:
                self.game.state_manager.change_state("gameover")
            return

        self.paddle.update(self.game.input_handler)
        ball_result = self.ball.update()
        
        if ball_result == "lost":
            self.lives -= 1
            if self.lives <= 0:
                self._trigger_explosion()
                return
            else:
                self.ball.reset(self.paddle)

        if pygame.sprite.collide_rect(self.ball, self.paddle):
            if self.ball.vy > 0:
                self.ball.bounce_off_paddle(self.paddle)
                self.ball.rect.bottom = self.paddle.rect.top

        hits = pygame.sprite.spritecollide(self.ball, self.blocks_group, dokill=True)
        if hits:
            hit_block = hits[0]
            if abs(self.ball.rect.centerx - hit_block.rect.centerx) > hit_block.rect.width / 2:
                self.ball.vx = -self.ball.vx
            else:
                self.ball.vy = -self.ball.vy
            self.ball.rect.bottom = hit_block.rect.top - 1
            self.score += hit_block.points

        if len(self.blocks_group) == 0:
            next_lvl = self.level_manager.get_next_level_id()
            if next_lvl:
                self.enter()
            else:
                self.game.final_score = self.score
                self.game.state_manager.change_state("gameover")

    def _trigger_explosion(self):
        self.exploding = True
        self.explode_timer = 50
        cx, cy = self.paddle.rect.center
        for _ in range(60):
            self.particles.append(Particle(cx, cy, RED))
            self.particles.append(Particle(cx, cy, (255, 150, 50)))

    def draw(self):
        self.screen.fill(BG_COLOR)
        
        if not self.exploding:
            self.paddle.draw(self.screen)
            self.ball.draw(self.screen)
            self.blocks_group.draw(self.screen)
        
        for p in self.particles:
            p.draw(self.screen)
            
        # HUD
        hud_str = f"Ур: {self.level_manager.current_level_id} | Счёт: {self.score} |  {self.lives}"
        hud = self.font.render(hud_str, True, WHITE)
        self.screen.blit(hud, (10, 10))
        
        hint = self.font.render("ESC - Меню  |  P - Пауза", True, (100, 100, 100))
        self.screen.blit(hint, (WIDTH - hint.get_width() - 10, 10))
        
        if self.paused:  
            pause_text = self.font.render("ПАУЗА", True, WHITE)
            self.screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2))
