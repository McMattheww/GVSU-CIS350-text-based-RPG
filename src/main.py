#import world
import pygame
from pygame.locals import *


def main():
    pygame.init()    #initialize screen
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption('Test')


    background = pygame.Surface(screen.get_size())  #create background
    background = background.convert()
    background.fill((80, 80, 80))


    screen.blit(background, (0, 0))   #draw the background
    pygame.display.flip()  #render first frame
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        #render text or objects here to be drawn each frame
        pygame.display.flip()  #render frame
        clock.tick(60)  # limits FPS to 60



if __name__ == '__main__': main()