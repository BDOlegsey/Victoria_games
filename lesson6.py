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


class Button:
    def __init__(self, x, y, sizeX, sizeY, text, color):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.text = text
        self.color = color

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.sizeX, self.sizeY])
        _text = my_font.render(self.text, True, (255, 255, 255))
        screen.blit(_text, (self.x + self.sizeX//3, self.y + self.sizeY//3))


pygame.init()

screen = pygame.display.set_mode([sizeX, sizeY])
pygame.display.set_caption('Новое окно')

clock = pygame.time.Clock()


game_run = True
FPS = 60
count = 0

turn = 'start'

pygame.mixer.init()
pygame.mixer.music.load('snd\\test.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

is_music = True

person_img = pygame.image.load('img\\person.png')
person_img_left = pygame.image.load('img\\person_left.png')
person_img_right = pygame.image.load('img\\person_right.png')
ball_img = pygame.image.load('img\\ball.png')
player_img = pygame.image.load('img\\player.png')

my_font = pygame.font.SysFont('arial', 40)
text1 = my_font.render('Hello world!', True, (0, 0, 0))
text2 = my_font.render(str(count), True, (0, 0, 0))

person = Person(10, 10, person_img_right, person_img_left, True)
player = Player(15, 20, player_img)
player_bot = Player(800, 20, player_img)

ball = Ball(200, 200, 100, 10, 4, ball_img)

start_button = Button(400, 200, 300, 70, 'START', [0, 0, 0])
back_button = Button(400, 20, 300, 70, 'BACK', [0, 0, 0])

while game_run:
    if turn == 'start':
        screen.fill((255, 255, 255))
        start_button.draw()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    _x = pygame.mouse.get_pos()[0]
                    _y = pygame.mouse.get_pos()[1]
                    if _x >= start_button.x and _x <= start_button.x + start_button.sizeX:
                        if _y >= start_button.y and _y <= start_button.y + start_button.sizeY:
                            turn = 'game'
    elif turn == 'game':
        clock.tick(FPS)
        screen.fill((255, 255, 255))
        back_button.draw()

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
                if event.button == 1:
                    _x = pygame.mouse.get_pos()[0]
                    _y = pygame.mouse.get_pos()[1]
                    if _x >= back_button.x and _x <= back_button.x + back_button.sizeX:
                        if _y >= back_button.y and _y <= back_button.y + back_button.sizeY:
                            turn = 'start'
                    if is_music:
                        pygame.mixer.music.pause()
                        is_music = False
                    else:
                        pygame.mixer.music.unpause()
                        is_music = True
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
