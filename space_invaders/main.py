import pygame
import sys
from game import Game

# Init Pygame and Fonts
pygame.init()
pygame.font.init()

if __name__ == "__main__":
    Game().play()
    pygame.quit()
    sys.exit()
