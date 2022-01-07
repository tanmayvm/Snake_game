import random
import sys
import time

import pygame

window_X = 600
window_Y = 600

pygame.init()
screen = pygame.display.set_mode((window_X, window_Y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

speed = 10
sposition = [300, 300]

firstSnakebody = [[300, 300], [290, 300], [280, 300], [270, 300], [260, 300], [250, 300], [240, 300], [230, 300],
                  [220, 300], [210, 300], [200, 300], [190, 300]]
firstFruitPosition = [random.randrange(1, (window_X // 10)) * 10, random.randrange(1, (window_Y // 10)) * 10]
fSpawn = True

# Default Direction
sDir = 'RIGHT'
newDir = sDir

# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
playerscore = 0


def gameover():
    if sposition in firstSnakebody:
        score_font = pygame.font.SysFont('times new roman', 40)
        score_surface = score_font.render('Score : ' + str(playerscore), True, red)
        score_rect = score_surface.get_rect()
        score_rect.center = (window_X // 2, window_Y // 2)
        screen.blit(score_surface, score_rect)
        time.sleep(2)
        pygame.quit()

    if sposition[0] == 600 or sposition[0] == 0 or sposition[1] == 600 or sposition[1] == 0:
        score_font = pygame.font.SysFont('times new roman', 40)
        score_surface = score_font.render('Score : ' + str(playerscore), True, red)
        score_rect = score_surface.get_rect()
        score_rect.center = (window_X // 2, window_Y // 4)
        screen.blit(score_surface, score_rect)
        pygame.display.flip()
        time.sleep(2)
        pygame.quit()


def score():
    score_font = pygame.font.SysFont('times new roman', 20)
    score_surface = score_font.render('Score : ' + str(playerscore), True, white)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_DOWN:
                newDir = 'DOWN'
            elif event.key == pygame.K_UP:
                newDir = 'UP'
            elif event.key == pygame.K_RIGHT:
                newDir = 'RIGHT'
            elif event.key == pygame.K_LEFT:
                newDir = 'LEFT'

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if newDir == 'UP' and sDir != 'DOWN':
        sDir = 'UP'
    if newDir == 'DOWN' and sDir != 'UP':
        sDir = 'DOWN'
    if newDir == 'LEFT' and sDir != 'RIGHT':
        sDir = 'LEFT'
    if newDir == 'RIGHT' and sDir != 'LEFT':
        sDir = 'RIGHT'

    if sDir == 'UP':
        sposition[1] -= 10
    if sDir == 'DOWN':
        sposition[1] += 10
    if sDir == 'RIGHT':
        sposition[0] += 10
    if sDir == 'LEFT':
        sposition[0] -= 10
    gameover()

    firstSnakebody.insert(0, list(sposition))
    if sposition[0] == firstFruitPosition[0] and sposition[1] == firstFruitPosition[1]:
        fSpawn = False
        playerscore += 10
        # score()
    else:
        firstSnakebody.pop()

    if not fSpawn:
        firstFruitPosition = [random.randrange(1, (window_X // 10)) * 10, random.randrange(1, (window_Y // 10)) * 10]
    fSpawn = True

    screen.fill(black)
    score()
    for pos in firstSnakebody:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, white, pygame.Rect(firstFruitPosition[0], firstFruitPosition[1], 10, 10))
    pygame.display.update()
    fps.tick(speed)
