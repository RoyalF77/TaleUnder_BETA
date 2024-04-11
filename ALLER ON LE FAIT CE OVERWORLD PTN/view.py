import pygame

def draw_player(screen, perso, camera):
    screen.blit(perso.img, camera.apply(perso))

def draw_map(screen, map_image, camera):
    screen.blit(map_image, camera.apply(map_image))