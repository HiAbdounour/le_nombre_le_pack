from noormi.gaming import *

def build_level(diff=4):
    for i in range(diff):
        draw_rectangle(Point(70+i*120,200),100,100,pygame.Color(60,60,60),1)
    return

