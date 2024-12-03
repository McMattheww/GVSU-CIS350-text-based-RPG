#WIP
import room
import entities as EN

class World:


    rooms = {}  #dictionary of all rooms in current map, XY coordinates are keys, room objects are values

    roomLOS = {} #dictionary tracking which rooms in the map are in line of sight of eachother,
                 #key is room XY coordinates, value is set of XY coordinates of rooms that are in LOS of that room

    enemyList = []  #list of all enemies in current map, to be cycled through every turn to act.

    enemyInRange = [] #list of enemies in the current map that are in range, of the player's attack

    player = EN.Player()  #the player

    attackmode = False   # represents if the player is currently in attack mode

    selectedEnemy = ''  # object ID of currently selected attack target
    selectedEnemyIndex = ''


    def __init__(self):
        self.worldgen2(3)
        self.enemygen2()
        self.LOSgen()




    def turn(self):
        # one turn of gameplay - should be run after a player action
        for enemy in self.enemyList:
            EN.check_encounter(self.player, enemy, self.rooms)
            pass


### player actions ###

    def player_move(self, direction):
        self.player.move(direction, self.rooms)
        self.turn()

    def player_attack(self, targetID):
        pass
        #self.player.attack
        #self.turn()


### end player actions ###



    # generates rooms
    def worldgen2(self, size):
        size *= 3
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
            if r.XY[0] < -3 or r.XY[0] > 3 and r.XY[1] < -3 or r.XY[1] > 3:
                #todo define random chance to add enemies in each room
                self.enemyList.append(EN.Enemy(r.XY))

    def enemygen2(self):
        for r in self.rooms.values():
            if r.XY[0] == -2 or r.XY[0] == 2 or r.XY[1] == -2:
                self.enemyList.append(EN.Enemy(r.XY))
            if r.XY[0] == -2:
                self.enemyList.append(EN.Enemy(r.XY))





#TODO: add line of sight for diagonal rooms, currently its limited to a horizontal and vertical line of rooms from the current room
    def LOSgen(self):
        for room in self.rooms:
            self.roomLOS[room] = set((room)) #ensures that each room itself is always included in the roomLOS value sets

            x = self.rooms[room].XY[0]
            y = self.rooms[room].XY[1]
            x += 1
            while (x, y) in self.rooms:
                self.roomLOS[room].add((x, y))
                x += 1

            x = self.rooms[room].XY[0]
            y = self.rooms[room].XY[1]
            x -= 1
            while (x, y) in self.rooms:
                self.roomLOS[room].add((x, y))
                x -= 1

            x = self.rooms[room].XY[0]
            y = self.rooms[room].XY[1]
            y += 1
            while (x, y) in self.rooms:
                self.roomLOS[room].add((x, y))
                y += 1

            x = self.rooms[room].XY[0]
            y = self.rooms[room].XY[1]
            y -= 1
            while (x, y) in self.rooms:
                self.roomLOS[room].add((x, y))
                y -= 1






















