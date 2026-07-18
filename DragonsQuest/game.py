import pygame
import sys
from player import Player
import json
from button import Button
import meditation

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (220, 220, 220)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
NAVY_BLUE = (0, 0, 128)

def update_lines(player, day, time):
    return [
        f"Player Stats:",
        f"Health: {player.hp}/{player.maxhp}",
        f"Mana: {player.mana}",
        f"Strength: {player.str + player.Bstr}",
        f"Dexterity: {player.dex + player.Bdex}",
        f"Constitution: {player.const + player.Bconst}",
        f"Wisdom: {player.wis + player.Bwis}",
        f"Intelligence: {player.int + player.Bint}",
        f"Charisma: {player.char + player.Bchar}",
        f"Day: {day}",
        f"Time: {time.value} / 16"
    ]

class TimeClass:
    def __init__(self):
        self.value = 0


def game(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock, player):
    #creating panel of the game with stats etc
    day=0 #on day 3 you fight the dragon
    time = TimeClass()  #time in hours but 16/ day - then sleep
    #some actions will cost 1h others 2
    chat = ""  #chat box for the player to see what happened
    #1 rectangle as background on the right upper corner
    smallfont = pygame.font.SysFont("Arial", 16)
    panel=pygame.Rect(SCREEN_WIDTH - 250, 0, 250, 250)
    lines = update_lines(player, day, time)

    #2initializing options to spend time - buttons
    #study magic
    #smith
    #meditation
    #tavern (and shop)
    #quest table (4 quests each day)
    #on day 3 fight the dragon

    study_button =  Button(100, 50, 300, 100, "Study magic", LIGHT_BLUE, (100, 255, 100))
    smith_button =  Button(100, 150, 300, 100, "Smith", LIGHT_BLUE, (100, 255, 100))
    meditation_button =  Button(100, 250, 300, 100, "Meditation", LIGHT_BLUE, (100, 255, 100))
    tavern_button =  Button(100, 350, 300, 100, "Tavern", LIGHT_BLUE, (100, 255, 100))
    quests_button =  Button(100, 450, 300, 100, "Villager's quests", LIGHT_BLUE, (100, 255, 100))

    

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
                # Add your study magic logic here
            elif smith_button.is_clicked(mouse_pos, event):
                print("Smith button clicked!")
                # Add your smith logic here
            elif meditation_button.is_clicked(mouse_pos, event):
                meditation.Meditate(player, time, chat)
                lines=update_lines(player, day, time)
                # Add your meditation logic here
            elif tavern_button.is_clicked(mouse_pos, event):
                print("Tavern button clicked!")
                # Add your tavern logic here
            elif quests_button.is_clicked(mouse_pos, event):
                print("Villager's quests button clicked!")
                # Add your quests logic here
        # Game logic goes here

        # Clear the screen
        screen.fill((0, 0, 0))
        
        # Draw everything
        #display panel and stats:
        pygame.draw.rect(screen, (50, 50, 50), panel)
        y_offset = panel.y + 10
        for line in lines:
            line_surface = smallfont.render(line, True, (255, 255, 255))
            screen.blit(line_surface, (panel.x + 10, y_offset))
            y_offset += line_surface.get_height()

        study_button.draw(screen)
        smith_button.draw(screen)
        meditation_button.draw(screen)
        tavern_button.draw(screen)
        quests_button.draw(screen)


        # Update the display
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
    sys.exit()