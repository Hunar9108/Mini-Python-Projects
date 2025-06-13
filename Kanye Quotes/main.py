from tkinter import *
import requests

def get_quote():
    data = requests.get(url = "https://api.kanye.rest")
    quotes = data.json()
    canvas.itemconfig(quote,text = quotes["quote"])
    #Write your code here.


window = Tk()
window.title("Kanye Says....")
window.minsize(400,650)
window.config(padx=50,pady = 50)

back_pic = PhotoImage(file = "background.png")

canvas = Canvas(width=300 ,height = 414)
canvas.create_image(150,207,image = back_pic )
quote = canvas.create_text(150,207,text = "Kanye Quote Goes HERE",fill="white",width = 250,font=("Arial",23,"bold"))
canvas.grid(row = 0, column = 0)

kanye_pic = PhotoImage(file="kanye.png")
btn = Button(image=kanye_pic,highlightthickness=0,command=get_quote)
btn.grid(row = 1, column = 0)

window.mainloop()
