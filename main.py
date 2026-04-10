import random as rd

def gen_board(w, h, bombs):
    width, height = w, h
    board = []
    bomb_count = bombs

    for i in range(height):
        board.append([0 for _ in range(width)])

    for bomb in range(bomb_count):
        row, col = rd.randint(0,height-1), rd.randint(0,width-1)
        if board[row][col] != 9:
            board[row][col] = 9

    for i, row in enumerate(board):
        for j, col in enumerate(row):
            count = 0
            if board[i][j] != 9:
                if i-1 >= 0:
                    if board[i-1][j] == 9: count += 1
                    if j-1 >= 0:
                        if board[i-1][j-1] == 9: count += 1
                    if j+1 < width:
                        if board[i-1][j+1] == 9: count += 1
                if i+1 < height:
                    if board[i+1][j] == 9: count += 1
                    if j-1 >= 0:
                        if board[i+1][j-1] == 9: count += 1
                    if j+1 < width:
                        if board[i+1][j+1] == 9: count += 1
                if j-1 >= 0:
                    if board[i][j-1] == 9: count += 1
                if j+1 < width:
                    if board[i][j+1] == 9: count += 1
                board[i][j] = count
    return board

def print_board(board):
    for row in board:
        line = ""
        for col in row:
            if col == 9: line += "* "
            else: line += f"{col} "
        print(line)

board = gen_board(30,16,99)
print_board(board)
