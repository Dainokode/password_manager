from tkinter import *
from tkinter import messagebox
from generate_password import generate_password
import pyperclip


def get_values():
    # get entries values
    website = website_input.get()
    username_email = email_username_input.get()
    password = password_input.get()
    

    # ask if want to add account
    is_true = messagebox.askokcancel(title="Confirm", message="Do you want to add this account?")

    
    # cannot save if fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Empty fields", message="You cannot save empty fields.")
    elif is_true:
        # create text file or append to existing one
        with open("website_infos", "a") as website_file:
            website_file.write(f"{website} | {username_email} | {password}\n")
            # clear inputs
            website_input.delete(0, END)
            password_input.delete(0, END)


def random_password():
  password = generate_password()
  password_input.insert(0, password)
  pyperclip.copy(password)



# window setup
window = Tk()
window.title("Password Managaer")
window.config(padx=40, pady=40)


# canvas setup
canvas = Canvas(bd=0, height=200, width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)


# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(row=2, column=0, pady=5)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


# entrys(inputs)
website_input = Entry(width=35)
website_input.grid(row=1, column=1)
website_input.focus()


email_username_input = Entry(width=35)
email_username_input.grid(row=2, column=1)
email_username_input.insert(0, "@gmail.com")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")


# # buttons
generate_password_button = Button(text="Generate", command=random_password)
generate_password_button.grid(row=3, column=2, padx=5, sticky="EW")

add_button = Button(text="Add", width=20, command=get_values)
add_button.grid(row=4, column=1, pady=5, sticky="EW")


# run program
window.mainloop()