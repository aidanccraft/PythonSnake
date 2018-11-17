import tail
import configs as con


class Snake:

    moves = 0

    def __init__(self, initLength):
        self.length = initLength
        self.tails = []
        self.dead = False
        for i in range(0, self.length):
            self.tails.insert(i, tail.Tail(0, 0))

    def move(self, speed, grid):
        if(not speed[0] == 0 or not speed[1] == 0):
            self.moves += 1

        for i in range(0, self.length):
            if(self.moves > 1):
                if(self.tails[i].x == self.tails[0].x +
                        speed[0] * self.tails[i].width and
                        self.tails[i].y == self.tails[0].y +
                        speed[1] * self.tails[i].width):
                    self.dead = True
                    return
                if(self.tails[0].x < 0 or
                        self.tails[0].y < 0 or
                        self.tails[0].x > (grid.width - 1) * grid.tileWidth or
                        self.tails[0].y > (grid.height - 1) * grid.tileWidth):
                    self.dead = True
                    return

        for i in range(self.length - 1, -1, -1):
            if(not i == 0):
                self.tails[i].x = self.tails[i - 1].x
                self.tails[i].y = self.tails[i - 1].y
            else:
                self.tails[i].x = self.tails[i].x + \
                    speed[0] * self.tails[i].width
                self.tails[i].y = self.tails[i].y + \
                    speed[1] * self.tails[i].width

        self.checkFood(grid)

    def checkFood(self, grid):
        if(self.tails[0].x / self.tails[0].width == grid.currentFood[0] and
                self.tails[0].y / self.tails[0].width == grid.currentFood[1]):
            self.tails.insert(self.length,
                              tail.Tail(self.tails[self.length - 1].x, self.tails[self.length - 1].y))
            self.length += 1
            grid.setFood(self)

    def render(self, screen):
        for tail in self.tails:
            tail.render(screen)

        textsurface = con.font.render(
            'Score: ' + str(self.length), True, (255, 0, 0))
        textrect = textsurface.get_rect()
        textrect.centerx = 100
        textrect.centery = 20
        screen.blit(textsurface, textrect)
