from tkinter import*
from tkinter import ttk
import tkinter.messagebox as box

window = Tk()
window.title('Course at Noroff')

frame = Frame(window, height=100, width=100)

listbox = Listbox(frame, selectmode=MULTIPLE)
listbox.insert(1, 'PRG')
listbox.insert(3, 'SQL')
listbox.insert(2, 'HIR')

def dialog():
    stri = StringVar()
    print(listbox.curselection())
    for item in listbox.curselection():
        print(listbox.get(item))
        stri.set(stri.get() + listbox.get(item))

    box.showinfo('Selection', 'Your choice '+stri)

btn = ttk.Button(frame, text='Choose', command=dialog)
btn.pack(side=RIGHT, padx=5)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()