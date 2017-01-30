from tkinter import *
import tkinter.messagebox as box

windows = Tk()
windows.title('Message box')



def msg_box():
    print(box.askokcancel('Title', 'Question?'))
    print(box.askquestion('Title', 'Question?'))
    print(box.askretrycancel('Title', 'Question?'))
    print(box.askyesno('Title', 'Question?'))
    print(box.askyesnocancel('Title', 'Question?'))
    print(box.showerror('Title', 'Question?'))
    print(box.showinfo('Title', 'Question?'))
    print(box.showwarning('Title', 'Question?'))


btn = Button(windows, text='Press me', command=msg_box)
btn.pack()
windows.mainloop()