from noormi.gaming import *
from random import randint as rdt

DIFFICULTY = 4
MEMO_I,MEMO_J = 5,0

def build_level():
    for i in range(DIFFICULTY):
        draw_rectangle(Point(70+i*120,200),100,100,pygame.Color(60,60,60),1)
    return

def choose_number():
    return rdt(1,10**DIFFICULTY-1)


def press_key():
    k = wait_key()
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
    memorise(guess_nb,chosen_nb)
    return not(int(guess_nb)==chosen_nb)

def memorise(guess_nb,chosen_nb):
    global MEMO_I,MEMO_J
    clr = PYGAME_GOLD
    if int(guess_nb)<chosen_nb:
        clr = PYGAME_RED
    elif int(guess_nb)>chosen_nb:
        clr = PYGAME_GREEN

    display_text(guess_nb,("Verdana",12),(MEMO_I,MEMO_J),clr,True)
    MEMO_I += 45
    if MEMO_I>=455:
        MEMO_I = 5
        MEMO_J+=20
    if 130<=MEMO_J<=250:
        MEMO_J = 270   