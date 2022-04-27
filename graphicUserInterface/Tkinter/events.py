from tkinter import *

root = Tk()


def coordinate(event):
    print(f"You clicked at X: {event.x} and Y: {event.y}")


root.geometry("644x344")

event_button = Button(root, text="Click Me")
event_button.pack()

event_button.bind('<Button-1>', coordinate)
event_button.bind('<Double-1>', quit)
root.mainloop()
