import pygame
import configs as con


class Tail:

    def __init__(self, posX, posY):
        self.x = posX
        self.y = posY
        self.width = con.tileWidth

    def render(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), [
                         self.x, self.y, self.width, self.width], 1)
        pygame.draw.rect(screen, (200, 0, 0), [
            self.x + 1, self.y + 1, self.width - 2, self.width - 2])
