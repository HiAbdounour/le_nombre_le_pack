from noormi.gaming import *
from game import build_level, choose_number, logic

init_graphic(500,500,"Le Nombre")
clear_window(PYGAME_GRAY)


build_level()
chosen_nb = choose_number()
logic(chosen_nb)


running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()