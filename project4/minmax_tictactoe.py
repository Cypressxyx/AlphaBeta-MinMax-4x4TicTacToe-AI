'''
4x4 Tic Tac Toe minmax Solver
Ryan Boyle, Jorge Bautista
This program solves 4x4 tic tac toe problem using minmax and alpha beta pruning
'''
import numpy as np
import time as t

def eval(board):
    P1_pos = np.where(board == 1)
    P1_row = P1_pos[0].tolist()
    P1_col = P1_pos[1].tolist()
    
    P2_pos = np.where(board == 2)
    P2_row = P2_pos[0].tolist()
    P2_col = P2_pos[1].tolist()
    
    P1_winCount = 0
    P1_move = []
    P2_winCount = 0
    P2_move = []
    
    P1_moveCount = 0
    P2_moveCount = 0
    win_pos = [0, 1, 2, 3]
    
    #Checks if either player has won
    for i in range(0, len(winning_boards)):
        if (board[0][winning_boards[i][0]] == 1): #check for player 1
            if (board[1][winning_boards[i][1]] == 1):
                if (board[2][winning_boards[i][2]] == 1):
                    if (board[3][winning_boards[i][3]] == 1):
                        P1_winCount += 1
        if (P1_winCount == 1):
            return 100

        if (board[0][winning_boards[i][0]] == 2): #check for player 2
            if (board[1][winning_boards[i][1]] == 2):
                if (board[2][winning_boards[i][2]] == 2):
                    if (board[3][winning_boards[i][3]] == 2):
                        P2_winCount += 1
        if (P2_winCount == 1):
            return -100

    #Checks for possible player wins
    for i in range(0, len(winning_boards)):
        if (board[0][winning_boards[i][0]] != 2): #check for player 1
            if (board[1][winning_boards[i][1]] != 2):
                if (board[2][winning_boards[i][2]] != 2):
                    if (board[3][winning_boards[i][3]] != 2):
                        P1_moveCount += 1
                        P1_move.append(winning_boards[i])

        if (board[0][winning_boards[i][0]] != 1): #check for player 2
            if (board[1][winning_boards[i][1]] != 1):
                if (board[2][winning_boards[i][2]] != 1):
                    if (board[3][winning_boards[i][3]] != 1):
                        P2_moveCount += 1
                        P2_move.append(winning_boards[i])
    return P1_moveCount - P2_moveCount

def emptyBoard(board):
    return np.sum(board == 0) == 0

def leafNode(board):
    win = eval(board.copy())
    if(win == 100):
        return win
    if (win == -100):
        return win
    if(emptyBoard(board)):
        return .5
    return win #not a leaf node

def isValid(board):
    x = (np.sum(board == 1))
    y = (np.sum(board == 2))
    val = (x-y)
    return False if val > 1 else True

def getMove(board):
    x = (np.sum(board == 1))
    y = (np.sum(board == 2))
    if(x == y):
        return "x"
    return "O"

def maxnode(nodeType):
    return True if nodeType is 1 else False

def minmax(board,nodeType):
    global bestmin
    global minx
    global miny
    global nodes_expanded_minmax
    nodeVal = leafNode(board)
    if(nodeVal == 100 or nodeVal == -100 or nodeVal == .5):
        return nodeVal 

    val = -10000000 if maxnode(nodeType) else 10000000 #check if max or min node
    if(maxnode(nodeType)): #max node
        for i in range (4):
            for j in range(4):
                if(board[i][j] == 0): #choose
                    board[i][j] = 1
                    if(isValid(board.copy())):
                        nodes_expanded_minmax = nodes_expanded_minmax + 1
                        nextVal = minmax(board.copy(), 0)
                        val = max(val,nextVal)
                        if(val > bestmin):
                            bestmin = val
                            minx = j
                            miny = i
                    board[i][j] = 0 #unchoose
                
    else: #min node
        for i in range (4):
            for j in range(4):
                if(board[i][j] == 0): #choose
                    board[i][j] = 2
                    if(isValid(board.copy())):
                        nodes_expanded_minmax = nodes_expanded_minmax + 1
                        nextVal = minmax(board.copy(), 1)
                        val = min(val,nextVal)
                    board[i][j] = 0 #unchoose
    return val

def alphaBeta(board,alpha,beta,nodeType,depth):
    nodeVal = leafNode(board)
    if(nodeVal == 100 or nodeVal == -100 or nodeVal == .5 or depth == 0):
        return nodeVal 

    global expanded
    global bestab
    global ax
    global ay
    if(maxnode(nodeType)): #max node
        val = alpha
        for i in range (4):
            for j in range(4):
                if(board[i][j] == 0): #choose
                    board[i][j] = 1
                    if(isValid(board.copy())):
                        expanded = expanded + 1
                        nextVal = alphaBeta(board.copy(),val,beta,0,depth - 1)
                        val = max(val,nextVal)
                        if(val > bestab and depth == 6):
                            bestab = val
                            ax = j
                            ay = i
                        if(val >= beta):
                            return val
                    board[i][j] = 0 #unchose
    else: #min node
        val = beta
        for i in range (4):
            for j in range(4):
                if(board[i][j] == 0): #choose
                    board[i][j] = 2
                    if(isValid(board.copy())):
                        expanded = expanded + 1
                        nextVal = alphaBeta(board.copy(),alpha,val,1,depth - 1)
                        val = min(val,nextVal)
                        if(val <= alpha):
                            return val
                    board[i][j] = 0 #unchose
    return val

def printRes(algorithim,move):
        global nodes_expanded_minmax
        global expanded
        global minx
        global miny
        global ax
        global ay
        x = 0
        y = 0
        num_expanded = 0
        timeStart = 0
        print(algorithim,"Algorithim:")
        if(algorithim == "MiniMax"):
            timeStart = t.time()
            val = minmax(gameBoard.copy(),move)
            x = minx
            y = miny
            num_expanded = nodes_expanded_minmax
            nodes_expanded_minmax = 0
        else:
            timeStart = t.time()
            val = alphaBeta(gameBoard.copy(),-10000,100000,move,6)
            x = ax
            y = ay
            num_expanded = expanded
            expanded = 0


        print("Root Node Value: ", end='')
        if(val == 100):
            print("Player 1 Wins " , val)
        elif (val == -100):
            print("Player 2 Wins " , val)
        else:
            print("Tie ", val)

        print("Best moves are " , y, " " ,x)
        print("Numbers of nodes expanded in ", algorithim, " :", num_expanded)
        print("CPU Time: ", t.time() - timeStart, " seconds.")

winning_boards = [[0,1,2,3], [0,1,3,2], [0,2,1,3], [0,2,3,1], [0,3,1,2], 
                    [0,3,2,1], [1,0,2,3], [1,0,3,2], [1,2,0,3], [1,2,3,0], 
                    [1,3,0,2], [1,3,2,0], [2,0,1,3], [2,0,3,1], [2,1,0,3], 
                    [2,1,3,0], [2,3,0,1], [2,3,1,0], [3,0,1,2], [3,0,2,1], 
                    [3,1,0,2], [3,1,2,0], [3,2,0,1], [3,2,1,0]]

board = np.array( [[1, 2 , 1,2], [2,1,0,0], [1,0,0,0], [2,0,0,0]] )
nodes_expanded_minmax = 1
expanded = 1
bestmin = -100
minx = 0
miny = 0
move = 0
bestab = -100
ax = 0
ay = 0
choice = int(input("Enter option: 1 2 or quit(3)"))
while(choice is not 3):
    print("Enter the filename") 
    fileName = input()
    with open(fileName,"r") as gameFile:
        gameBoard = gameFile.read()
    print("Evaluating the game board: ")
    print(gameBoard)
    g = []
    for item in gameBoard.split("\n"):
        arr = []
        for val in item.split():
            arr.append(int(val))
        g.append(arr)
    g.pop()
    gameBoard = np.array(g)
    whosemove = getMove(gameBoard.copy())
    move = 1 if whosemove == "x"  else 0
    if (choice is 1):
        printRes("MiniMax",move)

    if (choice is 2):
        printRes("Alpha Beta Pruning",move)

    choice = int(input("Enter option: 1 2 or quit(3)"))
