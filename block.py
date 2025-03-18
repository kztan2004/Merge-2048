import pygame
from constant import *

font = pygame.font.SysFont('arial', F_SIZE)

class Block:
    def __init__(self, x, y, s = False):
        self.x = x
        self.y = y
        self.val = 0
        self.back = s
        self.rect = pygame.Rect(self.x, self.y, B_WIDTH, B_HEIGHT)
    
    def draw(self):
        if self.back:
            pygame.draw.rect(WIN, BASE, self.rect, 0, 10)
            return

        if self.val != 0:
            if self.val <= 11: 
                pygame.draw.rect(WIN, GRADE[self.val-1], self.rect, 0, 10)
                self.num = font.render(str(2**self.val), True, BLACK)
            else:
                pygame.draw.rect(WIN, BLACK, self.rect, 0, 10)    
                self.num = font.render(str(2**self.val), True, WHITE)
            WIN.blit(self.num, (self.rect[0] + (B_WIDTH - self.num.get_width())/2, self.rect[1] + (B_HEIGHT - self.num.get_height())/2))

    def reset(self):
        self.rect = pygame.Rect(self.x, self.y, B_WIDTH, B_HEIGHT)
