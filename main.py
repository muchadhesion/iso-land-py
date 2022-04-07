import three
import pygame
import pygame as pg
import math

isox, isoy = 20, 10

top = [ (1,2), (0,1), (1,0), (2,1) ]
top_zoomed = [ (x*isox,y*isoy) for (x,y) in top]
front_right = [ (2,1), (2,10), (1, 11), (1,2)]
front_right_zoomed = [ (x*isox,y*isoy) for (x,y) in front_right]
front_left= [ (1,2), (1,11), (0,10), (0,1)]
front_left_zoomed = [ (x*isox,y*isoy) for (x,y) in front_left]

origin = (200,200)

map = pygame.image.load('map.png')
map_z = pg.transform.scale(map, (200,200))

BLOCK_COL = 0xff4000

def draw(screen, t = 0):
    screen.blit( map_z, (100,100) )
    # t = 6000
    ox = int( 38 * math.sin(t/2000) + 50 )
    oy = int( 38 * math.cos(t/1000) + 50 )
    # oy = 10
    # ox = 80

    pygame.draw.rect(screen, 0xffffff, (ox*2 + 100, oy*2 + 100, 20,20))
    for ix in range(10):
        for iy in range(10):
            x = ix + ox
            y = iy + oy
            h = map.get_at((x,y))[0]
            hfr = map.get_at((x+1,y))[0]
            hfl = map.get_at((x,y+1))[0]
            d = 0
            if h < hfr or h < hfl:
                d = 30
            if iy == 9 or ix == 9:
                d = 30
            coladd = ((x * 0x10) & 0xff) + ((y * 0x1000) & 0xff00)
            block(screen, ix, iy, col= BLOCK_COL + coladd, height=h, depth=d)

def block(screen, x, y , col=0xffff00, height = 0, depth = 30):
    ix = x * 20 - y * 20 + origin[0]
    iy = x * 10 + y * 10 + origin[1] + height * 1
    t = [ (px+ix, py+iy) for (px,py) in top_zoomed]
    pygame.draw.polygon(screen, col, t )
    if depth > 0:
        fr = [ (px+ix, py+iy) for (px,py) in front_right_zoomed]
        fl = [ (px+ix, py+iy) for (px,py) in front_left_zoomed]
        pygame.draw.polygon(screen, 0x404040, fr )
        pygame.draw.polygon(screen, 0x202020, fl )

three.go(draw)
