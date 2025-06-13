from functools import partial
from tkinter import *
from tkinter import messagebox
import pandas
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
card = {}
count = 0

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

white_card = PhotoImage(file="images/card_front.png")
cross_pic = PhotoImage(file="images/wrong.png")
tick_pic = PhotoImage(file="images/right.png")
back_card = PhotoImage(file="images/card_back.png")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
    dict_data = data.to_dict(orient="records")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    dict_data = original_data.to_dict(orient="records")

def change_question():
    global card, change, count
    window.after_cancel(change)
    card = random.choice(dict_data)
    canvas.itemconfig(card_question, image=white_card)
    canvas.itemconfig(question, text=card["French"], fill="black")
    canvas.itemconfig(title, text="French", fill="black")
    change = window.after(3000, show_ans)
    count += 1

def is_known():
    dict_data.remove(card)
    known = pandas.DataFrame(dict_data)
    known.to_csv("data/words_to_learn.csv", index=False)
    change_question()

def show_ans():
    global card
    canvas.itemconfig(card_question, image=back_card)
    canvas.itemconfig(question, text=card["English"], fill="white")
    canvas.itemconfig(title, text="English", fill="white")
change = window.after(3000, show_ans)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_question = canvas.create_image(400, 263, image=white_card)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
question = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_btn = Button(image=cross_pic, highlightthickness=0, command=partial(change_question))
cross_btn.grid(row=1, column=0)

right_btn = Button(image=tick_pic, highlightthickness=0, command=partial(is_known))
right_btn.grid(row=1, column=1)

if count == 0:
    change_question()

window.mainloop()
k = messagebox.askyesno(title="Save", message="Do you want to save the progress?")
if k == 0:
    if os.path.exists("data/words_to_learn.csv"):
        os.remove("data/words_to_learn.csv")

