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
                (0, self.SCREEN_HEIGHT, 0, self.SCREEN_HEIGHT)
            )

        # Wrap the text to a maximum of 47 characters per line
        lines = textwrap.wrap(self.value, width=40)

        # Calculate the starting y position for the middle of the screen
        # This positions the chat starting from 2/3rds of the screen height
        y = (self.SCREEN_HEIGHT * 2 // 3)  # Adjust this value to fine-tune the position

        for line in lines:
            chat_surface = self.font.render(line, True, (255, 255, 255))

            # Center-align the text horizontally
            rect = chat_surface.get_rect()
            rect.centerx = self.SCREEN_WIDTH*2 // 3  # Center horizontally
            rect.centery = y  # Center vertically for each line

            self.screen.blit(chat_surface, rect)
            y += self.font.get_linesize()
