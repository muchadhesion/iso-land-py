import three
import pygame
import math

top = [ (1,2), (0,1), (1,0), (2,1) ]
top_zoomed = [ (x*20,y*10) for (x,y) in top]

origin = (200,200)

map = pygame.image.load('map.png')

BLOCK_COL = 0xff4000

def draw(screen, t = 0):
    pygame.draw.rect(screen, 0x0000ff, (100,100,200,200))

    ox = int( 40 * math.sin(t/1000) + 50 )
    for ix in range(10):
        for iy in range(10):
            x = ix + ox
            h = map.get_at((x,iy))[0]
            coladd = ix * 0x10 + iy * 0x1000
            block(screen, ix, iy, col= BLOCK_COL + coladd, height=h)

def block(screen, x, y , col=0xffff00, height = 0):
    ix = x * 20 - y * 20 + origin[0]
    iy = x * 10 + y * 10 + origin[1] + height * 1
    t = [ (px+ix, py+iy) for (px,py) in top_zoomed]
    pygame.draw.polygon(screen, col, t )


three.go(draw)
