import pygame
import sys
from core.game import Game
icon=pygame.image.load("dota.png")
pygame.display.set_icon(icon)

def main():
    game = Game()
    game.run()

if __name__ == "__main__":
    main()
