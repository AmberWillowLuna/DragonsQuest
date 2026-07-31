from types import NoneType
import pygame
import button
import ChatDisplay
import linesF
import colors
import basic_functions
import BattlePicker
import spell_battle

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)




def Battle(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
           player, enemy, chat):
    BattlePicker.ChooseEquipment(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
                    player, chat)
    font = pygame.font.SysFont("Arial", 24)
    smallfont = pygame.font.SysFont("Arial", 16)
    spell_disp=False
    panel = pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)

    actions_left = 2

    SpellButtons=spell_battle.PlayerSpellsToButtons(player)

    attackButton = button.Button(
        20, 20, 220, 60,
        "Attack",
        colors.LIGHT_BLUE,
        (100,255,100)
    )

    spellButton = button.Button(
        20, 100, 220, 60,
        "Spell",
        colors.LIGHT_BLUE,
        (100,255,100)
    )

    itemButton = button.Button(
        20, 180, 220, 60,
        "Item",
        colors.LIGHT_BLUE,
        (100,255,100)
    )

    defendButton = button.Button(
        20, 260, 220, 60,
        "Defend",
        colors.LIGHT_BLUE,
        (100,255,100)
    )

    fleeButton = button.Button(
        20, 420, 220, 60,
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


                chat = player.currentWeapon.attack(player, enemy, chat)


                actions_left -= 1

            ###############################
            # SPELL
            ###############################

            elif spellButton.is_clicked(mouse, event):
                if spell_disp==False:
                    spell_disp=True
                else:
                    spell_disp==False
                chat = "spells shown"

            ###############################
            # ITEM
            ###############################

            elif itemButton.is_clicked(mouse, event):

                chat = "Item system not implemented yet."
                actions_left -= 1

            ###############################
            # DEFEND
            ###############################

            elif defendButton.is_clicked(mouse, event):

                player.BAC += 2
                player.BACC+=2
                chat = "You prepare for incoming attacks."

                actions_left -= 1

            ###############################
            # FLEE
            ###############################

            elif fleeButton.is_clicked(mouse, event):

                if basic_functions.roll_dice(20) + player.dex > 12:
                    chat = "You escaped."
                    return False

                else:
                    chat = "You failed to escape."
                    actions_left = 0



            elif spell_disp:
                spell_used = False

                for spell, b in SpellButtons:

                    if b.is_clicked(mouse, event):

                        chat = spell.cast(player, enemy, chat)

                        spell_disp = False
                        spell_used = True

                        break

                if spell_used:
                    actions_left -= 1
                    continue
            ######################################
            # Enemy turn
            ######################################

            if enemy.hp <= 0:
                chat = f"You defeated the {enemy.type} !"
                player.gold+=enemy.gold
                return True

            if actions_left <= 0:

                actions_left = 2
                pygame.time.wait(500)
                ChatDisplay.ClearChat(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
                chat = "enemy's turn"
                ChatDisplay.ChatDisplay(
                    chat,
                    screen,
                    SCREEN_WIDTH,
                    SCREEN_HEIGHT,
                    smallfont
                )

                pygame.display.flip()
                pygame.time.wait(500)
                chat = enemy.WhichAttack(player, chat)

                player.BonusLoss()
                enemy.BonusLoss()

                if player.hp <= 0:
                    chat = "You were defeated."
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
        ]

        screen.fill(BLACK)
        if spell_disp:

            for _, b in SpellButtons:
                b.draw(screen)

        attackButton.draw(screen)
        spellButton.draw(screen)
        itemButton.draw(screen)
        defendButton.draw(screen)
        fleeButton.draw(screen)

        pygame.draw.rect(
            screen,
            (40,40,40),
            (280,30,250,30)
        )

        pygame.draw.rect(
            screen,
            (200,30,30),
            (280,30,
             max(0,250*enemy.hp/enemy.maxhp),
             30)
        )

        pygame.draw.rect(
            screen,
            (40,40,40),
            (280,80,250,30)
        )

        pygame.draw.rect(
            screen,
            (30,180,30),
            (280,80,
             max(0,250*player.hp/player.maxhp),
             30)
        )

        linesF.draw_lines(
            panel,
            lines,
            smallfont,
            screen
        )

        ChatDisplay.ChatDisplay(
            chat,
            screen,
            SCREEN_WIDTH,
            SCREEN_HEIGHT,
            smallfont
        )

        pygame.display.flip()