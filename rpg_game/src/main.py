from src.states import main_menu
from . import setup, tools
from . import constants as c

TOWN = 'town'
MAIN_MENU = 'main menu'
CASTLE = 'castle'
HOUSE = 'house'
INN = 'Inn'
ARMOR_SHOP = 'armor shop'
WEAPON_SHOP = 'weapon shop'
MAGIC_SHOP = 'magic shop'
POTION_SHOP = 'potion shop'
PLAYER_MENU = 'player menu'
OVERWORLD = 'overworld'
BROTHER_HOUSE = 'brotherhouse'
BATTLE = 'battle'
DUNGEON = 'dungeon'
DUNGEON2 = 'dungeon2'
DUNGEON3 = 'dungeon3'
DUNGEON4 = 'dungeon4'
DUNGEON5 = 'dungeon5'
INSTRUCTIONS = 'instructions'
DEATH_SCENE = 'death scene'
LOADGAME = 'load game'
CREDITS = 'credits'


def main():
    run_it = tools.Control(setup.ORIGINAL_CAPTION)
    state_dict = {MAIN_MENU: main_menu.Menu()}

    run_it.setup_state(state_dict, c.MAIN_MENU)
    run_it.main()
