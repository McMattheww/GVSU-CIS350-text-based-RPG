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

    #render map squares
    pygame.draw.rect(sc, (0, 0, 0), (560, 0, 720, 720))  # black background for rooms
    distance = [0, 0]
    for room in w1.rooms:
        distance[0] = room[0] - w1.player.coordinates[0] + 11
        distance[1] = room[1] - w1.player.coordinates[1] + 4

        # render rectangles based of coordinates, only within 4 squares of player, on right side of screen
        if 16 > distance[0] > 6 and -1 < distance[1] < 9:
            pygame.draw.rect(sc, (200, 200, 200), (distance[0] * 80, distance[1] * 80, 80, 80))


    #render player
    pygame.draw.circle(sc, (0, 200, 0), (920, 360), 10)


    #rendering enemies
    enemiesPerRoom = {}    # track the amount of enemies in the same room
    for enemy in w1.enemyList:
        if enemy.coordinates not in enemiesPerRoom:
            enemiesPerRoom[enemy.coordinates] = 1
        else:
            enemiesPerRoom[enemy.coordinates] += 1

        distance[0] = (enemy.coordinates[0] - w1.player.coordinates[0]) + 11
        distance[1] = (enemy.coordinates[1] - w1.player.coordinates[1]) + 4
        offset = determineOffset(enemiesPerRoom[enemy.coordinates])

        if 16 > distance[0] > 6 and -1 < distance[1] < 9:
            pygame.draw.circle(sc, (200, 0, 0), ((distance[0] * 80) + offset[0], (distance[1] * 80) + offset[1]), 5)





#determines how to draw enemy sprites based on how many enemies are in the same room
def determineOffset(enemyCounter):
    offset = (40, 40)
    if enemyCounter == 1:
        offset = (20, 20)
    elif enemyCounter == 2:
        offset = (60, 20)
    elif enemyCounter == 3:
        offset = (20, 60)
    elif enemyCounter == 4:
        offset = (60, 60)
    return offset










