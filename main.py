from noormiextracts import *
from game import build_level, choose_number, logic, reset_memos, change_difficulty
from menu import build_menu, choice_level

init_graphic(500,500,"Le Nombre")
clear_window(PYGAME_GRAY)

# booleans
ingame = False
inmenu = True

running = True
while running:

    if inmenu:
        BUTTONS_LIST = build_menu()
        click_pos = wait_clic()
        diff = choice_level(BUTTONS_LIST,click_pos)
        if diff!=-1:
            clear_window(PYGAME_GRAY)
            change_difficulty(diff)
            reset_memos()
            chosen_nb = choose_number()
            inmenu = False
            ingame = True

    if ingame:
        build_level()
        ingame = logic(chosen_nb) # note : doesn't return anything
        if not ingame:
            pygame.time.delay(1000) # we need to see we win
            inmenu = True
            clear_window(PYGAME_GRAY)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()