import pygame
import time
from constant import *
from game import Game
from button import Button, Switch

pygame.display.set_caption("Merge")

def main():
    run = True
    b_num = None
    clock = pygame.time.Clock()
    game = Game()
    btnGenerate = Button(60, 470, "Generate")
    btnAuto = Button(220, 470, "Auto Merge")
    btnAutoMode = Switch(380, 470)
    while run:
        clock.tick(FPS)
        WIN.fill(WHITE)
        game.draw(b_num)
        if btnGenerate.draw():
            for i in range(GENERATE_RATE):
                game.generate()
        if btnAuto.draw():
            game.auto()
        if btnAutoMode.draw():
            for i in range(GENERATE_RATE):
                game.generate()
            game.auto()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    b_num = game.select(event.pos)
                    if b_num != None and game.bArray[b_num].val == 0:
                        b_num = None

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and b_num != None:
                    game.bArray[b_num].reset()
                    t_num = game.select(event.pos)
                    if t_num != None:
                        game.merge(b_num, t_num)
                    b_num = None

            if event.type == pygame.MOUSEMOTION:
                if b_num != None:
                    game.bArray[b_num].rect.move_ip(event.rel)

            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    pygame.quit()

main()