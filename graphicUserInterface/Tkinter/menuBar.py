from tkinter import *

root = Tk()


def myFun():
    print("You are in File menu")


def editFunc():
    print("You are in Edit menu")


root.geometry("744x344")
root.title("Menu Bar")

mainMenu = Menu(root)

option1 = Menu(mainMenu, tearoff=0)
option1.add_command(label="New Project", command=myFun)
option1.add_command(label="Open", command=myFun)
option1.add_separator()
option1.add_command(label="Save", command=myFun)
option1.add_command(label="Save As", command=myFun)
option1.add_separator()
option1.add_command(label="Exit", command=quit)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="File", menu=option1)


option2 = Menu(mainMenu, tearoff=0)
option2.add_command(label="Copy", command=editFunc)
option2.add_command(label="Paste", command=editFunc)
option2.add_command(label="Cut", command=editFunc)
option2.add_separator()
option2.add_command(label="Find", command=editFunc)
option2.add_command(label="Find All", command=editFunc)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="Edit", menu=option2)

root.mainloop()
