from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("744x444")

# for png file
# dolphin_photo = PhotoImage(file="../dolphin.png")

# dolphin_image = Label(image=dolphin_photo)
# dolphin_image.pack()


#for pjg file
image = Image.open("../car.jpg")
car_photo = ImageTk.PhotoImage(image=image)

car_image = Label(image=car_photo)
car_image.pack()

root.mainloop()