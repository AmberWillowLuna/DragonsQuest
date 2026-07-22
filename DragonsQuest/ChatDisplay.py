import button
import pygame
def ChatDisplay(chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font):
    # Display the chat message on the screen
    # This function should be called whenever you want to update the chat display
    # For example, after a player action or event in the game
    # You can customize the display logic as needed

    # Clear the screen or a specific area for chat display
    pygame.draw.rect(screen, (0, 0, 0), (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))  # Clear chat area

    # Render the chat text
    chat_surface = font.render(chat, True, (255, 255, 255))
    screen.blit(chat_surface, (10, SCREEN_HEIGHT - 90))  # Position the chat text

    # Update the display to show the new chat message
