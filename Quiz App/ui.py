from tkinter import *
from cytoolz.functoolz import partial
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):

        self.quiz_brain  = quiz_brain
        self.window = Tk()
        self.window.title("Quizzier")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score = 0


        self.score_board = Label(text=f"Score:{self.score}",bg=THEME_COLOR,fg="white")
        self.score_board.grid(row=0,column = 1)

        self.canvas = Canvas(height=250,width =300,bg="white")
        self.write = self.canvas.create_text(150,125,width = 270,text=f"",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan = 2,pady = 50)

        tick_pic = PhotoImage(file="images/true.png")
        cross_pic =PhotoImage(file="images/false.png")

        self.tick_btn = Button(image=tick_pic,highlightthickness=0,command=partial (self.solution_ans,"True"))
        self.tick_btn.grid(row =2,column = 0)
        self.cross_btn=Button(image=cross_pic,highlightthickness=0,command=partial(self.solution_ans,"False"))
        self.cross_btn.grid(row = 2,column = 1)

        self.get_next_question()
        self.window.mainloop()

    def solution_ans(self,you):
        q_ans = self.quiz_brain.check_answer(you)
        if q_ans:
            self.score+=1
            self.canvas.config(bg="green")
            self.score_board.config(text =f"Score:{self.score}",bg=THEME_COLOR,fg="white")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.write,text=q_text)
        else:
            self.cross_btn.config(state="disabled")
            self.tick_btn.config(state="disabled")
            self.canvas.itemconfig(self.write,text="You've reached the end of the quiz.")