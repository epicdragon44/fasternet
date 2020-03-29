import ctypes
import runpy
import sys

import tkinter as tk
from tkinter import ttk

FONT = ("Lucida Sans", 15)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("Task Complete")
    label = ttk.Label(popup, text=msg, font=FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = sys.exit())
    B1.pack()
    popup.mainloop()

if __name__ == '__main__':
    if is_admin():
        runpy.run_path('./main.py', run_name='__main__')
        popupmsg("Done!")
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(" ".join(sys.argv)), None, 1)

