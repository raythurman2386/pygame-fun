import pygame
import sys
from game import Game


if __name__ == "__main__":
    # Init Pygame and Fonts
    pygame.init()
    pygame.font.init()
    Game().play()
    pygame.quit()
    sys.exit()
