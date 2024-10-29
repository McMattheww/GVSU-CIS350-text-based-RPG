#WIP
import room


class World:

    #list of all rooms in current map, XY coordinates are key, room object is value
    rooms = {}

    #list of all enemies in current map, to be cycled through every turn to act.
    enemyList = ()




    def __init__(self):
        pass





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







