from tkinter import *

root = Tk()
root.geometry("744x344")

scrollBar = Scrollbar(root)
scrollBar.pack(side=RIGHT, fill=Y)

listBox = Listbox(root, yscrollcommand= scrollBar.set)
for i in range(100):
    listBox.insert(END, f"Item {i}")

listBox.pack()
scrollBar.config(command=listBox.yview)

root.mainloop()
