class BaseScene:
    
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.font = game.font

    def enter(self):
        """Вызывается при входе в сцену."""
        pass

    def exit(self):
        """Вызывается при выходе из сцены."""
        pass

    def handle_events(self, events):
        """Обработка событий."""
        pass

    def update(self, dt):
        """Логика сцены."""
        pass

    def draw(self):
        """Отрисовка сцены."""
        pass
