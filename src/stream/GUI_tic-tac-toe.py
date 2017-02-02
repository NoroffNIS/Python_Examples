from tkinter import *
from tic_tac_toe import*

def press(btn):
    if theory.valid_move(btn):
        button[btn].config(text=theory.brick)
        theory.board[btn] = theory.brick
        theory.display_board()
        if theory.check_winner():
            print('there is a winner')
        theory.next_player()


window = Tk()
window.title('Tic Tac Toe')
board_frame = Frame(window)
button = []
theory = tictactoe('X')
theory.init_board()

for i in range(9):
    cell = i
    button.append(Button(board_frame, text=theory.board[cell], bd=10, font=('Cusier',16), command=lambda i=i : press(i)))
    button[i].grid(row=int(i/3), column=int(i%3))
board_frame.pack(padx=20, pady=20)
window.mainloop()