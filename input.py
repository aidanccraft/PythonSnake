import pygame


class Input:

    def __init__(self):
        self.close = False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close = True

    def isKeyPressed(self, key):
        keys = pygame.key.get_pressed()
        if keys[key]:
            return True
        return False

    def shouldClose(self):
        return self.close
