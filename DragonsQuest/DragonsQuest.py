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
from button import Button


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
titles=["Dragon's quest", "Elf vs dragon", "Can I seduce the dragon?", "Dragon's and dragon's", "quests, quests, quests...", "title for my cool game"]
pygame.display.set_caption(random.choice(titles))

font = pygame.font.SysFont("Arial", 40)
small_font = pygame.font.SysFont("Arial", 30)

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

def main():
    #main tittle buttons
    # Create buttons

    start_button = Button(300, 200, 200, 50, "Start", LIGHT_BLUE, (100, 255, 100))
    continue_button = Button(300, 200, 200, 50, "Continue", LIGHT_BLUE, (100, 255, 100))
    options_button = Button(300, 300, 200, 50, "Options", LIGHT_BLUE, (100, 100, 255))
    exit_button = Button(300, 400, 200, 50, "Exit", LIGHT_BLUE, (255, 100, 100))

    clock = pygame.time.Clock()
    running = True

    while running:
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check button clicks
            if start_button.is_clicked(mouse_pos, event):
                print("Start button clicked!")
                # Add your start game logic here
            if options_button.is_clicked(mouse_pos, event):
                print("Options button clicked!")
                # Add your options menu logic here
            if exit_button.is_clicked(mouse_pos, event):
                running = False

        # Check button hover
        start_button.check_hover(mouse_pos)
        options_button.check_hover(mouse_pos)
        exit_button.check_hover(mouse_pos)

        # Draw everything
        screen.fill(NAVY_BLUE)
        title_text = font.render("Dragon's quest", True, LIGHT_BLUE)
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