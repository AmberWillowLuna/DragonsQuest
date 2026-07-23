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
import linesF
from weapons import weapon

def Buy(player, chat, Allweapons, weaponary, weapon_size, b):
    #traj baj
    if player.gold>=Allweapons[weaponary[b]].cost:
        #buy
        player.gold-=Allweapons[weaponary[b]].cost
        player.weapons.append(Allweapons[weaponary[b]])
    else:
        chat = "not enough gold"
        return chat


def Smith(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, Allarmors, Allweapons):

    time.add(1)
    # roulette of armors and weapons all:
    weapon_size=len(Allweapons)
    armors_size=len(Allarmors)
    # choose weapons that are not in player eq
    while True:
        weaponary = random.sample(range(1, len(Allweapons)), 3)

        if all(Allweapons[i] not in player.weapon for i in weaponary):
            break

    while True:
        armory = random.sample(range(1, len(Allarmors)), 2)

        if all(Allarmors[i] not in player.armor for i in armory):
            break

    #defining things for displaying player stats
    smallfont2=pygame.font.SysFont("Arial", 16)
    panel=pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = linesF.update_lines(player, time.day, time)
    #buttons for smith
    weapon1_button=button.Button(20, 0, 440, 60, Allweapons[weaponary[0]].name+" "+str(Allweapons[weaponary[0]].cost), colors.LIGHT_BLUE, (100, 255, 100))
    weapon2_button=button.Button(20, 75, 440, 60, Allweapons[weaponary[1]].name+" "+str(Allweapons[weaponary[1]].cost) , colors.LIGHT_BLUE, (100, 255, 100))
    weapon3_button=button.Button(20, 150, 440, 60,Allweapons[weaponary[2]].name+" "+str(Allweapons[weaponary[2]].cost) , colors.LIGHT_BLUE, (100, 255, 100))

    armor1_button=button.Button(20, 225, 440, 60, Allarmors[armory[0]].name+" "+str(Allarmors[armory[0]].cost), colors.LIGHT_BLUE, (100, 255, 100))
    armor2_button=button.Button(20, 300, 440, 60, Allarmors[armory[1]].name+" "+str(Allarmors[armory[1]].cost), colors.LIGHT_BLUE, (100, 255, 100))

    Reroll_button = button.Button(20, 375, 440, 60, "Stay", colors.LIGHT_BLUE, (100, 255, 100))
    backButton =  button.Button(20, 450, 440, 60, "Back", colors.LIGHT_BLUE, (100, 255, 100))

    running = True
    while running:
        #implement smith interface
        current_time = pygame.time.get_ticks()
    
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if weapon1_button.is_clicked(pygame.mouse.get_pos(), event):
                    #chat = 
                    #remember that crafting armors and weapons take time!!!
                    i=1
                elif weapon2_button.is_clicked(pygame.mouse.get_pos(), event):
                    i=1

                elif weapon3_button.is_clicked(pygame.mouse.get_pos(), event):
                    i=1

                elif backButton.is_clicked(pygame.mouse.get_pos(), event):
                    chat ="You leave smith's hut."
                    running = False
                lines=linesF.update_lines(player, time.day, time)
                    # Add your back logic here


        #drawing
        screen.fill((0, 0, 0))
        linesF.draw_lines(panel, lines, smallfont2, screen)
        #spell3_button.draw(screen)
        backButton.draw(screen)
        weapon1_button.draw(screen)
        weapon2_button.draw(screen)
        weapon3_button.draw(screen)
        armor1_button.draw(screen)
        armor2_button.draw(screen)
        Reroll_button.draw(screen)
        ChatDisplay.ChatDisplay(chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, smallfont2)
        pygame.display.flip()