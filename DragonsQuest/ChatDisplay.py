import button
import pygame
import textwrap

def ClearChat(screen, SCREEN_WIDTH, SCREEN_HEIGHT):
            pygame.draw.rect(
            screen,
            (0, 0, 0),
            (0, SCREEN_HEIGHT, 0, SCREEN_WIDTH)
             )
            pygame.display.flip()

def ChatDisplay(chat, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font):
    if chat is not None:
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100)
        )

        # Wrap the text to a maximum of 47 characters per line
    
        lines = textwrap.wrap(chat, width=47)

        # Starting position
        y = SCREEN_HEIGHT - SCREEN_HEIGHT // 4

        for line in lines:
            chat_surface = font.render(line, True, (255, 255, 255))

            rect = chat_surface.get_rect()
            rect.topright = (SCREEN_WIDTH - 10, y)

            screen.blit(chat_surface, rect)

            y += font.get_linesize()

        return chat
    return