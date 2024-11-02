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
    rendermap(screen)  # renders map, using 720x720 screen space on the right side
    pygame.display.flip()  #render first frame


##################################################################
####################### START OF GAME LOOP #########################
##################################################################
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        keys = pygame.key.get_pressed()  # get keyboard input
        #
        check_movement(screen, keys)
        #
        #
        #
        ##
        #render text or objects here to be drawn each frame
        ##
        #
        #
        #
        pygame.display.flip()    # render next frame
        clock.tick(60)      # limits FPS to 60
#################################################################
#################### END OF GAME LOOP #############################
#################################################################
#nothing beyond here will run 'till the game quits





#matthew's function - working on rendering map squares around player each frame
def rendermap(sc):
    pygame.draw.rect(sc, (0, 0, 0), (560, 0, 720, 720)) #black background for rooms
    distance =  [0,0]
    for room in w1.rooms:    #w1 should be replaced with an instance of the world class
        distance[0] = room[0] - w1.player.coordinates[0] + 11
        distance[1] = room[1] - w1.player.coordinates[1] + 4

        #render rectangles based of coordinates, only within 4 squares of player, on right side of screen
        if 16 > distance[0] > 6 and -1 < distance[1] < 9:
            pygame.draw.rect(sc, (200, 200, 200), (distance[0] * 80, distance[1] * 80, 80, 80))



#checks user input for a movement command, then renders the map from the new position
def check_movement(sc, keys):
    if keys[pygame.K_UP]:
        w1.player_move("north")
        rendermap(sc)
    if keys[pygame.K_DOWN]:
        w1.player_move("south")
        rendermap(sc)
    if keys[pygame.K_LEFT]:
        w1.player_move("east")
        rendermap(sc)
    if keys[pygame.K_RIGHT]:
        w1.player_move("west")
        rendermap(sc)








if __name__ == '__main__':
    w1 = world.World()
    main()
#game testing



