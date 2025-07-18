#PASSWORD MANAGER
import ttkbootstrap as ttk 
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import pickle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = pass_letters + pass_numbers + pass_numbers
    shuffle(password_list)
    pword = "".join(password_list)
    password.delete(0, END)
    password.insert(0, pword)
    copy(pword)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_click_event():
    web = website.get()
    name = u_name.get()
    paswd = password.get()
    content = {
        web:{
            'Email':name,
            'Password' : paswd,
        }
    }
    
    
    if web=="" or paswd=="":
        messagebox.showerror(title="INVALID DATA", message="Some fields are empty!")
        
    else:
        try:        
            with open("data.dat", "rb") as data_file:
                global data 
                data = pickle.load(data_file)
                data.update(content)

            with open("data.dat","wb") as data_file:
                pickle.dump(data, data_file)

        except FileNotFoundError:

            with open("data.dat","wb") as data_file:
                pickle.dump(content, data_file)

        
        website.delete(0, END)
        password.delete(0, END)
# ---------------------------- SEARCH BUTTON ------------------------------- #
def search_click_event():
    try:
        with open("data.dat", "rb") as data_file:
            data = pickle.load(data_file)
            website_to_search = website.get()
            email = data[website_to_search]["Email"]
            paswd = data[website_to_search]["Password"]
            messagebox.showinfo(title=website_to_search, message=f"Email: '{email}'\nPassword: '{paswd}' ")
    except FileNotFoundError:
        messagebox.showerror(title="LIST EMPTY!", message="There is no record in the file")
    except KeyError:
        messagebox.showinfo(title="NOT FOUND", message="The entered entry for website is not available")
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PassWord Manager")
window.geometry("580x420")  # Adjusted for better spacing
window.config(padx=30, pady=30)
window.resizable(False, False)
style = ttk.Style('darkly')

# Canvas (logo)
canvas = ttk.Canvas(width=200, height=200)
logo = ttk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Labels
website_label = ttk.Label(text="Website:", font=('Segoe UI', 10))
website_label.grid(row=1, column=0, sticky='e', pady=5)

email_uname_label = ttk.Label(text="Email/Username:", font=('Segoe UI', 10))
email_uname_label.grid(row=2, column=0, sticky='e', pady=5)

pass_label = ttk.Label(text="Password:", font=('Segoe UI', 10))
pass_label.grid(row=3, column=0, sticky='e', pady=5)

# Entries
website = ttk.Entry(width=34, font=('Segoe UI', 10))
website.grid(row=1, column=1, pady=5, sticky='w')

u_name = ttk.Entry(width=51, font=('Segoe UI', 10))
u_name.grid(row=2, column=1, columnspan=2, pady=5, sticky='w')

password = ttk.Entry(width=40)
password.grid(row=3, column=1, pady=5, sticky='w')

# Buttons
search_btn = ttk.Button(text="Search", width=14, command=search_click_event, bootstyle='secondary')
search_btn.grid(row=1, column=2)

generate_btn = ttk.Button(text="Generate",width = 14, command=generate_pword, bootstyle='info')
generate_btn.grid(row=3, column=2)

add_btn = ttk.Button(text="Add", width=58, command=add_click_event, bootstyle='success')
add_btn.grid(row=4, column=1, columnspan=2, pady=15, sticky='w')

window.mainloop()