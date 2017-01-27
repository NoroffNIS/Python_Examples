from tkinter import *

window = Tk()

window.title('This is window title')

label = Label(window, text='Hello World ', background="Yellow")
label.pack(padx=200, pady=50)

window.mainloop()