import pygame

# Ship class to create Player and Enemy Ships
class Ship:
    def __init__(self, x, y, color, health=100):
        self.x = x
        self.y = y
        self.color = color
        self.health = health