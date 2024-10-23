import pygame
import time

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

def border_key(X, Y):
    if X - R <= 0:
        X = R
    elif X + R >= sizeX:
        X = sizeX - R
    elif Y - R <= 0:
        Y = R
    elif Y + R >= sizeY:
        Y = sizeY - R

    return [X, Y]

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

vx = 10; vy = 2
vx1 = 10; vy1 = 2
run_hor = 0


g = 2

while game_run:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, [0, 0, 0], [X, Y], R)
    #pygame.draw.circle(screen, [0, 0, 0], [X1, Y1], R)
    pygame.display.flip()

    X += vx * run_hor
    #X1 += vx1

    X, Y = border_key(X, Y)
    #vx1, vy1 = border(X1, Y1, vx1, vy1)

    #if dist(X, Y, X1, Y1) <= 2*R:
    #    vx = -vx
    #    vx1 = -vx1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                X += 20
            if event.key == pygame.K_a:
                run_hor = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                run_hor = 0

    # Круг, который может плавно перемещаться вверх вниз и 
screen.fill((255, 255, 255))
pygame.display.flip()



# screen.fill((0, 0, 255))

# pygame.draw.rect(screen, [0, 0, 0], [20, 20, 100, 100], 2, 10)
# pygame.draw.circle(screen, [0, 0, 0], [200, 300], 100)

# pygame.display.flip()

pygame.quit()


"""
1. Давайте реализуем квадрат, который может перемещаться

2. Пусть теперь у него будет физика, и он сможет прыгать на пробел, скоряться на shift и замедляться на ctrl
"""
