from state import *
from minimax import bot_play
import time
# timing is commented on lines 3, 56, 58 and 59

if __name__ == "__main__":
    # table setup
    table = [[None for _ in range(8)] for _ in range(8)]

    table[3][3] = "B"
    table[3][4] = "C"
    table[4][3] = "C"
    table[4][4] = "B"

    move = "C"

    change = {}

    # game start
    while True:
        change = add_possible_moves(table,move)
        
        playing = has_moves(table)
                
        if not playing:
            move = table_reset(table,move,True)
            change = add_possible_moves(table,move)
        
            playing = has_moves(table)
                    
            if not playing:
                break
        
        print("====================")
        print_table(table)
        
        print("\nIgra: " + move)
        place = None
        if move == "C":
            keys = list(change)
            for i in range(len(change)):
                key = keys[i]
                print(str(i + 1) + ". " + chr(key[1] + ord('a')) + str(key[0] + 1))
                
            try:
                place = int(input("Unesite zeljenu opciju: ")) - 1
                if place >= 0 and place < len(change):
                    key = keys[place]
                    place = chr(key[1] + ord('a')) + str(key[0] + 1)
                else:
                    raise Exception
            except:
                place = None
                
        else:
            start_time = time.time()
            place = bot_play(table)
            end_time = time.time()
            print("Potrebno vreme: " + str(end_time - start_time))
        
        isOkay = play_a_move(table,place,move,change)
        move = table_reset(table,move,isOkay)
        if isOkay:
            print("Odigran potez: " + place)
    
    # winner output    
    end(table)