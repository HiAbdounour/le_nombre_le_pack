from noormi.gaming import *
from game import build_level, choose_number, press_key

init_graphic(500,500,"Le Nombre")
clear_window(PYGAME_GRAY)


build_level()
print(choose_number())

for i in range(100):
    print(press_key())

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()