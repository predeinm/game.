import pygame

class InputHandler:
    
    def __init__(self):
        self.keys_pressed = None 
        self.mouse_pos = (0, 0)
        self.mouse_buttons = {}

    def update(self, events):
        # pygame.key.get_pressed() возвращает последовательность, не словарь!
        self.keys_pressed = pygame.key.get_pressed()
        self.mouse_pos = pygame.mouse.get_pos()
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_buttons[event.button] = True
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_buttons[event.button] = False

    def is_key_pressed(self, key):
        if self.keys_pressed is None:
            return False
        return bool(self.keys_pressed[key])

    def get_mouse_pos(self):
        return self.mouse_pos
