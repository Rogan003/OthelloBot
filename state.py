# function that prints out the playing table
def print_table(table,end = False):
    if not end:
        ret = "\nTrenutna tabla:\nLegenda:\nB - belo\nC - crno\n@ - moguce polje za odigrati\n\n"
    else:
        ret = "\n==================\n\n"

    for i in range(8):
        for j in range(8):
            if table[i][j] == None:
                ret += "_ "
            
            else:
                ret += table[i][j] + " "
                
        ret += " " + str(i + 1) + "\n"
    
    ret += "\nA B C D E F G H"    
    print(ret)

# function that adds all the possible moves
def add_possible_moves(table,move):
    change = {}
    
    # horizontal lines
    for i in range(8):
        first = None
        first_index = None
        last = None
        disk_first = None
        both = [False,False]
        
        for j in range(8):
            if table[i][j] == "B" or table[i][j] == "C":
                if disk_first is None:
                    disk_first = table[i][j]
                    if j > 0:
                        first_index = j - 1
                    
                if first is None and table[i][j] == move:
                    first = j
                    
                if table[i][j] == move:
                    last = j
                    
                both[ord(table[i][j]) - ord("B")] = True
            
            if table[i][j] is None or j == 7:
                if both[0] and both[1]:
                    if table[i][j - 1] != move and table[i][j] is None:
                        table[i][j] = "@"
                        if (i,j) in change:
                            for k in [(i,a) for a in range(last + 1,j)]:
                                change[(i,j)].append(k)
                        else:
                            change[(i,j)] = [(i,a) for a in range(last + 1,j)]
                    
                    if disk_first != move and first_index is not None:
                        table[i][first_index] = "@"
                        if (i,first_index) in change:
                            for k in [(i,a) for a in range(first_index + 1,first)]:
                                change[(i,first_index)].append(k)
                        else:
                            change[(i,first_index)] = [(i,a) for a in range(first_index + 1,first)]
                
                first = None
                last = None
                disk_first = None
                both = [False,False]
    
    # vertical lines            
    for j in range(8):
        first = None
        first_index = None
        last = None
        disk_first = None
        both = [False,False]
        
        for i in range(8):
            if table[i][j] == "B" or table[i][j] == "C":
                if disk_first is None:
                    disk_first = table[i][j]
                    if i > 0:
                        first_index = i - 1
                    
                if first is None and table[i][j] == move:
                    first = i
                    
                if table[i][j] == move:
                    last = i
                    
                both[ord(table[i][j]) - ord("B")] = True
            
            if table[i][j] is None or table[i][j] == "@" or i == 7:
                if both[0] and both[1]:
                    if table[i - 1][j] != move and (table[i][j] is None or table[i][j] == "@"):
                        table[i][j] = "@"
                        if (i,j) in change:
                            for k in [(a,j) for a in range(last + 1,i)]:
                                change[(i,j)].append(k)
                        else:
                            change[(i,j)] = [(a,j) for a in range(last + 1,i)]
                    
                    if disk_first != move and first_index is not None:
                        table[first_index][j] = "@"
                        if (first_index,j) in change:
                            for k in [(a,j) for a in range(first_index + 1,first)]:
                                change[(first_index,j)].append(k)
                        else:
                            change[(first_index,j)] = [(a,j) for a in range(first_index + 1,first)]
                
                first = None
                last = None
                disk_first = None
                both = [False,False]
                
    # diagonals 0 0 - 7 7          
    for i in range(8):
        first = None
        first_index = None
        last = None
        disk_first = None
        both = [False,False]
        
        first2 = None
        first_index2 = None
        last2 = None
        disk_first2 = None
        both2 = [False,False]
        
        for j in range(8 - i):
            if table[j][j + i] == "B" or table[j][j + i] == "C":
                if disk_first is None:
                    disk_first = table[j][j + i]
                    if j > 0:
                        first_index = j - 1
                    
                if first is None and table[j][j + i] == move:
                    first = j
                    
                if table[j][j + i] == move:
                    last = j
                    
                both[ord(table[j][j + i]) - ord("B")] = True
            
            if table[j][j + i] is None or table[j][j + i] == "@" or j + i == 7:
                if both[0] and both[1]:
                    if table[j - 1][j + i - 1] != move and (table[j][j + i] is None or table[j][j + i] == "@"):
                        table[j][j + i] = "@"
                        if (j,j + i) in change:
                            for k in [(a,a + i) for a in range(last + 1,j)]:
                                change[(j,j + i)].append(k)
                        else:
                            change[(j,j + i)] = [(a,a + i) for a in range(last + 1,j)]
                    
                    if disk_first != move and first_index is not None:
                        table[first_index][first_index + i] = "@"
                        if (first_index, first_index + i) in change:
                            for k in [(a,a + i) for a in range(first_index + 1,first)]:
                                change[(first_index,first_index + i)].append(k)
                        else:
                            change[(first_index,first_index + i)] = [(a,a + i) for a in range(first_index + 1,first)]
                
                first = None
                last = None
                disk_first = None
                both = [False,False]
            
                
            if i != 0:
                if table[j + i][j] == "B" or table[j + i][j] == "C":
                    if disk_first2 is None:
                        disk_first2 = table[j + i][j]
                        if j > 0:
                            first_index2 = j - 1
                        
                    if first2 is None and table[j + i][j] == move:
                        first2 = j
                        
                    if table[j + i][j] == move:
                        last2 = j
                        
                    both2[ord(table[j + i][j]) - ord("B")] = True
                
                if table[j + i][j] is None or table[j + i][j] == "@" or j + i == 7:
                    if both2[0] and both2[1]:
                        if table[j + i - 1][j - 1] != move and (table[j + i][j] is None or table[j + i][j] == "@"):
                            table[j + i][j] = "@"
                            if (j + i,j) in change:
                                for k in [(a + i,a) for a in range(last2 + 1,j)]:
                                    change[(j + i,j)].append(k)
                            else:
                                change[(j + i,j)] = [(a + i,a) for a in range(last2 + 1,j)]
                        
                        if disk_first2 != move and first_index2 is not None:
                            table[first_index2 + i][first_index2] = "@"
                            if (first_index2 + i,first_index2) in change:
                                for k in [(a + i,a) for a in range(first_index2 + 1,first2)]:
                                    change[(first_index2 + i,first_index2)].append(k)
                            else:
                                change[(first_index2 + i,first_index2)] = [(a + i,a) for a in range(first_index2 + 1,first2)]
                    
                    first2 = None
                    first_index2 = None
                    last2 = None
                    disk_first2 = None
                    both2 = [False,False]

    # diagonals 7 0 - 0 7          
    for i in range(7,-1,-1):
        first = None
        first_index = None
        last = None
        disk_first = None
        both = [False,False]
        
        first2 = None
        first_index2 = None
        last2 = None
        disk_first2 = None
        both2 = [False,False]
        
        for j in range(i + 1):
            if table[i - j][j] == "B" or table[i - j][j] == "C":
                if disk_first is None:
                    disk_first = table[i - j][j]
                    if j > 0:
                        first_index = j - 1
                    
                if first is None and table[i - j][j] == move:
                    first = j
                    
                if table[i - j][j] == move:
                    last = j
                    
                both[ord(table[i - j][j]) - ord("B")] = True
            
            if table[i - j][j] is None or table[i - j][j] == "@" or j == i:
                if both[0] and both[1]:
                    if table[i - j + 1][j - 1] != move and (table[i - j][j] is None or table[i - j][j] == "@"):
                        table[i - j][j] = "@"
                        if (i - j,j) in change:
                            for k in [(i - a,a) for a in range(last + 1,j)]:
                                change[(i - j,j)].append(k)
                        else:
                            change[(i - j,j)] = [(i - a,a) for a in range(last + 1,j)]
                    
                    if disk_first != move and first_index is not None:
                        table[i - first_index][first_index] = "@"
                        if (i - first_index,first_index) in change:
                            for k in [(i - a,a) for a in range(first_index + 1,first)]:
                                change[(i - first_index,first_index)].append(k)
                        else:
                            change[(i - first_index,first_index)] = [(i - a,a) for a in range(first_index + 1,first)]
                
                first = None
                last = None
                disk_first = None
                both = [False,False]
            
                
            if i != 0:
                if table[7 - j][7 - i + j] == "B" or table[7 - j][7 - i + j] == "C":
                    if disk_first2 is None:
                        disk_first2 = table[7 - j][7 - i + j]
                        if j > 0:
                            first_index2 = j - 1
                        
                    if first2 is None and table[7 - j][7 - i + j] == move:
                        first2 = j
                        
                    if table[7 - j][7 - i + j] == move:
                        last2 = j
                        
                    both2[ord(table[7 - j][7 - i + j]) - ord("B")] = True
                
                if table[7 - j][7 - i + j] is None or table[7 - j][7 - i + j] == "@" or j == i:
                    if both2[0] and both2[1]:
                        if table[7 - j + 1][7 - i + j - 1] != move and (table[7 - j][7 - i + j] is None or table[7 - j][7 - i + j] == "@"):
                            table[7 - j][7 - i + j] = "@"
                            if (7 - j,7 - i + j) in change:
                                for k in [(7 - a,7 - i + a) for a in range(last2 + 1,j)]:
                                    change[(7 - j,7 - i + j)].append(k)
                            else:
                                change[(7 - j,7 - i + j)] = [(7 - a,7 - i + a) for a in range(last2 + 1,j)]
                        
                        if disk_first2 != move and first_index2 is not None:
                            table[7 - first_index2][7 - i + first_index2] = "@"
                            if (7 - first_index2, 7 - i + first_index2) in change:
                                for k in [(7 - a,7 - i + a) for a in range(first_index2 + 1,first2)]:
                                    change[(7 - first_index2,7 - i + first_index2)].append(k)
                            else:
                                change[(7 - first_index2,7 - i + first_index2)] = [(7 - a,7 - i + a) for a in range(first_index2 + 1,first2)]
                    
                    first2 = None
                    first_index2 = None
                    last2 = None
                    disk_first2 = None
                    both2 = [False,False]
    
    return change

# function that removes all the possible moves and changes the player(move var)        
def table_reset(table,move,isOkay):
    for i in range(8):
        for j in range(8):
            if table[i][j] == "@":
                table[i][j] = None
    if isOkay:            
        if move == "C":
            return "B"
        else:
            return "C"
        
    return move

# function that places one disk on the board
def play_a_move(table,place,move,change):
    try:
        a = int(place[1]) - 1
        b = ord(place[0].lower()) - ord('a')
        if table[a][b] == "@":
            for i in change[(a,b)]:
                table[i[0]][i[1]] = move

            table[a][b] = move
            return True
        else:
            raise Exception("Nije @")
        
    except Exception:
        print("Nemoguc potez!")
        return False  

# function that checks if there are available moves
def has_moves(table):
    playing = False
    for row in table:
        if '@' in row:
            playing = True
            break
            
    return playing

# function that determines who won
def end(table):
    table_reset(table,None,False)
    print_table(table,True)
    
    white = 0
    black = 0
    
    for i in table:
        for j in i:
            if j == "C":
                black += 1
                
            elif j == "B":
                white += 1
                
    print("\nBeli: " + str(white))
    print("Crni: " + str(black))
    
    if black > white:
        print("Pobedio: crni")
        
    elif white > black:
        print("Pobedio: beli")
        
    else:
        print("Nereseno")