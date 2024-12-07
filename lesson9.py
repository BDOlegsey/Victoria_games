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
    def __init__(self, x, y, sizeX=30, sizeY=100):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), [self.x, self.y, self.sizeX, self.sizeY])



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
    def __init__(self, x, y, sizeX, sizeY, text, color, k):
        self.x = x
        self.y = y
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.text = text
        self.color = color
        self.k = k

    def draw(self):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.sizeX, self.sizeY])
        _text = my_font.render(self.text, True, (255, 255, 255))
        screen.blit(_text, (self.x + self.sizeX//self.k, self.y + self.sizeY//self.k))


class Bullet:
    def __init__(self, x, y, alive=True):
        self.x = x
        self.y = y
        self.alive = alive

    def move(self):
        self.y -= 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), [self.x, self.y, 10, 30])




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
pygame.mixer.music.pause()
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

player = Player(500, 400, 70, 70)

bullets = []

start_button = Button(400, 200, 300, 70, 'START', [0, 0, 0], 3)
back_button = Button(400, 20, 300, 70, 'BACK', [0, 0, 0], 3)
settings_button = Button(400, 333, 300, 70, 'SETTINGS', [0, 0, 0], 5)
settings_screen_fillw_button = Button(400, 200, 150, 70, 'WHITE', [0, 0, 0], 6)
settings_screen_fillg_button = Button(550, 200, 150, 70, 'BLACK', [0, 0, 0], 6)

screen_fill = (255, 255, 255)


while game_run:
    if turn == 'settings':
        screen.fill(screen_fill)
        back_button.draw()
        settings_screen_fillw_button.draw()
        settings_screen_fillg_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    _x = pygame.mouse.get_pos()[0]
                    _y = pygame.mouse.get_pos()[1]
                    if _x >= back_button.x and _x <= back_button.x + back_button.sizeX:
                        if _y >= back_button.y and _y <= back_button.y + back_button.sizeY:
                            turn = 'start'
                    if _x >= settings_screen_fillw_button.x and _x <= settings_screen_fillw_button.x + settings_screen_fillw_button.sizeX:
                        if _y >= settings_screen_fillw_button.y and _y <= settings_screen_fillw_button.y + settings_screen_fillw_button.sizeY:
                            screen_fill = (255, 255, 255)
                    if _x >= settings_screen_fillg_button.x and _x <= settings_screen_fillg_button.x + settings_screen_fillg_button.sizeX:
                        if _y >= settings_screen_fillg_button.y and _y <= settings_screen_fillg_button.y + settings_screen_fillg_button.sizeY:
                            screen_fill = (170, 170, 170)

        pygame.display.flip()
    elif turn == 'start':
        screen.fill(screen_fill)
        start_button.draw()
        settings_button.draw()
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
                    if _x >= settings_button.x and _x <= settings_button.x + settings_button.sizeX:
                        if _y >= settings_button.y and _y <= settings_button.y + settings_button.sizeY:
                            turn = 'settings'
    elif turn == 'game':
        clock.tick(FPS)
        screen.fill(screen_fill)
        back_button.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    player.x -= 10
                if event.button == 5:
                    player.x += 10
                if event.button == 1:
                    _x = pygame.mouse.get_pos()[0]
                    _y = pygame.mouse.get_pos()[1]
                    if _x >= back_button.x and _x <= back_button.x + back_button.sizeX:
                        if _y >= back_button.y and _y <= back_button.y + back_button.sizeY:
                            turn = 'start'

                    temp_bullet = Bullet(player.x + player.sizeX // 2, player.y)
                    bullets.append(temp_bullet)
            if event.type == pygame.MOUSEBUTTONUP:
                pass


        for i in range(len(bullets)):
            bullets[i].move()
            if bullets[i].y <= -50:
                bullets[i].alive = False
            bullets[i].draw(screen)

        player.draw(screen)
        pygame.display.flip()


screen.fill((255, 255, 255))
pygame.display.flip()


pygame.quit()
