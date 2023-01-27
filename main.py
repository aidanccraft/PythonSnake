import pygame
import math
import snake
import input
import grid
import configs as con

pygame.init()

size = (con.width, con.height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")
done = False
speed = [0, 0]

clock = pygame.time.Clock()
inputs = input.Input()
gameSnake = snake.Snake(5)
tileGrid = grid.Grid(math.floor(con.width / con.tileWidth),
                     math.floor(con.height / con.tileWidth), con.tileWidth)

tileGrid.setFood(gameSnake)

while not done:
    # Input
    inputs.update()

    if(inputs.shouldClose()):
        done = True

    if inputs.isKeyPressed(pygame.K_a) and speed[0] == 0:
        speed[0] = -1
        speed[1] = 0
    if inputs.isKeyPressed(pygame.K_d) and speed[0] == 0:
        speed[0] = 1
        speed[1] = 0
    if inputs.isKeyPressed(pygame.K_w) and speed[1] == 0:
        speed[0] = 0
        speed[1] = -1
    if inputs.isKeyPressed(pygame.K_s) and speed[1] == 0:
        speed[0] = 0
        speed[1] = 1
    if inputs.isKeyPressed(pygame.K_ESCAPE):
        done = True

    if(gameSnake.dead):
        if inputs.isKeyPressed(pygame.K_SPACE):
            gameSnake = snake.Snake(5)
            tileGrid.setFood(gameSnake)
            speed = [0, 0]

    # Game logic
    if(not gameSnake.dead):
        gameSnake.move(speed, tileGrid)

    # Rendering done here
    screen.fill([255, 255, 255])

    tileGrid.render(screen)
    gameSnake.render(screen)

    if(gameSnake.dead):
        gameOver = con.font.render(
            'Game Over!', True, (255, 0, 0))
        playAgain = con.font.render(
            'Press Space to play again', True, (255, 0, 0))
        textRect = gameOver.get_rect()
        textRect2 = playAgain.get_rect()
        textRect.centerx = screen.get_rect().centerx
        textRect.centery = screen.get_rect().centery - 15
        textRect2.centerx = screen.get_rect().centerx
        textRect2.centery = screen.get_rect().centery + 15
        screen.blit(gameOver, textRect)
        screen.blit(playAgain, textRect2)

    pygame.display.flip()

    # FPS
    clock.tick(10)
