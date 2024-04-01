from tkinter import *
from tkinter import ttk
from translate import Translator
import tkinter as tk

app = Tk()
app.geometry('590x370')
app.title("Dimzy Translator")

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()

    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the Text to Translate!')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator(to_lang=cl)
        output = translator.translate(lang_1)
        text_entry2.insert('end', output)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')


frame1 = Frame(app, width=590, height = 370, relief =RIDGE, borderwidth = 5, bg = '#F7DC6F')
frame1.place(x = 0, y = 0)

a = tk.StringVar()

Label(app, text = "Dimzy Translator", font = ("Helvetica 20 bold"), fg = 'black', bg = '#F7DC6F').pack(pady=10)


auto_select = ttk.Combobox(frame1, width = 27, textvariable = a, state = 'randomly', font = ('verdana', 10, 'bold'))

auto_select['values'] = ('Auto Select')

auto_select.place(x=15, y=50)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width= 27, textvariable =1, state = 'randomly', font = ('verdana', 10, 'bold'))

choose_language['values'] = (
    'af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW',
    'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu',
    'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'kk', 'km',
    'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn',
    'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd',
    'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur',
    'ug', 'uz', 'vi', 'cy', 'xh', 'yi'
)

choose_language.place(x=305, y = 50)
choose_language.current(0)

text_entry1 = Text(frame1, width = 20, height =9, borderwidth = 5, relief = RIDGE, font = ('verdana', 15))
text_entry1.place(x=10, y = 80)

text_entry2 = Text(frame1, width = 20, height =9, borderwidth = 5, relief = RIDGE, font = ('verdana', 15))
text_entry2.place(x=300, y = 80)

btn1 = Button(frame1, command = translate, text = 'Translate', relief = GROOVE, borderwidth=2, font = ('verdana', 10, 'bold'), bg = '#248aa2', fg ='white', cursor = 'hand2')
btn1.place(x=170, y = 325)

btn2 = Button(frame1, command = clear, text = 'Clear', relief = GROOVE, borderwidth=2, font = ('verdana', 10, 'bold'), bg = '#248aa2', fg ='white', cursor = 'hand2', width = 7)
btn2.place(x=340, y = 325)



app.mainloop()

