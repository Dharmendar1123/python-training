from tkinter import *

root = Tk()

root.geometry("744x344")


def Hello():
    print("Hello")


def Name():
    print("Name")


def Nice():
    print("Nice")


def Cool():
    print("Cool")


frame = Frame(root, bg="grey", borderwidth=5, relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, fg="red", text="Hello", command=Hello)
b1.pack(side=LEFT, padx=10, pady=10)

b2 = Button(frame, fg="red", text="Name", command=Name)
b2.pack(side=LEFT, padx=10, pady=10)

b3 = Button(frame, fg="red", text="Cool", command=Cool)
b3.pack(side=LEFT, padx=10, pady=10)

b4 = Button(frame, fg="red", text="Nice", command=Nice)
b4.pack(side=LEFT, padx=10, pady=10)

root.mainloop()
