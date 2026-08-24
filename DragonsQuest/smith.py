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
from achievementManage import AchievementManage

def Buy(player, chat, Allweapons, weaponary, weapon_size, b):
    #traj baj
    if player.gold>=Allweapons[weaponary[b]].cost:
        #buy
        player.gold-=Allweapons[weaponary[b]].cost
        player.weapons.append(Allweapons[weaponary[b]])
    else:
        chat += "not enough gold"


def Smith(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, Allarmors, Allweapons):
    chat.ClearChat()
    time.add(1)
    scale = 1.0*SCREEN_WIDTH/640
    # roulette of armors and weapons all:
    # choose weapons that are not in player eq
    while True:
        weaponary = random.sample(range(1, len(Allweapons)), 3)

        if all(Allweapons[i] not in player.weapon for i in weaponary):
            break

    while True:
        armory = random.sample(range(1, len(Allarmors)), 2)

        if all(Allarmors[i] not in player.armor for i in armory):
            break
        
    Weapons_A=[Allweapons[i] for i in weaponary]
    Armors_A = [Allarmors[i] for i in armory]

    if player.discountB==1:
        for weapon in Weapons_A:
            weapon.cost = int(weapon.cost * 0.85)
        for armor in Armors_A:
            armor.cost = int(armor.cost * 0.85)

    #defining things for displaying player stats
    smallfont2=pygame.font.SysFont("Arial", 16)
    panel=pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = linesF.update_lines(player, time.day, time)
    #buttons for smith


    weapon1_button=button.Button(10 *scale, 12*scale, 220*scale, 30*scale, Weapons_A[0].name+" "+str(Weapons_A[0].cost), colors.NAVY_BLUE, colors.GREEN)
    weapon2_button=button.Button(10 *scale, 52*scale, 220*scale, 30*scale, Weapons_A[1].name+" "+str(Weapons_A[1].cost) , colors.NAVY_BLUE, colors.GREEN)
    weapon3_button=button.Button(10 *scale, 92*scale, 220*scale, 30*scale,Weapons_A[2].name+" "+str(Weapons_A[2].cost) , colors.NAVY_BLUE, colors.GREEN)

    armor1_button=button.Button(10 *scale, 132*scale, 220*scale, 30*scale, Armors_A[0].name+" "+str(Armors_A[0].cost), colors.NAVY_BLUE, colors.GREEN)
    armor2_button=button.Button(10 *scale, 172*scale, 220*scale, 30*scale, Armors_A[1].name+" "+str(Armors_A[1].cost), colors.NAVY_BLUE, colors.GREEN)

    Reroll_button = button.Button(10 *scale, 212*scale, 220*scale, 30*scale, "Stay", colors.NAVY_BLUE, colors.GREEN)
    backButton =  button.Button(10 *scale, 252*scale, 220*scale, 30*scale, "Back", colors.NAVY_BLUE, colors.GREEN)

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

                        chat += f"You bought {item.name}."

                        available = [i for i in range(1, len(Allweapons))
                                    if Allweapons[i] not in player.weapon
                                    and i not in weaponary]

                        if available:
                            weaponary[0] = random.choice(available)
                            weapon1_button.text = Allweapons[weaponary[0]].name + " " + str(Allweapons[weaponary[0]].cost)

                    else:
                        chat += "Not enough gold."

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

                        chat += f"You bought {item.name}."

                        available = [i for i in range(1, len(Allweapons))
                                    if Allweapons[i] not in player.weapon
                                    and i not in weaponary]

                        if available:
                            weaponary[1] = random.choice(available)
                            weapon2_button.text = Allweapons[weaponary[1]].name + " " + str(Allweapons[weaponary[1]].cost)

                    else:
                        chat += "Not enough gold."

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

                        chat += f"You bought {item.name}."

                        available = [i for i in range(1, len(Allweapons))
                                    if Allweapons[i] not in player.weapon
                                    and i not in weaponary]

                        if available:
                            weaponary[2] = random.choice(available)
                            weapon3_button.text = Allweapons[weaponary[2]].name + " " + str(Allweapons[weaponary[2]].cost)

                    else:
                        chat += "Not enough gold."

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

                        chat += f"You bought {item.name}."

                        available = [i for i in range(1, len(Allarmors))
                                    if Allarmors[i] not in player.armor
                                    and i not in armory]

                        if available:
                            armory[0] = random.choice(available)
                            armor1_button.text = Allarmors[armory[0]].name + " " + str(Allarmors[armory[0]].cost)

                    else:
                        chat += "Not enough gold."

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

                        chat += f"You bought {item.name}."

                        available = [i for i in range(1, len(Allarmors))
                                    if Allarmors[i] not in player.armor
                                    and i not in armory]

                        if available:
                            armory[1] = random.choice(available)
                            armor2_button.text = Allarmors[armory[1]].name + " " + str(Allarmors[armory[1]].cost)

                    else:
                        chat += "Not enough gold."

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

                    chat += "The smith brings out new equipment."

                # ---------- Back ----------
                elif backButton.is_clicked(pygame.mouse.get_pos(), event):

                    if len(player.weapon)>2:
                        AchievementManage.Achieve("Weapon collectioner")
                    if len(player.armor)>2:
                        AchievementManage.Achieve("Armor collectioner")

                    for player_weapon in player.weapon:
                        if player_weapon.name=="Arcanus Sword":
                            AchievementManage.Achieve("Legendary weapon")
                        elif player_weapon.name=="Terra Blade":
                            AchievementManage.Achieve("Not that game 1")
                        elif player_weapon.name=="Dark Sword":
                            AchievementManage.Achieve("Not that game 2")
                        elif player_weapon.name=="Obanium Sword":
                            AchievementManage.Achieve("Not that game 3")

                    for player_armor in player.armor:
                        if player_armor.name=="Legendary armor":
                            AchievementManage.Achieve("Legendary weapon")
                    chat += "You leave the smith's hut."
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
        chat.Display()
        pygame.display.flip()