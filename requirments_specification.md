#Requirements - WIP -


##Functional:


####Game World:

- A map shall be populated with interconnected rooms each with a unique (x, y) coordinate value

- A "Player Character" object representing the user shall populate a room

- "Enemy" objects shall populate rooms

- "Item" objects shall populate rooms

- Each set of interconnected rooms that only have changes in either the x OR y value of their (x, y) coordinates, but not both, from one 
room to the next shall count as "in line of sight" of eachother

####Movement:

- User shall be able to move player character to rooms with adjacent (x, y) coordinates

- "Enemy" objects shall become alerted when they "see" Player character, when both are in rooms in line of sight of eachother

- "Enemy" objects alerted of player's presence shall pursue player, moving to rooms with adjacent (x, y) coordinates

- Movement shall be turn based, the player character moves once, then all alerted enemies move once

####Combat

- User shall be able to expend turn attacking an enemy object in the same room as their player character

- The strength of user's attack shall vary based on equipped weapon

- Alerted enemy objects already in the same room as the player character shall expend their turn performing an attack on the player character

- When player character has ranged weapon equipped, user shall be able to expend turn performing ranged attack on an enemy object in a room 
in line of sight of the player character

- Player Character object should track statistics related to combat. HP, etc.

####Items

- "Inventory" list should track items the player character is carrying

- "Equipped" item should track a specific weapon item the player character is currently holding

- User shall have ability to expend turn using a consumable item, that boosts player character statistics

- User shall be able to switch equipped weapon to another weapon item in their inventory

- User shall be able to "pick up" items when they are in the same room as the player character, removing them from the room and adding them to the inventory


##Non-Functional:

- User shall be presented with a main menu on execution of program

- User shall be able to start game using play button

- User shall be able to configure game using options button

- User shall be able be able to end program using quit button

-