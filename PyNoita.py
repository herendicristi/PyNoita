"""
PyNoita - A Python implementation inspired by the game Noita.

This project is a simple passion project created by Cristian Herendi.
Copyright (c) 2025 Cristian Herendi.

This program is free software: you may use, modify, and distribute it
This program was created for educational purposes and as part of the portfolio for Cristian Herendi.

Disclaimer:
- "Noita" and related aspects of the game are copyrighted and trademarked
  by Nolla Games. This program is not affiliated with or endorsed by
  Nolla Games in any way.
- This project was created solely for educational purposes and to learn Python.

License:
This project is licensed under the MIT licence. See the LICENSE file
for more details.

current version: beta

"""

#total monsters drank during creation of the game: 2

import random
import math
import time

# Global variables

# Luck variables
rawGlobalLuck = 1.00  # Base luck value
globalLuck = round(rawGlobalLuck, 2)  # Rounded luck value used in the game

# Player variables
playerHealth = 100  # Player health
inventory = []  # Player inventory
playerPerks = []  # Player perks
playerState = "alive"  # Player state (alive or dead)

# World variables
currentWorld = 0  # Current world index
currentWorldName = ""  # Name of the current world
currentLevel = 0  # Current level index
currentLevelName = ""  # Name of the current level

if currentLevel == 0:
    currentLevelName = "The Mines"
elif currentLevel == 1:
    currentLevelName = "Holy Mountain"
elif currentLevel == 2:
    currentLevelName = "Coal Pits"
elif currentLevel == 3:
    currentLevelName = "Holy Mountain"
elif currentLevel == 4:
    currentLevelName = "The Snowy Depths"
elif currentLevel == 5:
    currentLevelName = "Holy Mountain"
elif currentLevel == 6:
    currentLevelName = "The Jungle"
elif currentLevel == 7:
    currentLevelName = "Holy Mountain"
#if chain is probably not good, but it works for now

# Enemy variables
enemyDamageMultiplier = 1.0  # Multiplier for enemy damage
enemyHealthMultiplier = 1.0  # Multiplier for enemy health

# Enemy data
enemiesId = {
    1,
    2,
    3
}
#placeholder enemy data

enemiesNames = {
    "Murk",
    "Slime",
    "Rat"
}
#more to come

enemiesDamage = {
    1: 10,
    2: 15,
    3: 5
}
#placeholder enemy damage data
enemiesHealth = {
    1: 20,
    2: 10,
    3: 5,
}
#placeholder enemy health data

# global functions

def pickRandomEnemy():
    #Picks a random enemy from the enemiesId set and returns its ID.
    return random.choice(list(enemiesId))

def pickWorldName():
    # Generates a random world name
    name1 = random.choice(["monstrous", "dangerous", "mysterious", "dark", "light"])
    name2 = random.choice(["cave", "mountain", "forest", "lake", "river"])
    name3 = random.choice(["of", "in", "at", "on"])
    
    if name3 == "of":
        name4 = random.choice(["danger", "mystery", "darkness", "light"])
    elif name3 == "in":
        name4 = random.choice(["the village", "the city", "the forest", "the cave"])
    elif name3 == "at":
        name4 = random.choice(["the top", "the bottom", "the middle", "the edge"])
    elif name3 == "on":
        name4 = random.choice(["the mountain", "the hill", "the valley", "the plain"])
    else:
        name4 = "error"  # Fallback in case of unexpected value
    
    return f"{name1} {name2} {name3} {name4}"
# will add more names later


# end of global functions

def tutorialFight(currentEnemy, currentEnemyName, tutorialWand):
    global playerHealth  # Ensure playerHealth is accessible and modifiable
    while playerHealth > 0 and enemiesHealth[currentEnemy] > 0:
        print(f"\nYour health: {playerHealth}")
        print(f"The {currentEnemyName}'s health: {enemiesHealth[currentEnemy]}")
        option = input("What do you want to do? (1 = attack, 2 = defend, 3 = check stats): ")

        blocking = False  # Reset blocking status at the start of each turn
        
        if option == "1":
            print("You use " + tutorialWand["name"] + " to attack!")
            time.sleep(1)
            damageDealt = tutorialWand["spells"][0]["damage"] * tutorialWand["damage"]
            print(f"You deal {damageDealt} damage!")
            enemiesHealth[currentEnemy] -= damageDealt
            if enemiesHealth[currentEnemy] <= 0:
                global currentEnemyState
                currentEnemyState = "dead"
                break
        elif option == "2":
            print("You defend yourself, reducing incoming damage!")
            blocking = True
        elif option == "3":
            print("Your stats:")
            print(f"Health: {playerHealth}")
            print(f"Wand: {tutorialWand['name']}")
            print(f"Enemy: {currentEnemyName}, Health: {enemiesHealth[currentEnemy]}, Damage: {enemiesDamage[currentEnemy]}")
            continue  # Skip enemy's turn since checking stats is free
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
            continue

        # Enemy's turn (placeholder logic)
        print(f"\nThe {currentEnemyName} attacks!")
        if blocking == True:
            enemyDamage = enemiesDamage[currentEnemy]/2
        elif blocking == False:
            enemyDamage = enemiesDamage[currentEnemy]
        playerHealth -= enemyDamage
        print(f"The {currentEnemyName} deals {enemyDamage} damage to you!")
        if playerHealth <= 0:
            global playerState
            playerState = "dead"
            break

def runTutorial():
    print("Welcome to PyNoita! This is a simple implementation of the game Noita.")
    print("In this game, you will explore a randomly generated world and fight enemies.")
    print("You can also create your own spells and wands.")
    print("Let's start by generating a random world!")
    time.sleep(2)
    print("Generating world...")
    time.sleep(2)
    print("World name: " + pickWorldName())
    time.sleep(2)
    print("lets start by generating a random enemy!")
    time.sleep(1)
    currentEnemy = pickRandomEnemy()
    if currentEnemy == 1:
        print("You have encountered a Murk!")
        currentEnemyName = "Murk"
    elif currentEnemy == 2:
        print("You have encountered a Slime!")
        currentEnemyName = "Slime"
    elif currentEnemy == 3:
        print("You have encountered a Rat!")
        currentEnemyName = "Rat"
    else:
        print("error")
    
    time.sleep(2)
    print("lets get you used to the combat system!")
    print("this is a turn based combat system, so you will have to wait for your turn to attack")
    print("you will be given an option to attack, defend, or check stats")
    print("checking stats is free and does not take away your turn")
    time.sleep(2)
    print("you also have an inventory, which you can use to store items")
    print("you will be given a wand, which you can use to cast spells")
    time.sleep(2)
    tutorialWand = {
        "name": "Basic Wand",
        "spells/cast": 1,
        "damage": 1.2,
        "mana": 10,
        "capacity": 3,
        "spells": [
            {
                "name": "Fireball",
                "damage": 10,
                "mana": 5,
                "type": "projectile",
            }
        ]
    }
    print("You have received a wand!")
    print("Wand name: " + tutorialWand["name"])
    print("Wand spells/cast: " + str(tutorialWand["spells/cast"]))
    print("Wand damage: " + str(tutorialWand["damage"]))
    print("Wand mana: " + str(tutorialWand["mana"]))
    print("Wand capacity: " + str(tutorialWand["capacity"]))
    print("Wand spells: " + str(tutorialWand["spells"]))
    #will have to add a way to show the spells in a better way
    time.sleep(2)
    print("each wand hads a capacity, which is the number of spells it can hold")
    print("spells are used to cast projectiles, alter other spells, and many other things")
    time.sleep(2)
    print("a big part of the game is creating your wand in a way that it is effective")
    print("each wand goes through the spells in order, so you can create a chain of spells")
    print("some spells can be altered by other spells, so you can create some really powerful combinations")
    print("and some spells have a set amount of times they can be used, so you have to be careful")
    time.sleep(2)
    print("lets go through the wand's stats")
    print("the wand name is the name of the wand (obviously)")
    print("the wand spells/cast is the number of spells that can be cast at once per turn")
    print("the wand damage is the damage of the wand. each spell has its own damage, so the wand's damage is the multiplier")
    print("the wand has a max mana, which is the amount of mana it can hold, each spell has its own mana cost, if you run out of mana, you cant cast spells, and the mana regenerates after the enemy's turn")
    print("the wand capacity is the number of spells it can hold")
    print("the wand spells is the list of spells that the wand has, in order")
    time.sleep(2)
    print("lets go through the spells stats")
    print("the spell name is the name of the spell (obviously)")
    print("the spell damage is the damage of the spell, which is multiplied by the wand's damage")
    print("the spell mana is the mana cost of the spell, taking away from the wand's mana")
    print("the spell type is the type of the spell, which can be projectile, support, or other")
    print("projectile spells are the most common, and they are the ones that deal damage")
    print("support spells are the ones that alter other spells, and they are the ones that create chains")#
    time.sleep(2)
    print("each enemy has its own stats, they do not have a wand, but they have their own damage and health")
    print("the enemy damage is the damage the enemy does, and the enemy health is the health of the enemy")
    print("you can also defend, which reduces the damage you take by half")
    print("if the enemy health reaches 0, the enemy is defeated")
    print("if your health reaches 0, you are defeated")
    time.sleep(2)
    print("sorry for the long tutorial, but it is important to understand the game")
    print("lets try fighting the enemy!")
    time.sleep(2)
    tutorialFight(currentEnemy, currentEnemyName, tutorialWand)
    if playerState == "dead":
        retry = input("You have been defeated! would you like to retry? (y/n): ")
        if retry.lower() == "y":
            print("Retrying...")
            playerHealth = 100
            tutorialFight(currentEnemy, currentEnemyName, tutorialWand)
        elif retry.lower() == "n":
            print("Exiting tutorial...")
          

    
    if currentEnemyState == "dead":
        print("You have defeated the " + currentEnemyName + "!")
    #placeholder

# Main logic
tutorialOption = input("Do you want to play in tutorial mode? (y/n): ")
if tutorialOption.lower() == "y":
    runTutorial()
elif tutorialOption.lower() == "n":
    print("Skipping tutorial...")
else:
    print("Invalid input. Defaulting to tutorial mode.")
    runTutorial()


# chisel out the tutorial
# add more content to the global variables, enemys, wands, spells, etc.
# start main game loop

# not sure how to implement the main game loop yet, will need to think about it
# add a way to save and load the game, using file handling
# add rooms using a 2D array, and add a way to move between rooms, if the player is in a room and has cleared it, the room will be marked as cleared, and no enemies will spawn in it
# add a way to create a map, using a 2D array, and add a way to move between rooms.

# just putting ideas out there, not sure how to implement them yet, brainstorming
# a good idea would be to have settings for the game, mainly just
# the speed of the text, something like time.sleep(gameSpeed)
# and the gameSpeed variable would be set to 1 by default, and the player could change it in the settings

# Gduskit. easter egg
# gduskit, if youre reading this, tell me if u want to help me with the game
# co-creator maybe?
