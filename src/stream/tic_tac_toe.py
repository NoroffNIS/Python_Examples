class tictactoe:
    no_winner = True
    game_round = 0
    high = 3
    board = []

    def __init__(self, brick='X'):
        self.brick = brick
        self.init_board()
        self.no_winner = True
        self.game_round = 0
        self.high = 3
        self.board = []
        self.brick = 'X'

    def init_board(self):
        for cell in range(1, (self.high*self.high)+1):
            self.board.append(cell)

    def display_board(self):
        for c in range(len(self.board)-1, 1, -3):
            print(self.board[c-2],'|', self.board[c-1],'|', self.board[c])
            if c > self.high:
                print('---------')
            else:
                print('')

    def check_winner(self):
        winner = False
        for cell in range(0,len(self.board), 3):
            if self.board[cell] == self.board[cell+1] == self.board[cell+2]:
                winner = True
            elif self.board[int(cell/3)] == self.board[int(cell/3+3)] == self.board[int(cell/3+6)]:
                winner = True

        if self.board[0] == self.board[4] == self.board[8]:
            winner = True
        elif self.board[2] == self.board[4] == self.board[6]:
            winner = True

        return winner


    def valid_move(self, move):
        print(move)
        if str(self.board[move]).upper() == 'X' or str(self.board[move]).upper() == 'O':
            return False
        else:
            return True

    def next_player(self):
        self.game_round += 1
        self.brick = 'X' if self.game_round % 2 == 0 else 'O'





