from tkinter import *

app = Tk()
app.geometry('450x450+450+100')
app.title("Dimroid -- Cipher Message")

frame1 = Frame(app, relief=RIDGE, bd=5, bg='#658aa1', width=450, height=450)
frame1.pack()

def open_encryption_window():
    global text_space1
    encryption_window = Toplevel(app)
    encryption_window.geometry('590x400+450+100')
    encryption_window.title("Encryption Window")
    frame = Frame(encryption_window, relief=RIDGE, bd=5, bg='#658aa1', width=590, height=400)
    frame.pack()
    text_space1 = Text(frame, width=20, height=9, borderwidth=5, relief=RIDGE, font=('verdana', 15))
    text_space1.place(x=10, y=80)

    text_entry2 = Text(frame, width=20, height=9, borderwidth=5, relief=RIDGE, font=('verdana', 15))
    text_entry2.place(x=300, y=80)

    ceaserHeading1 = Label(frame, text='Raw Message', bd=5, font=('Helvetica', 14, 'bold'), bg='#828aa1', pady=4, relief=RIDGE)
    ceaserHeading1.place(x=10, y=35)

    ceaserHeading2 = Label(frame, text='Encrypted', bd=5, font=('Helvetica', 14, 'bold'), bg='#828aa1', pady=4, relief=RIDGE)
    ceaserHeading2.place(x=300, y=35)

    def encrypt_message():
        encrypted_message = caesar_encrypt()  # Encrypt the message using caesar_encrypt function
        text_entry2.delete("1.0", "end")  # Clear the previous content of text_entry2
        text_entry2.insert("1.0", encrypted_message)  # Insert the encrypted message into text_entry2

    EncryptButton = Button(frame, text="Encrypt", font=('Helvetica', 17, 'bold'), bg='light blue', pady=3, bd=5, relief=RAISED, command=encrypt_message)
    EncryptButton.place(x=238, y=320)

    app.withdraw()  # Hide the main window
    encryption_window.protocol("WM_DELETE_WINDOW", lambda: [app.deiconify(), encryption_window.destroy()])

def open_decryption_window():
    global text_space2
    decryption_window = Toplevel(app)
    decryption_window.geometry('590x400+450+100')
    decryption_window.title("Decryption Window")
    frame = Frame(decryption_window, relief=RIDGE, bd=5, bg='#658aa1', width=590, height=400)
    frame.pack()
    text_space2 = Text(frame, width=20, height=9, borderwidth=5, relief=RIDGE, font=('verdana', 15))
    text_space2.place(x=10, y=80)

    text_entry2 = Text(frame, width=20, height=9, borderwidth=5, relief=RIDGE, font=('verdana', 15))
    text_entry2.place(x=300, y=80)

    ceaserHeading1 = Label(frame, text='Encrypted Message', bd=5, font=('Helvetica', 13, 'bold'), bg='#828aa1', pady=4, relief=RIDGE)
    ceaserHeading1.place(x=10, y=38)

    ceaserHeading2 = Label(frame, text='Decrypted', bd=5, font=('Helvetica', 13, 'bold'), bg='#828aa1', pady=4, relief=RIDGE)
    ceaserHeading2.place(x=300, y=38)

    def decrypt_message():
        decrypted_message = caesar_decrypt()  # Encrypt the message using caesar_encrypt function
        text_entry2.delete("1.0", "end")  # Clear the previous content of text_entry2
        text_entry2.insert("1.0", decrypted_message)  # Insert the encrypted message into text_entry2

    DecryptButton = Button(frame, text="Decrypt", font=('Helvetica', 17, 'bold'), bg='light blue', pady=3, bd=5, relief=RAISED, command=decrypt_message)
    DecryptButton.place(x=238, y=320)

    app.withdraw()  # Hide the main window
    decryption_window.protocol("WM_DELETE_WINDOW", lambda: [app.deiconify(), decryption_window.destroy()])

ceaserHeading1 = Label(frame1, text='Dimzy Secret Message Encryptor', bd=5, font=('Helvetica', 15, 'bold'), bg='#828aa1', pady=4, relief=RIDGE)
ceaserHeading1.place(x=55, y=20)

EncryptButton = Button(frame1, text="Encrypt", font=('Helvetica', 20, 'bold'), bg='light blue', pady=4, bd=5, relief=RAISED, command=open_encryption_window)
EncryptButton.place(x=158, y=95)

DecryptButton = Button(frame1, text="Decrypt", font=('Helvetica', 20, 'bold'), bg='light blue', pady=4, bd=5, relief=RAISED, command=open_decryption_window)
DecryptButton.place(x=158, y=290)

orLabel = Label(frame1, text='OR', bd=5, font=('Helvetica', 15, 'bold'), bg='#828aa1', pady=4, relief=RIDGE)
orLabel.place(x=200, y=215)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_encrypt():
    end_text = ""
    shift_amount = 9
    raw_message = text_space1.get("1.0", "end-1c")
    start_text = raw_message
    
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)  # Use modulo to wrap around the alphabet
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    return end_text

def caesar_decrypt():
    end_text = ""
    shift_amount = 9
    raw_message = text_space2.get("1.0", "end-1c")
    start_text = raw_message
    
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % 26  # Use modulo to wrap around the alphabet
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    return end_text

app.mainloop()
