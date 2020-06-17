import pickle
import sys
import os
import pygame
# TODO: tilerender.py
from .. import setup, tools, tilerender
# TODO: observer.py
from .. import observer
from .. import constants as c
# TODO: death.py
import death


class Menu(tools._State):
    def __init__(self):
        super(Menu, self).__init__()
        self.music = setup.MUSIC['kings_theme']
        self.music_title = 'kings_theme'
        self.volume = 0.4
        self.next = c.INSTRUCTIONS
        self.tmx_map = setup.TMX['title']
        self.name = c.MAIN_MENU
        self.startup(0, 0)

    def startup(self, *args):
        pass

    def make_viewport(self, map_image):
        # Create the viewport to view the level through
        pass

    def make_state_dict(self):
        # Dictionary of state methods for the level
        pass

    def update(self, surface, *args):
        # Update scene
        pass

    def draw_level(self, surface):
        # blit tmx map and title box onto screen
        pass

    def get_event(self, event):
        pass

    def transition_in(self):
        # Transition into scene with fade
        pass

    def transition_out(self):
        # Transition into scene with fade
        pass

    def normal_update(self):
        pass


class Instructions(tools._State):
    # Instructions page
    pass


class LoadGame(Instructions):
    pass
