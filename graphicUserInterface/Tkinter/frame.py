from tkinter import *

root = Tk()

root.geometry("744x344")

f1 = Frame(root, bg="black", borderwidth=5, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root, bg="black", borderwidth=5, relief=SUNKEN)
f2.pack(side=TOP)

l1 = Label(f1, text="GUI Course - Pycharm")
l1.pack(pady=150)

l2 = Label(f2, text="Welcome to GUI")
l2.pack(padx=250)

root.mainloop()