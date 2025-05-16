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

# ^^ legal bullshit

# total monsters drank during creation of the game: 3
# i have a feeling they are going to be a lot more



import random
import math
import time
import pickle
import os

# Define the base directory for saving and loading files
base_dir = os.path.dirname(os.path.abspath(__file__))

# Update file paths for achievements and tutorial save
achievements_file = os.path.join(base_dir, "achievements.pickle")
tutorial_save_file = os.path.join(base_dir, "tutorialsave.pickle")

# Global variables

# Load achievements
try:
    with open(achievements_file, "rb") as file:
        acheivements = pickle.load(file)
except FileNotFoundError:
    acheivements = {
        "First Steps": False, "shadow": False,
        "Main Menu Easter Egg": False, "shadow": True
    }

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
currentWorldName = ""  # Name of the current world"
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

def saveAchievement(achievement_name):
    global acheivements
    try:
        acheivements[achievement_name] = True
        with open(achievements_file, "wb") as file:
            pickle.dump(acheivements, file)
    except (FileNotFoundError, EOFError):
        print(f"Error saving achievement: {achievement_name}. File not found or corrupted.")

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

tutorialComplete = False

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
    print("each enemy has its own stats, they do not have a wand but they have their own damage and health")
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
            tutorialComplete = True
            print("You have gained the \"First Steps\" achievement!")

                
        else:
            print("Invalid input. Exiting tutorial...")
            tutorialComplete = True
            print("You have gained the \"First Steps\" achievement!")
    
    if currentEnemyState == "dead":
        print("You have defeated the " + currentEnemyName + "!")
    #placeholder
        print("basic tutorial complete!")
        print("this tutorial was intentionally short, so you can find out more about the game yourself")
        print("as of version \'beta\', there is not an official tutorial other than this one")
        print("the game is still in development, so there will be more content added in the future")
        print("if you have any suggestions, please let me know!")
        tutorialComplete = True
        print("You have gained the \"First Steps\" achievement!")

skipTutorial = False


# Main logic
try:
    with open(tutorial_save_file, "rb") as file:
        tutorialCompleteLoaded = pickle.load(file)
except (FileNotFoundError, EOFError):  # Handle missing or corrupted file
    tutorialCompleteLoaded = False

tutorialComplete = tutorialCompleteLoaded

if tutorialComplete == False:
    tutorialOption = input("Do you want to play in tutorial mode? (y/n): ")
    if tutorialOption.lower() == "y":
        runTutorial()
        skipTutorial = False
    elif tutorialOption.lower() == "n":
        print("Skipping tutorial...")
        tutorialComplete = True
        skipTutorial = True
    else:
        print("Invalid input. Defaulting to tutorial mode.")
        runTutorial()
        skipTutorial = False
else:
    pass

# some redundant code, but it helps with readability

if tutorialComplete == True and skipTutorial == False:
    saveAchievement("First Steps")



#main menu
print("Welcome to PyNoita!")
time.sleep(1)
print("would you like to...")
mainMenuOption = input("1. Start a new game\n2. Load a game\n3. Settings\n4. Exit\n")
mainMenuValid = False

while mainMenuValid == False:
    if mainMenuOption == "1":
        print("Starting a new game...")
        time.sleep(1)
        mainMenuValid = True
        # start a new game
    elif mainMenuOption == "2":
        print("Loading game...")
        time.sleep(1)
        mainMenuValid = True
        # load a game
    elif mainMenuOption == "3":
        print("Settings")
        time.sleep(1)
        mainMenuValid = True
        # settings menu
    elif mainMenuOption == "4":
        print("Exiting game...")
        time.sleep(1)
        mainMenuValid = True
        exit()
    elif mainMenuOption == "easter egg":
        print("You found an easter egg!")
        saveAchievement("Main Menu Easter Egg")
        time.sleep(1)
        mainMenuValid = True
        # this game may have alot of easter eggs...
    else:
        mainMenuValid = False
        print("Invalid input. Please choose 1, 2, 3, or 4.")
        mainMenuOption = input("1. Start a new game\n2. Load a game\n3. Settings\n4. Exit\n")



# main game variables



# main game loop




# chisel out the tutorial - check
# add more content to the global variables, enemys, wands, spells, etc.
# start main game loop - check

# not sure how to implement the main game loop yet, will need to think about it
# add a way to save and load the game, using file handling
# add rooms using a 2D array, and add a way to move between rooms, if the player is in a room and has cleared it, the room will be marked as cleared, and no enemies will spawn in it
# add a way to create a map, using a 2D array, and add a way to move between rooms.

# just putting ideas out there, not sure how to implement them yet, brainstorming
# a good idea would be to have settings for the game, mainly just
# the speed of the text, something like time.sleep(gameSpeed)
# and the gameSpeed variable would be set to 1 by default, and the player could change it in the settings
