#WIP
import room
import Entities as EN

class World:


    rooms = {}  #list of all rooms in current map, XY coordinates are keys, room objects are values

    enemyList = []  #list of all enemies in current map, to be cycled through every turn to act.

    player = EN.Player()  #the player



    def __init__(self):
        pass




    def game_loop(self):
        # continues to run turns while player has health
        while self.player.hitpoints > 0:
            self.turn()

    def turn(self):
        # one turn of gameplay
        self.player_action()
        for enemy in self.enemyList:
            EN.check_encounter(self.player, enemy)

    def player_action(self):
        #TODO
        #need to get input from keyboard/button press to determine which action to perform
        self.player.move("north", self.rooms)







    #generates rooms in straight line, in all 4 directions, from (0, 0)
    def worldgen1(self, size):
        x=0
        y=0

        x=-size
        while x <= size:
            self.rooms[(x, y)] = room.Room((x, y))
            x+=1

        x = 0
        y = -size
        while y <= size:
            self.rooms[(x, y)] = room.Room((x, y))
            y+=1

    # generates rooms in the outline of a square, creating a new layer each 3 rooms
    def worldgen2(self, size):
        x=0
        y=0
        interval=0

        x = -size
        while x <= size:
            interval = x % 3
            if interval == 0:
                y = -size
                while y <= size:
                    self.rooms[(x, y)] = room.Room((x, y))
                    y += 1
            x += 1

        y = -size
        while y <= size:
            interval = y % 3
            if interval == 0:
                x = -size
                while x <= size:
                    self.rooms[(x, y)] = room.Room((x, y))
                    x += 1
            y += 1


#randomly populate rooms with enemies, enemies will not spawn a certain distance form (0, 0)
    def enemygen1(self):
        for r in self.rooms.values():
            if r.XY[0] < -2 or r.XY[0] > 2 and r.XY[1] < -2 or r.XY[1] > 2:
                #todo define random chance to add enemies in each room
                self.enemyList.append(EN.Enemy(r.XY))



