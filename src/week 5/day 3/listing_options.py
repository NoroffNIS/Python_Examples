from tkinter import*
from tkinter import ttk
import tkinter.messagebox as box

window = Tk()
window.title('Course at Noroff')

frame = Frame(window, colormap='new',height=100, width=100, bd=10, relief=SUNKEN)

listbox = Listbox(frame)
listbox.insert(1, 'PRG')
listbox.insert(2, 'SQL')
listbox.insert(3, 'HIR')

def dialog():
    box.showinfo('Selection', 'Your choice '+listbox.get(listbox.curselection()))

btn = ttk.Button(frame, text='Choose', command=dialog)
btn.pack(side=RIGHT, padx=5)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()