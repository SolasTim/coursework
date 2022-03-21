import pygame

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ScreenResX = 800
ScreenResY = 600
screen = pygame.display.set_mode((ScreenResX, ScreenResY))


class Menu():
    def __int__(self, game):
        self.game = game
        self.mid_w = ScreenResX / 2
        self.mid_h = ScreenResY / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text("#", 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Main Menu", 20, self.game.ScreenResX/ 2, self.game.ScreenResY/ 2)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()

    def move_cursor(self):
        if event.type == pygame.KEYDOWN:
            if self.state == "Start":
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state == "Options"
            elif self.state == "Options":
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state == "Credits"
            elif self.state == "Credits":
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = "Start"
        elif self.game.UP_KEY:




