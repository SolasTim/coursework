import pygame
import math

# initialise pygame
pygame.init()
clock = pygame.time.Clock()

# creating time delay
time_delay = 500
# 0.5 seconds
time_event = pygame.USEREVENT + 1
pygame.time.set_timer(time_event, time_delay)
# sets timer for when an event has happened and how long it should go for.

# create screen
ScreenResX = 800
ScreenResY = 600
screen = pygame.display.set_mode((ScreenResX, ScreenResY))
# sets the resolution of the screen allowing it to be displayed in the main loop
# allows screen resolution to be changed easily

# Title and Icon
pygame.display.set_caption("woah I don't know what im doing!")
# title of window
icon = pygame.image.load("knight.png")
# sets the icon at the top of the screen
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("cowboy.png")
playerImg = pygame.transform.scale(playerImg, (46, 68))
# this formats the players sprite so it can be displayed onto the screen
playerX = 100
playerY = 500


# sets players initial x and y co ordinated

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
                # picks up when left key is pressed
                self.x -= self.vel
                # changes sprite location in accordance to speed
                if self.x <= 0:
                    self.x = 0
                    return self.x
                    # stops player from moving off the screen
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
                # picks up when down key is pressed
                self.y += self.vel
                if self.y >= (ScreenResY - 68):
                    self.y = ScreenResY - 68
                    return self.y
                else:
                    return self.y
        # will change x and y co-ordinates to move player around screen.
        # added boundary so player cant move out of screen

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 46, 68)


    def display(self):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 45, 70), 2)


# Enemy
knightImg = pygame.image.load("knight.png")
goblinImg = pygame.image.load("goblin.png")
knightImg = pygame.transform.scale(knightImg, (46, 68))
goblinImg = pygame.transform.scale(goblinImg, (46, 68))
enemyX = 380
enemyY = 260


# same as player class for now will again most likely change

class Enemy:

    def __init__(self, x, y, img, vel, health):
        self.x = x
        self.y = y
        self.img = img
        self.vel = vel
        self.health = health

    def isclose(self, playerX, playerY, distance):
        return math.hypot(self.x - playerX, self.y - playerY) < float(distance)
        # this returns the distance that the player is away from the enemy so when the player
        # comes close enough the enemy will come towards the player

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
        # moves enemy towards player

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 46, 68)
        # print(self.rect)

    def display(self):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 45, 70), 2)
        # unsure why self.rect doesnt work but calling its var does


# Projectile

class Projectile:

    def __init__(self, x, y, vel, isPlayer, pX, pY):
        if isPlayer == True:
            # this statement will execute when the player is shooting
            mx, my = pygame.mouse.get_pos()
            # get position of mouse on screen
            self.pos = (x, y)
            # position of bullet
            self.dir = (mx - x, my - y)
            # direction of bullet
            length = math.hypot(*self.dir)
            if length == 0.0:
                self.dir = (0, -1)
            else:
                self.dir = (self.dir[0] / length, self.dir[1] / length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

            self.bullet = pygame.Surface((7, 2)).convert_alpha()
            self.bullet.fill((0, 0, 0))
            # colour of bullet
            self.bullet = pygame.transform.rotate(self.bullet, angle)
            # moves the rotation of the bullet to its trajectory path

        elif isPlayer == False:
            # this statement will execute when the enemy is shooting
            # this condition is for when enemies shoot the player
            self.pos = (x, y)
            # position of bullet
            self.dir = (pX - x, pY - y)
            # direction of bullet
            length = math.hypot(*self.dir)
            if length == 0.0:
                self.dir = (0, -1)
            else:
                self.dir = (self.dir[0] / length, self.dir[1] / length)
            angle = math.degrees(math.atan2(-self.dir[1], self.dir[0]))

            self.bullet = pygame.Surface((7, 2)).convert_alpha()
            self.bullet.fill((0, 0, 0))
            # colour of bullet
            self.bullet = pygame.transform.rotate(self.bullet, angle)
            # moves the rotation of the bullet to its trajectory path

        self.vel = vel

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.vel,
                    self.pos[1] + self.dir[1] * self.vel)
        self.rect = ((*self.pos, 9, 4))
        # print(self.rect)

    # updates bullets position on the screen

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, bullet_rect)
        pygame.draw.rect(screen, (0, 255, 0), (*self.pos, 9, 4), 2)
    # draws bullet to screen

#def halo(targetX, targetY, objectX, objectY):
#    dist=math.hypot(objectX - targetX, objectY - targetY)
#    print(dist)
#halo(10, 10, 0, 0)

class item:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = self.rect = ((self.x, self.y, 10, 10))

    def draw(self):
        screen.blit(self.img, (self.x, self.y))


cowboy = Character(playerX, playerY, playerImg, 5)
goblin = Enemy(enemyX + 30, enemyY - 50, goblinImg, 2, 3)
knight = Enemy(enemyX, enemyY, knightImg, 0.5, 5)
pos = (cowboy.x, cowboy.y)
bullets = []
enemies = []
hit = 0
KA = True
GA = True

# game loop will allow game to run. Will iterate players model to move along with projectiles and enemy movement.
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(Projectile(cowboy.x, cowboy.y, 4, True, cowboy.x, cowboy.y))
        if event.type == time_event and KA == True and knight.isclose(cowboy.x, cowboy.y, 200):
            bullets.append(Projectile(knight.x - 45, knight.y, 1, False, cowboy.x, cowboy.y))
    # allows for mouse button to be pressed down signalling a shot has been fired

    for bullet in bullets[:]:
        bullet.update()
        if not screen.get_rect().collidepoint(bullet.pos):
            bullets.remove(bullet)
        if knight.rect.colliderect(bullet.rect):
            # checks whether a collision has occured between the bullet and enemy
            print("hit")
            bullets.remove(bullet)
            # this removes bullet from screen
            knight.health -= 1
            if knight.health == 0:
                KA = False
                # KA is checks the alive state of the knight
                print("knight dead")
                # this is testing to see if the knight has died
        if goblin.rect.colliderect(bullet.rect):
            # checks whether a collision has occured between the bullet and enemy
            print("hit")
            bullets.remove(bullet)
            # this removes bullet from screen
            goblin.health -= 1
            if goblin.health == 0:
                GA = False
                # GA is checks the alive state of the goblin
                print("knight dead")
        if cowboy.rect.colliderect(bullet.rect):
            #checks collision between player and bullet
            print("players hit")
            bullets.remove(bullet)

        # This handles the goblins collisions and health
        # either updates bullets position or removes bullet if not on screen

    cowboy.KeyStroke()
    screen.fill((50.2, 50.2, 50.2))
    # wipes page
    cowboy.display()
    cowboy.update()

    if KA == True:
        knight.update()
        if knight.isclose(cowboy.x, cowboy.y, 200):
            knight.move(cowboy.x, cowboy.y)
        knight.display()
    elif KA == False:
        knight.rect = pygame.Rect(0, 0, 0, 0)
        # this elif statement will just set the knights rect to 0 size so it appears dead

    if GA == True:
        goblin.update()
        if goblin.isclose(cowboy.x, cowboy.y, 300):
            goblin.move(cowboy.x, cowboy.y)
        goblin.display()
    elif GA == False:
        goblin.rect = pygame.Rect(0, 0, 0, 0)
        # this elif statement will just set the knights rect to 0 size so it appears dead

    for bullet in bullets:
        bullet.draw(screen)

    clock.tick(60)
    pygame.display.update()
