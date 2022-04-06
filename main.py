import three
import pygame

top = [ (1,2), (0,1), (1,0), (2,1) ]
top_zoomed = [ (x*20,y*10) for (x,y) in top]

origin = (100,100)

BLOCK_COL = 0xffff00

def draw(screen):
    pygame.draw.rect(screen, 0x0000ff, (100,100,200,200))
    
    block(screen, 0,0, BLOCK_COL)
    block(screen, 1,0, BLOCK_COL + 0x80)
    block(screen, 2,0, BLOCK_COL + 0xf0)
    block(screen, 0,1, BLOCK_COL - 0x004000)
    block(screen, 1,1, BLOCK_COL - 0x004000)
    block(screen, 2,1, BLOCK_COL - 0x004000)


def block(screen, x, y , col):
    ix = x * 20 - y * 20 + origin[0]
    iy = x * 10 + y * 10 + origin[1]
    t = [ (px+ix, py+iy) for (px,py) in top_zoomed]
    pygame.draw.polygon(screen, col, t )


three.go(draw)
