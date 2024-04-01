from tkinter import Tk, Canvas, PhotoImage
from tkinter import simpledialog, messagebox
import pandas as pd
import time

def on_canvas_click(event):
    x, y = event.x, event.y
    print(f"Clicked at ({x}, {y})")
    
app = Tk()
app.title("Dimroid -- Nigeria States")
app.geometry('740x600+500+100')

image = PhotoImage(file="NG_Image.png")
small_pic = image.subsample(2, 2)
canvas = Canvas(app, height=600, width=780)
canvas.create_image(365, 290, image=small_pic)
canvas.pack()

data = pd.read_csv("States.csv")
all_states = data.states.to_list()

guessed_states = []
start_time = time.time()

while len(guessed_states) < 36:
    answer_state = simpledialog.askstring(f"GUESS THE STATE: {36 - len(guessed_states)} Left", "Enter An Africa State").title()

    if answer_state.lower() == 'exit':
        response = messagebox.askyesno("Display Missed States", "Do you want to display the missed states?")
        if response:
            missing_states = [state for state in all_states if state not in guessed_states]
            for state in missing_states:
                state_data = data[data.states == state]
                state_name = state_data.states.iloc[0]  # Assuming the state name is in the 'states' column
                canvas.create_text(int(state_data.x), int(state_data.y), text=state.replace(' ', '\n'), fill="#03fc4e", font=("Arial", 12, "bold"))
        break

    if len(guessed_states) == 36:
        for state in all_states:
            state_data = data[data.states == state]
            canvas.create_text(int(state_data.x), int(state_data.y), text=state.replace(' ', '\n'), fill="#03fc4e", font=("Arial", 12, "bold"))
        messagebox.showinfo("Congratulations", "Congratulations! You guessed all the statles correctly!")
        break

    if answer_state in all_states:
        if answer_state in guessed_states:
            continue
        else:
            guessed_states.append(answer_state)
            state_data = data[data.states == answer_state]
            state_name = state_data.states  # Assuming the state name is in the 'item' column
            canvas.create_text(int(state_data.x), int(state_data.y), text=answer_state.replace(' ', '\n'), fill="blue", font=("Arial", 12, "bold"))
    
    # Check if more than 5 minutes have elapsed
    # elapsed_time = time.time() - start_time
    # if elapsed_time > 300:
    #     for state in all_states:
    #         state_data = data[data.states == state]
    #         canvas.create_text(int(state_data.x), int(state_data.y), text=state.replace(' ', '\n'), fill="#03fc4e", font=("Arial", 12, "bold"))
    #     score = len(guessed_states)
    #     messagebox.showinfo("Time's Up!", f"Time's up! Your score: {score}/{len(all_states)}")
    #     break

#canvas.bind("<Button-1>", on_canvas_click)

app.mainloop()
