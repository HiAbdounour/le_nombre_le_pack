from noormi.gaming import *

init_graphic(500,500,"Le Nombre")
clear_window(PYGAME_GRAY)



running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()