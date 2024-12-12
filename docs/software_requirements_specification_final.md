# Software Requirements
This document specifies requirments that have been met by our final product delivery, December 11, 2024.

## Functional Requirements 

### Map
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR1 | Map shall be populated with interconnected rooms each with a unique (x, y) coordinate value | 
| FR2 | Player character object representing the user shall populate a room | 
| FR3 | Enemy objects shall populate rooms | 

### Graphics
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR4 | The rooms surrounding the player character shall be drawn as a 9x9 grid of tiles | 
| FR5 | green icon shall be drawn at the location of the player character | 
| FR6 | red icon shall be drawn at the location of each enemy | 
| FR7 | Status bar shall be drawn to indicate the palyer character's current health | 
| FR8 | Message log shall display a message each time the player character moves | 

### Player Character
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR9 | User shall be able to move player character to move to an adjacent room | 
| FR10 | Player character shall be able to attack an enemy, removing them from the game | 
| FR11 | Player movement or attacking shall count as performing an action, giving the enemy a turn to act | 
| FR12 | Player character shall have a health value, starting at 100 | 


### Enemies
| ID  | Requirement     |
| :-------------: | :----------: | 
| FR13 | During the enemy turn to act, all enemies in the map shall perform one action | 
| FR14 | Enemies shall movement to an adjacent room for their action if the player character is in a seperate room, towards the player | 
| FR15 | Enemies shall perform an attack for their action if the player character is in the same room, reducing the player's health | 
 

## Non-Functional Requirements

### Performance
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR1 | Game shall achieve average 200 Mhz CPU usage in testing with at least 20 enemies drawn on screen | 
| NFR2 | Game shall achieve average 200 Mhz CPU usage in testing with a map consisting of at least 100 rooms|
| NFR3 | Game shall achieve average 200 Mhz CPU usage in testing with message log rendered |
| NFR4 | Game shall achieve average 200 Mhz CPU usage in testing with status bar rendered |

### Compatability
| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR5 | Game shall run on Windows | 
| NFR6 | Game shall run on Mac OS | 
| NFR7 | Game shall run on Linux | 



* User shall be able to run executable on Windows
* User shall be able to run executable on MacOS
* User shall be able to run executable on Linux




# Software Artifacts

Here are various links to resources used in the course of development.

[Use Case Diagram](https://github.com/McMattheww/GVSU-CIS350-text-based-RPG/blob/main/artifacts/use_case_diagram/Use%20case%20diagram.pdf)

[UI Mockup](https://github.com/McMattheww/GVSU-CIS350-text-based-RPG/blob/main/artifacts/UI%20Mockup.pdf)

[Trello Board](https://trello.com/b/Vjng2tHl/text-based-rpg-scrum)

[Extended Description](https://github.com/McMattheww/GVSU-CIS350-text-based-RPG/blob/main/artifacts/extended_description.md)



