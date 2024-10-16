import pygame
import time

pygame.init()

screen = pygame.display.set_mode([1000, 500])
pygame.display.set_caption('Новое окно')

clock = pygame.time.Clock()


game_run = True
FPS = 30

X = 20
Y = 20

vx = 3
vy = 2

g = 2

while game_run:
    clock.tick(FPS)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, [0, 0, 0], [X, Y, 100, 100], 2, 10)
    pygame.display.flip()

    X += vx
    Y += vy
    vy += g

    if X <= 0:
        vx = -vx
    elif X + 100 >= 1000:
        vx = -vx
    elif Y < 0:
        vy = -vy
    elif Y + 100 >= 500:
        vy = -20


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_run = False

    # Задание 2: Попрыгунчик из стороны в сторону
    # Задание 3: Два круга соударяются со стенками и с друг другом


screen.fill((255, 255, 255))
pygame.display.flip()



# screen.fill((0, 0, 255))

# pygame.draw.rect(screen, [0, 0, 0], [20, 20, 100, 100], 2, 10)
# pygame.draw.circle(screen, [0, 0, 0], [200, 300], 100)

# pygame.display.flip()

pygame.quit()
