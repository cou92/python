import pygame

def drawfigure(scr,clr,x,y):
    pygame.draw.line(scr,clr,[100+x,100+y], [105+x,110+y], 2)
    pygame.draw.line(scr, clr, [100+x,100+y], [95+x,110+y], 2)
    pass
