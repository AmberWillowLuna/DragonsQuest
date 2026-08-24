from tkinter import W
import pygame
import sys
from achievementManage import AchievementManage
from dragons import dragon
from enemies import drawRandomEnemy
from player import Player
import json
from button import Button
import meditation
import tavern
import colors
import spells
import random
import magic_learning
import linesF
import weapons
import armors
import smith
import dragons
import VillagersQuests
import quests
import Battle
import ChatDisplay

class TimeClass:
    def __init__(self):
        self.value = 0
        self.day=0
        self.q=False
    def add(self, amount):
        self.value+=amount
        if self.value>19:
            self.value=0
            self.day+=1
            self.q=True
            

def game(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock, player):
    #creating panel of the game with stats etc
    time = TimeClass()  #time in hours but 16/ day - then sleep
    #some actions will cost 1h others 
    
    scale = 1.0*SCREEN_WIDTH/640
    smallfont = pygame.font.SysFont("Arial", int(8*scale))
    chatFont = pygame.font.SysFont("Arial", int(16*scale))

    chat = ChatDisplay.ChatDisplay(screen, SCREEN_WIDTH, SCREEN_HEIGHT, chatFont)  #chat +box for the player to see what happened
    #1 rectangle as background on the right upper corner

    panel=pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = linesF.update_lines(player, time.day, time)
    #2initializing options to spend time - buttons
    #study magic
    #smith
    #meditation
    #tavern (and shop)
    #quest table (4 quests each day)
    #on day 3 fight the dragon

    study_button =  Button(50*scale, 10*scale, 150*scale, 50*scale, "Study magic", colors.NAVY_BLUE, colors.GREEN)
    smith_button =  Button(50*scale, 80*scale, 150*scale, 50*scale, "Smith", colors.NAVY_BLUE, colors.GREEN)
    meditation_button =  Button(50*scale, 150*scale, 150*scale, 50*scale, "Meditation", colors.NAVY_BLUE, colors.GREEN)
    tavern_button =  Button(50*scale, 220*scale, 150*scale, 50*scale, "Tavern", colors.NAVY_BLUE, colors.GREEN)
    quests_button =  Button(50*scale, 290*scale, 150*scale, 50*scale, "Villager's quests", colors.NAVY_BLUE, colors.GREEN)
    #make 7 classes of spells possible to lerarn:
    #fireball, self cure, hyperfocus, turtle shells, ray of doom, poisonous breath, arcanus shot
    AllSpells=[spells.fireball(), spells.selfCure(), spells.hyperfocus(), spells.turtleShells(), spells.rayOfDoom(), spells.poisonousBreath(), spells.arcanusShot()]
    #drawing 3 spells to learn
    StudySpells = random.sample(range(0, 6), 3)
    #weapons
    AllWeapons = [weapons.basic_dagger(), weapons.iron_sword(), weapons.steel_sword(), weapons.miths_hammer(), weapons.galaxyDagger(), weapons.terra_blade(), weapons.enchanted_diamond_sword(), weapons.legendary_dragon_slayer(), weapons.obanium_sword(), weapons.crystal_sword(), weapons.crystal_sword(), weapons.magic_bow(), weapons.flamethrower(), weapons.mace_of_destruction(), weapons.dark_sword(), weapons.arcanus_sword()]
    #armors
    AllArmory = [armors.leather_armor(), armors.rubin_amulet(), armors.steel_armor(), armors.dragon_scale_armor(), armors.crown_of_fools(), armors.chainmail(), armors.miths_armor(), armors.legendary_armor(), armors.grassy_armor(), armors.enchanted_armor(), armors.crystal_armor()]

    TheDragon=dragons.drawRandomDragon()

    DailyQuests = quests.RandomQuests()

    enemy=drawRandomEnemy()

    #meditation 5 times in a row achievement counter
    Mctr = 0

    # Main game loop
    running = True
    while running: 
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            #checking buttons
            if study_button.is_clicked(mouse_pos, event):
                print("Study magic button clicked!")
                magic_learning.Study_magic(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, AllSpells,StudySpells)
                lines=linesF.update_lines(player, time.day, time)
                Mctr = 0
                # Add your study magic logic here
            elif smith_button.is_clicked(mouse_pos, event):
                print("Smith button clicked!")
                smith.Smith(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, AllArmory, AllWeapons)
                lines=linesF.update_lines(player, time.day, time)
                Mctr = 0
                # Add your smith logic here
            elif meditation_button.is_clicked(mouse_pos, event):
                meditation.Meditate(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font)
                lines=linesF.update_lines(player, time.day, time)
                Mctr +=1
                if Mctr==5:
                    AchievementManage.Achieve("Zen master")

                # Add your meditation logic here
            elif tavern_button.is_clicked(mouse_pos, event):
                print("Tavern button clicked!")
                tavern.Tavern(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, TheDragon)
                lines=linesF.update_lines(player, time.day, time)
                Mctr = 0
                # Add your tavern logic here
            elif quests_button.is_clicked(mouse_pos, event):
                print("Villager's quests button clicked!")
                VillagersQuests.QuestBoard(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, DailyQuests, enemy)
                lines=linesF.update_lines(player, time.day, time)
                Mctr = 0
                # Add your quests logic here
        # Game logic goes here



        if time.day==3:
                Battle.Battle(screen, SCREEN_WIDTH, SCREEN_HEIGHT, player, TheDragon, chat)
                time.day=4
                if TheDragon.hp<=0:
                    screen.fill((0, 0, 0))
                    chat.value=" You have defeated the dragon! You win the game!"
                    chat.Display()
                    AchievementManage.Achieve("The chosen one")
                    AchievementManage.DragonSlayed(TheDragon.type)
                    pygame.display.flip()
                    pygame.time.wait(2500)
                    running=False
                    return
                #Fight the dragon!!!!!!!
        #NEW DAY - QUESTS RESETS

        if player.hp<=0:
            screen.fill((0, 0, 0))
            chat.value="You have died. Game over."
            chat.Display()
            pygame.display.flip()
            pygame.time.wait(2500)
            running=False
            return

        if time.q==True:
            time.q=False
            DailyQuests = quests.RandomQuests()
            enemy=drawRandomEnemy()
            StudySpells = random.sample(range(1, 7), 3)
            player.discountA=0
            player.discountB=0
            if player.mana_exhaust<3:
                player.mana_exhaust+=1

            #reset quests and

        # Clear the screen
        screen.fill((0, 0, 0))
        #pygame.draw.rect(screen, (50, 50, 50), panel)
        linesF.draw_lines(panel, lines, smallfont, screen)
        # Draw everything
        #display panel and stats:


        chat.Display()
        study_button.draw(screen)
        smith_button.draw(screen)
        meditation_button.draw(screen)
        tavern_button.draw(screen)
        quests_button.draw(screen)


        # Update the display
        pygame.display.flip()

    return
