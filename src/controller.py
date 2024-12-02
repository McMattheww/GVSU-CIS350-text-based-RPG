import time
import pygame
from pygame.locals import *

## misc. functions for use in main.py


# checks user input for arrow key input, performs movement, then renders new map position
def check_movement(sc, keys, w1, messages):
    if keys[pygame.K_UP]:
        w1.player_move("south")
        messages.append("Player moved south")
        rendermap(sc, w1)
        time.sleep(0.1)
        print(w1.roomLOS[w1.player.coordinates])
    if keys[pygame.K_DOWN]:
        w1.player_move("north")
        messages.append("Player moved north")
        rendermap(sc, w1)
        time.sleep(0.1)
    if keys[pygame.K_LEFT]:
        w1.player_move("west")
        messages.append("Player moved west")
        rendermap(sc, w1)
        time.sleep(0.1)
    if keys[pygame.K_RIGHT]:
        w1.player_move("east")
        messages.append("Player moved east")
        rendermap(sc, w1)
        time.sleep(0.1)


#check if user presses space to enter attack mode
def enter_attack_mode(sc, keys, w1):
    if keys[pygame.K_SPACE]:
        w1.attackmode = True
        for enemy in w1.enemyList:
            xDiff = abs(enemy.coordinates[0] - w1.player.coordinates[0])
            yDiff = abs(enemy.coordinates[1] - w1.player.coordinates[1])
            distance = xDiff + yDiff
            if w1.player.attack_range >= distance and enemy.coordinates in w1.roomLOS[w1.player.coordinates]:
                w1.enemyInRange.append(enemy)
        w1.selectedEnemyIndex = 0
        if len(w1.enemyInRange) > 0:
            w1.selectedEnemy = id(w1.enemyInRange[0])
        rendermap(sc, w1)

#check if user presses escape to exit attack mode
def escape_attack_mode(sc, keys, w1):  # press space to enter attack targeting mode
    if keys[pygame.K_ESCAPE]:  # escape key to cancel tageting mode
        w1.enemyInRange.clear()
        w1.attackmode = False
        w1.selectedEnemy = ''
        rendermap(sc, w1)

        #check if the user presses an arrow key in attack mode, changing target selection
def check_attack_selection(sc, keys, w1):
    #TODO: arrows keys should cycle through the enemies in enemyInRange list, setting one to be actively selecvted as target
    if keys[pygame.K_UP]:
        rendermap(sc, w1)
    if keys[pygame.K_DOWN]:
        rendermap(sc, w1)
    if keys[pygame.K_LEFT]:
        if len(w1.enemyInRange) > 0:
            w1.selectedEnemyIndex -= 1
        if w1.selectedEnemyIndex == -1:
            w1.selectedEnemyIndex = len(w1.enemyInRange) - 1
        w1.selectedEnemy = id(w1.enemyInRange[w1.selectedEnemyIndex])
        rendermap(sc, w1)
        time.sleep(0.1)
    if keys[pygame.K_RIGHT]:
        if len(w1.enemyInRange) > 0:
            w1.selectedEnemyIndex += 1
        if w1.selectedEnemyIndex == len(w1.enemyInRange):
            w1.selectedEnemyIndex = 0
        w1.selectedEnemy = id(w1.enemyInRange[w1.selectedEnemyIndex])
        rendermap(sc, w1)
        time.sleep(0.1)


#checks for user presses CTRL while in attack mode, confirming their current target selection
def confirm_attack_selection(sc, keys, w1):
    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
        if len(w1.enemyInRange) > 0:
            w1.player_attack(w1.selectedEnemy)

            w1.enemyInRange.clear()
            w1.attackmode = False
            w1.selectedEnemy = ''
            rendermap(sc, w1)


# Render message log
def render_message_log(sc, messages, x=10, y=10, width=500, height=200, line_height=20, font_size=16):
    pygame.draw.rect(sc, (0, 0, 0), (x, y, width, height))  # Background for the log
    pygame.draw.rect(sc, (255, 255, 255), (x, y, width, height), 2)  # Border for the log

    font = pygame.font.Font(None, font_size)
    for i, message in enumerate(messages[-(height // line_height):]):  # Display last messages
        text = font.render(message, True, (255, 255, 255))
        sc.blit(text, (x + 5, y + i * line_height + 5))

# Render character name and status bars
def render_status_bars(sc, player, x=10, y=220, width=500, bar_height=20, font_size=16):
    pygame.draw.rect(sc, (0, 0, 0), (x, y, width, 100))  # Background for the status section
    pygame.draw.rect(sc, (255, 255, 255), (x, y, width, 100), 2)  # Border for the section

    font = pygame.font.Font(None, font_size)
    name_text = font.render(f"Name: {player.name}", True, (255, 255, 255))
    sc.blit(name_text, (x + 10, y + 10))

    # Render health bar
    pygame.draw.rect(sc, (255, 0, 0), (x + 10, y + 40, width - 20, bar_height))
    pygame.draw.rect(sc, (0, 255, 0), (x + 10, y + 40, (width - 20) * (player.hitpoints / player.max_hitpoints), bar_height))

    hp_text = font.render(f"HP: {player.hitpoints}/{player.max_hitpoints}", True, (255, 255, 255))
    sc.blit(hp_text, (x + 10, y + 40 + bar_height + 5))

    # Render attack range
    range_text = font.render(f"Attack Range: {player.attack_range}", True, (255, 255, 255))
    sc.blit(range_text, (x + 10, y + 80))



# matthew's function - working on rendering map squares around player each frame, and player himself
def rendermap(sc, w1):

    tile = pygame.image.load("80x80tile.bmp")

    pygame.draw.rect(sc, (0, 0, 0), (560, 0, 720, 720))  # black background for rooms


    # render map squares ##TODO: instead of drawing square, draw square sprite with a grid on the edge
    distance = [0, 0]
    for room in w1.rooms:
        distance[0] = room[0] - w1.player.coordinates[0] + 11
        distance[1] = room[1] - w1.player.coordinates[1] + 4

        # render rectangles based of coordinates, only within 4 squares of player, on right side of screen
        if 16 > distance[0] > 6 and -1 < distance[1] < 9:
            sc.blit(tile, (distance[0] * 80, distance[1] * 80, 80, 80))



    #render player
    pygame.draw.circle(sc, (0, 200, 0), (920, 360), 6)


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
            if id(enemy) == w1.selectedEnemy:
                pygame.draw.circle(sc, (100, 170, 170), ((distance[0] * 80) + offset[0], (distance[1] * 80) + offset[1]), 5)
            else:
                pygame.draw.circle(sc, (200, 0, 0), ((distance[0] * 80) + offset[0], (distance[1] * 80) + offset[1]), 5)

#determines how to draw enemy sprites based on how many enemies are in the same room
def determineOffset(enemyCounter):
    offset = (40, 40)
    if enemyCounter == 1:
        offset = (25, 25)
    elif enemyCounter == 2:
        offset = (55, 25)
    elif enemyCounter == 3:
        offset = (25, 55)
    elif enemyCounter == 4:
        offset = (55, 55)
    return offset


