##
# rpg_battle_sim.py
# Date: 1/07/19
# Author: NZK
# RPG battle sim focused around dental hygiene.



# Main Function - Hub for battle
def main():
    # Stats and moves assigned to each character
    player_stats = {"level":5 , "type":"rock", "hp":100, "sp":50, "atk":58, "def":44, "spd":61}
    player_moves = {1:"Slap", 2:"Whiten", 3:"Paste Blast", 4:"Floss Whip"}
    enemy_stats = {"level":5, "type":"scissors", "hp":100, "sp":50, "atk":48, "def":64, "spd":31}
    stats_bar = "--------------------\ Stats \--------------------"
    stats_bar_2 = "--------------------/ Stats /--------------------"
    # Fight menu which shows the user the options
    print("""Player encnountered an infected brush!
What will you do?
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
        fight_command(player_stats, enemy_stats, player_moves)
    elif option == "C":
        character_command()
    elif option == "B":
        bag_command()
    elif option == "R":
        run_command()
    else:
        print("Please only input one of the 4 options")
        
def fight_command(player_stats, enemy_stats, player_moves):
    moves = {"Slap":("rock", 20, "Phys", 6), "Whiten":("normal", 50, "Spec", 5), "Paste Blast":("paper", 25, "Spec", 4), "Floss Whip":("scissors", 30, "Phys", 12)}
    for i in range(len(player_moves)):
        print_move = player_moves[i+1]
        if moves[print_move][2] == "Phys":
            type_move = "HP"
        if moves[print_move][2] == "Spec":
            type_move = "SP"
        print("{}. [{}][{}{}]".format(i + 1, player_moves[i+1], moves[print_move][3], type_move))
    # Input for the move to be used
    try:
        move_decision = int(input("Which move would you like to use? (1/2/3/4) "))
        move = player_moves[move_decision]
        if moves[move][2] == "Phys":
            if player_stats["hp"] > moves[move][3]:
                print("Player used {}".format(move))
                enemy_stats["hp"] -= moves[move][1]
                print("The enemy Brush lost {} HP".format(moves[move][1]))
            else:
                print("You don't have enough HP to perform this action")
        if moves[move][2] == "Spec":
            if player_stats["sp"] > moves[move][3]:
                print("Player used {}".format(move))
                enemy_stats["hp"] -= moves[move][1]
                print("The enemy Brush lost {} HP".format(moves[move][1]))
            else:
                print("You don't have enough SP to perform this action")
    except:
        print("Please only input a number from 1 - 4")

main()
