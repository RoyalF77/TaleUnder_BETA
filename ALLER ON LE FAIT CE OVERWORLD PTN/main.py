import pygame
from model import *
from controller import *
from view import *

pygame.init()
pygame.font.init()
map = Map(pygame.image.load("ressources/maps/Fullmap.png"))
map.img = pygame.transform.scale(map.img, (5812, 3070))
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 824
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

col11 = Obstacle(pygame.Rect(2470,1875,3340,10))
col12 = Obstacle(pygame.Rect(2510,2500,3300,10))
col13 = Obstacle(pygame.Rect(5802,1875,10,585))
col14 = Obstacle(pygame.Rect(5490,1885,65,50))
col15 = Obstacle(pygame.Rect(5555,1885,65,100))
col16 = Obstacle(pygame.Rect(5620,1885,80,175))
col17 = Obstacle(pygame.Rect(5700,1885,90,250))
col18 = Obstacle(pygame.Rect(2510,2500,10,55))
col19 = Obstacle(pygame.Rect(2020,2555,490,10))
col20 = Obstacle(pygame.Rect(2020,2555,10,300))
col21 = Obstacle(pygame.Rect(1570,2845,450,10))
col22 = Obstacle(pygame.Rect(1570,2845,10,150))
col23 = Obstacle(pygame.Rect(1495,2995,75,10))
col24 = Obstacle(pygame.Rect(1495,2905,10,90))
col25 = Obstacle(pygame.Rect(0,2905,1495,10))
col26 = Obstacle(pygame.Rect(0,2155,720,10))
col27 = Obstacle(pygame.Rect(720,2095,10,60))
col28 = Obstacle(pygame.Rect(720,2095,600,10))
col29 = Obstacle(pygame.Rect(1320,2095,10,60))
col30 = Obstacle(pygame.Rect(1320,2155,600,10))
col31 = Obstacle(pygame.Rect(1920,2035,10,120))
col32 = Obstacle(pygame.Rect(1920,2035,70,10))
col33 = Obstacle(pygame.Rect(1990,1975,10,60))
col34 = Obstacle(pygame.Rect(1990,1975,60,10))
col35 = Obstacle(pygame.Rect(2050,1905,10,70))
col36 = Obstacle(pygame.Rect(2050,1905,150,10)) 
col37 = Obstacle(pygame.Rect(2200,1630,10,275)) 
col38 = Obstacle(pygame.Rect(2070,1630,130,10)) 
col39 = Obstacle(pygame.Rect(2070,1565,10,65)) 
col40 = Obstacle(pygame.Rect(800,1565,1270,10))
col41 = Obstacle(pygame.Rect(800,1505,10,60))
col42 = Obstacle(pygame.Rect(740,1505,60,10))
col43 = Obstacle(pygame.Rect(740,705,10,800))
col44 = Obstacle(pygame.Rect(740,705,110,10))
col45 = Obstacle(pygame.Rect(850,635,10,70))
col46 = Obstacle(pygame.Rect(850,635,670,10))
col47 = Obstacle(pygame.Rect(1520,635,10,65))
col48 = Obstacle(pygame.Rect(1520,700,200,10))
col49 = Obstacle(pygame.Rect(1720,700,10,65))
col50 = Obstacle(pygame.Rect(1720,765,180,10))
col51 = Obstacle(pygame.Rect(1900,765,10,130))
col52 = Obstacle(pygame.Rect(1900,895,450,10))
col53 = Obstacle(pygame.Rect(2350,895,10,130))
col54 = Obstacle(pygame.Rect(2350,1025,120,10))
col55 = Obstacle(pygame.Rect(2470,1025,10,850))
col56 = Obstacle(pygame.Rect(5742,2135,10,365))
col57 = Obstacle(pygame.Rect(50,2155,10,750))

map_collisions = [col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,
                  col31,col32,col33,col34,col35,col36,col37,col38,col39,col40,col41,col42,col43,col44,col45,col46,col47,col48,col49,
                  col50,col51,col52,col53,col54,col55,col56,col57]


combat1 = Debutcombat(pygame.Rect(5000,1885,10,600))
combat2 = Debutcombat(pygame.Rect(700,2165,10,740))
combat3 = Debutcombat(pygame.Rect(1100,950,500,400))

combats = [combat1,combat2,combat3]
overworld = True
screen.fill((0, 0, 20))

perso = Personnage()
map.set_position((0,0))
camera = Camera(5700,2975)
perso.set_position((1414,1054))
while overworld:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            overworld = False

    deplacement(perso)
    camera.update(perso)
    for elt in map_collisions:
        elt.collisions(perso)
        pygame.draw.rect(map.img,(255,0,0),elt.rect)
    for combat in combats:
        combat.collisions(perso)
        pygame.draw.rect(map.img,(0,0,255),combat.rect)
    print(perso.rect)
    draw_map(screen, map.img, camera)
    draw_player(screen, perso,camera)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
