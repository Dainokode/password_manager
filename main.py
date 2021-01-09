# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------
from tkinter import *


# window setup
window = Tk()
window.title("Password Managaer")


# canvas setup
canvas = Canvas(bd=0, height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=2, column=3, padx=20, pady=20)


# run program
window.mainloop()