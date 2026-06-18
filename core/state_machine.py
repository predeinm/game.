class StateManager:
    """Управляет переключением между сценами."""
    
    def __init__(self, game):
        self.game = game
        self.states = {}
        self.current_state = None

    def add_state(self, name, state_instance):
        """Добавить сцену в менеджер."""
        self.states[name] = state_instance

    def change_state(self, name):
        """Переключиться на другую сцену."""
        if name not in self.states:
            raise ValueError(f"State '{name}' not found!")
        
        if self.current_state:
            self.current_state.exit()
        
        self.current_state = self.states[name]
        self.current_state.enter()
        
        print(f" Смена состояния: {name}")

    def handle_events(self, events):
        """Передать события текущей сцене."""
        if self.current_state:
            self.current_state.handle_events(events)

    def update(self, dt):
        """Обновить текущую сцену."""
        if self.current_state:
            self.current_state.update(dt)

    def draw(self):
        """Отрисовать текущую сцену."""
        if self.current_state:
            self.current_state.draw()
