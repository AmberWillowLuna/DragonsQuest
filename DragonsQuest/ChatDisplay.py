import button
import pygame
import textwrap

class ChatDisplay:  
    def __init__(self, screen, SCREEN_WIDTH, SCREEN_HEIGHT, font):
        self.screen = screen
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.font = font
        self.value = "Welcome to Dragon's Quest!"


    def __iadd__(self, other):
        # Override += to update self.value
        self.value += other
        if len(self.value)>=270:
            self.value=self.value[-200:]
        return self  # Return self to allow chainings


    def ClearChat(self):
            self.value=""
            self.Display()

    def Display(self):
        if self is not None:
            pygame.draw.rect(
            self.screen,
            (0, 0, 0),
            (0, self.SCREEN_HEIGHT - 100, self.SCREEN_WIDTH, 100)
            )

        # Wrap the text to a maximum of 47 characters per line

            lines = textwrap.wrap(self.value, width=40)

            # Starting position
            y = self.SCREEN_HEIGHT - self.SCREEN_HEIGHT // 4

            for line in lines:
                chat_surface = self.font.render(line, True, (255, 255, 255))

                rect = chat_surface.get_rect()
                rect.topright = (self.SCREEN_WIDTH - 10, y)

                self.screen.blit(chat_surface, rect)

                y += self.font.get_linesize()
