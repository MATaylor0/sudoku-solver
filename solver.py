import math

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]]

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
    for i in board:
        print(i)

def main():
    printBoard(board)
    print('\n-----------------------------\n')

    solve(board)
    printBoard(board)

if __name__ == '__main__':
    main()