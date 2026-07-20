import pygame

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, screen_width, screen_height):
        super().__init__()
        self.original_image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(
            self.original_image,
            (screen_width, screen_height)
        )
        self.rect = self.image.get_rect()
        self.rect.x = 0  # Position at the top-left corner
        self.rect.y = 0
