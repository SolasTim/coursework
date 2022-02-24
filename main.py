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
    def __init__(self, x, y, img, vel):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel

    def KeyStroke(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left")
                self.x -= self.vel
                if self.x <= 0:
                    self.x = 0
                    return self.x
                else:
                    return self.x
            if event.key == pygame.K_RIGHT:
                print("Right")
                self.x += self.vel
                if self.x >= 754:
                    self.x = 754
                else:
                    return self.x
            if event.key == pygame.K_UP:
                print("up")
                self.y -= self.vel
                if self.y <= 0:
                    self.y = 0
                    return self.y
                else:
                    return self.y
            if event.key == pygame.K_DOWN:
                print("down")
                self.y += self.vel
                if self.y >= 530:
                    self.y = 530
                    return self.y
                else:
                    return self.y
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key released")

    def display(self):
        screen.blit(self.img, (self.x, self.y))


cowboy = character(playerX, playerY, playerImg, 1)

# game loop
running = True
while running:

    #    playerX += 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cowboy.KeyStroke()
    screen.fill((255, 255, 255))
    cowboy.display()

    pygame.display.update()
