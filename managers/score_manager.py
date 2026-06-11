# managers/score_manager.py
import json
import os

class ScoreManager:
    def __init__(self):
        self.file_path = "high_score.json"
        self.high_score = self._load()

    def _load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as f:
                    return int(json.load(f))
            except Exception:
                return 0
        return 0

    def check_and_save(self, current_score):
        """Сохраняет, если текущий счёт выше рекорда."""
        if current_score > self.high_score:
            self.high_score = current_score
            with open(self.file_path, "w") as f:
                json.dump(self.high_score, f)
            return True
        return False