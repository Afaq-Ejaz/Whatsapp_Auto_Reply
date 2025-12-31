import pyautogui as pg
import pyperclip as ppc
import time


# while True:

#     result = pg.position()
#     print(result)

def cop():
    pg.click(850,750) 
    time.sleep(1)

    pg.moveTo(511 , 149) 

    pg.dragTo(691 , 675, duration=3 , button="left") 
    time.sleep(1)

    pg.hotkey('ctrl', 'c')
    time.sleep(1)

    pg.click(1331 , 657) 


def pasting():
    text = ppc.paste()
    return text


def reply_back():
    
    pg.click(610 , 701) 
    
    pg.hotkey('ctrl', 'v') 

    time.sleep(0.5)

    pg.click(1335 , 701) 

