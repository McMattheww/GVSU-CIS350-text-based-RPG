# Software Requirements
Here is a list specifying the requirments we have met in our final product.

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




### Player Character> 
| ID  | Requirement     | 
| :-------------: | :----------: | 
| FR6 | User shall be able to move player character to move to an adjacent room either directly north, east, south, or west, using up arrow, right arrow, down arrowm or left arrow | 
| FR7 | Player character shall be able to attack an enemy, removing them from the game | 
| FR8 | Player movement or attacking shall count as performing an action, giving the enemy a turn to act | 
| FR9 | Player character shall have a health value, starting at 100 | 
TODO: add attack mode


  
  

### Enemies
| ID  | Requirement     |
| :-------------: | :----------: | 
| FR1 | During the enemy turn to act, all enemies in the map shall perform one action | 
| FR2 | Enemies shall perform a movement for their action if the player character is in a seperate room | 
| FR3 | Enemies shall perform an attack for their action if the player character is in the same room, reducing the player's health | 
| FR3 | Enemy movement shall move the enemy to an adjacent room either directly north, east, south, or west, in an attempt to get closer to the player | 
| FR3 | If the enemy attack lowers the player hitpoints to 0 or lower, the game shall end | 





## Non-Functional Requirements

### <Name of Feature 1> 

| ID  | Requirement     | 
| :-------------: | :----------: | 
| NFR1 | <Non-Functional Requirement 1> | 
| NFR2 | < Non-Functional Requirement 2> |
| NFR3 | < Non-Functional Requirement 3> |
| … | … | 


* User shall be able to run executable on Windows
* User shall be able to run executable on MacOS
* User shall be able to run executable on Linux




# Software Artifacts

<Describe the purpose of this section>

* [I am a link](to_some_file.pdf)

