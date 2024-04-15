from state import add_possible_moves,table_reset

# heuristic function
def heuristic(table):
    # number of disks and stability for each player
    white = 0
    black = 0
    values = [[20, -3, 11, 8, 8, 11, -3, 20],[-3, -7, -4, 1, 1, -4, -7, -3],[11, -4, 2, 2, 2, 2, -4, 11],[8, 1, 2, -3, -3, 2, 1, 8],
              [8, 1, 2, -3, -3, 2, 1, 8],[11, -4, 2, 2, 2, 2, -4, 11],[-3, -7, -4, 1, 1, -4, -7, -3],[20, -3, 11, 8, 8, 11, -3, 20]]
    difference = 0
    x1 = [-1, -1, 0, 1, 1, 1, 0, -1]
    y1 = [0, 1, 1, 1, 0, -1, -1, -1]
    white_front = 0
    black_front = 0
    
    for i in range(8):
        for j in range(8):
            if table[i][j] == "B":
                white += 1
                difference += values[i][j]
                
            elif table[i][j] == "C":
                black += 1
                difference -= values[i][j]
                
            if table[i][j] == "B" or table[i][j] == "C":
                x = 0
                y = 0
                for k in range(8):
                    x = i + x1[k]
                    y = j + y1[k]
                    
                    if x >= 0 and x < 8 and y >= 0 and y < 8 and table[x][y] is None:
                        if table[i][j] == "B":
                            white_front += 1
                        else:
                            black_front += 1
                        
                        break
                    
                
    coin_parity = 0
    
    if white + black == 64:
        if white > black:
            return 1000000
        elif white < black:
            return -1000000
        else:
            return 0
        
    if white > black:
        coin_parity = (100 * white) / (white + black)
    elif black > white:
        coin_parity = -(100 * black) / (white + black)
        
    fronts = 0
    if white_front > black_front:
        fronts = -(100 * white_front) / (white_front + black_front)
    elif black_front > white_front:
        fronts = (100 * black_front) / (white_front + black_front)
    
    # disks in corners
    white_corners = 0
    black_corners = 0
    
    if table[0][0] == "B":
        white_corners += 1
    elif table[0][0] == "C":
        black_corners += 1
    
    if table[0][7] == "B":
        white_corners += 1
    elif table[0][7] == "C":
        black_corners += 1
    
    if table[7][0] == "B":
        white_corners += 1
    elif table[7][0] == "C":
        black_corners += 1
        
    if table[7][7] == "B":
        white_corners += 1
    elif table[7][7] == "C":
        black_corners += 1
    
    corners = 25 * (white_corners - black_corners)
    
    # disks close to the corners
    white_corners_close = 0
    black_corners_close = 0
    
    if table[0][0] is None:
        if table[0][1] == "B":
            white_corners_close += 1
        elif table[0][1] == "C":
            black_corners_close += 1
        
        if table[1][0] == "B":
            white_corners_close += 1
        elif table[1][0] == "C":
            black_corners_close += 1
            
        if table[1][1] == "B":
            white_corners_close += 1
        elif table[1][1] == "C":
            black_corners_close += 1
    
    if table[0][7] is None:
        if table[1][7] == "B":
            white_corners_close += 1
        elif table[1][7] == "C":
            black_corners_close += 1
        
        if table[0][6] == "B":
            white_corners_close += 1
        elif table[0][6] == "C":
            black_corners_close += 1
            
        if table[1][6] == "B":
            white_corners_close += 1
        elif table[1][6] == "C":
            black_corners_close += 1
    
    if table[7][0] is None:
        if table[7][1] == "B":
            white_corners_close += 1
        elif table[7][1] == "C":
            black_corners_close += 1
        
        if table[6][0] == "B":
            white_corners_close += 1
        elif table[6][0] == "C":
            black_corners_close += 1
            
        if table[6][1] == "B":
            white_corners_close += 1
        elif table[6][1] == "C":
            black_corners_close += 1
    
    if table[7][7] is None:
        if table[7][6] == "B":
            white_corners_close += 1
        elif table[7][6] == "C":
            black_corners_close += 1
        
        if table[6][7] == "B":
            white_corners_close += 1
        elif table[6][7] == "C":
            black_corners_close += 1
            
        if table[6][6] == "B":
            white_corners_close += 1
        elif table[6][6] == "C":
            black_corners_close += 1
    
    close_corners = -12.5 * (white_corners_close - black_corners_close)
        
        
    # disk mobility
    change = add_possible_moves(table,"B")
    white_mobility = len(change)
    move = table_reset(table,"B",True)
    change = add_possible_moves(table,move)
    black_mobility = len(change)
    move = table_reset(table,move,True)
    if white_mobility == 0 and black_mobility == 0:
        if white > black:
            return 1000000
        elif white < black:
            return -1000000
        else:
            return 0
        
    mobility = 0
    if white_mobility > black_mobility:
        mobility = (100 * white_mobility) / (white_mobility + black_mobility)
    elif black_mobility > white_mobility:
        mobility = -(100 * black_mobility) / (white_mobility + black_mobility)
    
    return (78.922 * mobility) + (801.724 * corners) + (10 * coin_parity) + (382.026 * close_corners) + (10 * difference) + (74.396 * fronts)
    
    
if __name__ == "__main__":
    from state import print_table
    print_table([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, 'B', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]])
    print(heuristic([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, 'B', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]))
    
    print_table([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, 'C', None, None, None, None], [None, None, None, 'C', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]])
    print(heuristic([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, 'C', None, None, None, None], [None, None, None, 'C', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]))
    
    print_table([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, 'B', 'C', None, None, None, None], [None, None, None, 'B', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]])
    print(heuristic([[None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, 'B', 'C', None, None, None, None], [None, None, None, 'B', 'C', None, None, None], [None, None, None, 'C', 'B', None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None]]))