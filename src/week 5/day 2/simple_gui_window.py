from tkinter import *
from tkinter import ttk
import time
window = Tk()

window.title('This is window title')

label = Label(window, text='Hello World TOP', background="Yellow")
label.pack(side=TOP)

strvar = StringVar()
strvar.set(0)
label = ttk.Label(window, textvariable=strvar, background="Yellow")
label.pack(side=BOTTOM)

min_ = 0
max_ = 100
pb_hd = ttk.Progressbar(window, orient='horizontal', mode='determinate', maximum=max_)

pb_hd.pack(expand=True, fill=BOTH, side=TOP)
#pb_hd.start()

i = 0
pb_hd.step(i)

for i in range(min_, max_):
    strvar.set(i)
    pb_hd.step()
    pb_hd.update()

    time.sleep(0.1)

window.mainloop()