from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=100,width=200)
window.config(padx=25,pady=25)

entry = Entry()
entry.grid(row = 0,column =1 )

def result():
    m =entry.get()
    k=int(m)*1.60934
    my_label3.config(text=f"{int(k)}")

my_label1 = Label(text="Miles" ,font=("Arial" , 12 ))
my_label1.grid(row = 0,column =2 )

my_label2 = Label(text="is equal to" ,font=("Arial" , 12 ))
my_label2.grid(row = 1,column = 0)

my_label3 = Label(text="0" ,font=("Arial" , 12 ))
my_label3.grid(row = 1,column = 1)

my_label4=Label(text="Km" ,font=("Arial" , 12 ))
my_label4.grid(row = 1,column = 2)

button = Button(text="Calculate",font=("Arial",12),command=result)
button.grid(row =2 ,column =1 )

window.mainloop()
