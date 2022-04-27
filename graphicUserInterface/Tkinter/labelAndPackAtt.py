from tkinter import *

root = Tk()
root.geometry("744x433")

root.title("Lorem ipsum")

text_label = Label(text="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has "
                        "\nbeen the industry's standard dummy text ever since the 1500s, when an unknown printer took a"
                        "\ngalley of type and scrambled it to make a type specimen book. It has survived not only five "
                        "\ncenturies, but also the leap into electronic typesetting, remaining essentially unchanged. "
                        "\nIt was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum "
                        "\npassages, and more recently with desktop publishing software like Aldus PageMaker including "
                        "\nversions of Lorem Ipsum.",
                   bg="orange", fg="white", padx=20, pady=30, borderwidth=5, relief=SUNKEN)

text_label.pack(side="bottom", anchor="se", fill=X)

root.mainloop()
