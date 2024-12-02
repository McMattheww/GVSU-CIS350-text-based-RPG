# Overview
Here is a list specifying the requirments we plan on implementing in our project.
# Functional Requirements 
1. Player shall be able to walk, moving one space in a turn
2. Player shall be able to sprint, moving two spaces in a turn, but using additonal stamina
3. Player movement shall be restricted by the amount of adjacent rooms
4. Player Character object representing the user shall populate a room
5. Map shall be populated with interconnected rooms each with a unique (x, y) coordinate value
6. Enemy objects shall populate rooms
7. Item objects shall populate rooms
8. Inventory list should track items the player character is carrying
9. Certain actions such as movement, attacking, or enemies becoming alerted should create a "sound" event
10. Enemy objects shall become alerted when they "see" Player character, when both are in rooms in line of sight of each other
11. Movement shall be turn based, the player character moves once, then all alerted enemies move once
12. Enemy Objects should have HP statistic representing health
13. User shall be able to eattack an enemy object in the same room as their player character
14. The strength of user's attack shall vary based on equipped weapon item
15. Alerted enemy objects already in the same room as the player character shall expend their turn performing an attack on the player character
# Non-Functional Requirements
1. User shall be able to run executable on Windows
2. User shall be able to run executable on MacOS
3. User shall be able to run executable on Linux
