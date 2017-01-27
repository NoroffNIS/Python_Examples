from tkinter import *
import tkinter.messagebox as box

windows = Tk()
windows.title('Message box')

for b in dir(box):
    print(b)