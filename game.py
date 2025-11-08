from noormi.gaming import *

def build_level(diff=4):
    for i in range(diff):
        draw_rectangle(Point(250,80+diff*50),50,50,pygame.Color(60,60,60),1)
    return

