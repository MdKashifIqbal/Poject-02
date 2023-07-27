# Before running this code please install tkcalendar in your system

from tkinter import *
from tkcalendar import Calendar

tkobj = Tk()
tkobj.geometry("400x400")
tkobj.title("Calendar picker")

tkc = Calendar(tkobj,selectmode = "day",date_pattern="d/m/yy")
tkc.pack(pady=40)

def fetch_date():
    date.config(text = "Selected Date is: " + tkc.get_date())

but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
but.pack()

date = Label(tkobj,text="",bg='white',fg='black')
date.pack(pady=20)

tkobj.mainloop()