from tkinter import *


def submitValue():
    print(f"The User Name is {userValue.get()}")
    print(f"The Password is {passValue.get()}")


root = Tk()

root.geometry("744x344")

user = Label(root, text="UserName")
password = Label(root, text="Password")

user.grid()
password.grid(row=1)

userValue = StringVar()
passValue = StringVar()

userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passValue)
userEntry.grid(row=0, column=1)
passEntry.grid(row=1, column=1)

Button(root, text="Submit", command=submitValue).grid()

root.mainloop()
