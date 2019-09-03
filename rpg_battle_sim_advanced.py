##
# rpg_battle_sim.py
# Date: 1/07/19
# Author: NZK
# RPG battle sim focused around dental hygiene.
import random
import time
# Main Function - Hub for battle
def main():
     # =====------------------ Stats and moves assigned to each character ------------------=====

    # This is the list of moves available in the game and their stats
    moves = {
        "Slap":("Rock", 15, "Phys", 7),
        "Whiten":("Normal", 30, "Heal", 10),
        "Paste Blast":("Paper", 35, "Spec", 5),
        "Floss Whip":("Scissors", 30, "Phys", 15),
        "Clean Punch":("Rock", 25, "Phys", 12),
        "Brush Bash":("Rock", 40, "Phys", 20),
        "Replenish":("Normal", 15, "Heal", 5),
        "Pacify":("Normal", "Sleep", "Status", 10),
        "Cavity Crush":("Rock", 15, "Phys", 8),
        "Decaying Beam":("Paper", 25, "Spec", 10),
        "Plaque":("Scissors", 10, "Spec", 4),
        "Bad Breath":("Paper", 30, "Phys", 20)}

    # This is the list of moves descriptions that is used in the INFO TAB
    moves_desc = {
        "Slap":"A simple Slap",
        "Whiten":"The user cleans their brush and heals them",
        "Paste Blast":"A powerful blast of Toothpaste",
        "Floss Whip":"The user grabs a piece of floss and whips the opponent",
        "Clean Punch":"The user punches the opponent with force",
        "Brush Bash":"The user throws themselves at the opponent with extreme speed",
        "Replenish":"The user drinks some water and heals a bit of health",
        "Pacify":"The user quells the enemys fighting spirit for a turn",
        "Cavity Crush":"The user attacks the enemy with a disgusting attack",
        "Decaying Beam":"The user attacks the enemy with dirty water in hopes of decaying them",
        "Plaque":"The user dirties the other, inflicting damage",
        "Bad Breath":"The user throws their rancid breath at the enemy"}

    # This is the list of items available for finding in the game and their uses
    items = {
        "Mini Mouthwash":("Heal", 10, "HP"),
        "Med. Mouthwash":("Heal", 30, "HP"),
        "Massive Mouthwash":("Heal", 50, "HP"),
        "Ethereal Floss":("Heal", 10, "SP"),
        "Spectral Floss":("Heal", 25, "SP"),
        "Drain Plug":("Escape", 90, "Escape"),
        "Revive":("Revive", 50, "HP")}

    # This is the list of the items descriptions that is used in the INFO TAB
    items_desc = {
        "Mini Mouthwash":"Heals the user for 10 HP",
        "Med. Mouthwash":"Heals the user for 30 HP",
        "Massive Mouthwash":"Heals the user for 50 HP",
        "Ethereal Floss":"Revitalises the user and restores 10 SP",
        "Spectral Floss":"Revitalises the user and restores 25 SP",
        "Drain Plug":"Grants a 90% chance for the user to escape the battle",
        "Revive":"Revives the player if they ever get down to 0 HP"}

    # ===----- PLAYER STATS -----===
    # These are used for finding different stats and checking moves and health, this area helps the game run properly, these are called in the [F]ight, [B]ag, [R]un and Enemy Fight Functions
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61, "status":"none"}
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Brush Bash"}
    player_items = {1:("Mini Mouthwash", 1), 2:("Med. Mouthwash", 1), 3:("Massive Mouthwash", 1), 4:("Ethereal Floss", 1), 5:("Spectral Floss", 1), 6:("Drain Plug", 1), 7:("Revive", 1)}
    # ===----- PLAYER STATS -----===


    # ===----- ENEMY STATS -----===
    # These are used in the same sense as the player stats but are used for the enemy instead, these are called in the Enemy Fight and [F] Functions
    enemy_stats = {"level":5, "type":"scissors", "hp":50, "sp":50, "atk":48, "def":64, "spd":31, "status":"none", "classifier":"Normal"}
    enemy_moves = {1:"Cavity Crush", 2:"Decaying Beam", 3:"Plaque", 4:"Bad Breath"}
    # ===----- ENEMY STATS -----===


    # ===----- OTHER STATS -----===
    # The other stats area includes EXP and Gold, it also includes the EXP and Gold an enemy will drop when defeated
    enemy_exp = 10
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
    player_hp_sp = {"hp":player_stats["hp"], "sp":player_stats["sp"]}
    enemy_hp_sp = {"hp":enemy_stats["hp"], "sp":enemy_stats["sp"]} 
    print("""Welcome to: The Quest for the GOLDEN BRUSH!""")
    # Checks what difficulty the user sets the game to, uses the multiplier to set difficulty
    while difficulty_set == False:
        difficulty = difficulty_setting()
        if difficulty == "Easy":
            print("Difficulty set to: {}".format(difficulty))
            difficulty_set = True
            
        elif difficulty == "Normal":
            enemy_hp_sp["hp"] = enemy_hp_sp["hp"] * NORMAL_MULTIPLIER
            enemy_hp_sp["sp"] = enemy_hp_sp["sp"] * NORMAL_MULTIPLIER
            print("Difficulty set to: {}".format(difficulty))
            difficulty_set = True
            
        elif difficulty == "Hard":
            enemy_hp_sp["hp"] = enemy_hp_sp["hp"] * HARD_MULTIPLIER
            enemy_hp_sp["sp"] = enemy_hp_sp["sp"] * HARD_MULTIPLIER
            print("Difficulty set to: {}".format(difficulty))
            difficulty_set = True
    print("\n===---------- STORY ----------===\n")
    print("""Your journey follows a boy who has awoken to his entire village that has
been overrun by a strange curse from not brushing their teeth, however your character finds himself immune. It is up to you
to find a cure. You recall hearing of a powerful relic hidden deep in the villages mines.
You decide to venture down into the mines to save your town, on the quest for the Golden Brush""")
    print("You make your way to the front of the mine and are greeted by an enemy, it lunges at you!")
    # Checks if the user skips the tutorial, if not then it plays the tutorial
    while tutorial_over == False:
        tutorial_over = tutorial(tutorial_over)
    
    battle_start(moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp)
    print("Whew, that was close!")


def battle_start(moves, moves_desc, items, items_desc, player_stats, enemy_stats, player_moves, enemy_moves, player_items, combat_help, item_help, player_hp_sp, enemy_hp_sp, gold, enemy_gold, exp, enemy_exp):
    finished_battle = False
    turn_number = 1
    stats_bar = "--------------------\ Stats \--------------------"
    stats_bar_2 = "--------------------/ Stats /--------------------"
    max_hp = player_stats["hp"]
    max_sp = player_stats["sp"]
    print("Player encountered an infected brush!")
    # Checks if the battle is over, if not then plays the next turn
    while finished_battle == False:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
                
        if battle_ended == False:
            finished_battle = False
            print("\n===---------- TURN {} ----------===\n".format(turn_number))
            # Stats Bar which shows the user the HP and SP of both your player and the enemy
            print(stats_bar)
            print("Player: LEVEL: {}, HP: {}, SP:{}".format(player_stats["level"], player_hp_sp["hp"], player_hp_sp["sp"]))
            print("Enemy: LEVEL: {}, HP: {}, SP:{}".format(enemy_stats["level"], enemy_hp_sp["hp"], enemy_hp_sp["sp"]))
            print(stats_bar_2)
            print("""What will you do?
[F] for Fight
[B] for Bag
[R] for Run
[H] for Help""")
            # Input for decisions on what to do, these include Fight, Bag, Run and Help
            option = input("Please choose your option: ").upper()
            print("")
            if option == "F":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp = fight_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp, enemy_gold, enemy_exp, gold, exp, max_hp, max_sp, items, player_items)
            elif option == "B":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items = bag_command(turn_number, finished_battle, player_stats, enemy_stats, player_hp_sp, enemy_hp_sp, player_moves, enemy_moves, moves, items, items_desc, player_items, gold, enemy_gold, exp, enemy_exp)
            elif option == "R":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items = run_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp, player_items, items)
            elif option == "H":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items = help_command(turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items, combat_help, item_help)
            else:
                print("Please only input one of the 4 options")
       # Checks if the battle is over by checking the health of both parties or if the escape item used was successful
        elif battle_ended == True:
            if player_items[7][1] == 0:
                if player_hp_sp["hp"] <= 0:
                    print("You have been defeated")
                if enemy_hp_sp["hp"] <= 0:
                    # If enemy is defeated, this will appear and player will be awarded EXP and Gold
                    print("You have won the battle!")
                    print("Your brush has gained {} EXP and you obtained {} Gold!".format(enemy_exp, enemy_gold))
                    gold += enemy_gold
                    exp += enemy_exp
                    if exp >= 20:
                        # If players EXP goes above 20, they level up
                        player_stats["level"] = 6
                        print("You have grown to Level {}!".format(player_stats["level"]))
                finished_battle = True
                return finished_battle, player_hp_sp, enemy_hp_sp
            # If the player reaches 0 HP, this will check if the user has a revive, which will restore 50HP and use the item
            elif player_items[7][1] > 0:
                revive_usage = player_items[7][0]
                print("\nPlayer used a {}".format(player_items[7][0]))
                player_hp_sp["hp"] = items[revive_usage][1]
                print("Player recovered {} HP".format(items[revive_usage][1]))
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
    INFO_TAB_BACK = 5
    FIGHT_TAB_INFO = 5
    FIGHT_TAB_BACK = 6
    NO_HEALTH = 0
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
                            print("Player used {}".format(move))
                            enemy_hp_sp["hp"] -= moves[move][1]
                            print("The enemy Brush lost {} HP\n".format(moves[move][1]))
                            player_hp_sp["hp"] -= moves[move][3]
                        else:
                            print("You don't have enough HP to perform this action")
                            taken_turn = False
                    # if the move chosen is a special attack, costs SP, does damage to enemy, if they do not have sufficient SP for the move chosen, resets back to the input
                    if moves[move][2] == "Spec":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            print("Player used {}".format(move))
                            enemy_hp_sp["hp"] -= moves[move][1]
                            print("The enemy Brush lost {} HP\n".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                    # if the move chosen is heal, acts the same as if the move is special, however heals the user rather than damaging the opponent
                    if moves[move][2] == "Heal":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            print("Player used {}".format(move))
                            player_hp_sp["hp"] += moves[move][1]
                            print("You regained {} HP!\n".format(moves[move][1]))
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
                            print("Player used {}".format(move))
                            enemy_hp_sp["status"] == moves[move][1]
                            print("The enemy Brush was inflicted with {}\n".format(moves[move][1]))
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
                    if player_hp_sp["hp"] <= NO_HEALTH:
                        if player_items[7][1] == 0:
                            print("You have been defeated")
                        elif player_items[7][1] > 0:
                            revive_usage = player_items[7][0]
                            print("Player used a {}".format(player_items[7][0]))
                            player_hp_sp == items["Revive"][1]
                            print("Player recovered {} HP".format(revive_usage))
                            # This changes the number of items the user carries to - 1 of the previous amount
                            change_number = player_items[7][1]
                            change_number -= 1
                            player_items[7] = player_items[7][0], change_number
                    # If the enemy was the one that had their health depleted, displays this and awards gold and EXP
                    if enemy_hp_sp["hp"] <= 0:
                        print("You have won the battle!")
                        print("Your brush has gained {} EXP and you obtained {} Gold!".format(enemy_exp, enemy_gold))
                        gold += enemy_gold
                        exp += enemy_exp
                        # If exp goes above 20, the player levels up to a level higher than what was previously their level
                        if exp >= 20:
                            player_stats["level"] = 6
                            print("You have grown to Level {}!".format(player_stats["level"]))
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
    enemy_partition = "===---------- ENEMY MOVE ----------===\n"
    max_enemy_hp = enemy_stats["hp"]
    enemy_moved = False
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
                        print("Enemy used {}".format(move))
                        player_hp_sp["hp"] -= moves[move][1]
                        print("You lost {} HP".format(moves[move][1]))
                        enemy_hp_sp["hp"] -= moves[move][3]
                        time.sleep(0.7)
                    else:
                        enemy_move = random.randint(1, 4)
                        enemy_moved = False
                if moves[move][2] == "Spec":
                    if enemy_hp_sp["sp"] >= moves[move][3]:
                        enemy_moved = True
                        print("Enemy used {}".format(move))
                        player_hp_sp["hp"] -= moves[move][1]
                        print("You lost {} HP".format(moves[move][1]))
                        enemy_hp_sp["sp"] -= moves[move][3]
                        time.sleep(0.7)
                    else:
                        enemy_move = random.randint(1, 4)
                        enemy_moved = False
                        
                if moves[move][2] == "Heal":
                    if enemy_hp_sp["sp"] >= moves[move][3]:
                        enemy_moved = True
                        print("Enemy used {}".format(move))
                        enemy_hp_sp["hp"] += moves[move][1]
                        print("The enemy Brush regained {} HP!".format(moves[move][1]))
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
                            print("Player used a {}".format(item))
                            player_hp_sp["hp"] += items[item][1]
                            print("Player regained {} HP\n".format(items[item][1]))
                            if player_hp_sp["hp"] > max_hp:
                                player_hp_sp["hp"] = max_hp
                            used_item = True
                            
                        elif items[item][2] == "SP":
                            print(bag_partition)
                            print("Player used a {}".format(item))
                            player_hp_sp["sp"] += items[item][1]
                            print("Player regained {} SP\n".format(items[item][1]))
                            if player_hp_sp["sp"] > max_sp:
                                player_hp_sp["sp"] = max_sp
                            used_item = True
                            
                    elif items[item][0] == "Escape":
                        print(bag_partition)
                        if enemy_stats["classifier"] == "Normal":
                            print("Player used a {}".format(item))
                            escape_chance = random.randint(1,100)
                            if escape_chance < items[item][1]:
                                print("Player escaped the battle!\n")
                            else:
                                print("The {} didn't work!\n".format(item))
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
            if player_hp_sp["hp"] <= 0:
                print("You have been defeated")
            if enemy_hp_sp["hp"] <= 0:
                print("You have won the battle!")
                print("Your brush has gained {} EXP and you obtained {} Gold!".format(enemy_exp, enemy_gold))
                gold += enemy_gold
                exp += enemy_exp
                if exp >= 20:
                    player_stats["level"] = 6
                    print("You have grown to Level {}!".format(player_stats["level"]))
                    
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
        print("You Escaped the Battle!")
        print("Your brush has gained 0 EXP and you obtained 0 Gold!")
        finished_battle = True
        return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items
        
    else:
        print("Couldn't Escape!\n")
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
        # Plays tutorial, it shows all information that is essential to playing this game, it also puts stops inbetween every string so that the user can read them, when it is over it returns back to main
        tutorial = input("Would you like to see the tutorial for this game? (Y/N) ").upper()
        if tutorial == "Y":
            print("Welcome to this game, there are many mechanics to get acquainted to...")
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
            tutorial_over = True
            chosen = True
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
        difficulty = input("Easy, Normal or Hard? ").title()
        if difficulty != "Easy" and difficulty != "Normal" and difficulty != "Hard":
            print("Please only input one of the 3 options")
            chosen = False
        else:
            chosen = True
            return difficulty 
    
main()
