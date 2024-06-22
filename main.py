from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_genarator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z']
    symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
               '@',
               '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""

    for char in password_list:
        password += str( char)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
            "email" : email,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="please fill all the boxes..")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            data.update(new_data)

        with open("data.json", "w") as data_file:

            json.dump(new_data, data_file, indent=4)
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_entry.delete(0, END)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title="Error", message="No data file found..")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"email: {email}\npassword : {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details in that file..")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)
photo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

website_label = Label(text="Web site")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_entry = Entry(width=32)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=32)
email_entry.grid(row=2, column=1, columnspan=1)
password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)

search_button = Button(text="search",width=22, command=find_password)
search_button.grid(row=1, column=2)
genarate_passowrd_button = Button(text="Genarate Password",command=password_genarator,width=22)
genarate_passowrd_button.grid(row=3, column=2)
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
