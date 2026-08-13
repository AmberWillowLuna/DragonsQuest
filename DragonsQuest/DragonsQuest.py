from re import S
import pygame
pygame.init()
import sys
import random
import player
import enemies
import tavern
import meditation
import spells
import magic_learning
import json
import start
import game
from button import Button
import colors
import options
import json

#get screen size from settings file
#as well as state




SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
titles=["Dragon's quest", "Elf vs dragon", "Can I seduce the dragon?", "Dragon's and dragon's", "quests, quests, quests...", "title for my cool game"]
pygame.display.set_caption(random.choice(titles))

font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 30)



def main():

    #get the state from settings file
    # Get the state from settings file
    with open("settings.json", "r", encoding="utf-8") as file:
        settings = json.load(file)

    STATE = settings["state"]
    Resolution = settings["resolution"]

    new_width, new_height = map(int, Resolution.split("x"))
    SCREEN_WIDTH = new_width
    SCREEN_HEIGHT = new_height

    if STATE == "Fullscreen":
        screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            pygame.FULLSCREEN
        )
    else:
        screen = pygame.display.set_mode(
            (SCREEN_WIDTH, SCREEN_HEIGHT),
        )

    scale = 1.0*SCREEN_WIDTH/640




    start_button = Button(240*scale, 100*scale, 160*scale, 40*scale, "Start", colors.NAVY_BLUE, colors.GREEN)
    continue_button = Button(240*scale, 160*scale, 160*scale, 40*scale, "Continue", colors.NAVY_BLUE, colors.GREEN)
    options_button = Button(240*scale, 220*scale, 160*scale, 40*scale, "Options", colors.NAVY_BLUE, colors.GREEN)
    exit_button = Button(240*scale, 280*scale, 160*scale, 40*scale, "Exit", colors.NAVY_BLUE, colors.GREEN)

    clock = pygame.time.Clock()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Check button clicks
            if start_button.is_clicked(mouse_pos, event):
                start.start_game(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock)
                # Add your start game logic here
            if options_button.is_clicked(mouse_pos, event):
                options.options(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock)
                # Add your options menu logic here
            if continue_button.is_clicked(mouse_pos, event):
                i=-1
                # Add your continue game logic here
            if exit_button.is_clicked(mouse_pos, event):
                running = False

        # Check button hover
        start_button.check_hover(mouse_pos)
        options_button.check_hover(mouse_pos)
        exit_button.check_hover(mouse_pos)

        # Draw everything
        screen.fill(colors.BLACK)
        title_text = font.render("Dragon's quest", True, colors.WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        start_button.draw(screen)
        options_button.draw(screen)
        exit_button.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()