##
# rpg_battle_sim.py
# Date: 1/07/19
# Author: NZK
# RPG battle sim focused around dental hygiene.
import random
import time
# Main Function - Hub for battle
def main():
    # =====------------------Stats and moves assigned to each character------------------=====
    
    moves = {
        "Slap":("Rock", 15, "Phys", 6),
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

    moves_desc = {"Slap":"A simple Slap",
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

    items = {"Mini Mouthwash":("Heal", 10, "HP"),
             "Med. Mouthwash":("Heal", 30, "HP"),
             "Massive Mouthwash":("Heal", 50, "HP"),
             "Ethereal Floss":("Heal", 10, "SP"),
             "Spectral Floss":("Heal", 25, "SP"),
             "Drain Plug":("Escape", 90),
             "Revive":("Revive", 50, "HP")}

    items_desc = {"Mini Mouthwash":"Heals the user for 10 HP",
                  "Med. Mouthwash":"Heals the user for 30 HP",
                  "Massive Mouthwash":"Heals the user for 50 HP",
                  "Ethereal Floss":"Revitalises the user and restores 10 SP",
                  "Spectral Floss":"Revitalises the user and restores 25 SP",
                  "Drain Plug":"Grants a 90% chance for the user to escape the battle",
                  "Revive":"Revives the player if they ever get down to 0 HP"}
    
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61, "status":"none"}
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Replenish"}
    player_items = {1:("Mini Mouthwash", 2), 2:("Med. Mouthwash", 0), 3:("Masssive Mouthwash", 1), 4:("Ethereal Floss", 1), 5:("Spectral Floss", 0), 6:("Drain Plug", 1), 7:("Revive", 1)}
 
    enemy_stats = {"level":5, "type":"scissors", "hp":100, "sp":50, "atk":48, "def":64, "spd":31, "status":"none"}
    enemy_moves = {1:"Cavity Crush", 2:"Decaying Beam", 3:"Plaque", 4:"Bad Breath"}

    enemy_exp = 10
    enemy_gold = 50

    gold = 0
    exp = 0
    
    # =====------------------Stats and moves assigned to each character------------------=====
    finished_battle = False
    turn_number = 1
    max_hp = player_stats["hp"]
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
            # Fight menu which shows the user the options
            print(stats_bar)
            print("Player: LEVEL: {}, HP: {}, SP:{}".format(player_stats["level"], player_hp_sp["hp"], player_hp_sp["sp"]))
            print("Enemy: LEVEL: {}, HP: {}, SP:{}".format(enemy_stats["level"], enemy_hp_sp["hp"], enemy_hp_sp["sp"]))
            print(stats_bar_2)
            print("""What will you do?
[F] for Fight
[B] for Bag
[R] for Run""")
            # Input for decisions on what to do
            option = input("Please choose your option: ").upper()
            if option == "F":
                turn_number, finished_battle, player_hp_sp, enemy_hp_sp = fight_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp, enemy_gold, enemy_exp, gold, exp)
            elif option == "B":
                bag_command(finished_battle, player_stats, enemy_stats, player_hp_sp, enemy_hp_sp, moves, items, items_desc, player_items)
            elif option == "R":
                run_command()
            else:
                print("Please only input one of the 4 options")
   
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
            finished_battle = True
            return finished_battle, player_hp_sp, enemy_hp_sp

def fight_command(turn_number, finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp, enemy_gold, enemy_exp, gold, exp):
    player_partition = "===---------- PLAYER MOVE ----------===\n"
    taken_turn = False
    max_player_hp = player_stats["hp"]
    for move_counter in range(len(player_moves)):
        print_move = player_moves[move_counter + 1]
        if moves[print_move][2] == "Phys":
            type_move = "HP"
        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
            type_move = "SP"
        print("{}. [{}][{}{}]".format(move_counter + 1, player_moves[move_counter + 1], moves[print_move][3], type_move))
    # Input for the move to be used
    while taken_turn == False:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
        if battle_ended == False:
            try:
                move_decision = int(input("Which move would you like to use? (5 for Info & 6 for Back)(1/2/3/4/5/6) "))
                if move_decision >= 1 and move_decision <= 4:
                    time.sleep(0.7)
                    move = player_moves[move_decision]
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
                            
                    if moves[move][2] == "Heal":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print(player_partition)
                            print("Player used {}".format(move))
                            player_hp_sp["hp"] += moves[move][1]
                            print("You regained {} HP!\n".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                            if player_hp_sp["hp"] > max_player_hp:
                                player_hp_sp["hp"] = max_player_hp
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False

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
                            
                            
                elif move_decision == 5:
                    desc_decision = 0
                    print("---------- INFO TAB ----------")
                    for move_counter in range(len(player_moves)):
                        print_move = player_moves[move_counter + 1]
                        if moves[print_move][2] == "Phys":
                            type_move = "HP"
                        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
                            type_move = "SP"
                        print("{}. [{}][{}{}]".format(move_counter + 1, player_moves[move_counter + 1], moves[print_move][3], type_move))
                    while desc_decision != 5:
                        try:
                            desc_decision = int(input("Which move would you like to check? (5 for Back)(1/2/3/4/5) "))
                            if desc_decision >= 1 and desc_decision <= 4:
                                move = player_moves[desc_decision]
                                if moves[move][2] == "Phys":
                                    type_move = "HP"
                                if moves[move][2] == "Spec" or moves[move][2] == "Heal":
                                    type_move = "SP"
                                print("---------- {} ---------".format(move))
                                print("""Move: {}
Description : {}
Power : {}
Type : {}
Cost : {}{}""".format(move, moves_desc[move], moves[move][1], moves[move][2], moves[move][3], type_move))
                            elif desc_decision == 5:
                                return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                                
                        except:
                            print("Please only input a number from 1 - 5")

                elif move_decision == 6:
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                
                else:
                    print("Please only input a number from 1 - 6")
                    taken_turn = False

            except:
                print("Please only input a number from 1 - 6")
                taken_turn = False

            if taken_turn == True:
                battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
                
                if battle_ended == False:
                    finished_battle = False
                    enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp)
                    turn_number += 1
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                
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
                    finished_battle = True
                    return turn_number, finished_battle, player_hp_sp, enemy_hp_sp
                
            
def battle_over(player_hp_sp, enemy_hp_sp):
    battle_ended = False
    if player_hp_sp["hp"] <= 0 or enemy_hp_sp["hp"] <= 0:
        battle_ended = True  
    else:
        battle_ended = False
    return battle_ended
             
def enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp):
    enemy_partition = "===---------- ENEMY MOVE ----------===\n"
    max_enemy_hp = enemy_stats["hp"]
    enemy_moved = False
    time.sleep(0.7)
    print(enemy_partition)
    while enemy_moved == False:
        if enemy_stats["status"] != "Sleep":
            enemy_move = random.randint(1, 4)
            move = enemy_moves[enemy_move]
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

def bag_command(finished_battle, player_stats, enemy_stats, player_hp_sp, enemy_hp_sp, moves, items, items_desc, player_items):
    bag_partition = "===---------- BAG ----------==="
    used_item = False
    print_no = 0
    for item_counter in range(len(player_items)):
        item_amount = player_items[item_counter + 1][1]
        if item_amount >= 1:
            print_no += 1
            print("{}. [{}][x{}]".format(print_no, player_items[item_counter + 1][0], player_items[item_counter + 1][1]))
            
    while used_item == False:
        battle_ended = battle_over(player_hp_sp, enemy_hp_sp)
        if battle_ended == False:
            try:
                item_usage = int(input("What item would you like to use? 1/2/3/4/5/6 (5 for Info & 6 for Back) "))
                if item_usage >= 1 and item_usage <= 4:
                    time.sleep(0.7)
                    item = player_items[item_usage]
                    if items[item][0] == "Heal":
                        if items[item][2] == "HP":
                            print("Player used a {}".format(item))
                            player_hp_sp["hp"] += items[item][1]
                            print("Player regained {} HP".format(items[item][1]))
                            if player_hp_sp["hp"] > max_
                            
                            

                        elif items[item][2] == "SP":

                            

                    elif items[item][0] == "Escape":


                    elif items[item][0] == "Revive":
                        print("This item is an auto-use item and will be used if the player reaches 0 HP")
                        used_item = False
        
            
        
    
    
        

main()
