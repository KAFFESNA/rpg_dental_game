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
    # These are used for finding different stats and checking moves and health, this area helps the game run properly
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61, "status":"none"}
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Brush Bash"}
    player_items = {1:("Mini Mouthwash", 1), 2:("Med. Mouthwash", 1), 3:("Massive Mouthwash", 2), 4:("Ethereal Floss", 1), 5:("Spectral Floss", 2), 6:("Drain Plug", 0), 7:("Revive", 1)}
    # ===----- PLAYER STATS -----===


    # ===----- ENEMY STATS -----===
    # These are used in the same sense as the player stats but are used for the enemy instead
    enemy_stats = {"level":5, "type":"scissors", "hp":100, "sp":50, "atk":48, "def":64, "spd":31, "status":"none", "classifier":"Normal"}
    enemy_moves = {1:"Cavity Crush", 2:"Decaying Beam", 3:"Plaque", 4:"Bad Breath"}
    # ===----- ENEMY STATS -----===


    # ===----- OTHER STATS -----===
    # The other stats area includes EXP and Gold, it also includes the EXP and Gold an enemy will drop when defeated
    enemy_exp = 10
    enemy_gold = 50

    gold = 0
    exp = 0

    max_hp = player_stats["hp"]
    max_sp = player_stats["sp"]
    # ===----- OTHER STATS -----===
    
    # =====------------------ Stats and moves assigned to each character ------------------=====
    finished_battle = False
    turn_number = 1
    stats_bar = "--------------------\ Stats \--------------------"
    stats_bar_2 = "--------------------/ Stats /--------------------"
    player_hp_sp = {"hp":player_stats["hp"], "sp":player_stats["sp"]}
    enemy_hp_sp = {"hp":enemy_stats["hp"], "sp":enemy_stats["sp"]}
    print("Player encountered an infected brush!")
    # Checks if the battle is over
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
                help_command()
            else:
                print("Please only input one of the 4 options")
       # Checks if the battle is over by checking the health of both parties or if the escape item used was successful
        elif battle_ended == True:
            if player_items[7][1] == 0:
                if player_hp_sp["hp"] <= 0:
                    # If player is defeated, this will appear 
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
                # This changes the number of this item held to - 1 of what the user originally had
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
        # Checks if the move is Physical or Special to allocate cost type
        if moves[print_move][2] == "Phys":
            type_move = "HP"
        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
            type_move = "SP"
        print("{}. [{}] [Cost : {}{}] - [Effect : {}]".format(move_counter + 1, player_moves[move_counter + 1], moves[print_move][3], type_move, moves[print_move][1]))
    # Checks if the battle has ended, if not, lets the user take their turn, otherwise checks who has lost their HP or if the user used an escape item
    while taken_turn == False:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
        if battle_ended == False:
            try:
                # Input for a move to be used, 1-4 for moves and 5 for info, 6 to go back to the Options menu
                move_decision = int(input("Which move would you like to use? (5 for Info & 6 for Back)(1/2/3/4/5/6) "))
                # Checks what move was selected, if 1-4, checks moves and if 5, opens the info tab
                if move_decision >= 1 and move_decision <= 4:
                    time.sleep(0.7)
                    move = player_moves[move_decision]
                    # Checks what type of move was used, this is to check what cost type to remove from
                    if moves[move][2] == "Phys":
                        # If the move selected was a Physical attack, takes cost from HP
                        # Checks if the user has enough SP to perform the attack, if not, they will be told to choose another attack
                        if player_hp_sp["hp"] > moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            # Takes HP away from the user, dictated by Cost, and takes HP away from the enemy, dictated by damage
                            print("Player used {}".format(move))
                            enemy_hp_sp["hp"] -= moves[move][1]
                            print("The enemy Brush lost {} HP\n".format(moves[move][1]))
                            player_hp_sp["hp"] -= moves[move][3]
                        else:
                            print("You don't have enough HP to perform this action")
                            taken_turn = False
                        # If the move selected was a Special attack, takes cost from SP
                    if moves[move][2] == "Spec":
                        # Checks if the user has enough SP to perform the attack, if not, they will be told to choose another attack
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            # Takes SP away from the user, dictated by Cost, and takes HP away from the enemy, dictated by damage
                            print("Player used {}".format(move))
                            enemy_hp_sp["hp"] -= moves[move][1]
                            print("The enemy Brush lost {} HP\n".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                        # If the move selected was a Healing attack, takes cost from SP
                    if moves[move][2] == "Heal":
                        # Checks if the user has enough SP to perform the attack, if not, they will be told to choose another attack
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            # Takes SP away from the user, dictated by Cost, and gives HP back to the player, dictated by effect
                            print("Player used {}".format(move))
                            player_hp_sp["hp"] += moves[move][1]
                            print("You regained {} HP!\n".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                            if player_hp_sp["hp"] > max_hp:
                                player_hp_sp["hp"] = max_hp
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                        # If the move selected was a Status attack, takes cost from SP
                    if moves[move][2] == "Status":
                        # Checks if the user has enough SP to perform the attack, if not, they will be told to choose another attack
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            # Takes SP away from the user, dictated by Cost, and gives the enemy a status, dictated by effect
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
                    print("---------- INFO TAB ----------")
                    
                    # Prints out the moves in order to display input options
                    for move_counter in range(len(player_moves)):
                        print_move = player_moves[move_counter + 1]
                        if moves[print_move][2] == "Phys":
                            type_move = "HP"
                        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
                            type_move = "SP"
                        print("{}. [{}][{}{}]".format(move_counter + 1, player_moves[move_counter + 1], moves[print_move][3], type_move))
                    while desc_decision != 5:
                        try:
                            # Input for the Info Section, if 5 is input the user is taken back to the options menu
                            desc_decision = int(input("Which move would you like to check? (5 for Back)(1/2/3/4/5) "))
                            
                            # If the input was between 1-4, checks what move was checked and then displays information regarding the move checked
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
                                
                            # If the number input is 5, takes the user back to the Options menu
                            elif desc_decision == INFO_TAB_BACK:
                                return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                            
                        # If 1-5 is not input or is not an integer, displays an error and repeats the question for the Info Tab
                        except:
                            print("Please only input a number from 1 - 5")
 
                # If 6 is chosen in the Fight tab, takes the user back to the Options Menu
                elif move_decision == FIGHT_TAB_BACK:
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                
                # If 1-6 is not input on the Fight Tab, displays an error and repeats the question
                else:
                    print("Please only input a number from 1 - 6")
                    taken_turn = False
                    
            # If 1-6 is not input or is not an integer, displays an error and repeats the question for the Fight Tab
            except:
                print("Please only input a number from 1 - 6")
                taken_turn = False
                
            # Checks if the user has taken their turn, if true, runs battle ended code and checks if any parties have been defeated
            if taken_turn == True:
                battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
                
                # If the battle hasn't ended, plays the enemys turn and then starts the next turn at the Options Menu and carries over all stats.
                if battle_ended == False:
                    finished_battle = False
                    enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp)
                    turn_number += 1
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                # If the battle has ended, checks who had lost their health, or if the user used an item to make them leave, also checks if the user has a revive on them in case the player lost their HP
                elif battle_ended == True:
                    # If the player does not have a revive and was the one who lost all their health, they are defeated
                    if player_hp_sp["hp"] <= NO_HEALTH:
                        if player_items[7][1] == 0:
                            print("You have been defeated")
                        # If the player does have a revive, the player is revived and the battle continues
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
    # Loops the code until a suitable move is found, it randomises until they use a move
    while enemy_moved == False:
        # If the enemy has health under 8 or sp under 4, it skips their turn as they have no moves that they can use and it avoids softlocking the user. 
        if enemy_hp_sp["hp"] >= 8 or enemy_hp_sp["sp"] >= 4:
            # Checks if the enemies status is "sleep" and if they are asleep, skips their turn and then after, changes it back to none, if not, lets them attack
            if enemy_stats["status"] != "Sleep":
                enemy_move = random.randint(1, 4)
                move = enemy_moves[enemy_move]
                # Checks if the move chosen in Physical, Spec, Heal or Status to choose cost type and then decide appropriate effects based on the move
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
    bag_partition = "\n===---------- ITEM USAGE ----------===\n"
    used_item = False
    print_no = 0
    max_hp = player_stats["hp"]
    max_sp = player_stats["sp"]
    for item_counter in range(len(player_items)):
        item_amount = player_items[item_counter + 1][1]
        print_no += 1
        print("{}. [{}][x{}]".format(print_no, player_items[item_counter + 1][0], player_items[item_counter + 1][1]))
            
    while used_item == False:
        try:
            item_usage = int(input("What item would you like to use? 1/2/3/4/5/6/7/8/9/ (8 for Info & 9 for Back) "))
            if item_usage >= 1 and item_usage <= 7:
                time.sleep(0.7)
                item = player_items[item_usage][0]
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

            elif item_usage == 8:
                info_print_no = 0
                desc_decision = 0
                print("---------- INFO TAB ----------")
                for info_counter in range(len(player_items)):
                    info_amount = player_items[info_counter + 1][1]
                    info_print_no += 1
                    print("{}. [{}]".format(info_print_no, player_items[info_counter + 1][0]))
                while desc_decision != 8:
                    try:
                        desc_decision = int(input("Which item would you like to check? (8 for Back)(1/2/3/4/5/6/7/8) "))
                        if desc_decision >= 1 and desc_decision <= 7:
                            item = player_items[desc_decision][0]
                            print("---------- {} ----------".format(item))
                            print("""Item : {}
Description : {}
Amount Left : {}
Type : {}
Power / Chance : {}
Thing it affects : {}""".format(item, items_desc[item], player_items[desc_decision][1], items[item][0], items[item][1], items[item][2]))
                            
                        elif desc_decision == 8:
                            return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items
                            
                    except:
                        print("Please only input a number from 1 - 8")


            elif item_usage == 9:
                return turn_number, finished_battle, player_hp_sp, enemy_hp_sp, player_items

            else:
                print("Please only input 1-5")
                used_item = False
        except:
            print("Please only input an integer and only 1-5")
            used_item = False
    
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
    run_partition = "\n===---------- RUNNING ----------===\n"
    run_chance = random.randint(1,100)
    print(run_partition)
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

# def help_command(): (continue later)
    
    
main()
