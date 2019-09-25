##
# rpg_battle_sim.py
# Date: 1/07/19
# Author: NZK
# RPG battle sim focused around dental hygiene.
import random
import time
import sys
try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("Use IDLE")
# Main Function - Hub for battle
def main():
     # =====------------------ Stats and moves assigned to each character ------------------=====

    # This is the list of moves available in the game and their stats
    moves = {
        "Slap":("Rock", 15, "Phys", 6),
        "Super Slap":("Rock", 25, "Phys", 8),
        "Whiten":("Normal", 50, "Heal", 12),
        "Paste Blast":("Paper", 30, "Spec", 5),
        "Paste Explosion":("Paper", 40, "Spec", 7),
        "Ultra Bash":("Rock", 50, "Phys", 18),
        "Brush Bash":("Rock", 40, "Phys", 20),
        "Replenish":("Normal", 100, "Heal", 25),
        "Pacify":("Normal", "Sleep", "Status", 10),
        "Cavity Crush":("Rock", 15, "Phys", 8),
        "Decaying Beam":("Paper", 25, "Spec", 10),
        "Plaque":("Scissors", 10, "Spec", 4),
        "Bad Breath":("Paper", 30, "Phys", 20),
        "Scourge's Wrath":("Rock", 40, "Spec", 15),
        "Filling":("Scissors", 20 ,"Heal", 10),
        "Plaque Punch":("Paper", 30, "Phys", 18),
        "Neverending Decay":("Paper", 10, "Phys", 5)}

    # This is the list of moves descriptions that is used in the INFO TAB
    moves_desc = {
        "Slap":"A simple Slap",
        "Super Slap":"An upgraded version of the Slap, it has significantly more force.",
        "Whiten":"The user cleans their brush and heals them",
        "Paste Blast":"A powerful blast of Toothpaste",
        "Paste Explosion":"An upgraded Paste Blast, the user fires a bomb of Toothpaste at the enemy",
        "Ultra Bash":"An upgraded Brush Bash, The user throws their entire body at the opponent",
        "Brush Bash":"The user throws themselves at the opponent with extreme speed",
        "Replenish":"An upgraded whiten which heals significantly",
        "Pacify":"The user quells the enemys fighting spirit for a turn",
        "Cavity Crush":"The user attacks the enemy with a disgusting attack",
        "Decaying Beam":"The user attacks the enemy with dirty water in hopes of decaying them",
        "Plaque":"The user dirties the other, inflicting damage",
        "Bad Breath":"The user throws their rancid breath at the enemy",
        "Scourge's Wrath":"The enemy attacks in a flurry",
        "Filling":"The enemy heals itself by repairing the flesh",
        "Plaque Punch":"The enemy attacks with a fist made of grime",
        "Neverending Decay":"The Scourge's Signature move, its decaying body attacks!"}

    # This is the list of items available for finding in the game and their uses
    items = {
        "Mini Mouthwash":("Heal", 25, "HP"),
        "Med. Mouthwash":("Heal", 50, "HP"),
        "Massive Mouthwash":("Heal", 75, "HP"),
        "Ethereal Floss":("Heal", 20, "SP"),
        "Spectral Floss":("Heal", 40, "SP"),
        "Drain Plug":("Escape", 90, "Escape"),
        "Revive":("Revive", 75, "HP")}

    # This is the list of the items descriptions that is used in the INFO TAB
    items_desc = {
        "Mini Mouthwash":"Heals the user for 25 HP",
        "Med. Mouthwash":"Heals the user for 50 HP",
        "Massive Mouthwash":"Heals the user for 75 HP",
        "Ethereal Floss":"Revitalises the user and restores 20 SP",
        "Spectral Floss":"Revitalises the user and restores 40 SP",
        "Drain Plug":"Grants a 90% chance for the user to escape the battle",
        "Revive":"Revives the player if they ever get down to 0 HP"}

    # ===----- PLAYER STATS -----===
    # These are used for finding different stats and checking moves and health, this area helps the game run properly, these are called in the [F]ight, [B]ag, [R]un and Enemy Fight Functions
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61, "status":"none", "exp":0}
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Brush Bash"}
    player_items = {1:("Mini Mouthwash", 1), 2:("Med. Mouthwash", 1), 3:("Massive Mouthwash", 1), 4:("Ethereal Floss", 1), 5:("Spectral Floss", 1), 6:("Drain Plug", 1), 7:("Revive", 1)}
    # ===----- PLAYER STATS -----===


    # ===----- ENEMY STATS -----===
    # These are used in the same sense as the player stats but are used for the enemy instead, these are called in the Enemy Fight and [F] Functions
    enemy_stats = {"level":5, "type":"scissors", "hp":50, "sp":25, "atk":48, "def":64, "spd":31, "status":"none", "classifier":"Normal"}
    enemy_moves = {1:"Cavity Crush", 2:"Decaying Beam", 3:"Plaque", 4:"Bad Breath"}
    # ===----- ENEMY STATS -----===


    # ===----- OTHER STATS -----===
    # The other stats area includes EXP and Gold, it also includes the EXP and Gold an enemy will drop when defeated
    enemy_exp = 20
    enemy_gold = 50

    gold = 0
    exp = 0
    # ===----- OTHER STATS -----===

    # ===----- HELP BAR STUFF -----===
    # These are the help bar descriptions and names for each part, they are called in the [H]elp Function
    combat_help = {1:("HP","HP is short for Health Points, it decreases when attacked and increases when you heal"),
                   2:("SP","SP is short for Spirit Points, its how you and your enemy cast spells and magic"),
                   3:("Level","Your level dictates your stats, when you defeat enemies it may level up..."),
                   4:("Moves","You and the enemy have 4 moves each, you can use any of them as long as you have enough HP or SP"),
                   5:("Phys Moves","Physical Moves cost the user HP to cast and do damage to HP"),
                   6:("Spec Moves","Special Moves cost the user SP to cast and do damage to HP"),
                   7:("Heal Moves","These moves heal the user at the cost of SP"),
                   8:("Status Moves","These moves append a status to the opponent, which have a variety of effects"),
                   9:("Win Conditions","You either win or lose when HP drops to zero, or you escape the battle")}
    
    item_help = {1:("Mouthwashes","These restore HP based on how big they are"),
                 2:("Floss","These restore SP based on how they have been created, Ethereal is not as strong as Spectral"),
                 3:("Escape Items","These items let you escape battle, these normally have a higher chance of working than simply running"),
                 4:("Revive","Will automatically revive the holder if they reach zero HP")}
    # ===----- HELP BAR STUFF -----===
    
    # =====------------------ Stats and moves assigned to each character ------------------=====
    tutorial_over = False
    difficulty_set = False
    NORMAL_MULTIPLIER = 2
    HARD_MULTIPLIER = 3
    story_wait = 2
    player_hp_sp = {"hp":player_stats["hp"], "sp":player_stats["sp"]}
    enemy_hp_sp = {"hp":enemy_stats["hp"], "sp":enemy_stats["sp"]} 
    print("""Welcome to: The Quest for the GOLDEN BRUSH!
This game takes inspiration from Pokemon, Shin Megami Tensei and Final Fantasy""")
    time.sleep(story_wait)
    # Checks what difficulty the user sets the game to, uses the multiplier to set difficulty
    while difficulty_set == False:
        difficulty = difficulty_setting()
        if difficulty == "Easy" or difficulty == "E":
            difficulty = "EASY"
            print("Difficulty set to: {}".format(difficulty))
            difficulty_set = True
            
        elif difficulty == "Normal" or difficulty == "N":
            enemy_hp_sp["hp"] = enemy_hp_sp["hp"] * NORMAL_MULTIPLIER
            enemy_hp_sp["sp"] = enemy_hp_sp["sp"] * NORMAL_MULTIPLIER
            enemy_stats["hp"]= enemy_hp_sp["hp"]
            enemy_stats["sp"]= enemy_hp_sp["sp"]
            difficulty = "NORMAL"
            print("Difficulty set to: {}".format(difficulty))
            difficulty_set = True
            
        elif difficulty == "Hard" or difficulty == "H":
            enemy_hp_sp["hp"] = enemy_hp_sp["hp"] * HARD_MULTIPLIER
            enemy_hp_sp["sp"] = enemy_hp_sp["sp"] * HARD_MULTIPLIER
            enemy_stats["hp"]= enemy_hp_sp["hp"]
            enemy_stats["sp"]= enemy_hp_sp["sp"]
            difficulty = "HARD"
            print("Difficulty set to: {}".format(difficulty))
            difficulty_set = True
    enemy_hp_sp_recall = {"hp":enemy_hp_sp["hp"], "sp":enemy_hp_sp["sp"]}
    # Story print, you can skip by pressing Ctrl + C
    try:
        print("\n===---------- STORY ----------===\n")
        time.sleep(story_wait)
        print("Press Ctrl + C whenever to skip")
        time.sleep(story_wait)
        print("Your journey follows a boy who has awoken to his entire village that has been cursed with bad dental hygiene")
        time.sleep(story_wait)
        print("however your character finds himself immune. It is up to you to find a cure")
        time.sleep(story_wait)
        print("You recall hearing of a powerful relic hidden deep in the villages mines.")
        time.sleep(story_wait)
        print("You decide to venture down into the mines")
        time.sleep(story_wait)
        print("With your trusty magic brush to save your town, on the quest for the Golden Brush.")
        time.sleep(story_wait)
        print("You make your way to the front of the mine and are greeted by an enemy, it lunges at you!")
        time.sleep(story_wait)
        
    except KeyboardInterrupt:
        pass
    
    # Checks if the user skips the tutorial, if not then it plays the tutorial
    while tutorial_over == False:
        tutorial_over = tutorial(tutorial_over)
    # Plays first battle, then it plays the actual game
    battle_start(moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp, enemy_hp_sp_recall)
    time.sleep(story_wait)
    print("Whew, that was close!")
    print("You brush yourself off and head down.")
    floor_number = 1
    print("\n===---------- FLOOR {} ----------=== \n".format(floor_number))
    time.sleep(story_wait)
    print("You are X, Chests are C and the Stairs are S\n")
    time.sleep(story_wait)
    floor_number, enemy_stats = map_movement(floor_number, moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp, enemy_hp_sp_recall)
    if enemy_stats["classifier"] == "Boss":
        floor_number = 4
        if enemy_hp_sp["hp"] <= 0:
            color.write("\nYou Beat the Game!!", "STRING")
            return
    if enemy_stats["classifier"] == "Normal":
        print("You Managed to make it to Floor {}".format(floor_number))
        return

def map_movement(floor_number, moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp, enemy_hp_sp_recall):
    """This function is the main way in which the map is created, the map_movement function calls to assign_items,
    display and create_floor functions to make the map system possible,
    this is also where the movement is done and is the main hub for movement in the game"""
    finished_game = False
    ending_wait = 2
    moved = False
    # Sets floor borders, answer options and assigns the variables for placements
    options = ["left", "right", "up", "down", "w", "a", "s", "d"]
    
    # ===------ FLOOR VARIABLES -----===
    floor = []
    floor_borders = []
    floor_1_borders = [-1, 5]
    floor_2_borders = [-1, 6]
    floor_3_borders = [-1, 7]
    floor_number = 1
    # ===------ FLOOR VARIABLES -----===

    # ===----- ITEM/CO-ORD VARIABLES -----===
    chest_item = 0
    chest_coords = [0, 0]
    stair_coords = [0, 0]
    player_coords = [0, 0]
    prev_player_coords = [0, 0]
    # ===----- ITEM/CO-ORD VARIABLES -----===
    
    # assigns the different items their coordinates and places them on the map
    chest_item, chest_coords, stair_coords, player_coords, prev_player_coords = assign_items(floor_number, chest_coords, stair_coords, player_coords, prev_player_coords)
    # creates the list that holds all the variables and holds the grid
    floor, floor_borders = create_floor(floor, floor_number, floor_borders, floor_1_borders, floor_2_borders, floor_3_borders)

    # Places the character, chest and stairs at their designated coordinates
    floor[player_coords[0]][player_coords[1]] = "X"
    floor[chest_coords[0]][chest_coords[1]] = "C"
    floor[stair_coords[0]][stair_coords[1]] = "S"
    # Prints the grid
    display(floor)
    while finished_game == False:
        # If floor is 2, then it reloops, otherwise continues as floor has been printed once before
        if floor_number == 2 or floor_number == 3:
            print("\n===---------- FLOOR {} ----------=== \n".format(floor_number))
            display(floor)
        enemy_hp_sp = {"hp":enemy_hp_sp_recall["hp"], "sp":enemy_hp_sp_recall["sp"]}
        # Asks for movement and asks the user what they would want to do
        print("\nType: [w] = Up, [a] = Down, [s] = Left or [d] = Right to perform actions")
        movement = input("What would you like to do? ").lower().strip()
        # decides where to go based on users input, if input not in options then repeats
        if movement == "right" or movement == "d":
            player_coords[1] = player_coords[1] + 1
            
        elif movement == "left" or movement == "a":
            player_coords[1] = player_coords[1] - 1
            
        elif movement == "up" or movement == "w":
            player_coords[0] = player_coords[0] - 1
            
        elif movement == "down" or movement == "s":
            player_coords[0] = player_coords[0] + 1
            
        elif movement not in options:
            print("Please enter a proper option")
        # if the player coordinates are the same as any of the borders then you are put back where you were before
        if player_coords[1] in floor_borders or player_coords[0] in floor_borders:
            print("You try to go in that direction but you are met with a wall".format(movement))
            player_coords[0] = prev_player_coords[0]
            player_coords[1] = prev_player_coords[1]
            floor[player_coords[0]][player_coords[1]] = "X"
        # if your coords are not on a chest or the stairs then a battle has the chance to play, if the character is defeated then the game is over
        elif player_coords != chest_coords or player_coords != stair_coords:
            enemy_attack = random.randint(1, 100)
            if enemy_attack >= 30 and enemy_attack <= 40 or enemy_attack <= 70 and enemy_attack >= 80:
                time.sleep(ending_wait)
                # plays battle by calling the battle_start function
                battle_start(moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp, enemy_hp_sp_recall)
                if player_hp_sp["hp"] <= 0:
                    finished_game = True
                    return floor_number
        # if the player lands on a chest then they collect the item inside and the chest disappears by respawning off screen       
        if player_coords[0] == chest_coords[0] and player_coords[1] == chest_coords[1]:
            change_number = player_items[chest_item][1]
            change_number += 1
            player_items[chest_item] = player_items[chest_item][0], change_number
            print("Found {}, You now have x{}".format(player_items[chest_item][0], player_items[chest_item][1]))
            chest_coords = [10, 10]
        # if player lands on stairs then the map is replaced with the next one.
        if player_coords[0] == stair_coords[0] and player_coords[1] == stair_coords[1]:
            print("\n===----------NEXT LEVEL ----------=== \n")
            print("You traversed down the stairs")
            # if the floor number is 3 when the player touches the stairs then the final boss starts
            if floor_number == 3:
                print("You spot the relic sitting on a pedestal before your eyes")
                time.sleep(ending_wait)
                print("However, before you can reach it... A powerful enemy blocks the path!")
                time.sleep(ending_wait)
                # Enemy stats are changed to accomodate for the Boss and the moveset is changed. Then HP and SP are set and the battle begins, if the boss is defeated then the end of the game plays, otherwise the game ends with defeat.
                enemy_stats = {"level":10, "type":"rock", "hp":250, "sp":100, "atk":48, "def":64, "spd":31, "status":"none", "classifier":"Boss"}
                enemy_moves = {1:"Neverending Decay", 2:"Filling", 3:"Plaque Punch", 4:"Scourge's Wrath"}
                enemy_hp_sp = {"hp":enemy_stats["hp"], "sp":enemy_stats["sp"]}
                battle_start(moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp, enemy_hp_sp_recall)
                if enemy_hp_sp["hp"] <= 0:
                    game_ending()
                    return floor_number, enemy_stats
                elif player_hp_sp["hp"] <= 0:
                    finished_game = True
                    return floor_number
            # if not floor 3, goes to the next floor and reassigns the player, chest and stairs via new coords for the map 
            else:
                floor_number += 1
                floor, floor_borders = create_floor(floor, floor_number, floor_borders, floor_1_borders, floor_2_borders, floor_3_borders)
                chest_item, chest_coords, stair_coords, player_coords, prev_player_coords = assign_items(floor_number, chest_coords, stair_coords, player_coords, prev_player_coords)
                floor[player_coords[0]][player_coords[1]] = "X"
                floor[chest_coords[0]][chest_coords[1]] = "C"
                floor[stair_coords[0]][stair_coords[1]] = "S"
        # unless game has been beaten, continues to print the map and play the game
        if finished_game == False:    
            floor[prev_player_coords[0]][prev_player_coords[1]] = "O"
            floor[player_coords[0]][player_coords[1]] = "X"
            prev_player_coords[0] = player_coords[0]
            prev_player_coords[1] = player_coords[1]
            if floor_number == 1:
                print("\n===---------- FLOOR {} ----------=== \n".format(floor_number))
                display(floor)

def create_floor(create, floor_number, floor_borders, floor_1_borders, floor_2_borders, floor_3_borders):
    """This function is for creating the actual map that the player moves around in,
    it creates a grid and appends it to a list, which the size of the grid
    is dictated by the floor_number and then defines the spaces variable"""
    # Decides how big the map is by what floor the user is going to
    if floor_number == 1:
        floor_borders = floor_1_borders
        spaces = 5
    elif floor_number == 2:
        floor_borders = floor_2_borders
        create = []
        spaces = 6
    elif floor_number == 3:
        floor_borders = floor_3_borders
        create = []
        spaces = 7
    # Appends the grid to a list and does that based on the number "spaces" has been assigned
    for walls in range(spaces):
        create.append(["O"] * spaces)
    return create, floor_borders

def display(floor_list):
    """This function prints out the list as a grid and joins each part with a space"""
    # Prints out the list and joins each grid piece with a space
    for walls in floor_list:
        print(" ".join(walls))

def assign_items(floor_number, chest_coords, stair_coords, player_coords, prev_player_coords):
    """This function is used to assign all the items different coordinates and then reset the players coordinates to 0,0
    and also assigns which item is housed inside the chest on each floor, these variables are dictated by the floor_number.
    It will then return them and use them when printing out the floor"""
    # Decides where items will be placed based on floor number and returns them for appending to the list.
    if floor_number == 1:
        chest_item = 7
        chest_coords = [2, 2]
        stair_coords = [4, 4]
        player_coords = [0, 0]
        prev_player_coords = [0, 0]
        return chest_item, chest_coords, stair_coords, player_coords, prev_player_coords

    if floor_number == 2:
        chest_item = 3
        chest_coords = [5, 1]
        stair_coords = [5, 5]
        player_coords = [0, 0]
        prev_player_coords = [0, 0]
        return chest_item, chest_coords, stair_coords, player_coords, prev_player_coords

    if floor_number == 3:
        chest_item = 5
        chest_coords = [3, 3]
        stair_coords = [6, 6]
        player_coords = [0, 0]
        prev_player_coords = [0, 0]
        return chest_item, chest_coords, stair_coords, player_coords, prev_player_coords
        
def battle_start(moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp, enemy_hp_sp_recall):
    """This is the main options area, this is used whenever a battle is encountered.
    All of the different stats and information is called when the user enters a battle,
    and it is used as a hub for the battle."""
    finished_battle = False
    turn_number = 1
    HP_LEVEL_INCREASE = 10
    SP_LEVEL_INCREASE = 5
    stats_bar = "--------------------\ Stats \--------------------"
    stats_bar_2 = "--------------------/ Stats /--------------------"
    max_hp = player_stats["hp"]
    max_sp = player_stats["sp"]
    # Assigns enemy type for printing
    if enemy_stats["classifier"] == "Normal":
        enemy_type = "an Infected Brush"
    elif enemy_stats["classifier"] == "Boss":
        enemy_type = "The Scourge of the Mouth"
    color.write("Player encountered {}!".format(enemy_type), "ERROR")
    # Checks if the battle is over, if not then plays the next turn
    while finished_battle == False:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
                
        if battle_ended == False:
            finished_battle = False
            print("\n===---------- TURN {} ----------===\n".format(turn_number))
            # Stats Bar which shows the user the HP and SP of both your player and the enemy
            print(stats_bar)
            color.write("Player: LEVEL: {}, HP: {}/{}, SP:{}/{}\n".format(player_stats["level"], player_hp_sp["hp"], player_stats["hp"], player_hp_sp["sp"], player_stats["sp"]), "STRING")
            color.write("Enemy: LEVEL: {}, HP: {}/{}, SP:{}/{}\n".format(enemy_stats["level"], enemy_hp_sp["hp"], enemy_stats["hp"], enemy_hp_sp["sp"], enemy_stats["sp"]), "COMMENT")
            print(stats_bar_2)
            print("""What will you do?
[F] for Fight
[I] for Items
[R] for Run
[H] for Help""")
            # Input for decisions on what to do, these include Fight, Bag, Run and Help
            option = input("Please choose your option: ").upper()
            print("")
            if option == "F" or option == "FIGHT":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp = fight_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp, enemy_gold, enemy_exp, gold, exp, max_hp, max_sp, items, player_items)
            elif option == "I" or option == "ITEMS":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items = bag_command(turn_number, finished_battle, player_stats, enemy_stats, player_hp_sp, enemy_hp_sp, player_moves, enemy_moves, moves, items, items_desc, player_items, gold, enemy_gold, exp, enemy_exp)
            elif option == "R" or option == "RUN":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items = run_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp, player_items, items)
            elif option == "H" or option == "HELP":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items = help_command(turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items, combat_help, item_help)
            else:
                print("Please only input one of the 4 options")
       # Checks if the battle is over by checking the health of both parties or if the escape item used was successful
        elif battle_ended == True:
            print("\n=====---------- RESULT ----------=====\n")
            if player_items[7][1] == 0:
                if player_hp_sp["hp"] <= 0:
                    color.write("\nYou have been defeated", "COMMENT")
                if enemy_hp_sp["hp"] <= 0:
                    # If enemy is defeated, this will appear and player will be awarded EXP and Gold
                    color.write("You have won the battle!", "STRING")
                    print("Your brush has gained {} EXP and you obtained {} Gold!".format(enemy_exp, enemy_gold))
                    gold += enemy_gold
                    exp += enemy_exp
                    if exp >= 20:
                        player_stats["level"] = player_stats["level"] + 1
                        print("You have grown to Level {}!".format(player_stats["level"]))
                        player_stats["hp"] += HP_LEVEL_INCREASE
                        player_stats["sp"] += SP_LEVEL_INCREASE
                        player_hp_sp["hp"] += HP_LEVEL_INCREASE
                        player_hp_sp["sp"] += SP_LEVEL_INCREASE
                        print("\nPlayer's Max HP increased by {} and Max SP by {}".format(HP_LEVEL_INCREASE, SP_LEVEL_INCREASE))
                        exp = 0
                        if player_stats["level"] == 8:
                            player_moves[4] = "Ultra Bash"
                            print("Your 'Brush Bash' has upgraded to '{}'".format(player_moves[4]))
                        if player_stats["level"] == 10:
                            player_moves[1] = "Super Slap"
                            print("Your 'Slap' has upgraded to '{}'".format(player_moves[1]))
                        if player_stats["level"] == 12:
                            player_moves[3] = "Paste Explosion"
                            print("Your 'Paste Blast' has upgraded to '{}'".format(player_moves[3]))
                        if player_stats["level"] == 14:
                            player_moves[2] = "Replenish"
                            print("Your 'Whiten' has upgraded to '{}'".format(player_moves[2]))
                finished_battle = True
                return player_hp_sp, enemy_hp_sp, player_items
            # If the player reaches 0 HP, this will check if the user has a revive, which will restore 50HP and use the item
            elif player_items[7][1] > 0:
                revive_usage = player_items[7][0]
                color.write("Player used a {}\n".format(player_items[7][0]), "STRING")
                player_hp_sp["hp"] = items[revive_usage][1]
                color.write("Player recovered {} HP\n".format(items[revive_usage][1]), "STRING")
                change_number = player_items[7][1]
                change_number -= 1
                player_items[7] = player_items[7][0], change_number

def fight_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp, enemy_gold, enemy_exp, gold, exp, max_hp, max_sp, items, player_items):
    """This is the Fight Command,
    this allows the user to pick a move to use against the enemy and fight.
    When a move is picked, the enemy will take a turn and fight back,
    this command is chosen by inputting 'F' at the options menu,
    this menu also has an info tab, to check the info of any move that you have selected. """
    player_partition = "===---------- PLAYER MOVE ----------===\n"
    taken_turn = False
    max_player_hp = player_stats["hp"]
    max_player_sp = player_stats["sp"]
    HP_LEVEL_INCREASE = 10
    SP_LEVEL_INCREASE = 5
    INFO_TAB_BACK = 5
    FIGHT_TAB_INFO = 5
    FIGHT_TAB_BACK = 6
    NO_HEALTH = 0
    if enemy_stats["classifier"] == "Normal":
        enemy_type = "Brush"
    elif enemy_stats["classifier"] == "Boss":
        enemy_type = "Scourge of the Mouth"
        enemy_exp = 200
        enemy_gold = 1000
    # Prints out all of the moves in order of the player_moves list and prints out their cost alongside 
    for move_counter in range(len(player_moves)):
        print_move = player_moves[move_counter + 1]
        # Checks if the move is Physical or Special or Healing to allocate cost and usage type
        if moves[print_move][2] == "Phys":
            type_move = "HP"
            effect = "Damage"
        if moves[print_move][2] == "Spec":
            type_move = "SP"
            effect = "Damage"
        if moves[print_move][2] == "Heal":
            type_move = "SP"
            effect = "Healing"
        print("{}. [{}] [Cost : {}{}] - [{} : {}HP]".format(move_counter + 1, player_moves[move_counter + 1], moves[print_move][3], type_move, effect, moves[print_move][1]))
    print("""5. [INFO TAB]
6. [BACK]""")
    # Checks if the battle has ended, if not, lets the user take their turn, otherwise checks who has lost their HP or if the user used an escape item
    while taken_turn == False:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
        if battle_ended == False:
            try:
                # Input for a move to be used, 1-4 for moves and 5 for info, 6 to go back to the Options menu, if 1-6 is not input, repeats the question
                move_decision = int(input("Which move would you like to use? (1/2/3/4/5/6) "))
                if move_decision >= 1 and move_decision <= 4:
                    time.sleep(0.7)
                    move = player_moves[move_decision]
                    # Checks what type of move was used, this is to check what cost type to remove from, if the user does not have enough of the required cost type, the move doesnt work and the user is sent back to the input
                    if moves[move][2] == "Phys":
                        if player_hp_sp["hp"] > moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            color.write("Player used {}\n".format(move), "STRING")
                            enemy_hp_sp["hp"] -= moves[move][1]
                            color.write("The enemy {} lost {} HP\n".format(enemy_type, moves[move][1]), "COMMENT")
                            player_hp_sp["hp"] -= moves[move][3]
                        else:
                            print("You don't have enough HP to perform this action")
                            taken_turn = False
                    # if the move chosen is a special attack, costs SP, does damage to enemy, if they do not have sufficient SP for the move chosen, resets back to the input
                    if moves[move][2] == "Spec":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            color.write("Player used {}\n".format(move), "STRING")
                            enemy_hp_sp["hp"] -= moves[move][1]
                            color.write("The enemy {} lost {} HP\n".format(enemy_type, moves[move][1]), "COMMENT")
                            player_hp_sp["sp"] -= moves[move][3]
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                    # if the move chosen is heal, acts the same as if the move is special, however heals the user rather than damaging the opponent
                    if moves[move][2] == "Heal":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            color.write("Player used {}\n".format(move), "STRING")
                            if player_hp_sp["hp"] == player_stats["hp"]:
                                color.write("You are already at MAX HP\n", "STRING")
                            else:
                                player_hp_sp["hp"] += moves[move][1]
                                color.write("You regained {} HP!\n".format(moves[move][1]), "STRING")
                            player_hp_sp["sp"] -= moves[move][3]
                            if player_hp_sp["hp"] > max_hp:
                                player_hp_sp["hp"] = max_hp
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                        # If the move selected was a Status attack, takes cost from SP, puts a status on the enemy, if SP is not sufficient, resets back to input
                    if moves[move][2] == "Status":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            print("Player used {}\n".format(move))
                            enemy_hp_sp["status"] == moves[move][1]
                            print("The enemy {} was inflicted with {}\n".format(enemy_type, moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                            
                # If 5 was input before, open the info tab, this is where players can check what moves do and more in detail about their stats
                elif move_decision == FIGHT_TAB_INFO:
                    desc_decision = 0
                    print("===---------- INFO TAB ----------===")
                    
                    # Prints out the moves in order to display input options
                    for move_counter in range(len(player_moves)):
                        print_move = player_moves[move_counter + 1]
                        if moves[print_move][2] == "Phys":
                            type_move = "HP"
                        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
                            type_move = "SP"
                        print("{}. [{}][{}{}]".format(move_counter + 1, player_moves[move_counter + 1], moves[print_move][3], type_move))
                    print("5. [BACK]")
                    while desc_decision != 5:
                        try:
                            # Input for the Info Section, if 5 is input the user is taken back to the options menu, if input is 1-4, shows move info, if 5, goes back to options, if 1-5 not input, error shown and restarts input
                            desc_decision = int(input("Which move would you like to check?)(1/2/3/4/5) "))
                            
                            if desc_decision >= 1 and desc_decision <= 4:
                                move = player_moves[desc_decision]
                                if moves[move][2] == "Phys":
                                    type_move = "HP"
                                if moves[move][2] == "Spec" or moves[move][2] == "Heal":
                                    type_move = "SP"
                                    
                                # Information includes, name, description of what the move does, the damage / effect it has, the type of move it is and the cost to use the move
                                print("---------- {} ---------".format(move))
                                print("""Move: {}
Description : {}
Power : {}
Type : {}
Cost : {}{}""".format(move, moves_desc[move], moves[move][1], moves[move][2], moves[move][3], type_move))
                                
                            elif desc_decision == INFO_TAB_BACK:
                                return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                            
                        except:
                            print("Please only input a number from 1 - 5")
 
                elif move_decision == FIGHT_TAB_BACK:
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                
                else:
                    print("Please only input a number from 1 - 6")
                    taken_turn = False
                    
            except:
                print("Please only input a number from 1 - 6")
                taken_turn = False
                
            # Checks if the user has taken their turn, if true, runs battle ended code and checks if any parties have been defeated
            if taken_turn == True:
                battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
                
                # If the battle hasn't ended, plays the enemys turn and then starts the next turn at the Options Menu and carries over all HP and SP stats.
                if battle_ended == False:
                    finished_battle = False
                    enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp)
                    turn_number += 1
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                # If the battle has ended, checks who had lost their health, or if the user used an item to make them leave, also checks if the user has a revive on them in case the player lost their HP, checks items for revives
                elif battle_ended == True:
                    print("\n=====---------- RESULT ----------=====\n")
                    if player_hp_sp["hp"] <= NO_HEALTH:
                        if player_items[7][1] == 0:
                            color.write("You have been defeated\n", "COMMENT")
                        elif player_items[7][1] > 0:
                            revive_usage = player_items[7][0]
                            color.write("Player used a {}\n".format(player_items[7][0]), "STRING")
                            player_hp_sp["hp"] = items[revive_usage][1]
                            color.write("Player recovered {} HP\n".format(items[revive_usage][1]), "STRING")
                            # This changes the number of items the user carries to - 1 of the previous amount
                            change_number = player_items[7][1]
                            change_number -= 1
                            player_items[7] = player_items[7][0], change_number
                    # If the enemy was the one that had their health depleted, displays this and awards gold and EXP
                    if enemy_hp_sp["hp"] <= 0:
                        color.write("You have won the battle!\n", "STRING")
                        print("Your brush has gained {} EXP and you obtained {} Gold!".format(enemy_exp, enemy_gold))
                        gold += enemy_gold
                        exp += enemy_exp
                        # If exp goes above 20, the player levels up to a level higher than what was previously their level
                        if exp >= 20:
                            player_stats["level"] = player_stats["level"] + 1
                            print("You have grown to Level {}!".format(player_stats["level"]))
                            player_stats["hp"] += HP_LEVEL_INCREASE
                            player_stats["sp"] += SP_LEVEL_INCREASE
                            player_hp_sp["hp"] += HP_LEVEL_INCREASE
                            player_hp_sp["sp"] += SP_LEVEL_INCREASE
                            print("\nPlayer's Max HP increased by {} and Max SP by {}".format(HP_LEVEL_INCREASE, SP_LEVEL_INCREASE))
                            exp = 0
                            if player_stats["level"] == 8:
                                player_moves[4] = "Ultra Bash"
                                print("Your 'Brush Bash' has upgraded to '{}'".format(player_moves[4]))
                            if player_stats["level"] == 10:
                                player_moves[1] = "Super Slap"
                                print("Your 'Slap' has upgraded to '{}'".format(player_moves[1]))
                            if player_stats["level"] == 12:
                                player_moves[3] = "Paste Explosion"
                                print("Your 'Paste Blast' has upgraded to '{}'".format(player_moves[3]))
                            if player_stats["level"] == 14:
                                player_moves[2] = "Replenish"
                                print("Your 'Whiten' has upgraded to '{}'".format(player_moves[2]))
                    finished_battle = True
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp

def battle_over(player_hp_sp, enemy_hp_sp):
    """This is the battle over command,
    this checks if any enemies have been downed and then applies to the boolean; battle_ended,
    the proper variable, if any parties have been defeated then it is True,
    if not then it is False, then returns it to wherever it was called """
    battle_ended = False
    if player_hp_sp["hp"] <= 0 or enemy_hp_sp["hp"] <= 0:
        battle_ended = True  
    else:
        battle_ended = False
    # Returns battle ended to tell the code whether or not to display end screen
    return battle_ended
             
def enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp):
    """This is the enemy fight command, this allows the enemy to use a random move,
    however all cost and damage rules apply to enemies the same as they do to players,
    enemies also have only 4 moves, and have unique moves assigned to them that are not found with normal brushes"""
    enemy_partition = "\n===---------- ENEMY MOVE ----------===\n"
    max_enemy_hp = enemy_stats["hp"]
    enemy_moved = False
    if enemy_stats["classifier"] == "Normal":
        enemy_type = "Brush"
    elif enemy_stats["classifier"] == "Boss":
        enemy_type = "Scourge of the Mouth"
    time.sleep(0.7)
    print(enemy_partition)
    # Loops the code until a suitable move is found, it randomises until they use a move, checks hp and sp currently to avoid a softlock, and also checks status
    while enemy_moved == False:
        if enemy_hp_sp["hp"] >= 8 or enemy_hp_sp["sp"] >= 4:
            if enemy_stats["status"] != "Sleep":
                enemy_move = random.randint(1, 4)
                move = enemy_moves[enemy_move]
                # Checks if the move chosen in Physical, Spec, Heal or Status to choose cost type and then decide appropriate effects based on the move, checks until appropriate typing is found
                if moves[move][2] == "Phys":
                    if enemy_hp_sp["hp"] > moves[move][3]:
                        enemy_moved = True
                        color.write("Enemy {} used {}\n".format(enemy_type, move),"COMMENT")
                        player_hp_sp["hp"] -= moves[move][1]
                        color.write("You lost {} HP\n".format(moves[move][1]), "STRING")
                        enemy_hp_sp["hp"] -= moves[move][3]
                        time.sleep(0.7)
                    else:
                        enemy_move = random.randint(1, 4)
                        enemy_moved = False
                if moves[move][2] == "Spec":
                    if enemy_hp_sp["sp"] >= moves[move][3]:
                        enemy_moved = True
                        color.write("Enemy {} used {}\n".format(enemy_type, move), "COMMENT")
                        player_hp_sp["hp"] -= moves[move][1]
                        color.write("You lost {} HP\n".format(moves[move][1]), "STRING")
                        enemy_hp_sp["sp"] -= moves[move][3]
                        time.sleep(0.7)
                    else:
                        enemy_move = random.randint(1, 4)
                        enemy_moved = False
                        
                if moves[move][2] == "Heal":
                    if enemy_hp_sp["sp"] >= moves[move][3]:
                        enemy_moved = True
                        color.write("Enemy {} used {}\n".format(enemy_type, move), "COMMENT")
                        enemy_hp_sp["hp"] += moves[move][1]
                        color.write("The enemy {} regained {} HP!\n".format(enemy_type, moves[move][1]), "COMMENT")
                        enemy_hp_sp["sp"] -= moves[move][3]
                        if enemy_hp_sp["hp"] > max_enemy_hp:
                            enemy_hp_sp["hp"] = max_enemy_hp
                        time.sleep(0.7)
                    else:
                        enemy_move = random.randint(1, 4)
                        enemy_moved = False
            else:
                enemy_stats["status"] == "none"
        else:
            print("The Enemy can't move!")
            enemy_moved = True
    

def bag_command(turn_number, finished_battle, player_stats, enemy_stats, player_hp_sp, enemy_hp_sp, player_moves, enemy_moves, moves, items, items_desc, player_items, gold, enemy_gold, exp, enemy_exp):
    """This is the Bag Command, this lets the user use items that they have found or have been given at the start of the game,
    these include HP and SP healing items, an escape move and a revive move, when the user uses an item, their turn is used up and the enemy is available to attack"""
    # Sets max_hp and sp to the current stats found in the stats dictionary
    bag_partition = "\n===---------- ITEM USAGE ----------===\n"
    used_item = False
    print_no = 0
    HP_LEVEL_INCREASE = 10
    SP_LEVEL_INCREASE = 5
    INFO_TAB_NO = 8
    INFO_TAB_BACK = 8
    BAG_TAB_BACK = 9
    max_hp = player_stats["hp"]
    max_sp = player_stats["sp"]
    # Displays all items for usage, amount left and affect it has on the player for use when inputting an answer
    for item_counter in range(len(player_items)):
        item_type = player_items[item_counter + 1][0]
        if items[item_type][0] == "Heal":
            usage = items[item_type][1]
            effect = items[item_type][2]
        if items[item_type][0] == "Escape":
            usage = items[item_type][0]
            effect = "{}%".format(items[item_type][1])
        if items[item_type][0] == "Revive":
            usage = "Auto"
            effect = "Use"
        item_amount = player_items[item_counter + 1][1]
        print_no += 1
        print("{}. [{}][x{}] - [{} {}]".format(print_no, player_items[item_counter + 1][0], player_items[item_counter + 1][1], usage, effect))
    print("""8. [INFO TAB]
9. [BACK]""")
    # Until used item becomes true it will repeat the question, used item becomes true when the process of finding a suitable type of item, checking if the player has 1 or more and the actual usage of that item is complete
    while used_item == False:
        try:
            item_usage = int(input("What item would you like to use? (1/2/3/4/5/6/7/8/9) "))
            if item_usage >= 1 and item_usage <= 7:
                time.sleep(0.7)
                item = player_items[item_usage][0]
                # Checks if the player owns one of the items they want to use, then checks what type of item it is, repeats until suitable type of item is found, only works if the user has at least 1 of that item
                if player_items[item_usage][1] != 0:
                    if items[item][0] == "Heal":
                        if items[item][2] == "HP":
                            print(bag_partition)
                            color.write("Player used a {}\n".format(item), "STRING")
                            if player_hp_sp["hp"] == player_stats["hp"]:
                                color.write("You are already at MAX HP\n", "STRING")
                            else:
                                player_hp_sp["hp"] += items[item][1]
                                color.write("Player regained {} HP\n".format(items[item][1]), "STRING")
                            if player_hp_sp["hp"] > max_hp:
                                player_hp_sp["hp"] = max_hp
                            used_item = True
                            
                        elif items[item][2] == "SP":
                            print(bag_partition)
                            color.write("Player used a {}\n".format(item), "STRING")
                            if player_hp_sp["sp"] == player_stats["sp"]:
                                color.write("You are already at MAX SP\n", "STRING")
                            else:
                                player_hp_sp["sp"] += items[item][1]
                                color.write("Player regained {} SP\n".format(items[item][1]), "STRING")
                            if player_hp_sp["sp"] > max_sp:
                                player_hp_sp["sp"] = max_sp
                            used_item = True
                            
                    elif items[item][0] == "Escape":
                        print(bag_partition)
                        if enemy_stats["classifier"] == "Normal":
                            color.write("Player used a {}\n".format(item), "STRING")
                            escape_chance = random.randint(1,100)
                            if escape_chance < items[item][1]:
                                color.write("Player escaped the battle!\n", "STRING")
                            else:
                                color.write("The {} didn't work!\n".format(item), "COMMENT")
                            used_item = True
                        else:
                            color.write("You couldn't escape!\n", "COMMENT")
                            used_item = True
                            
                    elif items[item][0] == "Revive":
                        print(bag_partition)
                        print("This item is an auto-use item and will be used if the player reaches 0 HP\n")
                        used_item = False
                else:
                    print("You dont have any of this item.\n")
                    used_item = False
            # If you select 8 instead, you go to the info tab which lets you see what items do, it doesnt take up a turn. If you type 8, you go back to options
            elif item_usage == INFO_TAB_NO:
                info_print_no = 0
                desc_decision = 0
                print("===---------- INFO TAB ----------===")
                for info_counter in range(len(player_items)):
                    info_amount = player_items[info_counter + 1][1]
                    info_print_no += 1
                    print("{}. [{}]".format(info_print_no, player_items[info_counter + 1][0]))
                print("8. [BACK]")
                while desc_decision != INFO_TAB_BACK:
                    try:
                        desc_decision = int(input("Which item would you like to check? (1/2/3/4/5/6/7/8) "))
                        if desc_decision >= 1 and desc_decision <= 7:
                            item = player_items[desc_decision][0]
                            print("---------- {} ----------".format(item))
                            # Information includes; Item name, description of item, amount of the item left, type of item, power of item or chance of item working and the type of stat it affects
                            print("""Item : {}
Description : {}
Amount Left : {}
Type : {}
Power / Chance : {}
Thing it affects : {}""".format(item, items_desc[item], player_items[desc_decision][1], items[item][0], items[item][1], items[item][2]))
                            
                        elif desc_decision == INFO_TAB_BACK:
                            return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items
                            
                    except:
                        print("Please only input a number from 1 - 8")


            elif item_usage == BAG_TAB_BACK:
                return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items

            else:
                print("Please only input 1-9")
                used_item = False
        except:
            print("Please only input an integer and only 1-9")
            used_item = False
    # When the item is used, checks if any parties have been defeated or have escaped, if not, continues the battle, if yes, changes battle_ended to true and then checks who won
    if used_item == True:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
        change_number = player_items[item_usage][1]
        change_number -= 1
        player_items[item_usage] = player_items[item_usage][0], change_number
        if items[item][0] == "Escape" and escape_chance < items[item][1]:
            battle_ended = True
            
        if battle_ended == False:
            finished_battle = False
            enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp)
            turn_number += 1
            return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items
        
        elif battle_ended == True:
            print("\n=====---------- RESULT ----------=====\n")
            if player_hp_sp["hp"] <= 0:
                color.write("You have been defeated\n", "COMMENT")
            if enemy_hp_sp["hp"] <= 0:
                color.write("You have won the battle!\n", "STRING")
                print("Your brush has gained {} EXP and you obtained {} Gold!".format(enemy_exp, enemy_gold))
                gold += enemy_gold
                exp += enemy_exp
                if exp >= 20:
                    player_stats["level"] = player_stats["level"] + 1
                    print("You have grown to Level {}!".format(player_stats["level"]))
                    player_stats["hp"] += HP_LEVEL_INCREASE
                    player_stats["sp"] += SP_LEVEL_INCREASE
                    player_hp_sp["hp"] += HP_LEVEL_INCREASE
                    player_hp_sp["sp"] += SP_LEVEL_INCREASE
                    print("\nPlayer's Max HP increased by {} and Max SP by {}".format(HP_LEVEL_INCREASE, SP_LEVEL_INCREASE))
                    exp = 0
                    if player_stats["level"] == 8:
                        player_moves[4] = "Ultra Bash"
                        print("Your 'Brush Bash' has upgraded to '{}'".format(player_moves[4]))
                    if player_stats["level"] == 10:
                        player_moves[1] = "Super Slap"
                        print("Your 'Slap' has upgraded to '{}'".format(player_moves[1]))
                    if player_stats["level"] == 12:
                        player_moves[3] = "Paste Explosion"
                        print("Your 'Paste Blast' has upgraded to '{}'".format(player_moves[3]))
                    if player_stats["level"] == 14:
                        player_moves[2] = "Replenish"
                        print("Your 'Whiten' has upgraded to '{}'".format(player_moves[2]))
                    
            elif items[item][0] == "Escape" and escape_chance < 90:
                print("Your brush has gained 0 EXP and you obtained 0 Gold")
                
                
        finished_battle = True
        return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items

def run_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp, player_items, items):
    """This is the run command,this determines whether the user can run from a battle or not,
    it checks the run chance and then decides whether the user runs or stays in the battle."""
    run_partition = "\n===---------- RUNNING ----------===\n"
    run_chance = random.randint(1,100)
    print(run_partition)
    # checks run chance and rolls a random number to see if run is successful, if it doesnt work, uses up your turn, if it does then the user escapes the battle
    if run_chance <= 50:
        color.write("You Escaped the Battle!\n", "STRING")
        print("Your brush has gained 0 EXP and you obtained 0 Gold!")
        finished_battle = True
        return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items
        
    else:
        color.write("Couldn't Escape!\n", "COMMENT")
        finished_battle = False
        enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp)
        turn_number += 1
        return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items

def help_command(turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items, combat_help, item_help):
    """This is the help command, this command is the help bar for any users,
    it will display information for the users whenever you want,
    as it is very important,
    all you do is look through the help items and choose them to see different parts
    and get help on things that you might not know, this does not take up a turn"""
    helped = False
    combat_help_no = 1
    item_help_no = 2
    help_partition = "\n===---------- HELP PAGE ----------===\n"
    # Prints out the different sections of help
    while helped == False:
        print(help_partition)
        help_wait = 2
        print("""1. [Combat]
2. [Items]
3. [BACK]
""")
        # If 1 or 2 is input, goes to a helps ection, if 3 is input, goes back to options
        try:
            help_decision = int(input("What would you like help with? (1/2/3) "))
            if help_decision == combat_help_no:
                # Prints out the different help parts for the combat section numbered 1-9 and 10 is back
                for help_counter in range(len(combat_help)):
                    print("{}. [{}]".format(help_counter + 1, combat_help[help_counter + 1][0]))
                print("10. [BACK]")
                try:
                    combat_decision = int(input("What would you like to check? (1/2/3/4/5/6/7/8/9/10) "))
                    if combat_decision >= 1 and combat_decision <= 9:
                        print("=-----{}-----=\n{}".format(combat_help[combat_decision][0], combat_help[combat_decision][1]))
                        time.sleep(help_wait)
                    elif combat_decision == 10:
                        helped = False
                except:
                    print("Please only input an integer")
                    helped = False
                    
            elif help_decision == item_help_no:
                # Prints out the different help parts for the help section numbered 1-4 and 5 is back
                for help_counter in range(len(item_help)):
                    print("{}. [{}]".format(help_counter + 1, item_help[help_counter + 1][0]))
                print("5. [BACK]")
                try:
                    item_decision = int(input("What would you like to check? (1/2/3/4/5) "))
                    if item_decision >= 1 and item_decision <= 4:
                        print("=-----{}-----=\n{}".format(item_help[item_decision][0], item_help[item_decision][1]))
                        time.sleep(help_wait)
                    elif item_decision == 5:
                        helped = False
                except:
                    print("Please only input an integer")
                    helped = False
                    
            elif help_decision == 3:
                return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items
        except:
            print("Please only input an integer")
            helped = False
     
def tutorial(tutorial_over):
    """This is the tutorial function,
    this is a tutorial that you can look at throughout the game,
    this is important as some people starting the game may not
    know how to so this is a good place to start."""
    chosen = False
    tutorial_wait = 2
    while chosen == False:
        tutorial = None
        # Plays tutorial, it shows all information that is essential to playing this game, it also puts stops inbetween every string so that the user can read them, when it is over it returns back to main
        tutorial = input("Would you like to see the tutorial for this game? (Y/N) ").upper()
        if tutorial == "Y":
            try:
                tutorial_over = True
                chosen = True
                print("Press Ctrl + C to skip if you ever want to")
                time.sleep(tutorial_wait)
                print("Welcome to this game, there are many mechanics to get acquainted to...")
                time.sleep(tutorial_wait)
                print("\n===---------- MOVEMENT ----------===")
                time.sleep(tutorial_wait)
                print("""\n===----- EXAMPLE -----===
X O O O O
O O O O O
O O C O O
O O O O O
O O O O S
===----- EXAMPLE -----===\n""")
                time.sleep(tutorial_wait)
                print("You have 4 options on the map, all the 4 directions")
                time.sleep(tutorial_wait)
                print("You can also find chests and then go to the next floor")
                time.sleep(tutorial_wait)
                print("You are labelled X")
                time.sleep(tutorial_wait)
                print("Chests are labelled as C")
                time.sleep(tutorial_wait)
                print("and Stairs are labelled as S")
                time.sleep(tutorial_wait)
                print("Go down the stairs to reach the next floor")
                time.sleep(tutorial_wait)
                print("Who knows what awaits you down there...")
                time.sleep(tutorial_wait)
                print("\n===---------- COMBAT ----------===")
                time.sleep(tutorial_wait)
                print("""\n===----- EXAMPLE -----===
[F] for Fight
[B] for Bag
[R] for Run
[H] for Help
===----- EXAMPLE -----===\n""")
                time.sleep(tutorial_wait)
                print("In a battle, you have 4 Options; Fight, Bag, Run and Help")
                time.sleep(tutorial_wait)
                print("\n===---------- FIGHT ----------===")
                time.sleep(tutorial_wait)
                print("[Fight] lets you use a move that your trusty brush has learned")
                time.sleep(tutorial_wait)
                print("""\n===----- EXAMPLE -----===
1. [Slap] [Cost : 7HP] - [Effect : 15]
===----- EXAMPLE -----===\n""")
                time.sleep(tutorial_wait)
                print("This will display for all 4 moves that you have, you will also have the option to check all of them")
                time.sleep(tutorial_wait)
                print("Costs can be both HP and SP, SP acts like magic points in which you can cast Special moves or Healing with SP")
                time.sleep(tutorial_wait)
                print("And do Physical damage at the cost of HP")
                time.sleep(tutorial_wait)
                print("\n===---------- BAG ----------===")
                time.sleep(tutorial_wait)
                print("[Bag] lets you use an item that you have in your inventory")
                time.sleep(tutorial_wait)
                print("""\n===----- EXAMPLE -----===
1. [Mini Mouthwash][x1]
===----- EXAMPLE -----===\n""")
                time.sleep(tutorial_wait)
                print("This will display all items in the game, and how many you have of them")
                time.sleep(tutorial_wait)
                print("For example, a Mini Mouthwash will heal you for 10HP, and use up the item")
                time.sleep(tutorial_wait)
                print("You can also check the info for all items whenever")
                time.sleep(tutorial_wait)
                print("\n===---------- RUN ----------===")
                time.sleep(tutorial_wait)
                print("[Run] gives you a 50% chance to escape the battle")
                time.sleep(tutorial_wait)
                print("However, if it doesn't work, it uses up your turn.")
                time.sleep(tutorial_wait)
                print("\n===---------- HELP ----------===")
                time.sleep(tutorial_wait)
                print("[Help] lets you get any information about anything whenever you want")
                time.sleep(tutorial_wait)
                print("Thats all for the tutorial!\n")
                time.sleep(tutorial_wait)
            except KeyboardInterrupt:
                tutorial_wait = 0
                pass
            return tutorial_over
        # if tutorial is skipped, instantly returns back to main
        elif tutorial == "N":
            tutorial_over = True
            chosen = True
            return tutorial_over
        else:
            print("Please only input Y or N")
            chosen = False
            
def difficulty_setting():
    """This is the difficulty setting function,
    it asks the user what difficulty the user would like to change the game to,
    it changes the enemy HP and SP based on a multiplier that is defined in main,
    this is merely the input"""
    print("\n===---------- DIFFICULTY ----------===\n")
    chosen = False
    # Repeats the question until either Easy, Normal or Hard is chosen and then returns the choice back to main
    while chosen == False:
        print("What difficulty would you like?")
        difficulty = input("Easy, Normal or Hard (E, N, H)? ").title()
        if difficulty != "Easy" and difficulty != "Normal" and difficulty != "Hard" and difficulty != "H" and difficulty != "N" and difficulty != "E":
            print("Please only input one of the 3 options")
            chosen = False
        else:
            chosen = True
            return difficulty
        
def game_ending():
    """This plays at the end of the game when you defeat the final boss,
    it is merely an end to the game and is just some little story that ends the game off nicely."""
    ending_wait = 1.6
    print("\nYou defeated the Scourge and retrieved the Relic.")
    time.sleep(ending_wait)
    print("You made your way to the surface and called for the Golden Brush to save your town")
    time.sleep(ending_wait)
    print("All the townsfolk came out of their houses and looked around confused.")
    time.sleep(ending_wait)
    print("You explained to them your mission and then they all realised the problem")
    time.sleep(ending_wait)
    print("They had forgotten to maintain their teeth and had been cursed")
    time.sleep(ending_wait)
    print("Once they realised what had happened they all swore to care for their teeth properly")
    time.sleep(ending_wait)
    print("You were labelled as a hero and the Golden Brush was put on display in the town centre")
    time.sleep(ending_wait)
    print("This was a reminder to all the townsfolk to keep their teeth clean!")
    return

main()
