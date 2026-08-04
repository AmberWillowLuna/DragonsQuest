import pygame
import spells
import random
import button
import linesF
import colors
import ChatDisplay


class learningPoints:
    def __init__(self):
        self.value = [1,1,2]


def TryLearn(learning_points, b):
    if random.randint(1,4)<=learning_points.value[b]:
        return True
    else:
        learning_points.value[b]+=1
        if b==2:
            learning_points.value[b]+=1
        return False

def Learning(chat, AllSpells, StudySpells, player, time, b, learning_points):
    spell = AllSpells[StudySpells[b]]

    if any(s.name == spell.name for s in player.spells):
        chat += f"You already know {spell.name}."
    else:
        if player.mana < 1:
            chat.value="Not enough mana"
            return 
        else:
            time.add(1)
            learn = TryLearn(learning_points, b)
            if learn:
                player.mana-=1
                chat += f"You have learnt the spell {AllSpells[StudySpells[b]].name}"
                player.spells.append(AllSpells[StudySpells[b]])
            else:
                chat += "You tried to learn the spell but failed"

def Study_magic(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, AllSpells, StudySpells):
    #first you have to choose spell from 3 (overall there are 6 spells, 3 are available at the start, and 3 are unlocked after day 2))
    # one is scroll - 50% to learn in 1h 100% to learn in 2h
    #other two are books - 25% to learn in 1h 50% to learn in 2h, 75% to learn in 3h, 100% to learn in 4h
    #learning a spell costs 1 mana
    #spells should be rerolled each day, so you can learn different spells each day
     
    #ADD A MINIGAMEEEE!!!!


    #info on how it works
    chat += "An old mage looks and you and says: Blue are books - you have 25% to learn then each hour and +25% each hour you spend here, gold is a scroll, you have 50% to learn it and +50% each hour... however remember that to learn it succesfully you need mana"
    #defining things for displaying player stats
    smallfont2=pygame.font.SysFont("Arial", 16)
    panel=pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = linesF.update_lines(player, time.day, time)
    #make buttons for spell learning
    spell1_button=button.Button(20, 100, 440, 100, AllSpells[StudySpells[0]].name, colors.LIGHT_BLUE, (100, 255, 100))
    spell2_button=button.Button(20, 200, 440, 100, AllSpells[StudySpells[1]].name, colors.LIGHT_BLUE, (100, 255, 100))
    spell3_button=button.Button(20, 300, 440, 100, AllSpells[StudySpells[2]].name, colors.GOLD, (100, 255, 100))
    learning_points=learningPoints() #how many tries u made
    backButton= button.Button(50, 400, 400, 100, "Back", colors.LIGHT_BLUE, (100, 255, 100))
    #main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if spell1_button.is_clicked(pygame.mouse.get_pos(), event):
                    Learning(chat, AllSpells, StudySpells, player, time, 0, learning_points)
                elif spell2_button.is_clicked(pygame.mouse.get_pos(), event):
                    Learning(chat, AllSpells, StudySpells, player, time, 1, learning_points)

                elif spell3_button.is_clicked(pygame.mouse.get_pos(), event):
                    Learning(chat, AllSpells, StudySpells, player, time, 2, learning_points)

                elif backButton.is_clicked(pygame.mouse.get_pos(), event):
                    chat.value ="You leave the mage's home."
                    running = False
                lines=linesF.update_lines(player, time.day, time)
                    # Add your back logic here


        #drawing
        screen.fill((0, 0, 0))
        spell1_button.draw(screen)
        spell2_button.draw(screen)
        spell3_button.draw(screen)
        backButton.draw(screen)
        chat.Display()
        linesF.draw_lines(panel, lines, smallfont2, screen)
        pygame.display.flip()