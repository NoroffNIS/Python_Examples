from tkinter import *
from tkinter import ttk
import tkinter.messagebox as box
import tkinter

from tkinter import *


class Butpop:

    def __init__(self, master):
        self.root = master
        self.label = ttk.Label(master, text="Velg din foretrukne button/pop-up: ")
        self.label.grid(row=0, column=0, columnspan=2)

        ttk.Button(master, text="Question",
                   command=self.defa).grid(row=1, column=0)
        ttk.Button(master, text="okcancel",
                   command=self.defb).grid(row=1, column=1)
        ttk.Button(master, text="askretrycancel",
                   command=self.defc).grid(row=1, column=2)
        ttk.Button(master, text="yesno",
                   command=self.defd).grid(row=1, column=3)
        ttk.Button(master, text="yesnocancel",
                   command=self.defe).grid(row=1, column=4)
        ttk.Button(master, text="error",
                   command=self.deff).grid(row=1, column=5)
        ttk.Button(master, text="info",
                   command=self.defg).grid(row=1, column=6)
        ttk.Button(master, text="warning",
                   command=self.defh).grid(row=1, column=7)

        self.btn_tog = Button(master, text="switch", command=self.defi)
        self.btn_tog.grid(row=4, column=3)

        ttk.Button(master, text="exit",
                   command=self.defx).grid(row=2, column=3)

    def defa(self):
        box.askquestion('Title', 'Question')

    def defb(self):
        box.askokcancel('Title', 'Question')

    def defc(self):
        box.askretrycancel('Title', 'Question')

    def defd(self):
        box.askyesno('Title', 'Question')

    def defe(self):
        box.askyesnocancel('Title', 'Question')

    def deff(self):
        box.showerror('Title', 'Question')

    def defg(self):
        box.showinfo('Title', 'Question')

    def defh(self):
        box.showwarning('Title', 'Question')

    def defi(self):
        print(self.btn_tog.cget('bg'))
        if self.root.cget('bg') == 'yellow':
            self.root.config(bg='grey')
            self.btn_tog.configure(bg='red')

        else:
            self.root.config(bg='yellow')
            self.btn_tog.configure(background='grey')


    def defx(self):
        ttk.Button(text='Change color', command=exit())


def main():
    root = Tk()
    app = Butpop(root)
    root.mainloop()


if __name__ == "__main__": main()