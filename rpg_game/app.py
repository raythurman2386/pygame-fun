"""
Rebuilding an old Python 2 RPG game from scratch
Only thing being reused is the resources for the maps, sounds, fonts
"""

"""
This is a fantasy RPG game about a warrior whose
quest is to recover a magic crown
"""


from src.main import main
from src import setup
import pygame
import sys
if __name__ == '__main__':
    setup.GAME
    main()
    pygame.quit()
    sys.exit()
