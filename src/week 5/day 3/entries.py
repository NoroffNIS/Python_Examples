from tkinter import*
from tkinter import ttk

def getText(entry):
    print(entry.get())

window = Tk()

entry = ttk.Entry(window, width=30)
entry.grid(row=0, column=0)
entry1 = Entry(window, width=30)
entry1.grid(row=1, column=0)

btn = ttk.Button(window, text='Submit', command=lambda: getText(entry))
btn.grid(row=0, column=1)
btn = Button(window, text='Submit', command=lambda: getText(entry1))
btn.grid(row=1, column=1)

window.mainloop()