from tkinter import *

window = Tk()
window.title('Image Example')

img = PhotoImage(file='noroff-logo.gif')
label = Label(window, image=img)
label.pack(side=TOP)
small_img = img.subsample(5,5)
btn = Button(window, image=small_img)
btn.pack(side=LEFT, padx = 10)

txt = Text(window, width=25, height= 7)
txt.image_create('1.0', image=small_img)
txt.insert('1.1', 'Noroff Fagskole')
txt.pack(side=LEFT)

can = Canvas(window, width=300, height=100)
can.create_image((50,50), image=img)
can.pack(side=LEFT, padx = 10)
window.mainloop()
'''
label.pack(side=TOP)
btn.pack(side=LEFT, padx = 10)
txt.pack(side=LEFT)
can.pack(side=LEFT, padx = 10)
'''