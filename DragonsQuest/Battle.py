from types import NoneType
import pygame
from achievementManage import AchievementManage
import button
import ChatDisplay
import linesF
import colors
import basic_functions
import BattlePicker
import buttons_disp_battle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)



def Battle(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
           player, enemy, chat):
    x = BattlePicker.ChooseEquipment(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
                    player, chat)
    scale = 1.0 * SCREEN_WIDTH / 640
    
    if x==True:
        #font = pygame.font.SysFont("Arial", 24)
        smallfont = pygame.font.SysFont("Arial", int(10*scale))
        spell_disp = False
        item_disp = False
        panel = pygame.Rect(SCREEN_WIDTH - 140*scale, 0, 250*scale, 250*scale)
        chat.value= " You have encountered a " + enemy.type + " ! \n"
        chat.Display()

        AllAimPlaces=["head", "arms", "legs", "torso", "wings", "tail"]

        AimButton = button.Button(
            8*scale, 185*scale, 100*scale, 30*scale,
            "aim: "+player.limb,
            colors.NAVY_BLUE,
            (100,255,100)
        )

        actions_left = 2

        Max_heal_used=0
        max_heal_ar= [1.0,0.95,0.85,0.75,0.66,0.5]

        ItemButtons=buttons_disp_battle.PlayerItemsToButtons(player, scale)

        SpellButtons=buttons_disp_battle.PlayerSpellsToButtons(player, scale)

        attackButton = button.Button(
            8*scale, 10*scale, 100*scale, 30*scale,
            "Attack",
            colors.NAVY_BLUE,
            (100,255,100)
        )

        spellButton = button.Button(
            8*scale, 45*scale, 100*scale, 30*scale,
            "Spell",
            colors.NAVY_BLUE,
            (100,255,100)
        )

        itemButton = button.Button(
            8*scale, 80*scale, 100*scale, 30*scale,
            "Item",
            colors.NAVY_BLUE,
            (100,255,100)
        )

        defendButton = button.Button(
            8*scale, 115*scale, 100*scale, 30*scale,
            "Defend",
            colors.NAVY_BLUE,
            (100,255,100)
        )

        fleeButton = button.Button(
            8*scale, 150*scale, 100*scale, 30*scale,
            "Flee",
            colors.RED,
            (255,120,120)
        )

        running = True

        while running:

            mouse = pygame.mouse.get_pos()

            attackButton.check_hover(mouse)
            spellButton.check_hover(mouse)
            itemButton.check_hover(mouse)
            defendButton.check_hover(mouse)
            fleeButton.check_hover(mouse)

            if(actions_left==3):
                chat+=" You have 2 actions left this round."
                actions_left=2

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

                if event.type != pygame.MOUSEBUTTONDOWN:
                    continue

                ###############################
                # ATTACK
                ###############################

                if attackButton.is_clicked(mouse, event):


                    player.currentWeapon.attack(player, enemy, chat)


                    actions_left -= 1


                ###############################
                # SPELL
                ###############################

                elif spellButton.is_clicked(mouse, event):
                    if spell_disp==False:
                        spell_disp=True
                        item_disp=False
                        chat.value= " spells shown "
                    else:
                        spell_disp=False
                        chat.value= " spells hidden "

                ###############################
                # ITEM
                ###############################

                elif itemButton.is_clicked(mouse, event):
                    if item_disp==False:
                        item_disp=True
                        spell_disp=False
                        chat.value= " items shown "
                    else:
                        item_disp=False
                        chat.value= " Items hidden"


                ###############################
                # DEFEND
                ###############################

                elif defendButton.is_clicked(mouse, event):

                    player.BAC += basic_functions.roll_dice(2)-1
                    player.Bacc+=basic_functions.roll_dice(3)
                    chat.value= " You prepare for incoming attacks."

                    actions_left -= 1



                ###############################
                # FLEE
                ###############################

                elif fleeButton.is_clicked(mouse, event):

                    if basic_functions.roll_dice(20) + player.dex-10 > 10:
                        chat += " You escaped."
                        return False

                    else:
                        chat += " You failed to escape."
                        actions_left -=1

                elif AimButton.is_clicked(mouse, event):
                    current_index = AllAimPlaces.index(player.limb)
                    next_index = (current_index + 1) % len(AllAimPlaces)
                    player.limb = AllAimPlaces[next_index]
                    AimButton.setText("aim: "+player.limb)


                elif spell_disp:
                    spell_used = False

                    for spell, b in SpellButtons:

                        if b.is_clicked(mouse, event):

                            spell.cast(player, enemy, chat)

                            spell_disp = False
                            spell_used = True

                            break

                    if spell_used:
                        actions_left -= 1
                        continue

                elif item_disp:
                    item_used = False

                    for item, b in ItemButtons:

                        if b.is_clicked(mouse, event):

                            if item.type == "health potion" and Max_heal_used<=5:
                                item.value = int(item.value * max_heal_ar[Max_heal_used])
                                Max_heal_used += 1
                                chat+="You grow a bit resistant to heal effect"
                            elif item.type == "health potion":
                                item.value = int(item.value * 0.33)
                                chat+="the real worst really lame"

                            item.action(player)

                            item_disp = False
                            item_used = True
                            ItemButtons.remove((item, b))

                            if item in player.inventory:
                                player.inventory.remove(item)
                            break

                    if item_used:
                        actions_left -= 1
                        continue
                ######################################
                # Enemy turn
                ######################################

                if enemy.hp <= 0:
                    chat += f" You defeated the {enemy.type} !"
                    if enemy.type=="werewolf":
                        AchievementManage.Achieve("Wild beast")
                    elif enemy.type=="gremlin":
                        AchievementManage.Achieve("Lucky coins")  
                    player.gold+=enemy.gold
                    screen.fill(BLACK)
                    chat.Display()
                    pygame.display.flip()
                    pygame.time.wait(1000)
                    return True

            if actions_left <= 0:
                pygame.time.wait(200)
                actions_left = 3
                ctr=0
                chat.value= " new round begins... \n"
                pygame.time.wait(200)
                chat += " enemy's turn \n "

                pygame.display.flip()
                pygame.time.wait(200)
                enemy.WhichAttack(player, chat)

                player.BonusLoss()
                enemy.BonusLoss()

                if player.hp <= 0:
                    chat += " You were defeated."
                    return False

            ######################################
            # Draw
            ######################################

            lines = [
                f"Enemy: {enemy.type}",
                f"Enemy HP: {int(enemy.hp)}/{enemy.maxhp}",
                "",
                f"Player HP: {int(player.hp)}/{player.maxhp}",
                f"Mana: {player.mana}",
                f"Actions: {actions_left}",
                "",
                f"Weapon: {player.currentWeapon.name}",
                f"Armor: {player.currentArmor.name}",
                f"Armor Class: {player.AC + player.BAC}",
                f"Strength: {player.str + player.Bstr}",
                f"Dexterity: {player.dex + player.Bdex}",
                f"Constitution: {player.const + player.Bconst}",
                f"Intelligence: {player.int + player.Bint}",
                f"Wisdom: {player.wis+player.Bwis}",
                f"Charizma: {player.char+player.Bchar}",
                f"Health level: {max_heal_ar[Max_heal_used]}"
                f"Bonus accuracy: {player.Bacc}"
            ]

            screen.fill(BLACK)
            if spell_disp:

                for _, b in SpellButtons:
                    b.draw(screen)
        
            if item_disp:
                for _, b in ItemButtons:
                    b.draw(screen)
            attackButton.draw(screen)
            spellButton.draw(screen)
            itemButton.draw(screen)
            defendButton.draw(screen)
            fleeButton.draw(screen)
            AimButton.draw(screen)

            pygame.draw.rect(
                screen,
                (40,40,40),
                (scale*120,15*scale,240*scale,10*scale)
            )

            pygame.draw.rect(
                screen,
                (200,30,30),
                (scale*120,15*scale,
                 max(0,scale*240*enemy.hp/enemy.maxhp),
                 10*scale)
            )

            pygame.draw.rect(
                screen,
                (40,40,40),
                (scale*120,35*scale,240*scale,10*scale)
            )

            pygame.draw.rect(
                screen,
                (30,180,30),
                (scale*120,35*scale,
                 max(0,scale*240*player.hp/player.maxhp),
                 10*scale)
            )

            linesF.draw_lines(
                panel,
                lines,
                smallfont,
                screen
            )

            chat.Display()
            pygame.display.flip()

    return