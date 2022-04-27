from tkinter import *
import tkinter.messagebox as msg

root = Tk()


def placeOrder():
    msg.showinfo("Order", f"Your order placed for {food_var.get()}")


root.geometry("733x433")
root.title("Food Order")

Label(text="What would you like to have", font="roboto 16 bold").pack(pady=20)

food_var = StringVar()
food_var.set("hi")

foodRadio = Radiobutton(root, text="Pav Bhaji", variable=food_var, value="Pav Bhaji")
foodRadio.pack(anchor="w", padx=20)

foodRadio = Radiobutton(root, text="Dosa", variable=food_var, value="Dosa")
foodRadio.pack(anchor="w", padx=20)

foodRadio = Radiobutton(root, text="Paratha", variable=food_var, value="Paratha")
foodRadio.pack(anchor="w", padx=20)

foodRadio = Radiobutton(root, text="Samosa", variable=food_var, value="Samosa")
foodRadio.pack(anchor="w", padx=20)

Button(text="Place Order", command=placeOrder).pack()

root.mainloop()
