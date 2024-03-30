import pygame
from controller import blue_lock

fontsize = 30
font = pygame.font.Font("8bitoperator_jve.ttf",fontsize)

def display_StartScreen(screen):
    x,y = screen.get_size()
    logo = pygame.image.load("sprites/ui/TaleUnder_Cover.png").convert_alpha()
    logorect = logo.get_rect(center=(x//2,y//2))
    screen.blit(logo,logorect)
    xl,yl = logorect.bottomleft
    display(screen,"Press z to begin your journey",font,(xl+105,yl+20), "white",500)

def draw_player(screen,player):
    screen.blit(player.img,player.rect)

def display(surface,text,font,pos,color,limit=500):
    """
    Display Text on a Surface
    """
    line = ""
    x,y = pos
    size = font.__sizeof__()
    
    if len(text) > limit:
        for el in text:
            if len(line) > limit and el == " ":
                render = font.render(line,True,color)
                surface.blit(render,(x,y))
                y +=size* 1.1
                line = ""
            if el == "\n":
                render = font.render(line,True,color)
                surface.blit(render,(x,y))
                y +=size* 1.1
                line = ""
            else:
                line += el
    else:
        line = text

    render = font.render(line,True,color)
    rect = render.get_rect(topleft = (x,y))
    surface.blit(render,rect)
    return render, rect

def basics(screen,p=None,clock=None,elem=None,selec=None):
    """
    Display Debugg Text
    """
    display(screen,f"{p.rect,clock,elem,selec}",font,(0,0), "white")

background1 = pygame.image.load("sprites/ui/battle_back/battle_0.png").convert_alpha()
background1 = pygame.transform.scale_by(background1,1.5)
background2 = pygame.image.load("sprites/ui/battle_back/battle_1.png").convert_alpha()
background2 = pygame.transform.scale_by(background2,1.5)

def display_background(screen,type=1):
    if type == 1:
        backrect = background1.get_rect()
        x,y = screen.get_size()
        backrect.midbottom = (x//2,y//2)
        screen.blit(background1,backrect)
    else:
        backrect = background2.get_rect()
        x,y = screen.get_size()
        backrect.midbottom = (x//2,y*0.46)
        screen.blit(background2,backrect)

def display_line(screen,box,nb_line):
    L,l = box.size
    larg = l//3
    line = pygame.Surface((L,2))
    line.fill("white")
    x,y = box.topleft
    y += larg
    for i in range(nb_line):
        screen.blit(line,(x,y))
        y+= larg

def display_side_line(screen,box):
    L,l = box.size
    long = 2*L//3
    line = pygame.Surface((2,l))
    line.fill("white")
    x,y = box.topleft
    x += long
    screen.blit(line,(x,y))
        

def boxfight(screen,longueur,largeur,coord,colors="black"):
    x,y = coord  
    boxsurf = pygame.Surface((longueur, largeur))
    boxsurf.fill(colors)
    pygame.draw.rect(boxsurf, "white", (0, 0, longueur,  largeur), 3)
    moving_space = pygame.Surface((longueur-6, largeur-6))
    box = moving_space.get_rect(center=(x,y))
    screen.blit(boxsurf,(x-longueur//2,y-largeur//2))
    return boxsurf,box

fight = pygame.image.load("sprites/Buttons/fight.png").convert_alpha()
fight_s = pygame.image.load("sprites/Buttons/fight_selected.png").convert_alpha()
act = pygame.image.load("sprites/Buttons/act.png").convert_alpha()
act_s = pygame.image.load("sprites/Buttons/act_selected.png").convert_alpha()
items = pygame.image.load("sprites/Buttons/item.png").convert_alpha()
items_s = pygame.image.load("sprites/Buttons/item_selected.png").convert_alpha()
mercy = pygame.image.load("sprites/Buttons/mercy.png").convert_alpha()
mercy_s = pygame.image.load("sprites/Buttons/mercy_selected.png").convert_alpha()


def buttons(screen,boxrect,selected=[0,0,0,0]):
    x,y = boxrect.midbottom
    l,L = boxrect.size
    x -= L*2
    y += 100
    larg,long = fight.get_size()
    if selected == [0,0,0,0]:
        screen.blit(fight,(x,y))
        x+=250
        screen.blit(act,(x,y))
        x+=250
        screen.blit(items,(x,y))
        x+=250
        screen.blit(mercy,(x,y))
    else:
        if selected[0]:
            screen.blit(fight_s,(x,y))
        else:
            screen.blit(fight,(x,y))
        x+=250
        if selected[1]:
            screen.blit(act_s,(x,y))
        else:
            screen.blit(act,(x,y))
        x +=250
        if selected[2]:
            screen.blit(items_s,(x,y))
        else:
            screen.blit(items,(x,y))
        x+=250
        if selected[3]:
            screen.blit(mercy_s,(x,y))
        else:
            screen.blit(mercy,(x,y))

def fight_elements(screen,player,boxrect,KR_mode=False):
    x,y = boxrect.midbottom
    font_gros = pygame.font.Font("8bitoperator_jve.ttf",50)

    #Health bar
    health = pygame.Surface((player.info["hp"]*2.5,50))
    health.fill("red")
    healthrect = screen.blit(health,(x-100,y+25))
    #Current Health Bar
    pv = pygame.Surface((player.info["current_hp"]*2.5,50))
    pv.fill("yellow")
    pvrect = screen.blit(pv,healthrect.topleft)

    xh,yh = healthrect.topleft
    #Name + Level + HP
    display(screen,player.info["name"], font_gros,(xh-350,yh),"white")
    display(screen,f"LV {player.info['level']}", font_gros,(xh-200,yh),"white")
    display(screen,"HP",font,(xh-40,yh+9),"white")
    
    #KR + Life
    x,y = healthrect.topright
    if KR_mode:
         display(screen,"KR",font,(x+15,y+9),"white")
         display(screen,f"{player.info['current_hp']}/{player.info['hp']}", font_gros,(x+60,y-2),"white")
    else:
        display(screen,f"{player.info['current_hp']}/{player.info['hp']}",font_gros,(x+20,y-2),"white")

def display_enemy(screen,enemy,boxrect):
    sizex,sizey = enemy.size
    surf,rect = enemy.anim_simple(boxrect)

    if sizex < 100 or sizey < 100:
        if sizex < sizey:
            factor = sizey / sizex +1
            surf = pygame.transform.scale_by(enemy.img,factor)
            rect = surf.get_rect(topright=rect.topright)
        else:
            factor = sizex / sizey +1
            surf = pygame.transform.scale_by(enemy.img,factor)
            rect = surf.get_rect(topright=rect.topright)

    screen.blit(surf,rect)

def name_pad(screen,spec):
    w,h = spec
    font = pygame.font.Font("8bitoperator_jve.ttf",40)
    display(screen,"Name the fallen human.",font,(w*0.37,h*0.2), "white",500)

font35 = pygame.font.Font("8bitoperator_jve.ttf",35)

def display_info(screen,box,enemy):
    x,y = box.topleft
    display(screen,f"{enemy.info['desc']}",font35,(x+30,y+20), "white",40)

selection_arrow = pygame.image.load("sprites/ui/arrows/arrow_3.png")
selection_arrow = pygame.transform.scale_by(selection_arrow,3)
sa_rect = selection_arrow.get_rect()
index = 0
def display_arrow(screen,coord):
    global index
    sa_rect.center = coord
    screen.blit(selection_arrow,sa_rect)

arrow_up = pygame.image.load("sprites/ui/arrows/arrow_0.png")
arrow_up = pygame.transform.scale_by(arrow_up,3)
arrow_down = pygame.image.load("sprites/ui/arrows/arrow_1.png")
arrow_down = pygame.transform.scale_by(arrow_down,3)

def display_menu_arrows(screen,box,up,down):
    L,l = box.size
    x,y = box.topleft
    x += L*0.92
    if up:
        screen.blit(arrow_up,(x,y))
    if down:
        screen.blit(arrow_down,(x,y+l*0.82))

def display_fight(screen,box,player):
    x,y = box.topleft
    display(screen,"* Fight",font35,(x+75,y+20), "white")

def display_act(screen,box,enemy,elem):
    x,y = box.topleft
    i = 0
    y+= 20
    for el in enemy.act.values():
        i +=1
        if elem-3 < i and i <= elem:
            display(screen,f"* {el}",font35,(x+75,y), "white")
            y += 80
        if elem != 3:
            display_menu_arrows(screen,box,True,False)
        if elem != len(enemy.act):
            display_menu_arrows(screen,box,False,True)

def display_item(screen,box,player,elem):
    x,y = box.topleft
    i = 0
    y+=20
    for el in player.inv:
        i +=1
        if elem-3 < i and i <= elem:
            display(screen,f"* {el['name']}",font35,(x+75,y), "white")
            display(screen,f"+ {el['hp_give']} HP",font35,(x+550,y), "white")
            y += 80
        if elem != 3:
            display_menu_arrows(screen,box,True,False)
        if elem != len(player.inv):
            display_menu_arrows(screen,box,False,True)

def display_mercy(screen,box,enemy,elem):
    x,y = box.topleft
    i = 0
    y += 20
    for el in enemy.mercy.values():
        i +=1
        if elem-3 < i and i <= elem:
            display(screen,f"* {el}",font35,(x+75,y), "white")
            y += 80