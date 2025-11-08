from noormi.gaming import *
from random import randint as rdt

DIFFICULTY = 4

def build_level():
    for i in range(DIFFICULTY):
        draw_rectangle(Point(70+i*120,200),100,100,pygame.Color(60,60,60),1)
    return

def choose_number():
    return f"{rdt(1,10**DIFFICULTY-1):0{DIFFICULTY}d}"


def press_key():
    k = wait_key()
    try:
        k = int(k) # if works, means key is CAPS LOCK NUMBER
        # after testing, it seems to work regardless CAPS LOCK activation
        return k
    except Exception:
        try:
            k = int(k[1]) # if works, means key is a NUMBER from NUMPAD
            return k
        except Exception:
            if k==pygame.K_BACKSPACE: # for erasing
                return 10
            else:
                return -1
        
def print_key_at_i(nb,i):
    if 0<=nb<=9:
        display_text(str(nb),('Verdana',96),(70+i*120,200),text_bold=True)
    if nb==10:
        erase_at_i(i-1)

def erase_at_i(i):
    #if i!=0:
    pass