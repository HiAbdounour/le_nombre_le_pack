from noormi.gaming import *
from game import build_level, choose_number, logic
from menu import build_menu

init_graphic(500,500,"Le Nombre")
clear_window(PYGAME_GRAY)


chosen_nb = choose_number()

ingame = False
inmenu = True

running = True
while running:

    if inmenu:
        build_menu()

    if ingame:
        build_level()
        ingame = logic(chosen_nb) # note : doesn't return anything


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()