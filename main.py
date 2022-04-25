import pygame
import math

# initialise pygame
pygame.init()
clock = pygame.time.Clock()

# items collected counter
items = 0

# creating time delay
time_delay = 500
# 0.5 seconds
time_event = pygame.USEREVENT + 1
pygame.time.set_timer(time_event, time_delay)
# sets timer for when an event has happened and how long it should go for.

# create screen
ScreenResX = 600
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

# map
map = pygame.image.load("map.png").convert()
# loads the image so its usable by pygame

# player
playerImg = pygame.image.load("cowboy.png")
playerImg = pygame.transform.scale(playerImg, (30, 40))
# this formats the players sprite so it can be displayed onto the screen
playerX = 20
playerY = 550
# sets players initial x and y co ordinated

#item
itemImg = pygame.image.load("chest.png")
itemImg = pygame.transform.scale(itemImg, (25, 30))
#sets chests sprite


class Screen():
    def __init__(self, title, fill, width = 600, height = 600):
        self.title = title
        # title of the screen so i can differentiate between them
        self.width = width
        self.height = height
        # dimensions of screen which are set to a default 600x 600
        # unless I want them different then i can just change values when creating object
        self.fill = fill
        # set what will refresh each time
        self.current = False
        # decides which screen should be showing, if this is switched
        # to true it will show that screen

    def MakeCurrent(self):
        pygame.display.set_caption(self.title)
        # sets the caption of the current screen
        self.current = True
        # switches the screen that is being shown
        self.screen = pygame.display.set_mode((self.width, self.height))
        # sets dimension of screen

    def EndCurrent(self):
        self.current = False
        # makes previous screen stop showing

    def CheckUpdate(self):
        return self.current
        #checks what screen needs to be showing at that time

    def ScreenUpdate(self, isGame):
        if self.current and isGame == False:
            # the isGame parameter is nececarry as the game needs to blit
            # a picture not wipe a single colour
            self.screen.fill(self.fill)
            # wipes screen to one colour
        elif isGame == True and isGame == True:
            self.screen.blit(map, [0, 0])
            # displays the map onto the screen

    def ReturnTitle(self):
        return self.screen


class text:
  def __init__(self, font, width = 60, height = 200):
    self.font = pygame.font.sysfont(None, 48)
    #sets font as no italic and size 48
    self.width = width
    self.height = height

  def getkeys(self):
    for event in pygame.event.get():
      press = event.type
    
    
  

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
                if self.x >= (ScreenResX - 30):
                    self.x = ScreenResX - 30
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
                if self.y >= (ScreenResY - 40):
                    self.y = ScreenResY - 40
                    return self.y
                else:
                    return self.y
        # will change x and y co-ordinates to move player around screen.
        # added boundary so player cant move out of screen

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 30, 40)


    def display(self):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 30, 40), 2)


# Enemy
knightImg = pygame.image.load("knight.png")
goblinImg = pygame.image.load("goblin.png")
ghostImg = pygame.image.load("knight.png")
knightImg = pygame.transform.scale(knightImg, (30, 40))
goblinImg = pygame.transform.scale(goblinImg, (30, 40))
ghostImg = pygame.transform.scale(ghostImg, (30, 40))
knightX = 360
knightY = 550
goblinX = 150
goblinY = 120
ghostX = 200
ghostY = 480
# This sets the coordinates and relevant images for each enemy

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
        self.rect = pygame.Rect(self.x, self.y, 30, 40)
        # print(self.rect)

    def display(self):
        screen.blit(self.img, (self.x, self.y))
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 30, 40), 2)
        # unsure why self.rect doesnt work but calling its var does


# Projectile

class Projectile:

    def __init__(self, x, y, vel, isPlayer, pX, pY):
        self.isPlayer = isPlayer
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

            self.bullet = pygame.Surface((4, 1)).convert_alpha()
            self.bullet.fill((0, 0, 0))
            # colour of bullet
            self.bullet = pygame.transform.rotate(self.bullet, angle)
            # moves the rotation of the bullet to its trajectory path

        elif isPlayer == False:
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

            self.bullet = pygame.Surface((4, 1)).convert_alpha()
            self.bullet.fill((0, 0, 0))
            # colour of bullet
            self.bullet = pygame.transform.rotate(self.bullet, angle)
            # moves the rotation of the bullet to its trajectory path

        self.vel = vel

    def update(self):
        self.pos = (self.pos[0] + self.dir[0] * self.vel,
                    self.pos[1] + self.dir[1] * self.vel)
        self.rect = ((*self.pos, 7, 2))
        # print(self.rect)

    # updates bullets position on the screen

    def draw(self, surf):
        bullet_rect = self.bullet.get_rect(center=self.pos)
        surf.blit(self.bullet, bullet_rect)
        pygame.draw.rect(screen, (0, 255, 0), (*self.pos, 9, 4), 2)
    # draws bullet to screen


class Item:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        # base class sets the x,y and image

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 25, 30)
        # update method updates the rect of the object

    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        # draw method draws the sprite to the screen
        # at given coordinates


chest1 = Item(140, 30, itemImg)
chest2 = Item(470 ,430, itemImg)
chest3 = Item(490, 170, itemImg)
cowboy = Character(playerX, playerY, playerImg, 10)
goblin = Enemy(goblinX, goblinY, goblinImg, 2, 3)
knight = Enemy(knightX, knightY, knightImg, 0.5, 5)
ghost = Enemy(ghostX, ghostY, ghostImg, 2, 4)
pos = (cowboy.x, cowboy.y)
bullets = []
hit = 0
KA = True
#knight alvie
GA = True
#goblin alvive
HA = True
#ghost alive
collected1 = False
collected2 = False
collected3 = False
game = Screen("game", map)
menu = Screen("menu", (50.5, 50.5, 50.5))
leaderboard = Screen("leaderboard", (50.5, 50.5, 50.5))
game.MakeCurrent()
# sets this as the first screen

# game loop will allow game to run. Will iterate players model to move along with projectiles and enemy movement.
running = True
while running:


    if game.CheckUpdate():
        game.ScreenUpdate(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                bullets.append(Projectile(cowboy.x, cowboy.y, 4, True, cowboy.x, cowboy.y))
            if event.type == time_event and KA == True and knight.isclose(cowboy.x, cowboy.y, 100):
                bullets.append(Projectile(knight.x - 45, knight.y, 1, False, cowboy.x, cowboy.y))
        # allows for mouse button to be pressed down signalling a shot has been fired

        for bullet in bullets[:]:
            bullet.update()
            if not screen.get_rect().collidepoint(bullet.pos):
                bullets.remove(bullet)
            if knight.rect.colliderect(bullet.rect) and bullet.isPlayer == True:
                # checks whether a collision has occured between the bullet and enemy
                # also checks to see what object has shot it to prevent shooting itself
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
                    print("goblin dead")
                  
            if ghost.rect.colliderect(bullet.rect):
                # checks whether a collision has occured between the bullet and enemy
                print("hit")
                bullets.remove(bullet)
                # this removes bullet from screen
                ghost.health -= 1
                if ghost.health == 0:
                    HA = False
                    # GA is checks the alive state of the goblin
                    print("ghost dead")
            if cowboy.rect.colliderect(bullet.rect) and bullet.isPlayer == False:
                # checks collision between player and bullet
                print("players hit")
                bullets.remove(bullet)

            # This handles the goblins collisions and health
            # either updates bullets position or removes bullet if not on screen



        # places map onto screen

        cowboy.KeyStroke()
        cowboy.display()
        cowboy.update()
        chest1.update()
        chest2.update()
        chest3.update()

        if cowboy.rect.colliderect(chest1.rect) and collected1 == False:
            # checks if a collision between the player and item has occurred
            # and if it has already been collide with
            chest1.update()
            collected1 = True
            items += 1
            print(items)

        elif collected1 == False:
            chest1.draw()

        if cowboy.rect.colliderect(chest2.rect) and collected2 == False:
            # checks if a collision between the player and item has occurred
            # and if it has already been collide with
            chest2.update()
            collected2 = True
            items += 1
            print(items)

        elif collected2 == False:
            chest2.draw()

        if cowboy.rect.colliderect(chest3.rect) and collected3 == False:
            # checks if a collision between the player and item has occurred
            # and if it has already been collide with
            chest3.update()
            collected3 = True
            items += 1
            print(items)

        elif collected3 == False:
            chest3.draw()      


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
            if goblin.isclose(cowboy.x, cowboy.y, 150):
                goblin.move(cowboy.x, cowboy.y)
            goblin.display()
        elif GA == False:
            goblin.rect = pygame.Rect(0, 0, 0, 0)
            # this elif statement will just set the knights rect to 0 size so it appears dead

        if HA == True:
            ghost.update()
            if ghost.isclose(cowboy.x, cowboy.y, 300):
                ghost.move(cowboy.x, cowboy.y)
            ghost.display()
        elif HA == False:
            ghost.rect = pygame.Rect(0, 0, 0, 0)
            # this elif statement will just set the knights rect to 0 size so it appears dead
        for bullet in bullets:
            bullet.draw(screen)

        clock.tick(60)

        if items >= 3:
            leaderboard.MakeCurrent()
            game.EndCurrent()

    elif leaderboard.CheckUpdate():
        leaderboard.ScreenUpdate(False)
        print("this where leaderboard be's")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.update()
