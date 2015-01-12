import pygame, sys, time
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 400))
car = pygame.image.load('dragon.png')
myfont = pygame.font.SysFont("monospace", 15)

while True:
    screen.fill([255,255,255])
    pos=pygame.mouse.get_pos()
    x= pos[0]
    y= pos[1]
    screen.blit(car,(x,y))
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    time.sleep(0.01)