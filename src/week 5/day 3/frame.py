from tkinter import*
from tkinter import ttk


window = Tk()

frame = ttk.Frame(window,height=100, width=100, relief=RAISED)
frame.config(padding=(30,15))
frame.pack(padx=50, pady=5)

frame1 = Frame(window,colormap='new',height=100, width=100, bd=10, relief=GROOVE)
frame1.config(bg='red')
frame1.pack(padx=50, pady=5)
#Label(frame1,text='Frame 2').pack()

frame2 = Frame(window,colormap='new',height=100, width=100, bd=10, relief=RIDGE)
frame2.config(bg='red')
frame2.pack(padx=50, pady=5)

frame2 = Frame(window,colormap='new',height=100, width=100, bd=10, relief=SUNKEN)
frame2.config(bg='red')
frame2.pack(padx=50, pady=5)
#Label(frame2,text='Frame 3').pack()

window.mainloop()



'''
frame1 = Frame(window,colormap='new',height=100, width=100, bd=10, relief=GROOVE)
frame1.config(bg='red')
frame1.pack(padx=50, pady=5)
Label(frame1,text='Frame 2').pack()

frame2 = Frame(window,colormap='new',height=100, width=100, bd=10, relief=RIDGE)
frame2.config(bg='red')
frame2.pack(padx=50, pady=5)
Label(frame2,text='Frame 3').pack()
'''