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

                # ---------- Weapon 1 ----------
                if weapon1_button.is_clicked(pygame.mouse.get_pos(), event):

                    item = Allweapons[weaponary[0]]

                    if player.gold >= item.cost:
                        player.gold -= item.cost
                        player.weapon.append(item)

                        if item.cost >= 40:
                            time.add(2 if random.randint(1,2) == 1 else 1)
                        else:
                            time.add(2 if random.randint(1,4) == 1 else 1)

                        chat = f"You bought {item.name}."

                        available = [i for i in range(1, len(Allweapons))
                                    if Allweapons[i] not in player.weapon
                                    and i not in weaponary]

                        if available:
                            weaponary[0] = random.choice(available)
                            weapon1_button.text = Allweapons[weaponary[0]].name + " " + str(Allweapons[weaponary[0]].cost)

                    else:
                        chat = "Not enough gold."

                # ---------- Weapon 2 ----------
                elif weapon2_button.is_clicked(pygame.mouse.get_pos(), event):

                    item = Allweapons[weaponary[1]]

                    if player.gold >= item.cost:
                        player.gold -= item.cost
                        player.weapon.append(item)

                        if item.cost >= 40:
                            time.add(2 if random.randint(1,2) == 1 else 1)
                        else:
                            time.add(2 if random.randint(1,4) == 1 else 1)

                        chat = f"You bought {item.name}."

                        available = [i for i in range(1, len(Allweapons))
                                    if Allweapons[i] not in player.weapon
                                    and i not in weaponary]

                        if available:
                            weaponary[1] = random.choice(available)
                            weapon2_button.text = Allweapons[weaponary[1]].name + " " + str(Allweapons[weaponary[1]].cost)

                    else:
                        chat = "Not enough gold."

                # ---------- Weapon 3 ----------
                elif weapon3_button.is_clicked(pygame.mouse.get_pos(), event):

                    item = Allweapons[weaponary[2]]

                    if player.gold >= item.cost:
                        player.gold -= item.cost
                        player.weapon.append(item)

                        if item.cost >= 40:
                            time.add(2 if random.randint(1,2) == 1 else 1)
                        else:
                            time.add(2 if random.randint(1,4) == 1 else 1)

                        chat = f"You bought {item.name}."

                        available = [i for i in range(1, len(Allweapons))
                                    if Allweapons[i] not in player.weapon
                                    and i not in weaponary]

                        if available:
                            weaponary[2] = random.choice(available)
                            weapon3_button.text = Allweapons[weaponary[2]].name + " " + str(Allweapons[weaponary[2]].cost)

                    else:
                        chat = "Not enough gold."

                # ---------- Armor 1 ----------
                elif armor1_button.is_clicked(pygame.mouse.get_pos(), event):

                    item = Allarmors[armory[0]]

                    if player.gold >= item.cost:
                        player.gold -= item.cost
                        player.armor.append(item)

                        if item.cost >= 40:
                            time.add(2 if random.randint(1,2) == 1 else 1)
                        else:
                            time.add(2 if random.randint(1,4) == 1 else 1)

                        chat = f"You bought {item.name}."

                        available = [i for i in range(1, len(Allarmors))
                                    if Allarmors[i] not in player.armor
                                    and i not in armory]

                        if available:
                            armory[0] = random.choice(available)
                            armor1_button.text = Allarmors[armory[0]].name + " " + str(Allarmors[armory[0]].cost)

                    else:
                        chat = "Not enough gold."

                # ---------- Armor 2 ----------
                elif armor2_button.is_clicked(pygame.mouse.get_pos(), event):

                    item = Allarmors[armory[1]]

                    if player.gold >= item.cost:
                        player.gold -= item.cost
                        player.armor.append(item)

                        if item.cost >= 40:
                            time.add(2 if random.randint(1,2) == 1 else 1)
                        else:
                            time.add(2 if random.randint(1,4) == 1 else 1)

                        chat = f"You bought {item.name}."

                        available = [i for i in range(1, len(Allarmors))
                                    if Allarmors[i] not in player.armor
                                    and i not in armory]

                        if available:
                            armory[1] = random.choice(available)
                            armor2_button.text = Allarmors[armory[1]].name + " " + str(Allarmors[armory[1]].cost)

                    else:
                        chat = "Not enough gold."

                # ---------- Stay ----------
                elif Reroll_button.is_clicked(pygame.mouse.get_pos(), event):

                    time.add(1)

                    while True:
                        weaponary = random.sample(range(1, len(Allweapons)), 3)

                        if all(Allweapons[i] not in player.weapon for i in weaponary):
                            break

                    while True:
                        armory = random.sample(range(1, len(Allarmors)), 2)

                        if all(Allarmors[i] not in player.armor for i in armory):
                            break

                    weapon1_button.text = Allweapons[weaponary[0]].name + " " + str(Allweapons[weaponary[0]].cost)
                    weapon2_button.text = Allweapons[weaponary[1]].name + " " + str(Allweapons[weaponary[1]].cost)
                    weapon3_button.text = Allweapons[weaponary[2]].name + " " + str(Allweapons[weaponary[2]].cost)

                    armor1_button.text = Allarmors[armory[0]].name + " " + str(Allarmors[armory[0]].cost)
                    armor2_button.text = Allarmors[armory[1]].name + " " + str(Allarmors[armory[1]].cost)

                    chat = "The smith brings out new equipment."

                # ---------- Back ----------
                elif backButton.is_clicked(pygame.mouse.get_pos(), event):
                    chat = "You leave the smith's hut."
                    running = False

                lines = linesF.update_lines(player, time.day, time)


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