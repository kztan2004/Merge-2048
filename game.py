import pygame
import random
from constant import *
from block import Block

class Game:
    def __init__(self):
        self.bArray = []
        self.baseArr = []
        for i in range(ROWS):
            for j in range(COLS):
                posX = P_WIDTH + j * (B_WIDTH + PADDING)
                posY = P_HEIGHT + i * (B_HEIGHT + PADDING)
                self.bArray.append(Block(posX,posY))
                self.baseArr.append(Block(posX,posY,True))

    def select(self, pos):
        for i, b in enumerate(self.bArray):
            if b.rect.collidepoint(pos):
                return i
        return None

    def draw(self, b_num):
        pygame.draw.rect(WIN, DARK, (P_WIDTH-2*PADDING, P_HEIGHT-2*PADDING, 390, 390), 0, 10)
        for base in self.baseArr:
            base.draw()
        for i, b in enumerate(self.bArray):
            if b_num != None and i == b_num:
                continue
            b.draw()
        if b_num != None:
            self.bArray[b_num].draw()

    def merge(self, b_num, t_num):
        if b_num == t_num:
            return
        if self.bArray[b_num].val == self.bArray[t_num].val:
            self.bArray[t_num].val += 1
            self.bArray[b_num].val = 0
        else:
            temp = self.bArray[b_num].val
            self.bArray[b_num].val = self.bArray[t_num].val
            self.bArray[t_num].val = temp

    def checkEmpty(self):
        for b in self.bArray:
            if b.val == 0:
                return True
        return False
    
    def generate(self):
        if self.checkEmpty():
            rand_num = random.randint(0,len(self.bArray)-1)
            while(self.bArray[rand_num].val != 0):
                rand_num = random.randint(0,len(self.bArray)-1)
            self.bArray[rand_num].val = random.randint(1,4)

    def auto(self):
        for i, ib in enumerate(self.bArray):
            if ib.val == 0:
                continue
            for j, jb in enumerate(self.bArray):
                if i == j or jb.val == 0:
                    continue
                if ib.val == jb.val:
                    self.merge(i,j)
                    continue