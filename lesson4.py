import pygame
import time
from random import randint

R = 35


class Player:
    def __init__(self, x, y, sizeX=30, sizeY=100):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def face(self, x, y, vx, turn):
        if turn == 'left':
            if x - R <= self.x + 30:
                if y >= self.y and y <= self.y + 100:
                    return -vx
        else:
            if x + R >= self.x:
                if y >= self.y and y <= self.y + 100:
                    return -vx
        return vx

    def move_bot(self, y):
        if self.y + 50 < y - 50:
            self.y += 2
        elif self.y + 50 > y + 50:
            self.y -= 2


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
FPS = 60

player = Player(15, 20)
player_bot = Player(955, 20)

X, Y = 200, 200

vx = 10; vy = 4
vx1 = 10; vy1 = 2
run_hor = 0
run_vert = 0
k = 1

g = 4


is_draw = False

v1 = 0


while game_run:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                player.y -= 10
            if event.button == 5:
                player.y += 10
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    X += vx
    Y += vy

    vx, vy = border(X, Y, vx, vy)

    vx = player.face(X, Y, vx, 'left')
    vx = player_bot.face(X, Y, vx, 'right')

    if X - R <= 0:
        X = 500
        Y = randint(50, 450)
    if X + R >= 1000:
        X = 500
        Y = randint(50, 450)

    player_bot.move_bot(Y)

    pygame.draw.rect(screen, [0, 0, 0], [player.x, player.y, player.sizeX, player.sizeY])
    pygame.draw.rect(screen, [0, 0, 0], [player_bot.x, player_bot.y, player_bot.sizeX, player_bot.sizeY])
    pygame.draw.circle(screen, [0, 0, 0], [X, Y], R)

    pygame.display.flip()


screen.fill((255, 255, 255))
pygame.display.flip()



# screen.fill((0, 0, 255))

# pygame.draw.rect(screen, [0, 0, 0], [20, 20, 100, 100], 2, 10)
# pygame.draw.circle(screen, [0, 0, 0], [200, 300], 100)

# pygame.display.flip()

pygame.quit()
