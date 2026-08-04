from tkinter import W
import pygame
import sys
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
        if self.value>15:
            self.value=0
            self.day+=1
            self.q=True
            

def game(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock, player):
    #creating panel of the game with stats etc
    time = TimeClass()  #time in hours but 16/ day - then sleep
    #some actions will cost 1h others 
    smallfont = pygame.font.SysFont("Arial", 16)
    chat = ChatDisplay.ChatDisplay(screen, SCREEN_WIDTH, SCREEN_HEIGHT, smallfont)  #chat +box for the player to see what happened
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

    study_button =  Button(100, 50, 300, 100, "Study magic", colors.LIGHT_BLUE, (100, 255, 100))
    smith_button =  Button(100, 150, 300, 100, "Smith", colors.LIGHT_BLUE, (100, 255, 100))
    meditation_button =  Button(100, 250, 300, 100, "Meditation", colors.LIGHT_BLUE, (100, 255, 100))
    tavern_button =  Button(100, 350, 300, 100, "Tavern", colors.LIGHT_BLUE, (100, 255, 100))
    quests_button =  Button(100, 450, 300, 100, "Villager's quests", colors.LIGHT_BLUE, (100, 255, 100))
    #make 7 classes of spells possible to lerarn:
    #fireball, self cure, hyperfocus, turtle shells, ray of doom, poisonous breath, arcanus shot
    AllSpells=[spells.fireball(), spells.selfCure(), spells.hyperfocus(), spells.turtleShells(), spells.rayOfDoom(), spells.poisonousBreath(), spells.arcanusShot()]
    #drawing 3 spells to learn
    StudySpells = random.sample(range(1, 7), 3)
    #weapons
    AllWeapons = [weapons.basic_dagger(), weapons.iron_sword(), weapons.steel_sword(), weapons.miths_hammer(), weapons.galaxyDagger(), weapons.terra_blade(), weapons.enchanted_diamond_sword(), weapons.legendary_dragon_slayer(), weapons.obanium_sword(), weapons.crystal_sword(), weapons.crystal_sword(), weapons.magic_bow(), weapons.flamethrower(), weapons.mace_of_destruction(), weapons.dark_sword(), weapons.arcanus_sword()]
    #armors
    AllArmory = [armors.leather_armor(), armors.rubin_amulet(), armors.steel_armor(), armors.dragon_scale_armor(), armors.crown_of_fools(), armors.chainmail(), armors.miths_armor(), armors.legendary_armor(), armors.grassy_armor(), armors.enchanted_armor(), armors.crystal_armor()]

    TheDragon=dragons.drawRandomDragon()

    DailyQuests = quests.RandomQuests()

    enemy=drawRandomEnemy()

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
                # Add your study magic logic here
            elif smith_button.is_clicked(mouse_pos, event):
                print("Smith button clicked!")
                smith.Smith(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, AllArmory, AllWeapons)
                lines=linesF.update_lines(player, time.day, time)
                # Add your smith logic here
            elif meditation_button.is_clicked(mouse_pos, event):
                meditation.Meditate(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font)
                lines=linesF.update_lines(player, time.day, time)
                # Add your meditation logic here
            elif tavern_button.is_clicked(mouse_pos, event):
                print("Tavern button clicked!")
                tavern.Tavern(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, TheDragon)
                lines=linesF.update_lines(player, time.day, time)
                # Add your tavern logic here
            elif quests_button.is_clicked(mouse_pos, event):
                print("Villager's quests button clicked!")
                VillagersQuests.QuestBoard(player, time, chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, DailyQuests, enemy)
                lines=linesF.update_lines(player, time.day, time)
                # Add your quests logic here
        # Game logic goes here

        if time.day==3:
                Battle.Battle(screen, SCREEN_WIDTH, SCREEN_HEIGHT, player, TheDragon, chat)
                time.day=4
                if TheDragon.hp<=0:
                    chat.VALUE=" You have defeated the dragon! You win the game!"
                #Fight the dragon!!!!!!!
        #NEW DAY - QUESTS RESETS
        if time.q==True:
            time.q=False
            DailyQuests = quests.RandomQuests()
            enemy=drawRandomEnemy()
            StudySpells = random.sample(range(1, 7), 3)

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
    pygame.quit()
    sys.exit()