import pygame
from os.path import join
from random import randint

# Definições Gerais

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Invade Spacers")
running = True
title = "Jogo 1"
font = pygame.font.SysFont("Segoe UI Emoji", 32)
emoji_surface = font.render("🚀", True, (255, 255, 255))
pygame.display.set_icon(emoji_surface)


#Superfície Plana

surf = pygame.Surface((100, 200))
surf.fill('darkred')
x = 100

#Importando uma Imagem
player_surf = pygame.image.load(join('Images', 'player.png')).convert_alpha()           #Imagem do jogador (nave)
star_surf = pygame.image.load(join('Images', 'star.png')).convert()                     #Imagem das estrelas
star_position = [(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)) for i in range(20)]

while running:
    #Evento Loopado
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Draw the Game
    display_surface.fill('darkgray')
    for position in star_position:
        display_surface.blit(star_surf, position) #Distribui as estrelas aleatoriamente
    x += 0.1
    display_surface.blit(player_surf, (x, 150)) #Block Image Transfer
    pygame.display.update()

pygame.quit()
