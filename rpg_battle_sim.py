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
    
    characters = {1:"Char 1", 2:"Char 2", 3:"Char 3"}
    moves = {
        "Slap":("Rock", 20, "Phys", 6),
        "Whiten":("Normal", 50, "Heal", 10),
        "Paste Blast":("Paper", 25, "Spec", 5),
        "Floss Whip":("Scissors", 30, "Phys", 12),
        "Clean Punch":("Rock", 30, "Phys", 10),
        "Brush Bash":("Rock", 40, "Phys", 16),
        "Replenish":("Normal", 20, "Heal", 5),
        "Pacify":("Normal", "Sleep", "Status", 10)}

    moves_desc = {"Slap":"A simple Slap",
                  "Whiten":"The user cleans their brush and heals them",
                  "Paste Blast":"A powerful blast of Toothpaste",
                  "Floss Whip":"The user grabs a piece of floss and whips the opponent",
                  "Clean Punch":"The user punches the opponent with force"}
    
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61, "status":"none"}
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Floss Whip"}
    
    char_2_stats = {"level":5 , "type":"paper", "hp":100, "sp":50, "atk":48, "def":50, "spd":50, "status":"none"}
    char_2_moves = {1:"Slap", 2:"Brush Bash", 3:"Pacify", 4:"Replenish"}
    
    char_3_stats = {"level":5 , "type":"scissors", "hp":100, "sp":50, "atk":38, "def":60, "spd":40, "status":"none"}
    char_3_moves = {1:"Floss Whip", 2:"Clean Punch", 3:"Brush Bash", 4:"Replenish"}
 
    enemy_stats = {"level":5, "type":"scissors", "hp":100, "sp":50, "atk":48, "def":64, "spd":31, "status":"none"}
    enemy_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Floss Whip"}
    
    # =====------------------Stats and moves assigned to each character------------------=====
    finished_battle = False
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
             # Fight menu which shows the user the options
            print("""What will you do?
        [F] for Fight
        [C] for Characters
        [B] for Bag
        [R] for Run""")
            # Input for decisions on what to do
            print(stats_bar)
            print("Player: LEVEL: {}, HP: {}, SP:{}".format(player_stats["level"], player_hp_sp["hp"], player_hp_sp["sp"]))
            print("Enemy: LEVEL: {}, HP: {}, SP:{}".format(enemy_stats["level"], enemy_hp_sp["hp"], enemy_hp_sp["sp"]))
            print(stats_bar_2)
            option = input("Please choose your option: ").upper()
            time.sleep(0.7)
            if option == "F":
                finished_battle, player_hp_sp, enemy_hp_sp = fight_command(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp)
            elif option == "C":
                finished_battle = characters_command(finished_battle, characters, player_stats, char_2_stats, char_3_stats, player_moves, moves)
            elif option == "B":
                bag_command()
            elif option == "R":
                run_command()
            else:
                print("Please only input one of the 4 options")
   
        elif battle_ended == True:
            if player_hp_sp["hp"] <= 0:
                print("You have been defeated")
            if enemy_hp_sp["hp"] <= 0:
                print("You have won the battle!")
            finished_battle = True
            return finished_battle, player_hp_sp, enemy_hp_sp

def fight_command(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc, player_hp_sp, enemy_hp_sp):
    taken_turn = False
    max_player_hp = player_stats["hp"]
    for i in range(len(player_moves)):
        print_move = player_moves[i+1]
        if moves[print_move][2] == "Phys":
            type_move = "HP"
        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
            type_move = "SP"
        print("{}. [{}][{}{}]".format(i + 1, player_moves[i+1], moves[print_move][3], type_move))
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
                            print("\n===---------- PLAYER MOVE ----------===")
                            print("Player used {}".format(move))
                            enemy_hp_sp["hp"] -= moves[move][1]
                            print("The enemy Brush lost {} HP".format(moves[move][1]))
                            player_hp_sp["hp"] -= moves[move][3]
                        else:
                            print("You don't have enough HP to perform this action")
                            taken_turn = False
                            
                    if moves[move][2] == "Spec":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print("\n===---------- PLAYER MOVE ----------===")
                            print("Player used {}".format(move))
                            enemy_hp_sp["hp"] -= moves[move][1]
                            print("The enemy Brush lost {} HP".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                            
                    if moves[move][2] == "Heal":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print("\n===---------- PLAYER MOVE ----------===")
                            print("Player used {}".format(move))
                            player_hp_sp["hp"] += moves[move][1]
                            print("You regained {} HP!".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                            if player_hp_sp["hp"] > max_player_hp:
                                player_hp_sp["hp"] = max_player_hp
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False

                    if moves[move][2] == "Status":
                        if player_hp_sp["sp"] >= moves[move][3]:
                            taken_turn = True
                            print("\n===---------- PLAYER MOVE ----------===")
                            print("Player used {}".format(move))
                            enemy_hp_sp["status"] == moves[move][1]
                            print("The enemy Brush was inflicted with {}".format(moves[move][1]))
                            player_hp_sp["sp"] -= moves[move][3]
                        else:
                            print("You don't have enough SP to perform this action")
                            taken_turn = False
                            
                            
                elif move_decision == 5:
                    desc_decision = 0
                    print("---------- INFO TAB ----------")
                    for i in range(len(player_moves)):
                        print_move = player_moves[i+1]
                        if moves[print_move][2] == "Phys":
                            type_move = "HP"
                        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
                            type_move = "SP"
                        print("{}. [{}][{}{}]".format(i + 1, player_moves[i+1], moves[print_move][3], type_move))
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
                                return finished_battle, player_hp_sp, enemy_hp_sp
                                
                        except:
                            print("Please only input a number from 1 - 5")

                elif move_decision == 6:
                    return finished_battle, player_hp_sp, enemy_hp_sp
                
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
                    return finished_battle, player_hp_sp, enemy_hp_sp
                
                elif battle_ended == True:
                    if player_hp_sp["hp"] <= 0:
                        print("You have been defeated")
                    if enemy_hp_sp["hp"] <= 0:
                        print("You have won the battle!")
                    finished_battle = True
                    return finished_battle, player_hp_sp, enemy_hp_sp
                
            
def battle_over(player_hp_sp, enemy_hp_sp):
    battle_ended = False
    if player_hp_sp["hp"] <= 0 or enemy_hp_sp["hp"] <= 0:
        battle_ended = True  
    else:
        battle_ended = False
    return battle_ended
             
def enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, player_hp_sp, enemy_hp_sp):
    max_enemy_hp = enemy_stats["hp"]
    enemy_moved = False
    time.sleep(0.7)
    print("\n===---------- ENEMY MOVE ----------===")
    while enemy_moved == False:
        if enemy_stats["status"] != "Sleep":
            enemy_move = random.randint(1, 4)
            move = enemy_moves[enemy_move]
            if moves[move][2] == "Phys":
                if enemy_hp_sp["hp"] > moves[move][3]:
                    enemy_moved = True
                    print("Enemy used {}".format(move))
                    player_hp_sp["hp"] -= moves[move][1]
                    print("You lost {} HP\n".format(moves[move][1]))
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
                    print("You lost {} HP\n".format(moves[move][1]))
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
                    print("The enemy Brush regained {} HP!\n".format(moves[move][1]))
                    enemy_hp_sp["sp"] -= moves[move][3]
                    if enemy_hp_sp["hp"] > max_enemy_hp:
                        enemy_hp_sp["hp"] = max_enemy_hp
                    time.sleep(0.7)
                else:
                    enemy_move = random.randint(1, 4)
                    enemy_moved = False
        else:
            enemy_stats["status"] == "none"

def characters_command(finished_battle, characters, player_stats, char_2_stats, char_3_stats, player_moves, char_2_moves, char_3_moves, moves):
    for i in range(len(characters)):
        print_char = characters[i + 1]
        print("{}. [{}]".format(i + 1, print_char))
    char_decision = int(input("What character would you like to switch to? (I for Info & B for Back)(1/2/3/I/B) "))
    
        

main()
