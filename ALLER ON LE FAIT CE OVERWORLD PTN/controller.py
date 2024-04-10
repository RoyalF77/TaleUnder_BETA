import pygame


def deplacement(personnage):
    pressed =  pygame.key.get_pressed()
    if personnage.velocity[0] == 0:
        if pressed[pygame.K_UP]:
            personnage.velocity[1] = -1
        elif pressed[pygame.K_DOWN]:
            personnage.velocity[1] = 1
        else:
            personnage.velocity[1] = 0
    if personnage.velocity[1] == 0:
        if pressed[pygame.K_RIGHT]:
            personnage.velocity[0] = 1
        elif pressed[pygame.K_LEFT]:
            personnage.velocity[0] = -1
        else:
            personnage.velocity[0] = 0
    personnage.deplacer()