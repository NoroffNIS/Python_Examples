high = 3
board = []

def init_board():
    for cell in range(1, (high*high)+1):
        board.append(cell)


def display_board():
    for c in range(len(board)-1, 1, -3):
        print(board[c-2],'|', board[c-1],'|', board[c])
        if c > high:
            print('---------')
        else:
            print('')

def check_winner():
    pass

init_board()
display_board()
no_winner = True
game_round = 0
player = lambda x : x % 2

while no_winner:
    brick = 'X' if player(game_round) == 0 else 'O'
    choise = int(input('Type in the number you want to place the {} :'.format(brick)))
    board[choise-1] = brick
    display_board()
    game_round += 1
