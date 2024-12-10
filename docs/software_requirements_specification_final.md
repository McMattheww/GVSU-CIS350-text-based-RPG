# Overview -WIP
Here is a list specifying the requirments we have met in our final product.

## Functional Requirements 

### Map:
* Map shall be populated with interconnected rooms each with a unique (x, y) coordinate value
* Player Character object representing the user shall populate a room
* Enemy objects shall populate rooms

### Graphics:


### Player Character:  
* Player character shall be able to move to an adjacent room either directly north, east, south, or west
* Player character shall be able to attack an enemy, removing them from the game
* Player movement or attacking shall count as performing an action, giving the enemy a turn to act
* Player character shall have a health value, starting at 100
  
### User Input:
* User shall be able to press the up arrow key to move the player character north
* User shall be able to press the right arrow key to move the player character east
* User shall be able to press the down arrow key to move the player character south
* User shall be able to press the left arrow key to move the player character west
* TODO - attack mode stuff

### Enemies:

* During the enemy turn to act, all enemies in the map shall perform one action
* enemies shall perform a movement for their action if the player character is in a seperate room
* enemies shall perform an attack for their action if th eplayer character is in the same room
* Enemy movement shall move the enemy to an adjacent room either directly north, east, south, or west
* During movement enemies shall move in a direction that gets them closer to the player
* Enemy attack shall reduce the amount of hitpoint the player character possesses
* If the enemy attack lowers the player hitpoints to 0 or lower, the game shall end






## Non-Functional Requirements

* User shall be able to run executable on Windows
* User shall be able to run executable on MacOS
* User shall be able to run executable on Linux
