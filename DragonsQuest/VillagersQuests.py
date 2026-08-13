import pygame
import random
import button
import colors
import ChatDisplay
import linesF
import quests      # contains Quest and RandomQuests()
import Battle


def QuestBoard(player, time, chat,
               screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, DailyQuests, enemy):

    chat.value=" "
    chat += "The village notice board is filled with requests."

    smallfont2 = pygame.font.SysFont("Arial", 16)

    panel = pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = linesF.update_lines(player, time.day, time)

    scale = 1.0*SCREEN_WIDTH/640

    quest1 = button.Button(
        10*scale, 20*scale, 300*scale, 40*scale,
        f"{DailyQuests[0].name} ({DailyQuests[0].price}g)",
        colors.NAVY_BLUE,
        colors.GREEN
    )

    quest2 = button.Button(
        10*scale, 70*scale,  300*scale, 40*scale,
        f"{DailyQuests[1].name} ({DailyQuests[1].price}g)",
        colors.NAVY_BLUE,
        colors.GREEN
    )

    quest3 = button.Button(
        10*scale, 120*scale,  300*scale, 40*scale,
        f"{DailyQuests[2].name} ({DailyQuests[2].price}g)",
        colors.NAVY_BLUE,
        colors.GREEN
    )

    fightQuest = button.Button(
        10*scale, 170*scale,  300*scale, 40*scale,
        f"Monster Hunt: {enemy.type}",
        colors.RED,
        colors.GOLD
    )

    backButton = button.Button(
        15*scale, 225*scale,  250*scale, 40*scale,
        "Back",
        colors.NAVY_BLUE,
        colors.GREEN
    )

    running = True

    while running:

        mouse = pygame.mouse.get_pos()

        quest1.check_hover(mouse)
        quest2.check_hover(mouse)
        quest3.check_hover(mouse)
        fightQuest.check_hover(mouse)
        backButton.check_hover(mouse)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if quest1.is_clicked(mouse, event):

                    if DailyQuests[0].finished:
                        chat += "You have already completed this quest."
                    else:
                        DailyQuests[0].run(
                            screen,
                            SCREEN_WIDTH,
                            SCREEN_HEIGHT,
                            font,
                            player,
                            time,
                            chat
                        )

                elif quest2.is_clicked(mouse, event):
                    if DailyQuests[1].finished:
                        chat += "You have already completed this quest."
                    else:
                        DailyQuests[1].run(
                            screen,
                            SCREEN_WIDTH,
                            SCREEN_HEIGHT,
                            font,
                            player,
                            time,
                            chat
                        )
                elif quest3.is_clicked(mouse, event):

                    if DailyQuests[2].finished:
                        chat += "You have already completed this quest."
                    else:
                        DailyQuests[2].run(
                            screen,
                            SCREEN_WIDTH,
                            SCREEN_HEIGHT,
                            font,
                            player,
                            time,
                            chat
                        )
                elif fightQuest.is_clicked(mouse, event):
                    if enemy.hp<=0:
                        chat += "You have already killed this enemy."
                    else:
                        Battle.Battle(screen, SCREEN_WIDTH, SCREEN_HEIGHT,
                        player, enemy, chat)
                        time.add(2)

                elif backButton.is_clicked(mouse, event):
                    chat += "You leave the quest board."
                    running = False

                lines = linesF.update_lines(player, time.day, time)

        screen.fill((0,0,0))

        quest1.draw(screen)
        quest2.draw(screen)
        quest3.draw(screen)
        fightQuest.draw(screen)
        backButton.draw(screen)

        chat.Display()

        linesF.draw_lines(
            panel,
            lines,
            smallfont2,
            screen
        )

        pygame.display.flip()