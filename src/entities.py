class Player:
    attack_range = 2 # temp variable for testing - should change based on equipped weapon
    def __init__(self, name="", coordinates=(0, 0), hitpoints=100, max_hitpoints=100):
        self.name = name
        self.coordinates = coordinates
        self.hitpoints = hitpoints
        self.max_hitpoints = max_hitpoints

    def move(self, direction, room_list):
        # Define possible movements
        moves = {
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }

        if direction in moves:
            # Calculate new coordinates based on direction
            new_coordinates = (
                self.coordinates[0] + moves[direction][0],
                self.coordinates[1] + moves[direction][1]
            )
            # Check if new coordinates exist in room_list
            if new_coordinates in room_list:
                self.coordinates = new_coordinates
                return True
            else:
                return False  # Movement failed if room doesn't exist
        else:
            return False  # Invalid direction


    def player_attack(self, enemy, enemy_list):
        enemy_list.remove(enemy)



class Enemy:
    def __init__(self, coordinates, hitpoints=100, max_hitpoints=100, strength=10):
        self.coordinates = coordinates      # Room occupied by enemy, set by argument
        self.hitpoints = hitpoints          # Default hitpoints
        self.max_hitpoints = max_hitpoints  # Maximum hitpoints
        self.strength = strength            # Enemy's strength value


def check_encounter(player, enemy, room_list):
    # Check if player and enemy are in the same room
    if player.coordinates == enemy.coordinates:
        enemy_attack(player, enemy)  # Trigger enemy attack if they are in the same room
    else:
        enemy_movement(enemy, player, room_list)  # Move the enemy if they are in different rooms
def enemy_movement(enemy, player, room_list):
    # Calculate the difference in x and y coordinates between the enemy and player
    x_diff = player.coordinates[0] - enemy.coordinates[0]
    y_diff = player.coordinates[1] - enemy.coordinates[1]

    # Determine the movement direction based on the difference in coordinates
    if abs(x_diff) > abs(y_diff):
        # Move in the x direction (east or west)
        if x_diff > 0:
            enemy.coordinates = (enemy.coordinates[0] + 1, enemy.coordinates[1])  # Move east
        else:
            enemy.coordinates = (enemy.coordinates[0] - 1, enemy.coordinates[1])  # Move west
    else:
        # Move in the y direction (north or south)
        if y_diff > 0:
            enemy.coordinates = (enemy.coordinates[0], enemy.coordinates[1] + 1)  # Move north
        else:
            enemy.coordinates = (enemy.coordinates[0], enemy.coordinates[1] - 1)  # Move south


def enemy_attack(player, enemy):
    # Reduce player's hitpoints by the enemy's strength
    player.hitpoints -= enemy.strength

    # Ensure player's hitpoints do not go below 0
    if player.hitpoints < 0:
        player.hitpoints = 0

