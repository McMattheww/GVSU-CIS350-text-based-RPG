Team name: Text-Based-RPG

Team members: Matthew VanSlooten, Nathan Lenters.

# Introduction

We are creating a post-apocalyptic, turn-based RPG game, using a square grid for the map.

The main feature of the game is you have a player character with certain statistics, health points, hunger level, inventory, etc. 
As you engage in combat with enemies or deal with environemtal hazards, these statistics are affected. 

the player can interact with all the same monsters, items, traps, etc. in that room, or they can also move to an adjacent rooms in the grid.

Alot of the work could come from developing the combat system and enemies in an interesting way.
 It could be useful to look at the combat systems for other RPG games and see how they are implemented

Features
Character moves through map grid representing game world
combat system for fighting enemies that also populate game world
environmental factors, items in rooms to pick up, traps, low light level, slippery floor, etc. to makes rooms more interesting
Player character has statistics and items, possibly weapons and armor too, they use to help overcome challenges


# Anticipated Technologies

Python, with external library PyGame for game features, and PyInstaller to package game as executable instead
 of python script

Github to host repo

Trello to host scrum board, track issues, plan sprints.

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
