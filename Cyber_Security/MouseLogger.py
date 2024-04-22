#from pynput.mouse import Controller
from pynput.mouse import Listener

#def controlMouse():
#    mouse = Controller()
 #   mouse.position =(10,20)

#controlMouse()

def Write(x,y):
    print ('Position of Mouse cursor is {0}'.format((x,y)))

with Listener(on_move=Write) as l:
    l.join()
