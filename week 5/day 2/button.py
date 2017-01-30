from tkinter import *
from tkinter import ttk

window = Tk()

window.title('This is buttons')

btn_end = Button(window, text='Exit', command=exit)

def tog():
    global btn_tog
    if window.cget('bg') == 'yellow':
        window.config(bg='gray')
        btn_tog.config(bg='red')
    else:
        window.config(bg='yellow')
        btn_tog.config(bg='grey')

btn_tog = Button(window, text='Switch', command=tog)
btn_end.pack(padx=150, pady=20)
btn_tog.pack(padx=150, pady=20)

def callback(number):
    print ("button", number)

Button(text="one",   command=lambda: callback(1)).pack()
ttk.Button(text="two",   command=lambda: callback(2)).pack()
ttk.Button(text="three", command=lambda: callback(3)).pack()


window.mainloop()