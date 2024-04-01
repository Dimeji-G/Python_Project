from tkinter import *
from tkinter import ttk
import tkinter as tk
import qrcode
from PIL import Image, ImageTk
from tkinter import filedialog

app = Tk()
app.geometry('590x450')
app.title("Dimroid -- Qr Code Generator")
app.maxsize(590, 450)
app.resizable(False, False)

frame1 = Frame(app, width=590, height=450, relief=RIDGE , borderwidth=5, bg='#2e4e5c')
frame1.pack(fill=BOTH, expand=True)

Label(frame1, text='Dimzy QR Code Generator', font=("Helvetica 20 bold"), borderwidth=2, relief=RAISED, fg='black', bg='grey').pack(pady=7)

text = Text(frame1, width=34, height=1, relief=SUNKEN)
text.pack(pady=11)

Label(frame1, text='URL', relief=RAISED, borderwidth=2, fg='black', bg='grey').place(x=115, y=59)

text.insert('1.0', 'Enter your URL/LINK')

def on_entry_click(event):
    me = text.get(1.0, 'end').strip('\n')
    if me == 'Enter your URL/LINK':
        text.delete(1.0, "end")  # delete all the text in the entry
        text.insert(1.0, '')  # Insert blank for user input

def on_focusout(event):
    me = text.get(1.0, 'end').strip('\n')
    if me == '':
        text.insert(1.0, 'Enter your URL/LINK')

text.bind('<FocusIn>', on_entry_click)
text.bind('<FocusOut>', on_focusout)

qr_label = None

def Clicked():
    global save_btn
    global qr
    global qr_label
    global img
    global clear_btn
    url = text.get(1.0, 'end').strip('\n')
    # Generate the QR code
    data = url  # Replace with your data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the QR code image to a PhotoImage
    qr_photo = ImageTk.PhotoImage(img)

    # Display the QR code in a Label widget
    qr_label = Label(frame1, image=qr_photo, height=300)
    qr_label.image = qr_photo  # Keep a reference to prevent garbage collection
    qr_label.place(relx=0.5, rely=0.55, anchor=CENTER)

    save_btn = Button(frame1, text='Save QR Code', relief=RAISED, borderwidth=2, fg='black', bg='grey', height=1, command=save_qr_code)
    save_btn.place(x=150, y=400)

    clear_btn = Button(frame1, text='Clear QR Code', relief=RAISED, borderwidth=2, fg='black', bg='grey', height=1, command=clear_qr_code)
    clear_btn.place(x=320, y=400)

def save_qr_code():
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if file_path:
        img.save(file_path)
        print(f"QR code saved to: {file_path}")

#save_btn = Button(frame1, text='Save QR Code', relief=RAISED, borderwidth=2, fg='black', bg='grey', height=1, command=save_qr_code)
#save_btn.place(x=150, y=400)

def clear_qr_code():
    global qr_label
    if qr_label:
        if hasattr(qr_label, "destroy"):
            qr_label.destroy()  # Destroy the QR label window
        qr_label.image = None

        # Hide the save and clear buttons
        save_btn.place_forget()
        clear_btn.place_forget()

def run_both_functions():
    clear_qr_code()
    Clicked()



btn = Button(frame1, text='->', relief=RAISED, borderwidth=2, fg='black', bg='grey', command=run_both_functions)
btn.place(x=440, y=59)

app.mainloop()
