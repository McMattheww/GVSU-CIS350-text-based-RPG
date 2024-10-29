#WIP
class World:

    #list of all rooms in current map, XY coordinates are key, room object is value
    rooms = {}

    #list of all enemies in current map, to be cycled through every turn to act.
    enemyList = ()