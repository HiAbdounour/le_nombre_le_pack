from noormi.gaming import *

class Button:
    def __init__(self,lvl:int,rect:tuple[int,int,pygame.Color],txt_rect:tuple[str,int,int,pygame.Color]):
        self.level = lvl
        self.rect = rect
        self.txt_rect = txt_rect
    def display(self):
        draw_rectangle(Point(self.rect[0],self.rect[1]),50,50,self.rect[2],1)
        display_text(self.txt_rect[0],('Comic sans MS',32),(self.txt_rect[1],self.txt_rect[2]),clr=self.txt_rect[3],text_bold=True)
    def is_clicked(self,pos:Point)-> int:
        if self.rect[0]-25<=pos.x<=self.rect[0]+25 and self.rect[1]-25<=pos.y<=self.rect[1]+25:
            return self.level
        return -1
    
def choice_level(list_buttons,pos):
    for b in list_buttons:
        if b.is_clicked(pos)!=-1:
            return b.is_clicked(pos)
    return -1
    

def build_menu():
    pass