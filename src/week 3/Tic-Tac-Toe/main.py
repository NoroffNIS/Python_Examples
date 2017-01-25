brick = 'X'
is_winner = False
MAX_ROUND = 9


def init_board():
    global board
    board = []
    for cell in range(1,10):
            board.append(cell)


def display_board():
    for cell in range(0,9):
        if (cell+1)%3 == 0:
            if cell+1 == 9:
                print(' {} '.format(board[cell]))
            else:
                print(' {} \n------------'.format(board[cell]))
        else:
            print(' {} |'.format(board[cell]), end='')
    print('')

def display_board_numpad():
    tmp = 7
    for cell in range(0,9):
        if (cell+1) % 3 == 0:
            print(cell % 3 + tmp)
            tmp = 1 if cell == 5 else 4
        else:
            print(cell % 3 + tmp, end='')

def get_user_cell():
    try:
        cell = int(input('Type in the cell number you want to place {}:'.format(brick)))
    except ValueError as msg:
        print(msg)
    return cell-1


player = lambda x : x % 2


def winner(brick):
    cell_d = 0
    for cell_1 in range(0,9,3):
        print('Cell', cell_1)
        if board[cell_1] == brick and board[cell_1 + 1] == brick and board[cell_1 + 2] == brick:
            return brick
        elif board[cell_1/3] == brick and board[cell_1/3 + 3] == brick and board[cell_1/3 + 6] == brick:
            return brick

    if board[cell_d] == brick and board[cell_d+4] == brick and board[cell_d+8] == brick:
        return brick
    elif board[cell_d+2] == brick and board[cell_d+4] == brick and board[cell_d+6] == brick:
        return brick
    else:
        return ''

def two_player():
    init_board()
    game_round = 0

    while not is_winner:
        display_board()
        brick = 'X' if player(game_round) == 0 else 'O'
        cell = get_user_cell()
        board[cell] = brick
       # is_winner = True if winner(brick) != '' else False
        if is_winner:
            print('There is a winner!\nThe winner is ', brick)
            break
        game_round += 1

    display_board()

display_board_numpad()