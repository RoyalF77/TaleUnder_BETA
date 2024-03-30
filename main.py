import pygame
pygame.init()
from view import *
from controller import *
from model import *

def player_turn():
    # create the background static
    img = pygame.Surface((width,height))
    # Display the color background
    img.fill((0,0,20))
    # Background
    display_background(img,2)
    # TextBox
    surf,rect = boxfight(img,width*0.6,height*0.3,(width*0.5,height*0.6),colors= (15,15,15))
    line_all = pygame.Surface((width,height))
    line_all.blit(img,(0,0))
    display_line(line_all,rect,2)
    # display_side_line(line_all,rect)
    line_mercy = pygame.Surface((width,height))
    line_mercy.blit(img,(0,0))
    display_line(line_mercy,rect,1)
    # Begin the loop
    combat_lock = True
    buttonstab = [1,0,0,0]
    selected = None
    last_tab = [0,0,0,0]
    while combat_lock:
            # Print on the screen the static background
            if selected != None and selected not in ['f','m']:
                screen.blit(line_all,(0,0))
            elif selected == 'm':
                screen.blit(line_mercy,(0,0))
            else:
                screen.blit(img,(0,0))

            if selected == None:
                # Selection of the menu
                combat_lock, buttonstab,selected = pturn_events(buttonstab,player,enemy)
                display_info(screen,rect,enemy)
            else:
                # In a menu
                if buttonstab != [0,0,0,0]:
                    last_tab = buttonstab
                    buttonstab = [0,0,0,0]
                combat_lock,buttonstab,selected,arrow_coord,elem = in_menu(buttonstab,selected,rect,player,enemy)
                # debug
                basics(screen,player,clock,elem,selected)
                if selected == None:
                    buttonstab = last_tab
                    last_tab = [0,0,0,0]

                elif selected == 'f':
                    display_fight(screen,rect,player)

                elif selected == 'a':
                    display_act(screen,rect,enemy,elem)

                elif selected == 'i':
                    display_item(screen,rect,player,elem)

                elif selected == 'm':
                    display_mercy(screen,rect,enemy,elem)
                    
                display_arrow(screen,arrow_coord)

            
            # Buttons
            buttons(screen,rect,buttonstab)
            # Hp bar, name...
            fight_elements(screen,player,rect)
            # Enemy anim
            display_enemy(screen,enemy,rect)

            
            # Misc
            player.update_stats()
            sort_inv()
            clock.tick(120)
            
            pygame.display.update()

def enemy_turn(soul):
    # create the background static
    img = pygame.Surface((width,height))
    # Display the color background
    img.fill((0,0,20))
    # Display the green boxes
    display_background(img,2)
    # Init boxfight
    surf,rect = boxfight(img,width*0.4,height*0.3,(width*0.5,height*0.6))
    surfrect = surf.get_rect(center = rect.center)
    # Init buttons
    buttons(img,rect,[0,0,0,0])

    # Begin the loop
    combat_lock = True
    while combat_lock:
        # If window closed
        if window_quit():
            combat_lock = False
            return False
        else:
            # Print on the screen the static background
            screen.blit(img,(0,0))
            # Hp bar, name...
            fight_elements(screen,player,rect)
            # Enemy anim
            display_enemy(screen,enemy,rect)
            # draw the soul
            draw_player(screen,player)
            # debug
            basics(screen,player,clock)
            # blue/red soul
            soul = modif_soul(soul)
            # Stop condition
            combat_lock = eturn_events(soul_mode=soul,player=player,fightbox=rect)
            # Misc
            player.update_stats()
            sort_inv()
            clock.tick(120)
            pygame.display.update()

Emergency_Stop = False

# Window Name and Icon
ico = pygame.image.load("sprites/Souls/red_soul.png")
pygame.display.set_caption("TaleUnder_BETA")
pygame.display.set_icon(ico)
 
# Get the width and height of the window
height = 824
width = 1280

info = {}
info["name"] = "Frisk"
info["xp"] = 99999
info["level"] = 1
info["hp"] = hp_system[info["level"]]
info["current_hp"] = info["hp"]
info["at"] = at_system[info["level"]]
info["df"] = df_system[info["level"]]

screen = pygame.display.set_mode((width,height))
player = Player(info,player_inventory)

clock = pygame.time.Clock()
screenrect = screen.get_rect()

# Start of the Game
start_lock = False
while start_lock:
    screen.fill((0,0,20))
    if window_quit():
        start_lock = False
        Emergency_Stop = True
    else:
        display_StartScreen(screen)
        start_lock = waiting_room()
        clock.tick(120)
        pygame.display.update()

name_lock = Emergency_Stop

while name_lock:
    screen.fill((0,0,20))
    if window_quit():
        name_lock = False
        Emergency_Stop = True
        
    else:
        name_pad(screen,(width,height))
        name_lock = name_ev()
        clock.tick(120)
        pygame.display.update()

cube_box = boxfight(screen,width*0.2,height*0.3,(width*0.5,height*0.6))
large_box = boxfight(screen,width*0.4,height*0.3,(width*0.5,height*0.6))
dialogue_box = boxfight(screen,width*0.6,height*0.3,(width*0.5,height*0.6))

overworld_lock = not Emergency_Stop
soul = 'red'
monster_combat = False
enemy = Sans()
while overworld_lock:
    screen.fill((0,0,20))
    if window_quit():
        overworld_lock = False
        Emergency_Stop = True
    else:
        # Si on rencontre un monstre
        if monster_combat:
            player_turn()
            monster_combat = False
        player_turn()
        # enemy_turn(soul)
        overworld_lock = False
        
pygame.quit()