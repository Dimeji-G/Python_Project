import pyautogui as auto
import time
x = 100000
while True:
#    for me in ['jo', 'joblaq', 'joo', 'jojo', 'blaq', 'jomi', 'josi', 'jj', 'jk', 'jb',]:
#        variable = f'{me}, say hi'
#        auto.write(variable)
 #       auto.press('enter')
#    time.sleep()
    auto.write(str(x))
    auto.press('enter')
    x += 1
    time.sleep(3)
