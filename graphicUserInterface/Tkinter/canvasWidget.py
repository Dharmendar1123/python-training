from tkinter import *

root = Tk()

root.geometry("644x344")
root.title("Canvas Widget")

canvas_widget = Canvas(width=644, height=344)
canvas_widget.pack()

canvas_widget.create_line(0, 0, 644, 344)
canvas_widget.create_line(0, 344, 644, 0)

# canvas_widget.create_rectangle(50, 100, 500, 300, fill="green")

# canvas_widget.create_oval(50, 100, 500, 300, fill="orange")

canvas_widget.create_rectangle(100, 100, 450, 200, fill="blue")
canvas_widget.create_rectangle(100, 200, 450, 300, fill="yellow")

root.mainloop()