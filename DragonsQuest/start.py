
# import other stuff - screen, etc
from re import S


def start_game(screen):
    #print("Welcome to Dragon's Quest!")
    #print("Your adventure begins now...")
    # Add more game logic here
    #picture of the start
    starting = true
    start_text = font.render("Welcome to Dragon's Quest!", True, (255, 255, 255))
    bottom_text = font.render("Press any key to continue...", True, (255, 255, 255))
    while starting:
        #display image
        screen.fill((0, 0, 0))  # Clear the screen with black



