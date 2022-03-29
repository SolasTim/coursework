import pygame
from menu import *

#create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.isClicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()
        #gets the mouse position

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.isClicked == False:
                self.isClicked = True
                action = True
        #checks whether the mouse is over a button and has been clicked

        if pygame.mouse.get_pressed()[0] == 0:
            self.isClicked == False

        screen.blit(self.image, (self.rect.x, self.rect.y))
        #draws button to screen

        return action

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
exit_img = pygame.image.load('exit_btn.png').convert_alpha()

#create button instances
start_button = Button(100, 200, start_img, 0.8)
exit_button = Button(450, 200, exit_img, 0.8)

#game loop
run = True
while run:

	screen.fill((200, 200, 200))

	if start_button.draw(screen):
		print('START')
	if exit_button.draw(screen):
		print('EXIT')

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
