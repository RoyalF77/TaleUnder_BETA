import pygame
pygame.init()

height = 824
width = 1280

screen = pygame.display.set_mode((width,height))

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
    action_pressed = False
    nmb_hit = 0
    cursor = 0
    damage = 0
    glove_t = [0,0,0,0,0]
    i,t,g,k,p = 0,0,0,0,0
    while combat_lock:
            # Print on the screen the static background
            if not action_pressed and selected != None and selected not in ['f','m']:
                screen.blit(line_all,(0,0))
            elif not action_pressed and selected == 'm':
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
                
                if action_pressed:
                    
                    if selected == 'f':
                        combat_lock, when_att = fight_button_pressed()
                        basics(screen,[clock,selected,action_pressed,when_att,nmb_hit])
                        if nmb_hit <= 10:
                            display_attack(screen,rect)
                        if when_att:
                            nmb_hit += 1

                    if selected == 'a':
                        combat_lock = not window_quit()
                        display_act_txt(screen,rect,enemy,cursor)
                        if nmb_hit > 10:
                            return [selected,cursor]
                        nmb_hit += 0.1
                    
                    if selected == 'i':
                        
                        combat_lock = not window_quit()
                        display_item_txt(screen,rect,player,cursor)
                        if nmb_hit == 0:
                            recover_hp(player,player.inv[cursor]['hp_give'])
                        if nmb_hit > 10:
                            return [selected]
                        nmb_hit += 0.1

                    if selected == 'm':
                        combat_lock = not window_quit()
                        display_mercy_txt(screen,rect,enemy,cursor)
                        if nmb_hit > 10:
                            return [selected,cursor]
                        nmb_hit += 0.1
                else:
                    combat_lock,buttonstab,selected,arrow_coord,elem,action_pressed,cursor = in_menu(buttonstab,selected,rect,player,enemy)
                    basics(screen,[clock,selected,[action_pressed],elem,cursor,player.info["current_hp"]])
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
            # attack_anim(screen,rect,enemy,True)
            
            # Enemy anim
            display_enemy(screen,enemy,rect)
            if selected == 'f':
                diff = clock.tick_busy_loop()
                if nmb_hit == 1:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[0] = 1
                if nmb_hit == 3:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[1] = 1

                if nmb_hit == 5:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[2] = 1

                if nmb_hit == 7:
                    damage += diff * player.info["at"]
                    nmb_hit += 1
                    glove_t[3] = 1

                if nmb_hit == 9:
                    damage += diff * player.info["at"]
                    damage = damage // (enemy.info["df"]*2)
                    nmb_hit += 1
                    glove_t[4] = 1

                if nmb_hit > 9:
                    nmb_hit += 1
                    display_attack_damage(screen,rect,damage)
                    
                    if nmb_hit >= 100:
                        enemy.info['hp'] -= damage
                        return
                
                if glove_t[0]:
                    i = display_glove(screen,enemy,1,i)
                    if i > 16 :
                        glove_t[0] = 0
                if glove_t[1]:
                    t = display_glove(screen,enemy,2,t)
                    if t > 16 :
                        glove_t[1] = 0
                if glove_t[2]:
                    g = display_glove(screen,enemy,3,g)
                    if g > 16 :
                        glove_t[2] = 0
                if glove_t[3]:
                    k = display_glove(screen,enemy,4,k)
                    if k > 16 :
                        glove_t[3] = 0
                if glove_t[4]:
                    p = display_glove(screen,enemy,5,p)
                    if p > 16 :
                        glove_t[4] = 0
            # Misc
            player.update_stats()
            sort_inv()
            clock.tick(60)
            
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
    player.rect.center = rect.center

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
            basics(screen,[player,clock])
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

info = {}
info["name"] = "Frisk"
info["xp"] = 0
info["level"] = 5
info["hp"] = hp_system[info["level"]]
info["current_hp"] = info["hp"]//2
info["at"] = at_system[info["level"]]
info["df"] = df_system[info["level"]]


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