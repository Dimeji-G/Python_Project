import pyautogui
import time
while True:
    # Get and print the current mouse position
    #x, y = pyautogui.position()
    # print(f"Mouse position: x={x}, y={y}")
    x, y = 829, 63

    # Click at the current mouse position
    pyautogui.click(x, y)
    time.sleep(60)
