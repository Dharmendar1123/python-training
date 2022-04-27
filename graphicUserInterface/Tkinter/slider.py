from tkinter import *
import tkinter.messagebox as msg

root = Tk()


def myPercentage():
    msg.showinfo("Percentage", f"Your percentage is {mySlider.get()}%")


root.geometry("744x344")
root.title("Slider")

Label(text="What is your percentage").pack()
mySlider = Scale(root, from_=0, to=100, orient=HORIZONTAL)
mySlider.pack()
Button(text="Submit", command=myPercentage).pack()

root.mainloop()
