import world
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
    background.fill((60, 60, 60))


    screen.blit(background, (0, 0))   #draw the background
    pygame.display.flip()  #render first frame

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        ##
        #render text or objects here to be drawn each frame
        rendermap(screen)
        ##
        pygame.display.flip()  #render frame
        clock.tick(60)  # limits FPS to 60




#matthew's function - working on rendering map squares around player each frame
def rendermap(sc):
    distance =  [0,0]
    rectangles = []
    for room in w1.rooms:    #w1 should be replaced with an instance of the world class
        distance[0] = room[0] - w1.player.coordinates[0]
        distance[1] = room[1] - w1.player.coordinates[1]
        print(distance)

        #create recctangles based of coordintaes
        rectangles.append(pygame.draw.rect(sc, (200, 200, 200), (distance[0] * 50, distance[1] * 50, 50, 50)))
        #now attempting to render squares based off calculated distance







if __name__ == '__main__':
    w1 = world.World()
    main()




