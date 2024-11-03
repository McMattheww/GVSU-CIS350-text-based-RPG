import time
import pygame
from pygame.locals import *

## misc. functions for use in main.py






# checks user input for arrow key input, performs movement, then renders new map position
def check_movement(sc, keys, w1):
    if keys[pygame.K_UP]:
        w1.player_move("south")
        rendermap(sc, w1)
        time.sleep(0.1)
    if keys[pygame.K_DOWN]:
        w1.player_move("north")
        rendermap(sc, w1)
        time.sleep(0.1)
    if keys[pygame.K_LEFT]:
        w1.player_move("west")
        rendermap(sc, w1)
        time.sleep(0.1)
    if keys[pygame.K_RIGHT]:
        w1.player_move("east")
        rendermap(sc, w1)
        time.sleep(0.1)


def enter_attack_mode(keys, w1):
    if keys[pygame.K_SPACE]:
        w1.attackmode = True



def escape_attack_mode(keys, w1):  # press space to enter attack targeting mode

    if keys[pygame.K_ESCAPE]:  # escape key to cancel tageting mode
        w1.attackmode = False














# matthew's function - working on rendering map squares around player each frame, and player himself
def rendermap(sc, w1):
    pygame.draw.rect(sc, (0, 0, 0), (560, 0, 720, 720))  # black background for rooms
    distance = [0, 0]
    for room in w1.rooms:  # w1 should be replaced with an instance of the world class
        distance[0] = room[0] - w1.player.coordinates[0] + 11
        distance[1] = room[1] - w1.player.coordinates[1] + 4

        # render rectangles based of coordinates, only within 4 squares of player, on right side of screen
        if 16 > distance[0] > 6 and -1 < distance[1] < 9:
            pygame.draw.rect(sc, (200, 200, 200), (distance[0] * 80, distance[1] * 80, 80, 80))
    pygame.draw.circle(sc, (0, 200, 0), (920, 360), 10)















