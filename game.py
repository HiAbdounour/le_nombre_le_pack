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
    print(k)
    if k=="backspace": # for erasing
        return 10
    if k=="return": # for validating
        return 20
    try:
        k = int(k) # if works, means key is CAPS LOCK NUMBER
        # after testing, it seems to work regardless CAPS LOCK activation
        return k
    except Exception:
        try:
            k = int(k[1]) # if works, means key is a NUMBER from NUMPAD
            return k
        except Exception:
            return -1
        
def print_key_at_i(nb,i):
    if 0<=nb<=9 and i<DIFFICULTY:
        display_text(str(nb),('Verdana',96),(35+i*120,140),text_bold=True)
        return i+1
    if nb==10 and i!=0:
        erase_at_i(i-1)
        return i-1
    return -1 # means do nothing

def erase_at_i(i):
    draw_rectangle(Point(70+i*120,200),100,100,pygame.Color(60,60,60),1)


def logic(chosen_nb):
    guess_nb = ""
    i=0
    check = False
    while not check:
        k = press_key()
        if k!=-1 and k!=20:
            i_ = print_key_at_i(k,i)
            # something wrong happened
            if i_==-1:
                pass
            # erasing
            elif i_<i:
                i = i_
                guess_nb = guess_nb[:len(guess_nb)-1]
            # completing
            elif i_>i:
                i = i_
                guess_nb = guess_nb+str(k)
            # otherwise
            else:
                pass
        elif k==20 and i==DIFFICULTY:
            check = True
            for m in range(DIFFICULTY):
                erase_at_i(m)

    return int(guess_nb)==chosen_nb