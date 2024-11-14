import time
import world
import pygame
from pygame.locals import *
import controller as c


def main():
    w1 = world.World()   #create a game world instance
    pygame.init()    #initialize screen
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    pygame.display.set_caption('Test')


    background = pygame.Surface(screen.get_size())  #create background
    background = background.convert()
    background.fill((60, 60, 60))


    screen.blit(background, (0, 0))   #draw the background
    c.rendermap(screen, w1)  # renders map, using 720x720 screen space on the right side
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
        #
        #
        #
        ##
        #render text or objects here to be drawn each frame
        ##
        #
        if w1.attackmode:
            c.escape_attack_mode(keys, w1)
            #
            c.check_attack_selection(sc, keys, w1)
            #
            c.confirm_attack_selection(sc, keys, w1)
        else:
            c.check_movement(screen, keys, w1)  # check user input to move
            #
            c.enter_attack_mode(keys, w1)  # checks input for entering attack mode
        #
        #
        #
        pygame.display.flip()    # render next frame
        clock.tick(60)      # limits FPS to 60
    #################################################################
    #################### END OF GAME LOOP #############################
    #################################################################
    #nothing beyond here will run 'till the game quits







if __name__ == '__main__':
    main()




