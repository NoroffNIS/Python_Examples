from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)
frame.pack()
frame.config(height = 100, width = 200)
frame.config(relief = RIDGE)

ttk.Button(frame, text = 'trykk meg').grid()
frame.config(padding = (30,15))

root.mainloop()