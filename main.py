from noormi.gaming import *
from game import build_level, choose_number, logic

init_graphic(500,500,"Le Nombre")
clear_window(PYGAME_GRAY)


build_level()
chosen_nb = choose_number()

ingame = True

running = True
while running:

    if ingame:
        ingame = logic(chosen_nb)
        ingame = False # for testing


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()