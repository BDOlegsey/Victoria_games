import pygame
import time
from random import randint

sizeX, sizeY = 1000, 500


class Ball:
    def __init__(self, x, y, R, speedX, speedY):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.R = R

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def border(self):
        if self.x - self.R <= 0 or self.x + self.R >= sizeX:
            self.x = 500
            self.y = randint(50, 450)
        elif self.y - self.R <= 0 or self.y + self.R >= sizeY:
            self.speedY *= -1


class Player:
    def __init__(self, x, y, sizeX=30, sizeY=100):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def face(self, ball, turn):
        if turn == 'left':
            if ball.x - ball.R <= self.x + 30:
                if ball.y >= self.y and ball.y <= self.y + 100:
                    return -ball.speedX
        else:
            if ball.x + ball.R >= self.x:
                if ball.y >= self.y and ball.y <= self.y + 100:
                    return -ball.speedX
        return ball.speedX

    def move_bot(self, ball):
        if self.y + 50 < ball.y - 50:
            self.y += 2
        elif self.y + 50 > ball.y + 50:
            self.y -= 2


pygame.init()

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.display.set_caption('Новое окно')

clock = pygame.time.Clock()


game_run = True
FPS = 60

player = Player(15, 20)
player_bot = Player(955, 20)

ball = Ball(200, 200, 35, 10, 4)

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

    ball.move()
    ball.border()

    ball.speedX = player.face(ball, 'left')
    ball.speedX = player_bot.face(ball, 'right')


    player_bot.move_bot(ball)

    pygame.draw.rect(screen, [0, 0, 0], [player.x, player.y, player.sizeX, player.sizeY])
    pygame.draw.rect(screen, [0, 0, 0], [player_bot.x, player_bot.y, player_bot.sizeX, player_bot.sizeY])
    pygame.draw.circle(screen, [0, 0, 0], [ball.x, ball.y], ball.R)

    pygame.display.flip()


screen.fill((255, 255, 255))
pygame.display.flip()


pygame.quit()
