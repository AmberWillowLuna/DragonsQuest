#smith:
#out of all weapons and armor you have a few to choose
#you can reroll for one time set - every weapon has to be different 
# 3 weapons 2 armors
# if you decide to buy something - it takes 2 time values to build
#i should potencialy extend day to 24 at this rate
from ChatDisplay import ChatDisplay
from basic_functions import roll_dice
import button
import pygame
import random
import items
import colors
import ChatDisplay
from linesF import update_lines, draw_lines

def Smith(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, armors, weapons):
    time.add(1)
    # roulette of armors and weapons all:
    weapon_size=weapons.size()
    armors_size=armors.size()
    weaponary = random.sample(range(1, weapon_size), 3)
    armory = random.sample(range(1,armors_size), 2)

    #buttons for smith
    weapon1_button=button.Button(20, 100, 440, 100, weapons[weaponary[0]], colors.LIGHT_BLUE, (100, 255, 100))
    weapon2_button=button.Button(20, 200, 440, 100, weapons[weaponary[1]] , colors.LIGHT_BLUE, (100, 255, 100))
    weapon3_button=button.Button(20, 300, 440, 100, weapons[weaponary[2]] , colors.LIGHT_BLUE, (100, 255, 100))

    armor1_button=button.Button(20, 400, 440, 100, armors[armory[0]], colors.LIGHT_BLUE, (100, 255, 100))
    armor2_button=button.Button(20, 500, 440, 100, armors[armory[1]] , colors.LIGHT_BLUE, (100, 255, 100))

    Reroll_button = button.Button(20, 600, 440, 100, "Stay", colors.LIGHT_BLUE, (100, 255, 100))
    backButton =  button.Button(20, 700, 440, 100, "Back", colors.LIGHT_BLUE, (100, 255, 100))

    running = True
    while running:
        #implement smith interface






        pygame.display.flip()