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
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img

    def KeyStroke(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
                self.x -= 0.01
                return self.x
            if event.key == pygame.K_RIGHT:
                print("Right")
                self.x += 0.01
                return self.x
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")

    def display(self):
        screen.blit(self.img, (self.x, self.y))


cowboy = character(playerX, playerY, playerImg)

# game loop
running = True
while running:
    
#    playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    cowboy.KeyStroke()
    screen.fill((256, 256, 256))
    cowboy.display()

    pygame.display.update()
