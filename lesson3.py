import pygame
import time
from random import randint

R = 35
sizeX, sizeY = 1000, 500

def border(X, Y, vx, vy):
    if X - R <= 0:
        vx = -vx
    elif X + R >= sizeX:
        vx = -vx
    elif Y - R <= 0:
        vy = -vy
    elif Y + R >= sizeY:
        vy = -vy

    return [vx, vy]

def border_key(X, Y, g):
    if X - R <= 0:
        X = R
    if X + R >= sizeX:
        X = sizeX - R
    if Y - R <= 0:
        Y = R
    if Y + R >= sizeY:
        Y = sizeY - R
        g = 0

    return [X, Y, g]

def dist(X, Y, X1, Y1):
    return ((X - X1)**2 + (Y - Y1)**2)**0.5


pygame.init()

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.display.set_caption('Новое окно')

clock = pygame.time.Clock()


game_run = True
FPS = 30

X = 200; Y = 200
X1 = 600; Y1 = 200

vx = 10; vy = 10
vx1 = 10; vy1 = 2
run_hor = 0
run_vert = 0
k = 1

g = 4


is_draw = False


while game_run:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    '''
    Прак1: Реализуйте кликер: Кружок спавнится в случайном месте (74 и 75 строки)
    Вы должны на него кликнуть, тогда он переместится в дургое случайное место
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if dist(X, Y, event.pos[0], event.pos[1]) <= R:
                    X = randint(35, 965) # event.pos[0]
                    Y = randint(35, 465) # event.pos[1]
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                pass

    pygame.draw.circle(screen, [0, 0, 0], [X, Y], R)
    pygame.display.flip()


screen.fill((255, 255, 255))
pygame.display.flip()



# screen.fill((0, 0, 255))

# pygame.draw.rect(screen, [0, 0, 0], [20, 20, 100, 100], 2, 10)
# pygame.draw.circle(screen, [0, 0, 0], [200, 300], 100)

# pygame.display.flip()

pygame.quit()


"""
 1. Начало: пусть по клику мышки создаётся круг случайного размера и случайного цвета (1 он один, 2 их сколько угодно)
 2. Продолжение: кликер + аэрохоккей
"""
