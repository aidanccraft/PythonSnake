import pygame
import random


class Grid:

    def __init__(self, width, height, tileWidth):
        self.width = width
        self.height = height
        self.tileWidth = tileWidth
        self.currentFood = [5, 5]

    def render(self, screen):
        for i in range(0, self.width):
            for j in range(0, self.height):
                pygame.draw.rect(screen, (50, 50, 50), [
                    i * self.tileWidth, j * self.tileWidth, self.tileWidth, self.tileWidth], 1)
                pygame.draw.rect(screen, (0, 0, 0), [
                    i * self.tileWidth + 1, j * self.tileWidth + 1, self.tileWidth - 2, self.tileWidth - 2])

        pygame.draw.rect(screen, (255, 255, 0), [self.currentFood[0] * self.tileWidth + self.tileWidth / 4 + 1,
                                                 self.currentFood[1] *
                                                 self.tileWidth + self.tileWidth / 4 + 1,
                                                 self.tileWidth / 2, self.tileWidth / 2])

    def setFood(self, snake):
        x = random.randint(0, self.width - 1)
        y = random.randint(0, self.height - 1)
        for i in range(0, snake.length):
            if(snake.tails[i].x == x and snake.tails[i].y == y):
                self.setFood(snake)
        self.currentFood = [x, y]
