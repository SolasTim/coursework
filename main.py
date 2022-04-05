import pygame
import math

# initialise pygame
pygame.init()
clock = pygame.time.Clock()

# create screen
ScreenResX = 800
ScreenResY = 600
screen = pygame.display.set_mode((ScreenResX, ScreenResY))

#allows screen resolution to be changed easily

# Title and Icon
pygame.display.set_caption("woah I don't know what im doing!")
icon = pygame.image.load("knight.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("cowboy.png")
playerImg = pygame.transform.scale(playerImg, (46, 68))
playerX = 100
playerY = 500


# sets the players attributes outside of the class. Will most likely change this

class Character:  # this class handles most parts to do with the player
    def __init__(self, x, y, img, vel):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, 45, 70)

    # the constructor method allows for the player to have different attributes when called

    def KeyStroke(self):
        # keystrokes handles whenever a key is pressed to move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # picks up when left key is pressed
                self.x -= self.vel
                #changes sprite location in accordance to speed
                if self.x <= 0:
                    self.x = 0
                    return self.x
                else:
                    return self.x
            if event.key == pygame.K_RIGHT:
                # picks up when right key is pressed
                self.x += self.vel
                if self.x >= (ScreenResX - 46):
                    self.x = ScreenResX - 46
                else:
                    return self.x
            if event.key == pygame.K_UP:
                # picks up when up key is pressed
                self.y -= self.vel
                if self.y <= 0:
                    self.y = 0
                    return self.y
                else:
                    return self.y
            if event.key == pygame.K_DOWN:
                #picks up when down key is pressed
                self.y += self.vel
                if self.y >= (ScreenResY - 68):
                    self.y = ScreenResY - 68
                    return self.y
                else:
                    return self.y
        # will change x and y co-ordinates to move player around screen.
        # added boundary so player cant move out of screen

    def display(self):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 45, 70), 2)

# Enemy

enemyImg = pygame.image.load("knight.png")
enemyImg = pygame.transform.scale(enemyImg, (46, 68))
enemyX = 380
enemyY = 260


# same as player class for now will again most likely change

class Enemy:

    def __init__(self, x, y, img, vel, health):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel
        self.rect = pygame.Rect(self.x, self.y, 45, 70)
        self.health = health

    


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
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 45, 70), 2)
        #unsure why self.rect doesnt work but calling its var does



#Projecile

class Projectile:

    def __init__(self, x, y, vel):
        self.pos = (x, y)
        #position of bullet
        mx, my = pygame.mouse.get_pos()
        #get position of mouse on screen
        self.dir = (mx - x, my - y)
        #direction of bullet
        length = math.hypot(*self.dir)
        if length == 0.0:
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / length, self.dir[1] / length)
        angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

        self.bullet = pygame.Surface((7,2)).convert_alpha()
        self.bullet.fill((0, 0, 0))
        #colour of bullet
        self.bullet = pygame.transform.rotate(self.bullet, angle)
        #moves the rotation of the bullet to its trajectory path
        self.vel = vel
        self.rect = ((*self.pos, 9, 4))


    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.vel,
                    self.pos[1] + self.dir[1] * self.vel)
    #updates bullets position on the screen

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center = self.pos)
        surf.blit(self.bullet, bullet_rect)
        pygame.draw.rect(screen, (0, 255, 0), (*self.pos, 9, 4), 2)
    #draws bullet to screen


cowboy = Character(playerX, playerY, playerImg, 5)
knight = Enemy(enemyX, enemyY, enemyImg, 0.05, 3)
pos = (cowboy.x, cowboy.y)
bullets = []
hit = 0
Kalive = True

def RectCollision(rect1, rect2):
     return pygame.Rect.colliderect(rect1, rect2)
     #returns true or false depending on if collision has happened


# game loop will allow game to run. Will iterate players model to move along with projectiles and enemy movement.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(Projectile(cowboy.x , cowboy.y, 4))
        #allows for mouse button to be pressed down signalling a shot has been fired


    for bullet in bullets[:]:
        bullet.update()
        if not screen.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)
        if knight.rect.collidepoint(bullet.pos):
            print("hit")
            bullets.remove(bullet)
            knight.health -= 1
            if knight.health == 0:
                Kalive = False
                print ("knight dead")

        # either updates bullets position or removes bullet if not on screen

        #if RectCollision(cowboy.rect, bullet.rect) == True:
            #print("hit")

    cowboy.KeyStroke()
    screen.fill((50.2, 50.2, 50.2))
    #wipes page white
    cowboy.display()

    for bullet in bullets:
        bullet.draw(screen)

    if Kalive == True:
        knight.move(cowboy.x, cowboy.y)
        knight.display()

    clock.tick(60)
    pygame.display.update()
