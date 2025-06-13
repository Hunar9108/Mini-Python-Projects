from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN =20
reps= 0
work_s=0
timer="h"
# ---------------------------- TIMER RESET ------------------------------- #
def countdown_resset():
    name.config(text="Timer",fg=GREEN)
    window.after_cancel(timer)
    chk.config(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15))
    canvas.itemconfig(timer_text,text="00:00")
    global reps,work_s
    reps = 0
    work_s = 0


def chk_count():
    global work_s
    chk.config(text=f"{"✔"*work_s}",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15))

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def long_break():
    chk_count()
    name.config(text="Long Break",fg=RED)
    countdown(LONG_BREAK_MIN*60)
def countdown_break():
    chk_count()
    name.config(text="Break",fg=PINK)
    countdown(SHORT_BREAK_MIN*60)
def countdown_start():
    name.config(text="Work",fg=GREEN)
    countdown(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global reps,work_s
    mis=count//60
    secs=count%60
    if secs<10:
        secs= "0"+str(secs)
    canvas.itemconfig(timer_text,text=f"{mis}:{secs}")
    if count>0:
        global timer
        timer = window.after(1000,countdown,count-1)
    elif count==0:
        reps+=1
        if reps%7==0:
            work_s += 1
            long_break()
        elif reps%8==0:
            countdown_resset()
        elif reps%2!=0:
            work_s+=1
            countdown_break()
        else:
            countdown_start()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=100,pady=50,bg = YELLOW)
window.title("Pomodoro")


name = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,38))
name.grid(row=0,column=1)

tomato_pic = PhotoImage(file="tomato.png")

canvas = Canvas(width=200,height=224)
canvas.config(bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image = tomato_pic)
timer_text = canvas.create_text(100,130,text="00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)


start_btn=Button(text="Start")
start_btn.config(command=countdown_start)
start_btn.grid(row=2,column=0)

chk = Label(text="",fg=GREEN,bg=YELLOW,font=(FONT_NAME,15))
chk.grid(row=3,column=1)

reset_btn = Button(text = "Reset",command=countdown_resset)
reset_btn.grid(row=2,column=2)

window.mainloop()
