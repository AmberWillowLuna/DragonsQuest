
# import other stuff - screen, etc
from re import S
from player import Player
import json
import game
import pygame

def start_game(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock):
    #print("Welcome to Dragon's Quest!")
    #print("Your adventure begins now...")
    # Add more game logic here
    #picture of the start
    starting = True
    start_text = font.render("Welcome to Dragon's Quest!", True, (255, 255, 255))
    bottom_text =  font.render("Press any key to continue...", True, (255, 255, 255))
    while starting:
        #display image
        screen.fill((0, 0, 0))  # Clear the screen with black
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 100))
        screen.blit(bottom_text, (SCREEN_WIDTH // 2 - bottom_text.get_width() // 2, SCREEN_HEIGHT - 100))
        #go forward when event is keydown
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                starting = False
            elif event.type == pygame.KEYDOWN:
                starting = False
        pygame.display.flip()
        clock.tick(60)



    #player initialization
    player = Player()
    file_path = "run.json"
    with open(file_path, "w") as file:
        json.dump({}, file)


    #print("Your character has been created!")
    #create a file for player
    #start the actual game!
    game.game(screen, SCREEN_WIDTH, SCREEN_HEIGHT, font, clock, player)

