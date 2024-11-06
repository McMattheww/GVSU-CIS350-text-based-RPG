# Requirements - WIP -


## Functional:


#### Game World:

- A map shall be populated with interconnected rooms each with a unique (x, y) coordinate value

- A "Player Character" object representing the user shall populate a room

- "Enemy" objects shall populate rooms

- "Item" objects shall populate rooms

- Each set of interconnected rooms that only have changes in either the x OR y value of their (x, y) coordinates, but not both, from one 
room to the next shall count as "in line of sight" of each other

- Certain actions such as movement, attacking, or enemies becoming alerted should create a "sound" event, 

- Sound event should propagate a specified range amount to other adjacent rooms, ignoring if the rooms have line of sight

#### Movement:

- User shall be able to move player character to rooms with adjacent (x, y) coordinates

- "Enemy" objects shall become alerted when they "see" Player character, when both are in rooms in line of sight of each other

- Enemy objects shall become alerted when they "hear" player character, when the enemy objects are located in a room which sound has reached

- "Enemy" objects alerted of player's presence shall pursue player, moving to rooms with adjacent (x, y) coordinates

- Movement shall be turn based, the player character moves once, then all alerted enemies move once

#### Combat

- Enemy Objects should have "HP" statistic representing health

- Player Character object should track statistics related to combat. HP, etc.

- User shall be able to expend turn attacking an enemy object in the same room as their player character, reducing enemy object HP based on the attack strength

- The strength of user's attack shall vary based on equipped weapon item

- Alerted enemy objects already in the same room as the player character shall expend their turn performing an attack on the player character

- User shall be able to expend turn performing ranged attack on an enemy object in a room in line of sight of the player character's current room

- Player character must have ranged weapon equipped in order to perform ranged attack

- Player character must have at least one ammunition item associated with their equipped range weapon in order to perform ranged attack

- Performing ranged attack shall drain ammunition from the player character inventory

- User attacking shall drain durability rating of equipped weapon

- Attacks should have a probability of missing, doing no damage to target

- Weapons that reach 0 durability or less should be destroyed, or removed from the game

- After an equipped weapon is destroyed, the player shall be left with wit an "empty" weapon equipped, representing no weapon


#### Items

- "Inventory" list should track items the player character is carrying

- "Equipped" item should track a specific weapon item the player character is currently holding

- User shall have ability to expend turn using a consumable item, that boosts player character statistics

- User shall be able to switch equipped weapon to another weapon item in their inventory

- User shall be able to "pick up" items when they are in the same room as the player character, removing them from the room and adding them to the inventory


## Non-Functional:

- User shall be presented with a main menu on execution of program

- User shall be able to start game using play button

- User shall be able to configure game using options button

- User shall be able be able to end program using quit button

-
