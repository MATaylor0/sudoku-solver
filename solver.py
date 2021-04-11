import math
import csv

def readBoard():
    with open('board.csv', 'r') as file:
        data = csv.reader(file, delimiter = ',')

        board = []
        for row in data:
            tmp = []
            for elem in row:
                tmp.append(int(elem))
            
            board.append(tmp)
    
    return board

def findBlank(board):
    for row, i in enumerate(board):
        for col, j in enumerate(i):
            if j == 0:
                return [row, col]

def findValid(val, row, col, board):
    rowArray = board[row]
    colArray = [i[col] for i in board]
    sqrArray = []
    
    sqrX = [3 * math.floor(row / 3)]
    sqrY = [3 * math.floor(col / 3)]

    for i in range(1, 3):
        sqrX.append(sqrX[0] + i)
        sqrY.append(sqrY[0] + i)

    for i in sqrX:
        for j in sqrY:
            sqrArray.append(board[i][j])

    if (val not in rowArray) and (val not in colArray) and (val not in sqrArray):
        return True
    else:
        return False

def solve(board):
    search = findBlank(board)

    if not search:
        return True
    else:
        row, col = search

    for i in range(1, 10):
        if findValid(i, row, col, board):
            board[row][col] = i

            if solve(board):
                return True
            
            board[row][col] = 0

    return False

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - - ')
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end = '')
            
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + ' ', end = '')

def main():
    board = readBoard()

    printBoard(board)
    print('\n- - - - - - - - - - - - \n')

    solve(board)
    printBoard(board)

if __name__ == '__main__':
    main()