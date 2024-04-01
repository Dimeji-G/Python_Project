##==========================Imported Modules=======================================#
from tkinter import *
import pandas
import random

##==========================Predefined Variables===================================#
BACKGROUND_COLOR = "#B1DDC6"
FONT = ("New Times Roman", 15, 'bold')
current_card = {}
to_learn = {}

##==========================Functions===================================#
try:
    data = pandas.read_csv('words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/Spanish_lang.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def next_card():
    global current_card, flip_timer
    app.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["Spanish"])
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill = 'black')
    canvas.itemconfig(canvas_image, image=small_front_img)
    flip_timer = app.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill='white')
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(canvas_image, image=small_back_img)
    
def is_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv('words_to_learn.csv', index=False) 
    next_card()

##==========================GUI Interface==========================================#
app = Tk()
app.title("Dimroid -- Flash Cards")
# app.geometry('700x500+350+100')
app.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
flip_timer = app.after(3000, func=flip_card)

canvas = Canvas(width=400, height=326)
canvas.grid(row=0, column=0, columnspan=2)
card_front_img = PhotoImage(file='images/card_front.png')
small_front_img = card_front_img.subsample(2,2)
card_back_img = PhotoImage(file='images/card_back.png')
small_back_img = card_back_img.subsample(2,2)
canvas_image = canvas.create_image(200, 163, image = small_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(200, 100, text='Title', font=FONT)
card_word = canvas.create_text(200,163, text="word", font=FONT)

cross_image = PhotoImage(file="images/wrong.png")
small_cross = cross_image.subsample(2,2)
unknown_button = Button(image=small_cross, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
small_check_image = check_image.subsample(2,2)
known_button = Button(image=small_check_image, command=is_known)
known_button.grid(row=1, column=1)

next_card()


app.mainloop()