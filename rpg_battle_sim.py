##
# rpg_battle_sim.py
# Date: 1/07/19
# Author: NZK
# RPG battle sim focused around dental hygiene.
import random


# Main Function - Hub for battle
def main():
    # Stats and moves assigned to each character
    characters = {1:"Char 1", 2:"Char 2", 3:"Char 3"}
    moves = {
        "Slap":("rock", 20, "Phys", 6),
        "Whiten":("normal", 50, "Heal", 10),
        "Paste Blast":("paper", 25, "Spec", 4),
        "Floss Whip":("scissors", 30, "Phys", 12),
        "Clean Punch":("Rock", 30, "Phys", 10)}

    moves_desc = {"Slap":"A simple Slap",
                  "Whiten":"The user cleans their brush and heals them",
                  "Paste Blast":"A powerful blast of Toothpaste",
                  "Floss Whip":"The user grabs a piece of floss and whips the opponent",
                  "Clean Punch":"The user punches the opponent with force"}
    
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61}
    
    char_2_stats = {"level":5 , "type":"paper", "hp":100, "sp":50, "atk":48, "def":50, "spd":50}
    
    char_3_stats = {"level":5 , "type":"scissors", "hp":100, "sp":50, "atk":38, "def":60, "spd":40}
    
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Floss Whip"}
    
    enemy_stats = {"level":5, "type":"scissors", "hp":100, "sp":50, "atk":48, "def":64, "spd":31}
    
    enemy_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Floss Whip"}
    finished_battle = False
    max_hp = player_stats["hp"]
    stats_bar = "--------------------\ Stats \--------------------"
    stats_bar_2 = "--------------------/ Stats /--------------------"
    print("Player encountered an infected brush!")
    # Fight menu which shows the user the options
    while finished_battle == False:
        print("""What will you do?
    [F] for Fight
    [C] for Characters
    [B] for Bag
    [R] for Run""")
        # Input for decisions on what to do
        print(stats_bar)
        print("Player: LEVEL: {}, HP: {}, SP:{}".format(player_stats["level"], player_stats["hp"], player_stats["sp"]))
        print("Enemy: LEVEL: {}, HP: {}, SP:{}".format(enemy_stats["level"], enemy_stats["hp"], enemy_stats["sp"]))
        print(stats_bar_2)
        option = input("Please choose your option: ")
        if option == "F":
            finished_battle = fight_command(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc)
        elif option == "C":
            finished_battle = characters_command(finished_battle, characters, player_stats, char_2_stats, char_3_stats, player_moves, moves)
        elif option == "B":
            bag_command()
        elif option == "R":
            run_command()
        else:
            print("Please only input one of the 4 options")
        
def fight_command(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves, moves_desc):
    taken_turn = False
    for i in range(len(player_moves)):
        print_move = player_moves[i+1]
        if moves[print_move][2] == "Phys":
            type_move = "HP"
        if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
            type_move = "SP"
        print("{}. [{}][{}{}]".format(i + 1, player_moves[i+1], moves[print_move][3], type_move))
    # Input for the move to be used
    while taken_turn == False:
        try:
            move_decision = int(input("Which move would you like to use? (5 for Info & 6 for Back)(1/2/3/4/5/6) "))
            if move_decision >= 1 and move_decision <= 4:
                move = player_moves[move_decision]
                taken_turn = True
                if moves[move][2] == "Phys":
                    if player_stats["hp"] > moves[move][3]:
                        print("Player used {}".format(move))
                        enemy_stats["hp"] -= moves[move][1]
                        print("The enemy Brush lost {} HP".format(moves[move][1]))
                        player_stats["hp"] -= moves[move][3]
                    else:
                        print("You don't have enough HP to perform this action")
                if moves[move][2] == "Spec":
                    if player_stats["sp"] >= moves[move][3]:
                        print("Player used {}".format(move))
                        enemy_stats["hp"] -= moves[move][1]
                        print("The enemy Brush lost {} HP".format(moves[move][1]))
                        player_stats["sp"] -= moves[move][3]
                    else:
                        print("You don't have enough SP to perform this action")
                if moves[move][2] == "Heal":
                    if player_stats["sp"] >= moves[move][3]:
                        player_stats["hp"] += moves[move][1]
                        print("You regained {} HP!".format(moves[move][1]))
                        player_stats["sp"] -= moves[move][3]
                        if player_stats["hp"] > 100:
                            player_stats["hp"] = 100
                    else:
                        print("You don't have enough SP to perform this action")
                        
            elif move_decision == 5:
                print("---------- INFO TAB ----------")
                for i in range(len(player_moves)):
                    print_move = player_moves[i+1]
                    if moves[print_move][2] == "Phys":
                        type_move = "HP"
                    if moves[print_move][2] == "Spec" or moves[print_move][2] == "Heal":
                        type_move = "SP"
                    print("{}. [{}][{}{}]".format(i + 1, player_moves[i+1], moves[print_move][3], type_move))
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
Description: {}
Power: {}
Type: {}
Cost : {}{}""".format(move, moves_desc[move], moves[move][1], moves[move][2], moves[move][3], type_move))
                        
                except:
                    print("Please only input a number from 1 - 5")
            else:
                print("Please only input a number from 1 - 6")
                taken_turn = False

            
        except:
            print("Please only input a number from 1 - 6")
            taken_turn = False
    
    if player_stats["hp"] <= 0 or enemy_stats["hp"] <= 0:
        finished_battle = True
        if player_stats["hp"] <= 0 and enemy_stats["hp"] > 0:
            print("You were defeated")
        elif player_stats["hp"] > 0 and enemy_stats ["hp"] <= 0:
            print("You won the battle")
        return finished_battle
    else:
        finished_battle = False
        enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves)
        return finished_battle

def enemy_fight(finished_battle, player_stats, enemy_stats, player_moves, enemy_moves, moves):
    enemy_move = random.randint(1, 4)
    move = enemy_moves[enemy_move]
    if moves[move][2] == "Phys":
        if enemy_stats["hp"] > moves[move][3]:
            print("Enemy used {}".format(move))
            player_stats["hp"] -= moves[move][1]
            print("You lost {} HP".format(moves[move][1]))
            enemy_stats["hp"] -= moves[move][3]
        else:
            enemy_move = random.randint(1, 4)
    if moves[move][2] == "Spec":
        if enemy_stats["sp"] >= moves[move][3]:
            print("Enemy used {}".format(move))
            player_stats["hp"] -= moves[move][1]
            print("You lost {} HP".format(moves[move][1]))
            enemy_stats["sp"] -= moves[move][3]
        else:
            enemy_move = random.randint(1, 4)
    if moves[move][2] == "Heal":
        if enemy_stats["sp"] >= moves[move][3]:
            enemy_stats["hp"] += moves[move][1]
            print("The enemy Brush regained {} HP!".format(moves[move][1]))
            enemy_stats["sp"] -= moves[move][3]
            if enemy_stats["hp"] > 100:
                enemy_stats["hp"] = 100
        else:
            enemy_move = random.randint(1, 4)

def characters_command(finished_battle, characters, player_stats, char_2_stats, char_3_stats, player_moves, moves):
    for i in range(len(characters)):
        print_char = characters[i + 1]
        print("{}. [{}]".format(i + 1, print_char))
    char_decision = int(input("What character would you like to switch to? (I for Info & B for Back)(1/2/3/I/B) "))
    
        

main()
