Team name: Text-Based-RPG

Team members: Matthew VanSlooten, Nathan Lenters.

# Introduction

We are creating a text based RPG game, we may use some limited graphics or ASCII art, for a title screen for example.
The main feature of the game is you have a player character with certain statistics, health points, hunger level, inventory, etc. 
As you engage in combat with enemies or deal with environemtal hazards, these statistics are affected. 
Where the player is in the game world will be tracked on a room-by-room basis, like the different rooms of a dungeon. When in one of these rooms 
the player can interact with all the same monsters, items, traps, etc. in that room, or they can also move to an adjacent room.
All the room objects the player can travel to could be held in a dictionary, with a key value representing (x, y) coordinates that tracks the location of each room, 
making sure you can only travel to adjacent rooms, and easily changing the players current coordinates by incrementing the (x, y) value based on direction traveled. 

Once we have the player character, rooms, and the ability to travel between rooms, we then need to populate those rooms with interesting things. 
Items to collect or inspect, enemies to fight, traps to avoid, possibly some story elements or puzzles to solve.

Alot of the work could come from developing the combat system and enemies in an interesting way.
 It could be useful to look at the combat systems for other RPG games and see how they are implemented

Features
Character moves through rooms representing game world
combat system for fighting enemies that also populate game world
environmental factors, items in rooms to pick up, traps, low light level, slippery floor, etc. to makes rooms more interesting
Player character has statistics and items, possibly weapons and armor too, they use to help overcome challenges


# Anticipated Technologies

Python, with external library PyGame for game features, and PyInstaller to package game as executable instead
 of python script

Github to host repo

Jira to host scrum board, track issues, plan sprints.

# Method/Approach

We plan on using an Agile approach with a scrum board. It will be nice to be able to quickly churn out a working basic game in the first sprint, and 
then adapt based on how we, and other people we interview, feel about the results. This approach is more adaptable, since after every sprint we can evaluate how the previous sprint went when planning the next. 

# Estimated Timeline

Milestone 1 - preperation
We should have all the documentation and planning ready. SRS documents, class diagrams, use case, a list of backlog issues that 
can be added to Jira for the first sprint. We already have a good overview of the project and what technology we'll use, and the remote repo is all set up.
Finishing this should take 1 to 1 1/2 weeks

Milestone 2 - construction
Start looking at code and implementing features, should be in a basic playable state by the end
2 to 3 weeks

Milestone 3 - refining
 Start finishing up and posishing game, start testing.
2 weeks

Milestone 4 - presentation
Final documentation and prepare demo for demonstartion
1/2 to 1 week

# Anticipated Problems

The main problem I forsee is making content for the game, making maps with rooms, items, and enemies, possibly using 
some level of randomly generated content. Its important to try and code the game in a way where adding this kind 
of content to the game is as simple as possible. Even with a solid core system, a game is no fun if theres nothing 
to do. A game with limited content also has little replayability.
