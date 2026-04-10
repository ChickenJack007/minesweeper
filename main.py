from scripts.utility import gen_board, print_board
height, width, bombs = input("").split()
board = gen_board(int(height),int(width),int(bombs))
print_board(board)
