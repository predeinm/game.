import json
from entities.block import Block
from settings import *

class LevelManager:
    def __init__(self, game):
        self.game = game
        self.current_level_id = 1
        self.max_level = 5  #  Увеличили до 5 уровней

    def load_level(self, level_id):
        """Загружает уровень и возвращает список блоков."""
        try:
            with open(f"levels/level_{level_id}.json", "r") as f:
                matrix = json.load(f)
        except FileNotFoundError:
            print(f" level_{level_id}.json не найден! Загрузка пустого уровня.")
            return []

        blocks = []
        if not matrix:
            return blocks

        rows = len(matrix)
        cols = len(matrix[0])
        
        total_width = cols * (BLOCK_W + BLOCK_MARGIN) - BLOCK_MARGIN
        start_x = (WIDTH - total_width) / 2
        start_y = BLOCK_OFFSET_Y

        for row_idx, row in enumerate(matrix):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    x = start_x + col_idx * (BLOCK_W + BLOCK_MARGIN)
                    y = start_y + row_idx * (BLOCK_H + BLOCK_MARGIN)
                    blocks.append(Block(x, y, block_type=cell))
                    
        return blocks

    def get_next_level_id(self):
        if self.current_level_id < self.max_level:
            self.current_level_id += 1
            return self.current_level_id
        return None
