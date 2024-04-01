from tkinter import Tk
from tkinter import *
import math
import time
from plyer import notification

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    try:
        app.after_cancel(timer)
        canvas.itemconfig(timer_text, text="00:00")
        title_label.config(text="Timer")
        check_marks.config(text="")
        
        reps = 0
    except:
        canvas.itemconfig(timer_text, text="00:00")
        title_label.config(text="Timer")
        check_marks.config(text="")
        #global reps
        reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    #reset_timer(timer)
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
        notification.notify(
            title = "Time for your long break",
            message = "You've done well, you can have your 20min break",
            timeout = 10
            )
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
        notification.notify(
            title = "Time for your short break",
            message = "You've done well, you can have your 5min break",
            timeout = 10
            )
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)
        notification.notify(
            title = "Time to work",
            message = "Drop your phone and everything you're doing and focus",\
            timeout = 10
            )
        
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    #the math.floor returns the whole number without remainder
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
        
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        #update after 1 second, 1000 millisecond
        timer = app.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
app = Tk()
app.geometry('430x430+500+100')
app.config(bg=YELLOW, padx=40, pady=30)
app.title('Dimroid -- Pomodoro App')

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 28, 'bold'))
title_label.grid(column=1, row=0)

canvas = Canvas(width=230, height=250, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file='tomato.png')

canvas.create_image(110,130, image=tomato_img)
timer_text = canvas.create_text(110, 160, text='00:00', fill='white', font = (FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30))
check_marks.grid(column=1,row=2)

app.mainloop()