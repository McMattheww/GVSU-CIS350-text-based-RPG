#WIP
import room
import Entities as EN

class World:

    #list of all rooms in current map, XY coordinates are key, room object is value
    rooms = {}

    #list of all enemies in current map, to be cycled through every turn to act.
    enemyList = ()

    #the player
    player = EN.Player()



    def __init__(self):
        self.worldgen1(5)



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





    #call to generate rooms
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






