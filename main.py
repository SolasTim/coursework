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


# sets the players attributes outside of the class. Will most likely change this

class Character:  # this class handles most parts to do with the player
    def __init__(self, x, y, img, vel):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel

    # the constructor method allows for the player to have different attributes when called

    def KeyStroke(self):
        # keystrokes handles whenever a key is pressed to move the player
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
        # will change x and y co-ordinates to move player around screen.
        # added boundary so player cant move out of screen

    def display(self):
        screen.blit(self.img, (self.x, self.y))


# Enemy

enemyImg = pygame.image.load("knight.png")
enemyImg = pygame.transform.scale(enemyImg, (46, 68))
enemyX = 380
enemyY = 260


# same as player class for now will again most likely change

class Enemy:

    def __init__(self, x, y, img, vel):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel

    def move(self, playerX, playerY):  # chase movement
        # Movement along x direction
        if self.x > playerX:
            self.x -= self.vel
        elif self.x < playerX:
            self.x += self.vel
        # Movement along y direction
        if self.y < playerY:
            self.y += self.vel
        elif self.y > playerY:
            self.y -= self.vel

        #moves enemy towards player

    def display(self):
        screen.blit(self.img, (self.x, self.y))


cowboy = Character(playerX, playerY, playerImg, 1)
knight = Enemy(enemyX, enemyY, enemyImg, 0.05)

# game loop will allow game to run. Will iterate players model to move along with projectiles and enemy movement.
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cowboy.KeyStroke()
    knight.move(cowboy.x, cowboy.y)
    screen.fill((255, 255, 255))
    cowboy.display()
    knight.display()

    pygame.display.update()
