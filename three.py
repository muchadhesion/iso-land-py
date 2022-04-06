
import pygame

# pygame window params
WINDOW_WIDTH=640
WINDOW_HEIGHT=800
game_time_ms = 0

def default_drawfn(screen):
    pygame.draw.circle(screen, 0xffff00, (300,300), 100)

def go(drawfn=default_drawfn):
    pygame.init()

    screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    running = True
    clock = pygame.time.Clock()

    global game_time_ms
    while running:
        ms = clock.tick(60)
        game_time_ms += ms
        screen.fill((0,0,20))

        # draw the thing
        drawfn(screen)

        pygame.display.flip()
        # check exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__=="__main__":
    # call the main function
    go()

