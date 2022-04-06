import three
import pygame

top = [ (1,2), (0,1), (1,0), (2,1) ]
top_zoomed = [ (x*20,y*10) for (x,y) in top]

origin = (190,100)

BLOCK_COL = 0xff4000

def draw(screen):
    pygame.draw.rect(screen, 0x0000ff, (100,100,200,200))

    for ix in range(10):
        for iy in range(10):
            coladd = ix * 0x10 + iy * 0x1000
            block(screen, ix, iy, BLOCK_COL + coladd)

def block(screen, x, y , col):
    ix = x * 20 - y * 20 + origin[0]
    iy = x * 10 + y * 10 + origin[1]
    t = [ (px+ix, py+iy) for (px,py) in top_zoomed]
    pygame.draw.polygon(screen, col, t )


three.go(draw)
