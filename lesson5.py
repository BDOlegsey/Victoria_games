import pygame
import time
from random import randint

sizeX, sizeY = 1000, 500


class Ball:
    def __init__(self, x, y, R, speedX, speedY, image):
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.R = R
        self.image = image

    def move(self):
        self.x += self.speedX
        self.y += self.speedY

    def border(self, count):
        if self.x <= 0:
            self.x = 500
            self.y = randint(50, 450)
            count -= 1
        elif self.x + self.R >= sizeX:
            self.x = 500
            self.y = randint(50, 450)
            count += 1
        elif self.y <= 0 or self.y + self.R >= sizeY:
            self.speedY *= -1
        return count


class Player:
    def __init__(self, x, y, image, sizeX=30, sizeY=100):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.image = image

    def face(self, ball, turn):
        if turn == 'left':
            if ball.x <= self.x + 100:
                if ball.y >= self.y and ball.y <= self.y + 200:
                    return -ball.speedX
        else:
            if ball.x + ball.R >= self.x:
                if ball.y >= self.y and ball.y <= self.y + 200:
                    return -ball.speedX
        return ball.speedX

    def move_bot(self, ball):
        if self.y + 50 < ball.y - 50:
            self.y += 2
        elif self.y + 50 > ball.y + 50:
            self.y -= 2


class Person:
    def __init__(self, x, y, image_right, image_left, right):
        self.x = x
        self.y = y
        self.images = [image_right, image_left]
        self.right = right

    def draw(self, _screen):
        if self.right:
            _screen.blit(self.images[0], (self.x, self.y))
        else:
            _screen.blit(self.images[1], (self.x, self.y))


pygame.init()

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.display.set_caption('Новое окно')

clock = pygame.time.Clock()


game_run = True
FPS = 60
count = 0

person_img = pygame.image.load('img\\person.png')
person_img_left = pygame.image.load('img\\person_left.png')
person_img_right = pygame.image.load('img\\person_right.png')
ball_img = pygame.image.load('img\\ball.png')
player_img = pygame.image.load('img\\player.png')

my_font = pygame.font.SysFont('arial', 30)
text1 = my_font.render('Hello world!', True, (0, 0, 0))
text2 = my_font.render(str(count), True, (0, 0, 0))

person = Person(10, 10, person_img_right, person_img_left, True)
player = Player(15, 20, player_img)
player_bot = Player(800, 20, player_img)

ball = Ball(200, 200, 100, 10, 4, ball_img)

while game_run:
    clock.tick(FPS)
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                player.y -= 10
                person.x += 10
                person.right = True
            if event.button == 5:
                player.y += 10
                person.x -= 10
                person.right = False
        if event.type == pygame.MOUSEBUTTONUP:
            pass

    ball.move()
    count = ball.border(count)
    text2 = my_font.render(str(count), True, (0, 0, 0))

    ball.speedX = player.face(ball, 'left')
    ball.speedX = player_bot.face(ball, 'right')

    player_bot.move_bot(ball)

    #pygame.draw.rect(screen, [0, 0, 0], [player.x, player.y, player.sizeX, player.sizeY])
    #pygame.draw.rect(screen, [0, 0, 0], [player_bot.x, player_bot.y, player_bot.sizeX, player_bot.sizeY])
    #pygame.draw.circle(screen, [0, 0, 0], [ball.x, ball.y], ball.R)

    screen.blit(player.image, (player.x, player.y))
    screen.blit(player_bot.image, (player_bot.x, player_bot.y))
    screen.blit(ball.image, (ball.x, ball.y))

    person.draw(screen)

    screen.blit(text1, (50, 50))
    screen.blit(text2, (50, 100))

    pygame.display.flip()


screen.fill((255, 255, 255))
pygame.display.flip()


pygame.quit()
