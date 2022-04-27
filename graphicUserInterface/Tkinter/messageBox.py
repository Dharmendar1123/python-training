from tkinter import *
import tkinter.messagebox as msg
root = Tk()


def myFun():
    print("You are in File menu")


def editFunc():
    print("You are in Edit menu")


def helpFun():
    print("Help")
    msg.showinfo("Help", "I will help you")


def rate():
    rate_msg = msg.askyesno("Rate Us", "Was you Experience good")
    if rate_msg:
        msg.showinfo("Experience", "Rate us on appstore")
    else:
        msg.showinfo("Experience", "Tell us what went wrong")


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

option3 = Menu(mainMenu, tearoff=0)
option3.add_command(label="Help", command=helpFun)
option3.add_command(label="Rate Us", command=rate)
root.config(menu=mainMenu)
mainMenu.add_cascade(label="Help", menu=option3)

root.mainloop()
