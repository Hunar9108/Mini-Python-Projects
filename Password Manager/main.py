from tkinter import *
from  tkinter import messagebox
import random
import json
import  pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass_by_comp():
    alpha_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]
    alpha_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                   "U", "V", "W", "X", "Y", "Z"]
    num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    alpha_special = ["!", "@", "#", "$", "%","&", "*", "(", ")" "+"]

    generated_pass = []

    for i in range(3):
        generated_pass.append(random.choice(alpha_lower))
        generated_pass.append(random.choice(alpha_upper))
        generated_pass.append(random.choice(alpha_special))
        generated_pass.append(random.choice(num))
    random.shuffle(generated_pass)
    new_pass =""
    for i in generated_pass:
        new_pass+=str(i)
    pyperclip.copy(new_pass)
    pass_entry.delete(0,END)
    pass_entry.insert(END,new_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    w = web_entry.get()
    e = em_entry.get()
    p = pass_entry.get()

    if w=="" or e== "" or p == "":
        messagebox.showerror(title="Error",message="You left some field empty.")
    else:
        new_data = {w:{
            "email" : e,
            "password": p
        }}

        try:
            with open("data.json", "r") as file_data:
                data = json.load(file_data)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file_data:
                json.dump(new_data, file_data)
        else:
            with open("data.json","w") as file_data:
                json.dump(data,file_data)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)
            web_entry.focus()

def search_content():
    w=web_entry.get()
    if w == "":
        messagebox.showerror(title="Error", message="You left the field empty.")
    else:
        try:
            with open("data.json", "r") as file_data:
                data = json.load(file_data)
            if w in data:
                p=data[w]["password"]
                e=data[w]["email"]
                messagebox.showinfo(title=w,message=f"Email: {e}\nPassword: {p}")
            elif w != "":
                messagebox.showinfo(title=w, message=f"You have not saved in Password for {w} yet.")

        except FileNotFoundError:
            messagebox.showerror(title="Disclaimer",message="You did not have any passwords saved yet")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50,pady=50)
window.title("Password Manager")

lock_pic = PhotoImage(file="logo.png")

canvas=Canvas(height=200,width=200)
canvas.create_image(100,100,image = lock_pic)
canvas.grid(row=0,column = 1)

website = Label(text="Website:")
website.grid(row=1,column=0)
email=Label(text="Email/Username:")
email.grid(row=2,column=0)
password=Label(text="Password:")
password.grid(row=3,column=0)


web_entry = Entry(width=21)
web_entry.grid(row=1,column=1)
web_entry.focus()
em_entry = Entry(width=40)
em_entry.grid(row=2,column=1,columnspan = 2)
em_entry.insert(END,"hunar9108@gmail.com")
pass_entry = Entry(width=21)
pass_entry.grid(row=3,column=1)

search_btn = Button(text="Search",width = 15,command=search_content)
search_btn.grid(row=1,column=2)
pass_btn = Button(text="Generate Password",width=15,command=generate_pass_by_comp)
pass_btn.grid(row=3,column=2,padx=0,pady=0)
add_btn=Button(text="Add",width=34,padx=0,pady=0,command=save)
add_btn.grid(row=4,column = 1,columnspan=2)

window.mainloop()
