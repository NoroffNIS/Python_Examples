from tkinter import *
from tkinter import ttk

window = Tk()

window.title('This is window title')

label = Label(window, text='Hello World TOP', background="Yellow")
label.pack(side=TOP)

label = ttk.Label(window, text='Hello World BOTTOM', background="Yellow")
label.pack(side=BOTTOM)

window.mainloop()