from heuristic import heuristic
from state import *
from copy import deepcopy

# helper hashmap for already calculated heuristics
heuristics = {}

# function that makes one bot move
def bot_play(table):
    game_table = deepcopy(table)
    table_reset(game_table,None,False)
    return minimax(game_table,7,0,True,"-inf","+inf")["place"]

# maximum and minimum helpers for minimax
def max_inf(a,b):
    if a == "-inf" and b == "-inf":
        return "-inf"
    
    elif a == "-inf" and b != "-inf":
        return b
    
    elif a != "-inf" and b == "-inf":
        return a
    
    else:
        return max(a,b)

def min_inf(a,b):
    if a == "+inf" and b == "+inf":
        return "+inf"
    
    elif a == "+inf" and b != "+inf":
        return b
    
    elif a != "+inf" and b == "+inf":
        return a
    
    else:
        return min(a,b)
    
def max_inf_val(a,b):
    if a["heuristic"] == "-inf" and b["heuristic"] == "-inf":
        return a
    
    elif a["heuristic"] == "-inf" and b["heuristic"] != "-inf":
        return b
    
    elif a["heuristic"] != "-inf" and b["heuristic"] == "-inf":
        return a
    
    else:
        if a["heuristic"] < b["heuristic"]:
            return b
        else:
            return a

def min_inf_val(a,b):
    if a["heuristic"] == "+inf" and b["heuristic"] == "+inf":
        return "+inf"
    
    elif a["heuristic"] == "+inf" and b["heuristic"] != "+inf":
        return b
    
    elif a["heuristic"] != "+inf" and b["heuristic"] == "+inf":
        return a
    
    else:
        if a["heuristic"] < b["heuristic"]:
            return a
        else:
            return b

# minimax algorithm that creates possible tables(states) and determines the best move for the bot       
def minimax(table,depth,level,isMax,alpha,beta,move = "B",place_move = None):
    change = add_possible_moves(table,move)
    if level == 0: # variable depth
        if len(change) == 1:
            depth = 2
        elif len(change) <= 3:
            depth = 7
        elif len(change) <= 6:
            depth = 6
        elif len(change) <= 9:
            depth = 5
        else:
            depth = 4
            
    elif level == 1:
        if depth == 7 and len(change) > 3:
            depth -= 1
        elif depth == 6 and len(change) > 6:
            depth -= 1
        elif depth == 5 and len(change) > 8:
            depth -= 1
            
    if depth <= level or not has_moves(table):
        key = str(table)
        if key in heuristics:
            return {"place" : place_move, "heuristic" : heuristics[key]}
        else:
            val = heuristic(table)
            heuristics[key] = val
            return {"place" : place_move, "heuristic" : val}
            
    if isMax:
        bestVal = {"place" : place_move, "heuristic" : "-inf"}
        for key in change:
            game_table2 = deepcopy(table)
            place = chr(key[1] + ord('a')) + str(key[0] + 1)
            play_a_move(game_table2,place,move,change)
            table_reset(game_table2,None,False)
            if level == 0:
                place_move = place
            value = minimax(game_table2,depth,level + 1,False,alpha,beta,"C",place_move)
            bestVal = max_inf_val(bestVal,value)
            alpha = max_inf(bestVal["heuristic"],alpha)
            if beta != "+inf" and alpha != "-inf" and beta <= alpha:
                break
        
        return bestVal
    
    else:
        bestVal = {"place" : place_move, "heuristic" : "+inf"}
        for key in change:
            game_table2 = deepcopy(table)
            place = chr(key[1] + ord('a')) + str(key[0] + 1)
            play_a_move(game_table2,place,move,change)
            table_reset(game_table2,None,False)
            if level == 0:
                place_move = place
            value = minimax(game_table2,depth,level + 1,True,alpha,beta,"B",place_move)
            bestVal = min_inf_val(bestVal,value)
            beta = min_inf(bestVal["heuristic"],beta)
            if beta != "+inf" and alpha != "-inf" and beta <= alpha:
                break
        
        return bestVal
    
if __name__ == "__main__":
    print(minimax([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, 'C', None, None, None, None], [None, None, None, 'C', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]
                  ,3,0,True,"-inf","+inf"))