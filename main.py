import pygame

# initialise pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("woah I don't know what im doing!")
icon = pygame.image.load("knight.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("cowboy.png")
playerImg = pygame.transform.scale(playerImg, (46, 68))
playerX = 380
playerY = 260
playerX_change = 0

class character:
    def __init__(self):
        self.__init__()

    def KeyStroke():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
            if event.key == pygame.K_RIGHT:
                print("Right")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")


def player(x, y):
    screen.blit(playerImg, (x, y))


# game loop
running = True
while running:
    screen.fill((255, 255, 255))
    playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    character.KeyStroke()
    player(playerX, playerY)
    pygame.display.update()
