from noormi.gaming import *
from random import randint as rdt

DIFFICULTY = 4

def build_level():
    for i in range(DIFFICULTY):
        draw_rectangle(Point(70+i*120,200),100,100,pygame.Color(60,60,60),1)
    return

def choose_number():
    return f"{rdt(1,10**DIFFICULTY-1):0{DIFFICULTY}d}"


def press_key(): # or wait_key() from noormi.gaming ?
    pass
