#WIP
import room
import Entities as EN

class World:


    rooms = {}  #list of all rooms in current map, XY coordinates are keys, room objects are values

    enemyList = []  #list of all enemies in current map, to be cycled through every turn to act.

    player = EN.Player()  #the player

    attackmode = False   # represents if the player is currently in attack mode


    def __init__(self):
        self.worldgen1(6)
        self.worldgen2(6)
       #self.enemygen1()# generate enemies when ready




    def turn(self):
        # one turn of gameplay - should be run after a player action
        for enemy in self.enemyList:
            EN.check_encounter(self.player, enemy)


### player actions ###
    def player_move(self, direction):
        self.player.move(direction, self.rooms)
        self.turn()

    def player_attack(self):
        pass
        #self.player.attack
        #self.turn()
### end player actions ###

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




