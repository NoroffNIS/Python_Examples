from tkinter import*
from tkinter import ttk
import tkinter.messagebox as box

window = Tk()
window.title('Course at Noroff')

frame = Frame(window, colormap='new',height=100, width=100)

var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()

book_1 = Checkbutton(frame, text='PRG', variable= var_1, onvalue = 1, offvalue = 0)
book_2 = Checkbutton(frame, text='SQL', variable= var_2, onvalue = 1, offvalue = 0)
book_3 = Checkbutton(frame, text='HIR', variable= var_3, onvalue = 1, offvalue = 0)

def dialog():
    print(var_1.get())
    str = 'You choice:\n'
    if var_1.get() == 1 : str += 'PRG,'
    if var_2.get() == 1 : str += 'SQL,'
    if var_3.get() == 1 : str += 'HIR,'
    str += ' is easy'
    ok = box.showinfo('Selection', str)
    if ok == 'ok':
        book_1.deselect()
        book_3.select()
        book_2.toggle()


btn = Button(frame, text='Choose', command=dialog)
btn.pack(side=RIGHT, padx=5)
book_1.pack(side=LEFT)
book_2.pack(side=LEFT)
book_3.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()