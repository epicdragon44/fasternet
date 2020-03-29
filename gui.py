import runpy
import threading
from Tkinter import *

def run():

    th = threading.Thread(target=threadFunc)
    th.start()

    labelText1.set("Running...")

    th.join()

    labelText1.set("Done!")

def threadFunc():
    runpy.run_path('./run.py', run_name='__main__')

app = Tk()
app.title("Fasternet")
app.configure(bg="white")
app.geometry('500x500')

canvas = Canvas(app, width = 500, height = 150)
canvas.configure(bg="white")
canvas.pack()
img = PhotoImage(file="logo.gif")
canvas.create_image(20,20, anchor=NW, image=img)

button1 = Button(app, text="Start", width=10, command=run, bg="#1d9641", activebackground="#fff", activeforeground="#1d9641", fg="#fff", font=("Lucida Sans", 14))
button1.pack(side='bottom', padx=20, pady=50)

labelText1 = StringVar()
labelText1.set("Waiting to begin")
label1 = Label(app, textvariable=labelText1, height=1, text="Lucida Sans", font=("Lucida Sans", 15), bg="white")
label1.pack(side='bottom')

labelText2 = StringVar()
labelText2.set("")
label2 = Label(app, textvariable=labelText2, height=1, text="Lucida Sans", font=("Lucida Sans", 15), bg="white")
label2.pack()

labelText3 = StringVar()
labelText3.set("Click below to optimize your internet connection.")
label3 = Label(app, textvariable=labelText3, height=1, text="Lucida Sans", font=("Lucida Sans", 13), bg="white")
label3.pack()

labelText4 = StringVar()
labelText4.set("We'll take care of the details.")
label4 = Label(app, textvariable=labelText4, height=1, text="Lucida Sans", font=("Lucida Sans", 13), bg="white")
label4.pack()

app.iconbitmap(r'transparenticon.ico')

app.mainloop()