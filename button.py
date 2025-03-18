import pygame
from constant import *

font = pygame.font.SysFont('arial', F_SIZE)

class Button():
    def __init__(self, x, y, text):
        self.rect = pygame.Rect(x, y, BTN_WIDTH, BTN_HEIGHT)
        self.clicked = False
        self.text = text
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                for event in pygame.event.get():    
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.clicked = True
                        action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        pygame.draw.rect(WIN, DARK, self.rect, 0, 10)
        self.num = font.render(self.text, True, BLACK)
        WIN.blit(self.num, (self.rect[0] + (BTN_WIDTH - self.num.get_width())/2, self.rect[1] + (BTN_HEIGHT - self.num.get_height())/2))
        return action

class Switch():
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BTN_WIDTH, BTN_HEIGHT)
        self.clicked = False
        self.state = False
    
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                for event in pygame.event.get():    
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.clicked = True
                        action = True
            
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        pygame.draw.rect(WIN, DARK, self.rect, 0, 10)
        if self.state:
            self.text = "Auto On"
        else:
            self.text = "Auto Off"

        self.num = font.render(self.text, True, BLACK)
        WIN.blit(self.num, (self.rect[0] + (BTN_WIDTH - self.num.get_width())/2, self.rect[1] + (BTN_HEIGHT - self.num.get_height())/2))
        
        if action:
            self.state = True if self.state == False else False
        return self.state