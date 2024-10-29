class Player:
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


class Enemy:
    def __init__(self, coordinates, hitpoints=100, max_hitpoints=100, strength=10):
        self.coordinates = coordinates      # Room occupied by enemy, set by argument
        self.hitpoints = hitpoints          # Default hitpoints
        self.max_hitpoints = max_hitpoints  # Maximum hitpoints
        self.strength = strength            # Enemy's strength value


def check_encounter(player, enemy):
    # Check if player and enemy are in the same room
    if player.coordinates == enemy.coordinates:
        enemy_attack(player)  # Trigger enemy attack if they are in the same room
    else:
        enemy_movement(enemy)  # Move the enemy if they are in different rooms

