from tkinter import *

root = Tk()


def storeValue():
    print("Form Submitted Successfully")
    with open("records.txt", "a") as f:
        f.write(f"{nameValue.get()}, {phoneValue.get()}, {genderValue.get()}, {sourceValue.get()}, {destinationValue.get()}, {foodValue.get()} \n")


root.geometry("644x344")
title = Label(text="Welcome to Agent Travels", font="roboto 16 bold", pady=10)
title.grid(row=0, column=4)

name = Label(text="Name")
phone = Label(text="Phone Number")
gender = Label(text="Gender")
source = Label(text="Source")
destination = Label(text="Destination")

name.grid(row=1)
phone.grid(row=2)
gender.grid(row=3)
source.grid(row=4)
destination.grid(row=5)

nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
sourceValue = StringVar()
destinationValue = StringVar()
foodValue = IntVar()

nameEntry = Entry(textvariable=nameValue)
phoneEntry = Entry(textvariable=phoneValue)
genderEntry = Entry(textvariable=genderValue)
sourceEntry = Entry(textvariable=sourceValue)
destinationEntry = Entry(textvariable=destinationValue)

nameEntry.grid(row=1, column=3)
phoneEntry.grid(row=2, column=3)
genderEntry.grid(row=3, column=3)
sourceEntry.grid(row=4, column=3)
destinationEntry.grid(row=5, column=3)

foodService = Checkbutton(text="Want to include Food", variable=foodValue)
foodService.grid(row=6, column=1)

Button(text="Submit", command=storeValue).grid(row=7, column=1)

root.mainloop()
