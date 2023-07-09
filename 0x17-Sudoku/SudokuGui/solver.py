import numpy as np
board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

def solve(board):
    # Find next empty cell
    findEmpty = emptyCell(board)
    
    if not findEmpty:
        return True   # Board is filled 
    else:
        row, column = findEmpty
    
    for i in range(1,10):
        if isValid(board, i, (row, column)):
            board[row][column] = i

            if solve(board):
                return True

            board[row][column] = 0
    
    return False
             

def isValid (board, num, pos):
    # Check Row
    for i in range(9):
        if num == board[pos[0]][i]:
            return False
    # Check Column 
    for i in range(9):
        if num == board[i][pos[1]]:
            return False

    # Check Sub Grid
    row = pos[0] // 3 
    column = pos[1] // 3 

    for i in range(row * 3, (row * 3) + 3):
        for j in range(column * 3, (column * 3) + 3):
            if num == board[i][j]:
                return False 
    return True

def emptyCell(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return (row,column)
    return None

def printBoard(board):
    print(np.matrix(board))


    