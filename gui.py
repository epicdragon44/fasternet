from tkinter import *
from PIL import Image, ImageTk
import time

root = Tk()
root.geometry("500x500")
root.winfo_toplevel().title("Fasternet")
root.configure(background='#222222')
img = ImageTk.PhotoImage(Image.open("logo.png").resize((300,50)))

can = Canvas(root,bg="#222222",highlightthickness=0)
can.pack()
can.create_image(10, 10, anchor=NW, image=img)
#image = ImageTk.PhotoImage(Image.open("loading-gif-transparent-4.gif"))
#can.create_image(100, 100, anchor=NW, image=image)
frames = [PhotoImage(file='load.gif',format = 'gif -index %i' %(i)) for i in range(12)]

#can.create_image(100, 100, anchor=NW, image=frames[1])


def execute():
    can.create_image(100, 100, anchor=NW, image=frames[0])
    index = 0
    image = ImageTk.PhotoImage(Image.open("loading-gif-transparent-4.gif"))
    notDone= True
    while notDone:
        print(index)
        time.sleep(0.1)
#        can.create_image(100, 100, anchor=NW, image=frames[0])
        index+=1

button = Button(root, text='Start',width=15,background="lightgreen",command=execute).place(x=175,y=460)
root.mainloop()
description = ""

